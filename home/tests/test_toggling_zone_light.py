# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import unittest

import home
from home.tests.test_scheduler_trigger_state import CommandLight1
from home.tests.testcase import TestCase, Trigger


class TriggerLight1(Trigger):

    DEFAULT_EVENTS = [home.event.presence.Event.On]
    NAME = "Trigger presence for Light 1"

    def is_triggered(self, another_description):
        return True


class Stub(home.MyHome):
    def _build_appliances(self):
        light1 = home.appliance.light.zone.Appliance("light1", [])
        light1.notify(home.event.alarm.armed.Event.On)
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
            name="turn off after 1s",
            events=[home.event.toggle.Event.Off],
            state="Alarmed On",
            timeout_seconds=1,
        )
        triggers.append(trigger)
        trigger = home.scheduler.trigger.state.entering.delay.Trigger(
            name="turn on after 1s",
            events=[home.event.toggle.Event.On],
            state="Alarmed Off",
            timeout_seconds=1,
        )
        triggers.append(trigger)
        return triggers

    def _build_schedule_infos(self):
        return [
            (
                self.find_group_of_performers("lights"),
                self.find_scheduler_triggers("turn off after 1s"),
            ),
            (
                self.find_group_of_performers("lights"),
                self.find_scheduler_triggers("turn on after 1s"),
            ),
        ]


class TestSchedulerTriggerState(TestCase):
    def test_toggling_light(tc):
        tc.enable_logging()
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            STATE_CHANGED = "light_turned_off"
            MAX_LOOP = 40

            async def asyncSetUp(self):
                self._loop = asyncio.get_event_loop()
                tc.create_tasks(self._loop, tc.myhome)
                self._loop.create_task(self.emulate_bus_events())
                self._loop.create_task(self.check_state())

            async def asyncTearDown(self):
                tc.scheduler.shutdown()

            async def check_state(self):
                step1 = False
                step2 = False
                while True:
                    await asyncio.sleep(0.1)
                    light1 = tc.myhome.appliances.find("light1")
                    if step1 and not light1.state.is_on:
                        events.append("step 2")
                        step2 = True
                    elif step2 and light1.state.is_on:
                        events.append(self.STATE_CHANGED)
                    elif light1.state.is_on:
                        events.append("step 1")
                        step1 = True

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

        test = Test("test_state")
        test.run()
        print(events)
        tc.assertIn(Test.STATE_CHANGED, events)
