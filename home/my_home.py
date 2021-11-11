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
            self._group_of_performers[performer.name] = home.Performers([performer])
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
        return self._appliances

    @property
    def scheduler_triggers(self):
        return self._scheduler_triggers

    @property
    def performers(self):
        return self._performers

    @property
    def group_of_performers(self):
        return self._group_of_performers

    @property
    def schedule_infos(self):
        return self._schedule_infos

    @abstractmethod
    def _build_appliances(self):
        ...

    @abstractmethod
    def _build_performers(self):
        ...

    @abstractmethod
    def _build_group_of_performers(self):
        ...

    @abstractmethod
    def _build_scheduler_triggers(self):
        ...

    @abstractmethod
    def _build_schedule_infos(self):
        ...

    def schedule_performer(self, scheduler, callable, performer, trigger):
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
        for performers, triggers in self._schedule_infos:
            for performer in performers:
                for trigger in triggers:
                    if not isinstance(trigger, Unknown):
                        self.schedule_performer(scheduler, callable, performer, trigger)

        for trigger in self._triggers:
            for performers in self._group_of_performers.values():
                for performer in performers:
                    if performer.has(trigger):
                        self._performers_by_trigger[trigger].append(performer)

    def commands_by(self, protocol):
        return [
            command
            for command in self._commands
            if command.PROTOCOL == protocol or protocol is None
        ]

    def triggers_by(self, protocol):
        return [
            trigger
            for trigger in self._triggers
            if trigger.PROTOCOL == protocol or protocol is None
        ]

    def find_scheduler_triggers(self, name):
        return self._scheduler_triggers_by_name[name]

    def find_scheduler_trigger_by_performer(self, performer):
        return self._scheduler_triggers_by_performer[performer]

    def find_group_of_performers(self, name):
        return self._group_of_performers[name]

    def find_performers_by_trigger(self, trigger):
        return self._performers_by_trigger[trigger]

    def find_performers_by_appliance(self, appliance):
        return self._performers_by_appliance[appliance]

    def find_performers_by_scheduler_trigger(self, scheduler_trigger):
        return self._performers_by_scheduler_trigger[scheduler_trigger]
