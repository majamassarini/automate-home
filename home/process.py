# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import logging
import sys

import home

sys.path.append("..")


class Process(object):
    def __init__(self, my_home, redis_gateway):
        self._my_home = my_home
        self._appliances = {
            appliance.name: appliance
            for collection in my_home.appliances.values()
            for appliance in collection
        }
        self._performers = my_home.performers
        self._redis_gateway = redis_gateway

        self._protocols = []
        self._protocols_writers = []

        self._queue = None

        self._logger = logging.getLogger(__name__)

    async def disconnect(self):
        await self._redis_gateway.disconnect()
        for gateway in self._protocols:
            await gateway.disconnect()

    def add(self, protocol):
        self._protocols.append(protocol)
        self._protocols_writers = [protocol.writer for protocol in self._protocols]

    async def schedule(self, performer, trigger):
        await self._queue.put((performer, trigger, trigger.events))

    async def _schedule_by_appliance_state(
        self, scheduler, appliance, old_state, new_state
    ):
        for performer in self._my_home.find_performers_by_appliance(appliance):
            for scheduler_trigger in self._my_home.find_scheduler_trigger_by_performer(
                performer
            ):
                if scheduler_trigger.type == home.scheduler.trigger.state.Trigger.type:
                    if scheduler_trigger.is_triggered(old_state, new_state):
                        await self.schedule(performer, scheduler_trigger)
                        self._schedule_by_trigger_fork(
                            scheduler, scheduler_trigger, performer
                        )

    def _schedule_by_trigger_fork(self, scheduler, trigger, performer):
        for another_performer, another_trigger in trigger.fork(performer):
            self._my_home.schedule_performer(
                scheduler, self.schedule, another_performer, another_trigger
            )

    async def _schedule_by_protocol_trigger(self, trigger):
        for scheduler_trigger in self._my_home.scheduler_triggers:
            if scheduler_trigger.type == home.scheduler.trigger.protocol.Trigger.type:
                try:
                    triggered = scheduler_trigger.is_triggered(trigger)
                except Exception as e:
                    triggered = False
                    self._logger.debug(e)
                if triggered:
                    for performer in self._my_home.find_performers_by_scheduler_trigger(
                        scheduler_trigger
                    ):
                        await self.schedule(performer, scheduler_trigger)

    async def _update_performers_by_protocol_trigger(self, scheduler, trigger):
        for performer in self._my_home.find_performers_by_trigger(trigger):
            try:
                old_state, new_state = performer.update_by(trigger)
                if old_state and new_state:
                    await self._schedule_by_appliance_state(
                        scheduler, performer.appliance, old_state, new_state
                    )
                    msgs = performer.execute(old_state, new_state)
                    await self._redis_gateway.on_appliance_updated_by_process(
                        performer.appliance, old_state, new_state
                    )
                    if msgs:
                        for writer in self._protocols_writers:
                            await writer(msgs, performer)
            except Exception as e:
                self._logger.error(e)

    async def _on_appliance_updated_by_redis(self, scheduler, new_appliance):
        old_appliance = self._appliances[new_appliance.name]
        old_state, new_state = old_appliance.update(new_appliance)
        self._logger.debug("Appliance {} updated by redis".format(new_appliance.name))
        for performer in [
            performer
            for performer in self._performers
            if performer.is_for(old_appliance)
        ]:
            if (
                not performer.triggers
            ):  # otherwise it must be executed when a trigger is triggered...
                try:
                    await self._schedule_by_appliance_state(
                        scheduler, performer.appliance, old_state, new_state
                    )
                    msgs = performer.execute(old_state, new_state)
                    if msgs:
                        self._logger.info(
                            "Performer {} updated by redis will send {}".format(
                                performer.name, msgs
                            )
                        )
                    for writer in self._protocols_writers:
                        await writer(msgs, performer)
                except Exception as e:
                    self._logger.error(e)

    async def _on_performer_updated_by_redis(self, performer, old_state, new_state):
        try:
            msgs = performer.execute(old_state, new_state)
            self._logger.debug("Performer {} updated by redis".format(performer.name))
            if msgs:
                self._logger.info(
                    "Performer {} updated by redis will send {}".format(
                        performer.name, msgs
                    )
                )
            for writer in self._protocols_writers:
                await writer(msgs, performer)
        except Exception as e:
            self._logger.error(e)


    async def _on_protocol_event(self, scheduler, trigger):
        await self._schedule_by_protocol_trigger(trigger)
        await self._update_performers_by_protocol_trigger(scheduler, trigger)

    async def _run(self, scheduler):
        while True:
            performer, trigger, events = await self._queue.get()
            if trigger.is_enabled and events:
                try:
                    msgs, old_state, new_state = performer.notify(events)
                    self._logger.debug(
                        "Performer {} notified by Scheduler Trigger {}".format(
                            performer.name, trigger.name
                        )
                    )
                    await self._redis_gateway.on_performer_updated_by_process(
                        performer, old_state, new_state
                    )
                    if msgs:
                        self._logger.info(
                            "Performer {} called by Protocol Trigger {} will send {}".format(
                                performer.name, trigger.name, msgs
                            )
                        )
                    for writer in self._protocols_writers:
                        await writer(msgs, performer)

                    await self._schedule_by_appliance_state(
                        scheduler, performer.appliance, old_state, new_state
                    )
                except Exception as e:
                    self._logger.error(e)
            if trigger.is_enabled:
                try:
                    self._schedule_by_trigger_fork(scheduler, trigger, performer)
                except Exception as e:
                    self._logger.error(e)

    def create_tasks(self, loop, scheduler):
        self._queue = asyncio.Queue()
        loop.create_task(self._run(scheduler), name="Process _run(scheduler)")
        for gateway in self._protocols:
            loop.create_task(
                gateway.run(
                    [lambda trigger: self._on_protocol_event(scheduler, trigger)]
                ),
                name=("On protocol {} event".format(gateway.PROTOCOL))
            )
        scheduler.start()

    async def monitor(self):
        while True:
            self._logger.warning("\n\nNew tasks:\n")
            for task in asyncio.all_tasks():
                self._logger.warning(task.get_name())
            await asyncio.sleep(180)

    def run(self, scheduler):
        loop = asyncio.get_event_loop()
        loop.set_debug(enabled=False)
        self.create_tasks(loop, scheduler)
        loop.create_task(self.monitor(), name="monitor")
        try:
            loop.run_until_complete(self._redis_gateway.connect())
            self._redis_gateway.create_tasks(
                loop,
                lambda new_appliance: self._on_appliance_updated_by_redis(
                    scheduler, new_appliance
                ),
                self._on_performer_updated_by_redis,
            )
            loop.run_forever()
        except KeyboardInterrupt as e:
            self._logger.error(e)
            loop.run_until_complete(self.disconnect())
            loop.close()
        finally:
            loop.run_until_complete(self.disconnect())
            loop.close()
