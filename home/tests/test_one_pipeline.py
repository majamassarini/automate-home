# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

"""
Every source of a state change (a protocol trigger, a scheduler trigger, a
Redis update from the web UI) runs the commands of every performer of the
appliance, except the commands for the device that reported the change.
"""

import asyncio
from unittest.mock import Mock

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import home
from home.tests.testcase import TestCase, Command, Trigger


class Addressed:
    ADDRESSES: list = []

    @property
    def addresses(self):
        return self.ADDRESSES


class ButtonOn(Addressed, Trigger):
    """A button, on its own address, that forces the light on."""

    NAME = "button on"
    ADDRESSES = ["button"]
    DEFAULT_EVENTS = [home.appliance.light.event.forced.Event.On]

    def is_triggered(self, another_description):
        return another_description.name == self.name


class LampReportsOn(Addressed, Trigger):
    """The lamp itself reports it has been turned on."""

    NAME = "lamp reports on"
    ADDRESSES = ["lamp"]
    DEFAULT_EVENTS = [home.appliance.light.event.forced.Event.On]

    def is_triggered(self, another_description):
        return another_description.name == self.name


class TurnOn(Addressed, Command):
    """Sends its name when the light is turned on."""

    def make_msgs_from(self, old_state, new_state):
        if new_state.is_on and not old_state.is_on:
            return [self.NAME]
        return []


class TurnLampOn(TurnOn):
    NAME = "turn lamp on"
    ADDRESSES = ["lamp"]


class TurnSpeakerOn(TurnOn):
    NAME = "turn speaker on"
    ADDRESSES = ["speaker"]


class Stub(home.MyHome):
    """
    One light: a performer with the triggers only, and a performer with the
    commands only.
    """

    def _build_appliances(self):
        light = home.appliance.light.Appliance("light", [])
        collection = home.appliance.Collection()
        collection["lights"] = set([light])
        return collection

    def _build_performers(self):
        light = self.appliances.find("light")
        return [
            home.Performer(
                "light triggers", light, [], [ButtonOn(), LampReportsOn()]
            ),
            home.Performer(
                "light commands", light, [TurnLampOn(), TurnSpeakerOn()], []
            ),
        ]

    def _build_group_of_performers(self):
        return {}

    def _build_scheduler_triggers(self):
        return []

    def _build_schedule_infos(self):
        return []


class TestOnePipeline(TestCase):
    def setUp(self):
        super(TestOnePipeline, self).setUp()
        self.myhome = Stub()
        self.make_process(self.myhome)
        self.myhome.schedule(AsyncIOScheduler(), self.process.schedule)
        self.sent = []

        async def writer(msgs, performer):
            self.sent.append((performer.name, list(msgs)))

        self.process._protocols_writers = [writer]

    def test_a_protocol_trigger_runs_the_commands_of_another_performer(self):
        asyncio.run(
            self.process._update_performers_by_protocol_trigger(
                None, ButtonOn()
            )
        )

        self.assertEqual(
            self.sent,
            [("light commands", ["turn lamp on", "turn speaker on"])],
        )

    def test_a_device_report_is_not_echoed_back_to_the_device(self):
        asyncio.run(
            self.process._update_performers_by_protocol_trigger(
                None, LampReportsOn()
            )
        )

        self.assertEqual(self.sent, [("light commands", ["turn speaker on"])])

    def test_a_scheduler_trigger_runs_the_commands_of_every_performer(self):
        light_triggers = self.myhome.performers[0]
        scheduler_trigger = Mock(is_enabled=True, fork=Mock(return_value=[]))

        async def run():
            self.process._queue = asyncio.Queue()
            task = asyncio.create_task(self.process._run(None))
            await self.process._queue.put(
                (
                    light_triggers,
                    scheduler_trigger,
                    [home.appliance.light.event.forced.Event.On],
                )
            )
            await asyncio.sleep(0.05)
            task.cancel()

        asyncio.run(run())

        self.assertEqual(
            self.sent,
            [("light commands", ["turn lamp on", "turn speaker on"])],
        )

    def test_a_redis_update_runs_the_commands_of_every_performer(self):
        light = home.appliance.light.Appliance(
            "light", [home.appliance.light.event.forced.Event.On]
        )

        asyncio.run(self.process._on_appliance_updated_by_redis(None, light))

        self.assertEqual(
            self.sent,
            [("light commands", ["turn lamp on", "turn speaker on"])],
        )

    def test_no_state_change_sends_nothing(self):
        asyncio.run(
            self.process._update_performers_by_protocol_trigger(
                None, ButtonOn()
            )
        )
        self.sent.clear()

        asyncio.run(
            self.process._update_performers_by_protocol_trigger(
                None, ButtonOn()
            )
        )

        self.assertEqual(self.sent, [])
