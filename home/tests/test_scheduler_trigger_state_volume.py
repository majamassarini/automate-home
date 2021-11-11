# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import unittest

import home
from home.tests.testcase import TestCase, Command, Trigger


class Trigger1(Trigger):

    DEFAULT_EVENTS = [home.event.sleepiness.Event.Awake]
    NAME = "Trigger awake"

    def is_triggered(self, another_description):
        return True


class Command1(Command):

    NAME = "Set volume"

    def make_msgs_from(self, old_state, new_state):
        return [new_state.volume]


class Command2(Command):

    NAME = "Turn off"


class Stub(home.MyHome):
    VOLUME_A = 44
    VOLUME_B = 55
    VOLUME_C = 66

    def _build_appliances(self):
        player = home.appliance.sound.player.Appliance("player", [])
        collection = home.appliance.Collection()
        collection["players"] = set([player])
        return collection

    def _build_performers(self):
        performers = list()
        appliance = self.appliances.find("player")
        trigger1 = Trigger1()
        command1 = Command1()
        performer = home.Performer("set volume", appliance, [command1], [trigger1])
        performers.append(performer)
        command2 = Command2()
        performer = home.Performer("turn off", appliance, [command2], [])
        performers.append(performer)
        return performers

    def _build_group_of_performers(self):
        return {
            self._performers[0].name: [self._performers[0]],
            self._performers[1].name: [self._performers[1]],
        }

    def _build_scheduler_triggers(self):
        triggers = list()
        trigger_a = home.scheduler.trigger.state.entering.delay.Trigger(
            name="fade 1",
            events=[
                home.appliance.sound.player.event.fade_in.volume.Event(self.VOLUME_A)
            ],
            state="Fade In",
            timeout_seconds=1,
        )
        triggers.append(trigger_a)
        trigger_b = home.scheduler.trigger.state.entering.delay.Trigger(
            name="fade 2",
            events=[
                home.appliance.sound.player.event.fade_in.volume.Event(self.VOLUME_B)
            ],
            state="Fade In",
            timeout_seconds=2,
        )
        triggers.append(trigger_b)
        trigger_c = home.scheduler.trigger.state.entering.delay.Trigger(
            name="fade 3",
            events=[
                home.appliance.sound.player.event.fade_in.volume.Event(self.VOLUME_C)
            ],
            state="Fade In",
            timeout_seconds=3,
        )
        triggers.append(trigger_c)
        trigger_d = home.scheduler.trigger.state.entering.delay.Trigger(
            name="fade off",
            events=[home.event.elapsed.Event.On],
            state="Fade In",
            timeout_seconds=4,
        )
        triggers.append(trigger_d)
        return triggers

    def _build_schedule_infos(self):
        return [
            (
                self.find_group_of_performers("set volume"),
                self.find_scheduler_triggers("fade 1"),
            ),
            (
                self.find_group_of_performers("set volume"),
                self.find_scheduler_triggers("fade 2"),
            ),
            (
                self.find_group_of_performers("set volume"),
                self.find_scheduler_triggers("fade 3"),
            ),
            (
                self.find_group_of_performers("turn off"),
                self.find_scheduler_triggers("fade off"),
            ),
        ]


class TestSchedulerTriggerState(TestCase):
    def test_scheduler_trigger_state_fired_by_protocol_trigger(tc):
        tc.enable_logging()
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            STATE_CHANGED_A = "Volume A"
            STATE_CHANGED_B = "Volume B"
            STATE_CHANGED_C = "Volume C"
            TURNED_OFF = "Turned Off"
            MAX_LOOP = 50

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
                    if (
                        self.STATE_CHANGED_A in events
                        and self.STATE_CHANGED_B in events
                        and self.STATE_CHANGED_C in events
                    ):
                        if player.state.VALUE == "Off":
                            events.append(self.TURNED_OFF)
                    elif (
                        self.STATE_CHANGED_A in events
                        and self.STATE_CHANGED_B in events
                    ):
                        if player.state.volume == Stub.VOLUME_C:
                            events.append(self.STATE_CHANGED_C)
                    elif self.STATE_CHANGED_A in events:
                        if player.state.volume == Stub.VOLUME_B:
                            events.append(self.STATE_CHANGED_B)
                    else:
                        if player.state.volume == Stub.VOLUME_A:
                            events.append(self.STATE_CHANGED_A)

            async def test_state(self):
                i = 0
                while (
                    not (
                        self.STATE_CHANGED_A in events
                        and self.STATE_CHANGED_B in events
                        and self.STATE_CHANGED_C in events
                        and self.TURNED_OFF in events
                    )
                    and i < self.MAX_LOOP
                ):
                    await asyncio.sleep(0.3)
                    i += 1

            async def emulate_bus_events(self):
                await asyncio.sleep(0.1)
                trigger = Trigger1.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )

        test = Test("test_state")
        test.run()
        tc.assertIn(Test.STATE_CHANGED_A, events)
        tc.assertIn(Test.STATE_CHANGED_B, events)
        tc.assertIn(Test.STATE_CHANGED_C, events)
        tc.assertIn(Test.TURNED_OFF, events)
