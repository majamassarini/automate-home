# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import ABC, abstractmethod
from collections import defaultdict

import home
from home.protocol.message import Unknown


class MyHome(ABC):
    """
    Abstract base class for a concrete home configuration.

    Every deployment subclasses ``MyHome`` and implements the five
    ``_build_*`` factory methods to declare:

    * the appliances present in the home,
    * the performers that translate appliance state into protocol messages,
    * logical groups of performers,
    * the scheduler triggers (state-based, protocol-based, cron, …), and
    * the ``(performers, triggers)`` pairs that wire them together.

    On construction the instance builds all lookup tables so that
    :py:class:`Process` can efficiently resolve performers and triggers
    at runtime.
    """

    #: Seconds APScheduler is allowed to run a misfired job late before
    #: dropping it.  Set to three minutes to tolerate brief system load spikes.
    MISFIRE_GRACE_TIME = 180

    def __init__(self):
        self._appliances = self._build_appliances()
        self._performers = self._build_performers()
        self._group_of_performers = dict()
        self._performers_by_scheduler_trigger = defaultdict(list)
        self._performers_by_appliance = defaultdict(list)
        group_of_performers = self._build_group_of_performers()
        for key, value in group_of_performers.items():
            self._group_of_performers[key] = home.Performers(value)
        for performer in self.performers:
            self._group_of_performers[performer.name] = home.Performers(
                [performer]
            )
        for collection in self.appliances.values():
            for appliance in collection:
                self._performers_by_appliance[appliance] = [
                    p for p in self.performers if p.is_for(appliance)
                ]
        self._commands = list()
        for performers in self.performers:
            self._commands.extend(performers.commands)
        self._triggers = list()
        for performers in self.performers:
            self._triggers.extend(performers.triggers)

        self._performers_by_trigger = defaultdict(list)
        self._scheduler_triggers = self._build_scheduler_triggers()
        self._scheduler_triggers_by_name = defaultdict(list)
        for scheduler_trigger in self._scheduler_triggers:
            self._scheduler_triggers_by_name[scheduler_trigger.name].append(
                scheduler_trigger
            )
        self._schedule_infos = list()
        self._schedule_infos = self._build_schedule_infos()
        self._scheduler_triggers_by_performer = defaultdict(list)

        self._protocol_event_triggers = list()
        self._scheduler_event_triggers = list()
        self._appliance_state_triggers = list()

    @property
    def appliances(self):
        """All appliance collections, keyed by category name."""
        return self._appliances

    @property
    def scheduler_triggers(self):
        """Flat list of all scheduler triggers defined for this home."""
        return self._scheduler_triggers

    @property
    def performers(self):
        """Flat list of all performers defined for this home."""
        return self._performers

    @property
    def group_of_performers(self):
        """
        Dictionary mapping group name to a :py:class:`Performers` instance.

        Each individual performer is also accessible by its own name.
        """
        return self._group_of_performers

    @property
    def schedule_infos(self):
        """
        List of ``(Performers, triggers)`` pairs built by
        :py:meth:`_build_schedule_infos`.

        Used by :py:meth:`schedule` to register jobs with APScheduler.
        """
        return self._schedule_infos

    @abstractmethod
    def _build_appliances(self):
        """Return the :py:class:`Collection` of all appliances."""
        ...

    @abstractmethod
    def _build_performers(self):
        """Return the list of all :py:class:`Performer` instances."""
        ...

    @abstractmethod
    def _build_group_of_performers(self):
        """
        Return a dict mapping group name to a list of performers.

        Groups allow a single scheduler trigger to notify several
        performers at once.
        """
        ...

    @abstractmethod
    def _build_scheduler_triggers(self):
        """Return the list of all scheduler triggers."""
        ...

    @abstractmethod
    def _build_schedule_infos(self):
        """
        Return the list of ``(performers, triggers)`` pairs that
        associate scheduler triggers with performers.
        """
        ...

    def schedule_performer(self, scheduler, callable, performer, trigger):
        """
        Register a single ``(performer, trigger)`` job with APScheduler
        and update the internal lookup tables.

        :param scheduler: the APScheduler ``AsyncIOScheduler`` instance
        :param callable: the coroutine to call when the trigger fires
            (typically :py:meth:`Process.schedule`)
        :param performer: the performer to pass as the first argument
        :param trigger: the scheduler trigger to pass as the second argument
            and use as the APScheduler firing trigger
        """
        scheduler.add_job(
            callable,
            trigger,
            args=(performer, trigger),
            misfire_grace_time=self.MISFIRE_GRACE_TIME,
            coalesce=False,
        )
        self._performers_by_scheduler_trigger[trigger].append(performer)
        self._scheduler_triggers_by_performer[performer].append(trigger)

    def schedule(self, scheduler, callable):
        """
        Register all ``(performer, trigger)`` jobs from
        :py:attr:`schedule_infos` with APScheduler and build the
        protocol-trigger-to-performer lookup table.

        Called once during startup, before the event loop starts.

        :param scheduler: the APScheduler ``AsyncIOScheduler`` instance
        :param callable: the coroutine to invoke when a trigger fires
            (typically :py:meth:`Process.schedule`)
        """
        for performers, triggers in self._schedule_infos:
            for performer in performers:
                for trigger in triggers:
                    if not isinstance(trigger, Unknown):
                        self.schedule_performer(
                            scheduler, callable, performer, trigger
                        )

        for trigger in self._triggers:
            for performers in self._group_of_performers.values():
                for performer in performers:
                    if performer.has(trigger):
                        self._performers_by_trigger[trigger].append(performer)

    def commands_by(self, protocol):
        """
        Return all commands that belong to *protocol*, or every command
        if *protocol* is ``None``.

        :param protocol: a protocol identifier string, or ``None``
        :return: list of matching commands
        """
        return [
            command
            for command in self._commands
            if command.PROTOCOL == protocol or protocol is None
        ]

    def triggers_by(self, protocol):
        """
        Return all protocol triggers that belong to *protocol*, or every
        trigger if *protocol* is ``None``.

        :param protocol: a protocol identifier string, or ``None``
        :return: list of matching triggers
        """
        return [
            trigger
            for trigger in self._triggers
            if trigger.PROTOCOL == protocol or protocol is None
        ]

    def find_scheduler_triggers(self, name):
        """
        Return all scheduler triggers registered under *name*.

        :param name: the trigger name
        :return: list of matching scheduler triggers (may be empty)
        """
        return self._scheduler_triggers_by_name[name]

    def find_scheduler_trigger_by_performer(self, performer):
        """
        Return all scheduler triggers associated with *performer*.

        :param performer: a :py:class:`Performer` instance
        :return: list of scheduler triggers (may be empty)
        """
        return self._scheduler_triggers_by_performer[performer]

    def find_group_of_performers(self, name):
        """
        Return the :py:class:`Performers` group registered under *name*.

        :param name: the group name
        :return: a :py:class:`Performers` instance
        """
        return self._group_of_performers[name]

    def find_performers_by_trigger(self, trigger):
        """
        Return all performers that listen to the given protocol *trigger*.

        :param trigger: a protocol trigger instance
        :return: list of matching performers (may be empty)
        """
        return self._performers_by_trigger[trigger]

    def find_performers_by_appliance(self, appliance):
        """
        Return all performers associated with *appliance*.

        :param appliance: an :py:class:`Appliance` instance
        :return: list of matching performers (may be empty)
        """
        return self._performers_by_appliance[appliance]

    def find_performers_by_scheduler_trigger(self, scheduler_trigger):
        """
        Return all performers registered for the given *scheduler_trigger*.

        :param scheduler_trigger: a scheduler trigger instance
        :return: list of matching performers (may be empty)
        """
        return self._performers_by_scheduler_trigger[scheduler_trigger]
