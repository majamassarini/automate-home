# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import unittest

import home
from home.tests.testcase import TestCase
from home.tests.test_scheduler_trigger_state import Stub


class TestSchedulerTriggerState(TestCase):
    def test_scheduler_trigger_state_fired_by_redis_update(tc):
        tc.enable_logging()
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            STATE_CHANGED = "light_turned_off"
            MAX_LOOP = 10

            async def asyncSetUp(self):
                self._loop = asyncio.get_event_loop()
                tc.create_tasks(self._loop, tc.myhome)
                self._loop.create_task(self.check_state())
                self._loop.create_task(self.emulate_redis_update())

            async def asyncTearDown(self):
                tc.scheduler.shutdown()

            async def check_state(self):
                while True:
                    await asyncio.sleep(0.1)
                    light1 = tc.myhome.appliances.find("light1")
                    if "Off" in light1.state.compute():
                        events.append(self.STATE_CHANGED)

            async def test_state(self):
                i = 0
                while self.STATE_CHANGED not in events and i < self.MAX_LOOP:
                    await asyncio.sleep(0.3)
                    i += 1

            async def emulate_redis_update(self):
                await asyncio.sleep(0.1)
                new_appliance = home.appliance.light.Appliance(
                    "light1", [home.appliance.light.event.forced.Event.On]
                )
                await tc.process._on_appliance_updated_by_redis(
                    tc.scheduler, new_appliance
                )

        test = Test("test_state")
        test.run()
        tc.assertIn(Test.STATE_CHANGED, events)
