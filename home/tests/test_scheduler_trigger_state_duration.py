# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import unittest

import home
from home.tests.testcase import TestCase, Command, Trigger


class Trigger(Trigger):

    DEFAULT_EVENTS = [home.appliance.sprinkler.event.forced.Event.On]
    NAME = "Trigger Forced On for Sprinkler"

    def is_triggered(self, another_description):
        return True


class CommandLigh(Command):

    NAME = "Command for Sprinkler"


class Stub(home.MyHome):
    def _build_appliances(self):
        sprinkler = home.appliance.sprinkler.Appliance("sprinkler", [])
        sprinkler.notify(home.appliance.sprinkler.event.duration.Event(5))
        collection = home.appliance.Collection()
        collection["sprinklers"] = set(
            [
                sprinkler,
            ]
        )
        return collection

    def _build_performers(self):
        performers = list()
        appliance = self.appliances.find("sprinkler")
        trigger = Trigger()
        command = Command()
        performer = home.Performer(appliance.name, appliance, [command], [trigger])
        performers.append(performer)
        return performers

    def _build_group_of_performers(self):
        return {
            "sprinklers": [
                self._performers[0],
            ]
        }

    def _build_scheduler_triggers(self):
        triggers = list()
        trigger = home.scheduler.trigger.state.entering.delay.duration.Trigger(
            name="turn off after duration in sprinkler is elapsed",
            events=[home.appliance.sprinkler.event.forced.Event.Not],
            state="Forced On",
        )
        triggers.append(trigger)
        return triggers

    def _build_schedule_infos(self):
        return [
            (
                self.find_group_of_performers("sprinklers"),
                self.find_scheduler_triggers(
                    "turn off after duration in sprinkler is elapsed"
                ),
            )
        ]


class TestSchedulerTriggerState(TestCase):
    def test_scheduler_trigger_state_fired_by_protocol_trigger(tc):
        tc.enable_logging()
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            STATE_CHANGED = "sprinkler_turned_off"
            MAX_LOOP = 30

            async def asyncSetUp(self):
                self._loop = asyncio.get_event_loop()
                tc.create_tasks(self._loop, tc.myhome)
                self._loop.create_task(self.check_state())
                self._loop.create_task(self.emulate_bus_events())

            async def asyncTearDown(self):
                tc.scheduler.shutdown()

            async def check_state(self):
                while True:
                    await asyncio.sleep(0.3)
                    sprinkler = tc.myhome.appliances.find("sprinkler")
                    if "Off" in sprinkler.state.compute():
                        events.append(self.STATE_CHANGED)

            async def test_state(self):
                i = 0
                while self.STATE_CHANGED not in events and i < self.MAX_LOOP:
                    await asyncio.sleep(0.3)
                    i += 1

            async def emulate_bus_events(self):
                await asyncio.sleep(0.1)
                trigger = Trigger.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )

        test = Test("test_state")
        test.run()
        tc.assertIn(Test.STATE_CHANGED, events)
