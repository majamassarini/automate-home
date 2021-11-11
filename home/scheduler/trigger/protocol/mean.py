# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import collections
import functools
import datetime
import logging

from typing import Iterable
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger.protocol import Trigger as Parent


class Trigger(Parent, BaseTrigger):
    """
    A **Scheduler Trigger** which collects **Protocol Trigger** values in a time base.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        protocol_trigger: "home.protocol.mean.Mixin",
        num_of_samples: int,
        timeout_seconds: float,
    ):
        """
        :param name: the scheduler trigger name
        :param events: events to be notified
        :param protocol_trigger: a protocol trigger
        :param num_of_samples: num of samples for calculating mean value
        :param timeout_seconds: starts a new scheduler trigger that will be triggered in timeout seconds
        """
        super(Trigger, self).__init__(name, events, protocol_trigger)
        self._timeout = timeout_seconds
        self._last_compared_value = 0
        self._samples = collections.deque(maxlen=num_of_samples)
        self._mean = 0
        self._logger = logging.getLogger(__name__)

    @property
    def mean(self):
        return self._mean

    def __str__(self):
        s = ", mean: %s" % self._timeout
        return super(Trigger, self).__str__() + s

    def update_mean(self, value):
        self._samples.append(value)
        self._mean = functools.reduce(lambda a, b: a + b, self._samples, 0) / len(
            self._samples
        )
        self._logger.debug(str(self._mean) + " ")

    def is_triggered(self, description: "home.protocol.Description") -> bool:
        if self._protocol_trigger.is_triggered(description):
            value = self._protocol_trigger.get_value(description)
            self._last_compared_value = value
            self.update_mean(value)
            return True

    def get_next_fire_time(self, _, now):
        self.update_mean(self._last_compared_value)
        result = now + datetime.timedelta(seconds=self._timeout)
        return result


class Comparison(Trigger):
    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        protocol_trigger: "home.protocol.mean.Mixin",
        num_of_samples: int,
        hit_value: float,
        timeout_seconds: float,
    ):
        super(Comparison, self).__init__(
            name, events, protocol_trigger, num_of_samples, timeout_seconds
        )
        self._hit_value = hit_value


class GreaterThan(Comparison):
    """
    A **Scheduler Trigger** triggered when collected **Protocol Trigger**
    values in a time base are greater than given hit value.

    >>> import sys
    >>> import home
    >>> import asyncio
    >>> from apscheduler.schedulers.asyncio import AsyncIOScheduler
    >>>
    >>> class PT(home.protocol.Trigger, home.protocol.mean.Mixin):
    ...     def __init__(self, description, events):
    ...         super(PT, self).__init__(description, events)
    ...         self._values = [8, 6, 5, 2, ]
    ...     def is_triggered(self, another_description):
    ...         return True
    ...     def make(self):
    ...         ...
    ...     def make_from(cls, msg):
    ...         ...
    ...     def get_value(self, description):
    ...         try:
    ...             return self._values.pop()
    ...         except IndexError:
    ...             return 5
    >>>
    >>> async def wait_for_mean(scheduler_trigger, protocol_trigger):
    ...     while not scheduler_trigger.is_triggered(protocol_trigger):
    ...         await asyncio.sleep(0.01)
    ...     asyncio.get_event_loop().stop()
    >>>
    >>> protocol_trigger = PT({"a": "description"}, ["an event"])
    >>> scheduler_trigger = home.scheduler.trigger.protocol.mean.GreaterThan("a mean scheduler trigger",
    ...                                                                      ["another event"],
    ...                                                                      protocol_trigger,
    ...                                                                      10,
    ...                                                                      4,
    ...                                                                      0.1)
    >>> scheduler = AsyncIOScheduler()
    >>> performer = home.Performer("pippo", home.appliance.light.Appliance("a light", []), [], [])
    >>> job = scheduler.add_job(wait_for_mean,
    ...                         scheduler_trigger,
    ...                         args=(scheduler_trigger, protocol_trigger, ),
    ...                         misfire_grace_time=180,
    ...                         coalesce=False)
    >>> scheduler.start()
    >>> asyncio.get_event_loop().run_forever()
    """

    def is_triggered(self, description: "home.protocol.Description") -> bool:
        if super(GreaterThan, self).is_triggered(description):
            if self.mean > self._hit_value:
                return True

    @property
    def is_enabled(self):
        if self.mean > self._hit_value:
            return True


class LesserThan(Comparison):
    """
    A **Scheduler Trigger** triggered when collected **Protocol Trigger**
    values in a time base are lesser than given hit value.

    >>> import sys
    >>> import home
    >>> import asyncio
    >>> from apscheduler.schedulers.asyncio import AsyncIOScheduler
    >>>
    >>> class PT(home.protocol.Trigger, home.protocol.mean.Mixin):
    ...     def __init__(self, description, events):
    ...         super(PT, self).__init__(description, events)
    ...         self._values = [2, 3, 5, 8]
    ...     def is_triggered(self, another_description):
    ...         return True
    ...     def make(self):
    ...         ...
    ...     def make_from(cls, msg):
    ...         ...
    ...     def get_value(self, description):
    ...         try:
    ...             return self._values.pop()
    ...         except IndexError:
    ...             return 4
    >>>
    >>> async def wait_for_mean(scheduler_trigger, protocol_trigger):
    ...     while not scheduler_trigger.is_triggered(protocol_trigger):
    ...         await asyncio.sleep(0.01)
    ...     asyncio.get_event_loop().stop()
    >>>
    >>> protocol_trigger = PT({"a": "description"}, ["an event"])
    >>> scheduler_trigger = home.scheduler.trigger.protocol.mean.LesserThan("a mean scheduler trigger",
    ...                                                                      ["another event"],
    ...                                                                      protocol_trigger,
    ...                                                                      10,
    ...                                                                      5,
    ...                                                                      0.1)
    >>> scheduler = AsyncIOScheduler()
    >>> performer = home.Performer("pippo", home.appliance.light.Appliance("a light", []), [], [])
    >>> job = scheduler.add_job(wait_for_mean,
    ...                         scheduler_trigger,
    ...                         args=(scheduler_trigger, protocol_trigger, ),
    ...                         misfire_grace_time=180,
    ...                         coalesce=False)
    >>> scheduler.start()
    >>> asyncio.get_event_loop().run_forever()
    """

    def is_triggered(self, description: "home.protocol.Description") -> bool:
        if super(LesserThan, self).is_triggered(description):
            if self.mean < self._hit_value:
                return True

    @property
    def is_enabled(self):
        if self.mean < self._hit_value:
            return True


class InBetween(Trigger):
    """
    A **Scheduler Trigger** triggered when collected **Protocol Trigger**
    values in a time base are lesser than max value and greater than min value.

    >>> import sys
    >>> import home
    >>> import asyncio
    >>> from apscheduler.schedulers.asyncio import AsyncIOScheduler
    >>>
    >>> class PT(home.protocol.Trigger, home.protocol.mean.Mixin):
    ...     def __init__(self, description, events):
    ...         super(PT, self).__init__(description, events)
    ...         self._values = [8, 6, 5, 2, 4]
    ...     def is_triggered(self, another_description):
    ...         return True
    ...     def make(self):
    ...         ...
    ...     def make_from(cls, msg):
    ...         ...
    ...     def get_value(self, description):
    ...         try:
    ...             return self._values.pop()
    ...         except IndexError:
    ...             return 4
    >>>
    >>> async def wait_for_mean(scheduler_trigger, protocol_trigger):
    ...     while not scheduler_trigger.is_triggered(protocol_trigger):
    ...         await asyncio.sleep(0.01)
    ...     asyncio.get_event_loop().stop()
    >>>
    >>> protocol_trigger = PT({"a": "description"}, ["an event"])
    >>> scheduler_trigger = home.scheduler.trigger.protocol.mean.InBetween("a mean scheduler trigger",
    ...                                                                      ["another event"],
    ...                                                                      protocol_trigger,
    ...                                                                      10,
    ...                                                                      4,
    ...                                                                      5,
    ...                                                                      0.1)
    >>> scheduler = AsyncIOScheduler()
    >>> performer = home.Performer("pippo", home.appliance.light.Appliance("a light", []), [], [])
    >>> job = scheduler.add_job(wait_for_mean,
    ...                         scheduler_trigger,
    ...                         args=(scheduler_trigger, protocol_trigger, ),
    ...                         misfire_grace_time=180,
    ...                         coalesce=False)
    >>> scheduler.start()
    >>> asyncio.get_event_loop().run_forever()
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        protocol_trigger: "home.protocol.mean.Mixin",
        num_of_samples: int,
        min_value: float,
        max_value: float,
        timeout_seconds: float,
    ):
        super(InBetween, self).__init__(
            name, events, protocol_trigger, num_of_samples, timeout_seconds
        )
        self._min_value = min_value
        self._max_value = max_value

    def is_triggered(self, description: "home.protocol.Description") -> bool:
        if super(InBetween, self).is_triggered(description):
            if self._min_value < self.mean < self._max_value:
                return True

    @property
    def is_enabled(self):
        if self._min_value < self.mean < self._max_value:
            return True
