# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
from unittest.mock import AsyncMock, Mock

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import home
from home.tests.testcase import TestCase, Command


class Stub(home.MyHome):
    """
    One light with two performers without triggers (both run on a Redis
    update) and one state trigger scheduled for the first performer only.
    """

    def _build_appliances(self):
        light1 = home.appliance.light.Appliance("light1", [])
        collection = home.appliance.Collection()
        collection["lights"] = set([light1])
        return collection

    def _build_performers(self):
        appliance = self.appliances.find("light1")
        return [
            home.Performer("light1 commands", appliance, [Command()], []),
            home.Performer("light1 more commands", appliance, [Command()], []),
        ]

    def _build_group_of_performers(self):
        return {"light1 commands": [self._performers[0]]}

    def _build_scheduler_triggers(self):
        return [
            home.scheduler.trigger.state.entering.Trigger(
                name="entering forced on",
                events=[home.appliance.light.event.forced.Event.Not],
                state="Forced On",
            )
        ]

    def _build_schedule_infos(self):
        return [
            (
                self.find_group_of_performers("light1 commands"),
                self.find_scheduler_triggers("entering forced on"),
            )
        ]


class TestSchedulerTriggerStateOnceByRedis(TestCase):
    def test_state_trigger_is_scheduled_once_per_redis_update(self):
        myhome = Stub()
        self.make_process(myhome)
        myhome.schedule(AsyncIOScheduler(), self.process.schedule)
        self.process.schedule = AsyncMock()
        self.process._schedule_by_trigger_fork = Mock()
        new_appliance = home.appliance.light.Appliance(
            "light1", [home.appliance.light.event.forced.Event.On]
        )

        asyncio.run(
            self.process._on_appliance_updated_by_redis(None, new_appliance)
        )

        self.assertEqual(self.process.schedule.await_count, 1)
        self.assertEqual(self.process._schedule_by_trigger_fork.call_count, 1)
