# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

"""Regression test for a hanging protocol writer blocking _run.

Before the asyncio.wait_for fix, a writer whose coroutine never
completed (e.g. HA websocket send_str stalling while the remote was
connected but not consuming data) would block _run indefinitely.
Scheduled triggers queued by APScheduler would accumulate in the queue
but never be dequeued, even though KNX protocol events continued
arriving through their own task.

These tests verify that:
  - A hanging writer is cancelled after the 1-second timeout.
  - _run resumes and processes the next queue item (a scheduled trigger)
    within a bounded total time.
"""

import asyncio
import time
import unittest

import home
from home.tests.testcase import TestCase, Command, Trigger


# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------


class TriggerLight(Trigger):
    """Protocol trigger that drives the light to Forced On."""

    DEFAULT_EVENTS = [home.appliance.light.event.forced.Event.On]
    NAME = "Trigger for Light"

    def is_triggered(self, another_description):
        return True


class _BlockingCommand(Command):
    """Command that always returns a non-empty message list.

    The stub Command base returns [] from make_msgs_from / execute, which
    means writers are never called.  This subclass always returns [self]
    so the process writer loop is exercised.
    """

    NAME = "Blocking Command"

    def make_msgs_from(self, old_state, new_state):
        return [self]

    def execute(self):
        return [self]


class _HangingGateway:
    """Protocol gateway whose writer coroutine never completes.

    run() must exist so that process.create_tasks() can register it;
    it just sleeps so the task stays alive without doing anything.
    """

    PROTOCOL = "hanging"

    async def run(self, callbacks):
        await asyncio.sleep(3600)

    async def writer(self, msgs, *args):
        await asyncio.sleep(3600)  # effectively never returns


class Stub(home.MyHome):
    def _build_appliances(self):
        light = home.appliance.light.Appliance("light", [])
        collection = home.appliance.Collection()
        collection["lights"] = {light}
        return collection

    def _build_performers(self):
        appliance = self.appliances.find("light")
        return [
            home.Performer(
                "light",
                appliance,
                [_BlockingCommand()],
                [TriggerLight()],
            )
        ]

    def _build_group_of_performers(self):
        return {"lights": [self._performers[0]]}

    def _build_scheduler_triggers(self):
        return [
            home.scheduler.trigger.state.entering.delay.Trigger(
                name="turn off after 1s",
                events=[home.appliance.light.event.forced.event.Event.Not],
                state="Forced On",
                timeout_seconds=1,
            )
        ]

    def _build_schedule_infos(self):
        return [
            (
                self.find_group_of_performers("lights"),
                self.find_scheduler_triggers("turn off after 1s"),
            )
        ]


# ---------------------------------------------------------------------------
# Test: scheduled trigger fires despite hanging writer
# ---------------------------------------------------------------------------


class TestScheduledTriggerFiresWithHangingWriter(TestCase):
    """A hanging writer must not prevent scheduled triggers from firing.

    The 5-second timeout on each writer call in _run means the hanging
    writer is cancelled after 5 s and _run resumes.  The scheduled
    "turn off after 1s" trigger must still fire and change the light
    state to Off.
    """

    def test_scheduled_trigger_fires_despite_hanging_writer(tc):
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        tc.process.add(_HangingGateway())

        events = []

        class Test(unittest.IsolatedAsyncioTestCase):

            STATE_OFF = "light_off"
            # Budget: 5 s writer timeout + 1 s APScheduler delay
            # + 5 s writer timeout in _run + margin = 15 s
            MAX_LOOP = 50  # 50 × 0.3 s = 15 s

            async def asyncSetUp(self):
                loop = asyncio.get_event_loop()
                tc.create_tasks(loop, tc.myhome)
                loop.create_task(self._watch_state())
                loop.create_task(self._drive_protocol_event())

            async def asyncTearDown(self):
                tc.scheduler.shutdown()

            async def _watch_state(self):
                while True:
                    await asyncio.sleep(0.1)
                    light = tc.myhome.appliances.find("light")
                    if "Off" in light.state.compute():
                        if self.STATE_OFF not in events:
                            events.append(self.STATE_OFF)

            async def _drive_protocol_event(self):
                await asyncio.sleep(0.1)
                trigger = TriggerLight.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )

            async def test_state(self):
                i = 0
                while self.STATE_OFF not in events and i < self.MAX_LOOP:
                    await asyncio.sleep(0.3)
                    i += 1

        test = Test("test_state")
        test.run()
        tc.assertIn(
            Test.STATE_OFF,
            events,
            "Scheduled trigger never fired — hanging writer may still be "
            "blocking _run",
        )


# ---------------------------------------------------------------------------
# Test: total elapsed time is bounded by the writer timeout
# ---------------------------------------------------------------------------


class TestHangingWriterDoesNotBlockIndefinitely(TestCase):
    """_run must complete within a bounded time even with a hanging writer.

    With a 5-second timeout per writer and two writer calls (one in
    _update_performers_by_protocol_trigger, one in _run for the
    scheduled trigger), plus ~1 second for the APScheduler delay, the
    total should be well under 15 seconds.  Before the fix the process
    would hang indefinitely.
    """

    def test_elapsed_time_is_bounded(tc):
        tc.myhome = Stub()
        tc.make_process(tc.myhome)
        tc.process.add(_HangingGateway())

        timing = {}

        class Test(unittest.IsolatedAsyncioTestCase):

            async def asyncSetUp(self):
                loop = asyncio.get_event_loop()
                tc.create_tasks(loop, tc.myhome)

            async def asyncTearDown(self):
                tc.scheduler.shutdown()

            async def test_state(self):
                t0 = time.monotonic()

                trigger = TriggerLight.make_from(None)
                await tc.process._update_performers_by_protocol_trigger(
                    tc.scheduler, trigger
                )

                # Wait for light to reach Off (scheduled trigger + _run)
                light = tc.myhome.appliances.find("light")
                for _ in range(150):
                    if "Off" in light.state.compute():
                        break
                    await asyncio.sleep(0.1)

                timing["elapsed"] = time.monotonic() - t0

        test = Test("test_state")
        test.run()

        tc.assertIn("elapsed", timing)
        # Must finish well under 15 seconds even with two 5-second timeouts
        tc.assertLess(
            timing["elapsed"],
            15.0,
            f"Took {timing['elapsed']:.1f} s — hanging writer may still be "
            "blocking _run",
        )
