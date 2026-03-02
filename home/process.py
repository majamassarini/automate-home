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
    """
    Central orchestrator that routes events between protocol gateways,
    the Redis pub/sub layer, and the home appliance state machines.

    At runtime a single async queue (``_queue``) decouples event producers
    from consumers.  Protocol gateways push incoming bus messages via
    callbacks; APScheduler jobs push timed events via :py:meth:`schedule`.
    The :py:meth:`_run` coroutine drains the queue and dispatches each
    item to the appropriate handler.

    Typical lifecycle::

        process = Process(my_home, redis_gateway)
        process.add(knx_gateway)
        process.run(scheduler)           # blocks until KeyboardInterrupt
    """

    def __init__(self, my_home, redis_gateway):
        """
        :param my_home: the :py:class:`MyHome` instance holding all
            appliances, performers, and scheduler triggers
        :param redis_gateway: the Redis gateway used for inter-node
            state synchronisation
        """
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
        """Disconnect the Redis gateway and all registered protocol gateways."""
        await self._redis_gateway.disconnect()
        for gateway in self._protocols:
            await gateway.disconnect()

    def add(self, protocol):
        """
        Register a protocol gateway.

        :param protocol: a protocol gateway with a ``writer`` coroutine
            that sends messages onto the bus
        """
        self._protocols.append(protocol)
        self._protocols_writers = [
            protocol.writer for protocol in self._protocols
        ]

    async def schedule(self, performer, trigger):
        """
        Enqueue a ``(performer, trigger, events)`` tuple for processing
        by the :py:meth:`_run` loop.

        Called by APScheduler when a scheduled job fires.

        :param performer: the performer to notify
        :param trigger: the trigger that fired (used for the
            ``is_enabled`` check and event dispatch type)
        """
        await self._queue.put((performer, trigger, trigger.events))

    async def _schedule_by_appliance_state(
        self, scheduler, appliance, old_state, new_state
    ):
        """
        Examine every state-type scheduler trigger registered for the
        performers of *appliance* and, for each one that matches the
        state transition, enqueue its events and fork any delayed triggers.

        :param scheduler: the APScheduler instance used to register forked jobs
        :param appliance: the appliance whose state just changed
        :param old_state: the appliance state before the change
        :param new_state: the appliance state after the change
        """
        for performer in self._my_home.find_performers_by_appliance(appliance):
            for (
                scheduler_trigger
            ) in self._my_home.find_scheduler_trigger_by_performer(performer):
                if (
                    scheduler_trigger.type
                    == home.scheduler.trigger.state.Trigger.type
                ):
                    if scheduler_trigger.is_triggered(old_state, new_state):
                        await self.schedule(performer, scheduler_trigger)
                        self._schedule_by_trigger_fork(
                            scheduler, scheduler_trigger, performer
                        )

    def _schedule_by_trigger_fork(self, scheduler, trigger, performer):
        """
        Ask *trigger* to produce forked date triggers for *performer* and
        register each one with APScheduler.

        :param scheduler: the APScheduler instance
        :param trigger: the trigger whose :py:meth:`fork` method is called
        :param performer: the performer to associate with the forked triggers
        """
        for another_performer, another_trigger in trigger.fork(performer):
            self._my_home.schedule_performer(
                scheduler, self.schedule, another_performer, another_trigger
            )

    async def _schedule_by_protocol_trigger(self, trigger):
        """
        Check every protocol-type scheduler trigger and enqueue those
        that match the incoming protocol *trigger*.

        :param trigger: the protocol trigger received from the bus
        """
        for scheduler_trigger in self._my_home.scheduler_triggers:
            if (
                scheduler_trigger.type
                == home.scheduler.trigger.protocol.Trigger.type
            ):
                try:
                    triggered = scheduler_trigger.is_triggered(trigger)
                except Exception as e:
                    triggered = False
                    self._logger.debug(e)
                if triggered:
                    for (
                        performer
                    ) in self._my_home.find_performers_by_scheduler_trigger(
                        scheduler_trigger
                    ):
                        await self.schedule(performer, scheduler_trigger)

    async def _update_performers_by_protocol_trigger(self, scheduler, trigger):
        """
        Apply a protocol trigger to every performer that listens to it.

        For each matching performer the appliance state is updated, any
        state-based scheduler triggers are evaluated, the resulting
        protocol messages are sent, and the Redis gateway is notified.

        :param scheduler: the APScheduler instance (forwarded to
            :py:meth:`_schedule_by_appliance_state`)
        :param trigger: the protocol trigger received from the bus
        """
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
        """
        React to an appliance state update broadcast by another node via Redis.

        The local appliance is updated to match the received state, then
        every trigger-less performer for that appliance is executed and its
        protocol messages are sent.

        :param scheduler: the APScheduler instance
        :param new_appliance: the updated appliance received from Redis
        """
        old_appliance = self._appliances[new_appliance.name]
        old_state, new_state = old_appliance.update(new_appliance)
        self._logger.debug(
            "Appliance {} updated by redis ({} -> {})".format(
                new_appliance.name, old_state.compute(), new_state.compute()
            )
        )
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
                        self._logger.debug(
                            "Performer {} sending {} ({} -> {})".format(
                                performer.name,
                                msgs,
                                old_state.compute(),
                                new_state.compute(),
                            )
                        )
                    for writer in self._protocols_writers:
                        await writer(msgs, performer)
                except Exception as e:
                    self._logger.error(e)

    async def _on_performer_updated_by_redis(
        self, performer, old_state, new_state
    ):
        """
        Execute a performer whose state was updated directly by Redis
        (e.g. because another node sent a command) and send the resulting
        protocol messages.

        :param performer: the performer to execute
        :param old_state: the appliance state before the Redis update
        :param new_state: the appliance state after the Redis update
        """
        try:
            msgs = performer.execute(old_state, new_state)
            self._logger.debug(
                "Performer {} updated by redis".format(performer.name)
            )
            if msgs:
                self._logger.debug(
                    "Performer {} sending {} ({} -> {})".format(
                        performer.name,
                        msgs,
                        old_state.compute(),
                        new_state.compute(),
                    )
                )
            for writer in self._protocols_writers:
                await writer(msgs, performer)
        except Exception as e:
            self._logger.error(e)

    async def _on_protocol_event(self, scheduler, trigger):
        """
        Handle an incoming protocol event end-to-end: first check
        protocol-based scheduler triggers, then update performers.

        :param scheduler: the APScheduler instance
        :param trigger: the protocol trigger received from the bus
        """
        await self._schedule_by_protocol_trigger(trigger)
        await self._update_performers_by_protocol_trigger(scheduler, trigger)

    async def _run(self, scheduler):
        """
        Async queue consumer: continuously drain the event queue and
        dispatch each ``(performer, trigger, events)`` item.

        Dispatch rules:

        * :py:class:`state.entering.disable_events.Trigger` →
          disable each event in the appliance state machine.
        * :py:class:`date.enable_events.Trigger` →
          re-enable each event in the appliance state machine.
        * Any other trigger → notify the performer, publish the state
          change to Redis, send protocol messages, and evaluate
          state-based scheduler triggers.

        Items with a disabled trigger or an empty event list are silently
        skipped.  After processing, :py:meth:`_schedule_by_trigger_fork`
        is called so that recurring triggers can re-arm themselves.

        :param scheduler: the APScheduler instance (forwarded to
            :py:meth:`_schedule_by_appliance_state`)
        """
        while True:
            performer, trigger, events = await self._queue.get()
            if trigger.is_enabled and events:
                try:
                    if isinstance(
                        trigger,
                        home.scheduler.trigger.state.entering.disable_events.Trigger,
                    ):
                        for event in events:
                            performer.appliance.disable(event)
                        self._logger.debug(
                            "Performer {} disabled events {} by Trigger {}".format(
                                performer.name, events, trigger.name
                            )
                        )
                    elif isinstance(
                        trigger,
                        home.scheduler.trigger.date.enable_events.Trigger,
                    ):
                        for event in events:
                            performer.appliance.enable(event)
                        self._logger.debug(
                            "Performer {} enabled events {} by Trigger {}".format(
                                performer.name, events, trigger.name
                            )
                        )
                    else:
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
                                "Performer {} called by Protocol Trigger {}"
                                " will send {}".format(
                                    performer.name, trigger.name, msgs
                                )
                            )
                        for writer in self._protocols_writers:
                            await writer(msgs, performer)

                        await self._schedule_by_appliance_state(
                            scheduler,
                            performer.appliance,
                            old_state,
                            new_state,
                        )
                except Exception as e:
                    self._logger.error(e)
            if trigger.is_enabled:
                try:
                    self._schedule_by_trigger_fork(
                        scheduler, trigger, performer
                    )
                except Exception as e:
                    self._logger.error(e)

    def create_tasks(self, loop, scheduler):
        """
        Initialise the event queue, create all async tasks, and start
        the APScheduler.

        Must be called from within a running event loop (e.g. from an
        ``asyncSetUp`` coroutine or just before ``loop.run_forever()``).

        :param loop: the running :py:class:`asyncio.AbstractEventLoop`
        :param scheduler: an ``AsyncIOScheduler`` that has already been
            configured via :py:meth:`MyHome.schedule`
        """
        self._queue = asyncio.Queue()
        loop.create_task(self._run(scheduler), name="Process _run(scheduler)")
        for gateway in self._protocols:
            loop.create_task(
                gateway.run(
                    [
                        lambda trigger: self._on_protocol_event(
                            scheduler, trigger
                        )
                    ]
                ),
                name=("On protocol {} event".format(gateway.PROTOCOL)),
            )
        loop.call_soon(scheduler.start)

    async def monitor(self):
        """
        Periodically log all running asyncio tasks for debugging purposes.

        Sleeps for three minutes between each log entry.
        """
        while True:
            self._logger.debug("\n\nNew tasks:\n")
            for task in asyncio.all_tasks():
                self._logger.debug(task.get_name())
            await asyncio.sleep(180)

    def run(self, scheduler):
        """
        Start the asyncio event loop and run until a :py:exc:`KeyboardInterrupt`.

        Connects the Redis gateway, registers its callbacks, and then
        enters ``loop.run_forever()``.  On exit the loop is closed cleanly.

        :param scheduler: an ``AsyncIOScheduler`` that has already been
            configured via :py:meth:`MyHome.schedule`
        """
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
