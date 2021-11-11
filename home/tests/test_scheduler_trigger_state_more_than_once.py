# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import unittest

import home
from home.tests.testcase import TestCase, Command, Trigger


class TriggerLight1(Trigger):

    DEFAULT_EVENTS = [home.appliance.light.event.forced.Event.On]
    NAME = "Trigger for Light 1"

    def is_triggered(self, another_description):
        return True


class CommandLight1(Command):

    NAME = "Command for Light 1"


class Stub(home.MyHome):
    def _build_appliances(self):
        light1 = home.appliance.light.Appliance("light1", [])
        collection = home.appliance.Collection()
        collection["lights"] = set([light1])
        return collection

    def _build_performers(self):
        performers = list()
        appliance = self.appliances.find("light1")
        trigger_light1 = TriggerLight1()
        command_light1 = CommandLight1()
        performer = home.Performer(
            appliance.name, appliance, [command_light1], [trigger_light1]
        )
        performers.append(performer)
        return performers

    def _build_group_of_performers(self):
        return {"lights": [self._performers[0]]}

    def _build_scheduler_triggers(self):
        triggers = list()
        trigger = home.scheduler.trigger.state.entering.delay.Trigger(
            name="turn off after",
            events=[home.appliance.light.event.forced.event.Event.Not],
            state="Forced On",
            timeout_seconds=1,
        )
        triggers.append(trigger)
        return triggers

    def _build_schedule_infos(self):
        return [
            (
                self.find_group_of_performers("lights"),
                self.find_scheduler_triggers("turn off after"),
            )
        ]


class TestSchedulerTriggerState(TestCase):
    def test_scheduler_trigger_state_fired_by_protocol_trigger(tc):
        tc.enable_logging()
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            STATE_CHANGED = "light_turned_off"
            MAX_LOOP = 50

            async def asyncSetUp(self):
                self._loop = asyncio.get_event_loop()
                tc.create_tasks(self._loop, tc.myhome)
                self._loop.create_task(self.emulate_bus_events())
                self._loop.create_task(self.check_state(tc.myhome))

            async def asyncTearDown(self):
                tc.scheduler.shutdown()

            async def check_state(self, my_home):
                events.append("check_state")
                while True:
                    await asyncio.sleep(0.1)
                    light1 = my_home.appliances.find("light1")
                    if "Off" in light1.state.compute():
                        self._loop.create_task(self.emulate_bus_events())
                        self._loop.create_task(self.check_state2(my_home))
                        break

            async def check_state2(self, my_home):
                events.append("check_state2")
                while True:
                    await asyncio.sleep(0.2)
                    light1 = my_home.appliances.find("light1")
                    if "Off" in light1.state.compute():
                        events.append(self.STATE_CHANGED)

            async def test_state(self):
                i = 0
                while self.STATE_CHANGED not in events and i < self.MAX_LOOP:
                    events.append("test_state")
                    await asyncio.sleep(0.5)
                    i += 1

            async def emulate_bus_events(self):
                await asyncio.sleep(0.1)
                events.append("emulate_bus_events")
                trigger = TriggerLight1.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )

        test = Test("test_state")
        test.run()
        print(events)
        tc.assertIn(Test.STATE_CHANGED, events)
