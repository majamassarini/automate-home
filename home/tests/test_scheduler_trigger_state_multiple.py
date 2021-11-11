# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import unittest

import home
from home.tests.test_scheduler_trigger_state import (
    Stub as Parent,
    TriggerLight1,
    CommandLight1,
    CommandLight2,
)
from home.tests.testcase import TestCase, Trigger


class TriggerLight2(Trigger):

    DEFAULT_EVENTS = [home.appliance.light.event.forced.Event.On]
    NAME = "Trigger for Light 2"

    def is_triggered(self, another_description):
        return True


class Stub(Parent):
    def _build_performers(self):
        performers = list()
        appliance = self.appliances.find("light1")
        trigger_light1 = TriggerLight1()
        command_light1 = CommandLight1()
        performer = home.Performer(
            appliance.name, appliance, [command_light1], [trigger_light1]
        )
        performers.append(performer)
        appliance = self.appliances.find("light2")
        trigger_light2 = TriggerLight2()
        command_light2 = CommandLight2()
        performer = home.Performer(
            appliance.name, appliance, [command_light2], [trigger_light2]
        )
        performers.append(performer)
        return performers


class TestSchedulerTriggerState(TestCase):
    def test_scheduler_trigger_state_multiple_times(tc):
        tc.enable_logging()
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            STATE_CHANGED = "lights_turned_off"
            MAX_LOOP = 10

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
                    light1 = tc.myhome.appliances.find("light1")
                    light2 = tc.myhome.appliances.find("light2")
                    if (
                        "Off" in light1.state.compute()
                        and "Off" in light2.state.compute()
                    ):
                        events.append(self.STATE_CHANGED)

            async def test_state(self):
                i = 0
                while self.STATE_CHANGED not in events and i < self.MAX_LOOP:
                    await asyncio.sleep(0.3)
                    i += 1

            async def emulate_bus_events(self):
                await asyncio.sleep(0.1)
                trigger = TriggerLight1.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )
                trigger = TriggerLight2.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )

        test = Test("test_state")
        test.run()
        print(events)
        tc.assertIn(Test.STATE_CHANGED, events)
