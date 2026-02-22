# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import unittest

import home
from home.tests.testcase import TestCase, Trigger


class TriggerFadeIn(Trigger):
    """Protocol trigger that drives the sound player into Fade In state."""

    DEFAULT_EVENTS = [home.event.sleepiness.Event.Awake]
    NAME = "Trigger fade in"

    def is_triggered(self, another_description):
        return True


class Stub(home.MyHome):
    def _build_appliances(self):
        player = home.appliance.sound.player.Appliance("player", [])
        collection = home.appliance.Collection()
        collection["players"] = set([player])
        return collection

    def _build_performers(self):
        performer = home.Performer(
            "player triggers",
            self.appliances.find("player"),
            [],
            [TriggerFadeIn()],
        )
        return [performer]

    def _build_group_of_performers(self):
        return {"player triggers": [self._performers[0]]}

    def _build_scheduler_triggers(self):
        return [
            home.scheduler.trigger.state.entering.disable_events.Trigger(
                name="disable forced off on fade in",
                events=[home.appliance.sound.player.event.forced.Event.Off],
                state="Fade In",
            ),
            home.scheduler.trigger.state.entering.delay.enable_events.Trigger(
                name="enable forced off after fade in",
                events=[home.appliance.sound.player.event.forced.Event.Off],
                state="Fade In",
                timeout_seconds=1,
            ),
        ]

    def _build_schedule_infos(self):
        return [
            (
                self.find_group_of_performers("player triggers"),
                self.find_scheduler_triggers("disable forced off on fade in"),
            ),
            (
                self.find_group_of_performers("player triggers"),
                self.find_scheduler_triggers("enable forced off after fade in"),
            ),
        ]


class TestDisableEnableEvents(TestCase):
    def test_forced_off_disabled_on_fade_in_then_re_enabled(tc):
        """
        When the sound player enters Fade In:
          1. forced.Event.Off is immediately disabled so any echo from
             Sonos is ignored.
          2. After the configured timeout forced.Event.Off is re-enabled
             so that legitimate stop/pause commands are processed again.
        """
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            EVENT_DISABLED = "forced_off_disabled"
            EVENT_ENABLED = "forced_off_enabled"
            MAX_LOOP = 20

            async def asyncSetUp(self):
                self._loop = asyncio.get_event_loop()
                tc.create_tasks(self._loop, tc.myhome)
                self._loop.create_task(self.check_state())
                self._loop.create_task(self.emulate_bus_events())

            async def asyncTearDown(self):
                tc.scheduler.shutdown()

            async def check_state(self):
                while True:
                    await asyncio.sleep(0.1)
                    player = tc.myhome.appliances.find("player")
                    forced_off = (
                        home.appliance.sound.player.event.forced.Event.Off
                    )
                    if self.EVENT_DISABLED not in events:
                        if not player.is_enabled(forced_off):
                            events.append(self.EVENT_DISABLED)
                    elif self.EVENT_ENABLED not in events:
                        if player.is_enabled(forced_off):
                            events.append(self.EVENT_ENABLED)

            async def test_state(self):
                i = 0
                while (
                    self.EVENT_ENABLED not in events and i < self.MAX_LOOP
                ):
                    await asyncio.sleep(0.3)
                    i += 1

            async def emulate_bus_events(self):
                await asyncio.sleep(0.1)
                trigger = TriggerFadeIn.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )

        test = Test("test_state")
        test.run()
        tc.assertIn(Test.EVENT_DISABLED, events)
        tc.assertIn(Test.EVENT_ENABLED, events)
