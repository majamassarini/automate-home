# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import ABCMeta
import datetime
import logging
from tzlocal import get_localzone
from typing import Iterable, List, Tuple


registry = list()


def register_class(target_class):
    klass = "{}.{}".format(
        target_class.__module__.replace(".definition", "").replace(
            "home.scheduler.trigger.", ""
        ),
        target_class.__name__,
    )
    registry.append(klass)


class Registry(ABCMeta):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        if name not in registry:
            register_class(cls)
        return cls


class Trigger(metaclass=Registry):
    """
    A *Scheduler Trigger*.

    When triggered, given *events* are notified to scheduled *Performers*.
    """

    @staticmethod
    @property
    def type(self):
        return "SCHEDULER EVENT"

    def __init__(self, name: str, events: Iterable["home.Event"], *args, **kwargs):
        super(Trigger, self).__init__(*args, **kwargs)
        self._name = name
        self._events = list()
        self._events.extend(events)
        self._timedelta_fire = datetime.timedelta(weeks=52)
        self._timezone = get_localzone()
        self._logger = logging.getLogger(__name__)

    def __str__(self):
        s = "scheduler.Trigger name: %s, events: %s, %s" % (
            self._name,
            str(self._events),
            super(Trigger, self).__str__(),
        )
        return s

    def fork(
        self, performer: "home.Performer"
    ) -> List[Tuple["home.Performer", "home.scheduler.Trigger"]]:
        """
        Starts new *Scheduler Triggers*.

        The new *Scheduler Triggers*, when triggered,
        will notify the given *Performer*.

        :param performer: a *Performer* to be notified
        :return: list of (*Performer*, *Scheduler Triggers*) couples
        """
        return []

    @property
    def is_enabled(self):
        return True

    @property
    def name(self) -> str:
        """
        :return: the *Scheduler Trigger* name
        """
        return self._name

    @property
    def events(self) -> Iterable["home.Event"]:
        """
        :return: *Events* to be notified
        """
        return self._events


from home.scheduler.trigger import cron
from home.scheduler.trigger import date
from home.scheduler.trigger import interval
from home.scheduler.trigger import protocol
from home.scheduler.trigger import state
from home.scheduler.trigger import sun
from home.scheduler.trigger import circadian_rhythm
from home.scheduler.trigger import crawler
