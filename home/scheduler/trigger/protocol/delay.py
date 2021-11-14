# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import datetime
import logging
import copy

from typing import Iterable, List, Tuple
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger import date
from home.scheduler.trigger.protocol import Trigger as Parent


class Delay:
    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        timeout_seconds: float,
        timezone,
    ):
        self._trigger_name = name
        self._scheduler_trigger_events = events
        self._protocol_trigger_events = []
        self._timeout = timeout_seconds
        self._timezone = timezone
        self._logger = logging.getLogger(__name__)
        self._last_resettable_trigger = {}  # one for every performer

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    @property
    def protocol_trigger_events(self):
        return self._protocol_trigger_events

    @protocol_trigger_events.setter
    def protocol_trigger_events(self, value: List['home.Event']):
        self._protocol_trigger_events = value

    def fork(
        self, performer: "home.Performer"
    ) -> List[Tuple["home.Performer", "home.scheduler.Trigger"]]:
        """
        Starts a new 'home.scheduler.date.resettable.Trigger' which will
        be triggered in *timeout* seconds unless reset.

        When triggered will notify the given Performer.

        :param performer: a *Performer* to be notified
        :return: a list of (performer, trigger) couples
        """
        result = list()
        name = "date.resettable.Trigger for parent trigger {} and performer {}".format(
            self._trigger_name, performer.name
        )
        run_date = datetime.datetime.now() + datetime.timedelta(seconds=self._timeout)
        if name in self._last_resettable_trigger:
            self._last_resettable_trigger[name].disable()
        self._last_resettable_trigger[name] = date.resettable.Trigger(
            name, (self._scheduler_trigger_events + self.protocol_trigger_events), run_date=run_date, timezone=self._timezone
        )
        result.append((performer, self._last_resettable_trigger[name]))
        return result


class Trigger(Parent, BaseTrigger):
    """
    A **Scheduler Trigger** triggered *timeout_seconds* after its **Protocol Trigger** has been triggered.
    If the *Protocol Trigger* has been triggered twice, the old scheduler trigger is disabled and new one is started.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        protocol_trigger: "home.protocol.Trigger",
        timeout_seconds: float,
    ):
        """
        >>> import home
        >>> class PT(home.protocol.Trigger):
        ...     def is_triggered(self):
        ...         return True
        ...     @property
        ...     def events(self):
        ...         return [3]
        ...     def make(self):
        ...         ...
        ...     def make_from(cls, msg):
        ...         ...
        >>> t = Trigger("a delay trigger", [1, 2], PT(object), 0.1)
        >>> t.events
        []
        >>> p = home.Performer("pippo", home.appliance.light.Appliance("a light", []), [], [])
        >>> l = t.fork(p)
        >>> (_, resettable_trigger) = l[0]
        >>> resettable_trigger.events
        [1, 2, 3]
        >>> resettable_trigger.is_enabled
        True
        >>> l = t.fork(p)
        >>> (_, new_resettable_trigger) = l[0]
        >>> resettable_trigger.is_enabled
        False
        >>> new_resettable_trigger.events
        [1, 2, 3]
        >>> new_resettable_trigger.is_enabled
        True

        :param name: the scheduler trigger name
        :param events: events to be notified
        :param protocol_trigger: a protocol trigger
        :param timeout_seconds: starts a new scheduler trigger that will be triggered in timeout seconds
        """
        super(Trigger, self).__init__(name, events, protocol_trigger)
        self._delay = Delay(
            self.name, copy.deepcopy(events), timeout_seconds, self._timezone
        )
        self._timeout = timeout_seconds
        self._logger = logging.getLogger(__name__)

    @property
    def events(self):
        # this trigger has no events, wait for the forked trigger
        return []

    def __str__(self):
        s = ", delay: %s" % self._timeout
        return super(Trigger, self).__str__() + s

    def fork(
        self, performer: "home.Performer"
    ) -> List[Tuple["home.Performer", "home.scheduler.Trigger"]]:
        self._delay.protocol_trigger_events = self._protocol_trigger.events
        return self._delay.fork(performer)
