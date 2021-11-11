# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging

from typing import Iterable, List, Tuple
from home.scheduler.trigger.state import Trigger as Parent
from home.scheduler.trigger.protocol.delay import Delay


class Trigger(Parent):
    """
    A **Scheduler Trigger** triggered *timeout_seconds* after a given **Appliance state** has been triggered.
    If an *Appliance state* has been triggered twice, the old scheduler trigger is disabled and a new one is started.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        state: str,
        timeout_seconds: float,
    ):
        """
        >>> import home
        >>> t = Trigger("a delay trigger", [1, 2], "Off", 0.1)
        >>> t.events
        []
        >>> p = home.Performer("pippo", home.appliance.light.Appliance("a light", []), [], [])
        >>> l = t.fork(p)
        >>> (_, resettable_trigger) = l[0]
        >>> resettable_trigger.events
        [1, 2]
        >>> resettable_trigger.is_enabled
        True
        >>> l = t.fork(p)
        >>> (_, new_resettable_trigger) = l[0]
        >>> resettable_trigger.is_enabled
        False
        >>> new_resettable_trigger.events
        [1, 2]
        >>> new_resettable_trigger.is_enabled
        True

        :param name: the scheduler trigger name
        :param events: events to be notified
        :param state: a str representing a state
        :param timeout_seconds: starts a new scheduler trigger that will be triggered in timeout seconds
        """
        super(Trigger, self).__init__(name, events, state)
        self._delay = Delay(
            "delay trigger for {}".format(name), events, timeout_seconds, self._timezone
        )
        self._events = []  # this trigger has no events, wait for the forked trigger
        self._timeout = timeout_seconds
        self._logger = logging.getLogger(__name__)

    def __str__(self):
        s = ", state delay: %s" % self._timeout
        return super(Trigger, self).__str__() + s

    def fork(
        self, performer: "home.Performer"
    ) -> List[Tuple["home.Performer", "home.scheduler.Trigger"]]:
        return self._delay.fork(performer)
