# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import home

import logging

from typing import Iterable, List, Tuple
from home.scheduler.trigger.state import Trigger as Parent
from home.scheduler.trigger.protocol.delay import Delay


class Trigger(Parent):
    """
    A scheduler trigger that fires *timeout_seconds* after the appliance
    is in the specified state.

    This trigger itself carries no events (``events`` is always ``[]``);
    when the appliance state matches, :py:meth:`fork` is called to create
    a one-shot :py:class:`date.resettable.Trigger` that fires after the
    configured delay and delivers the actual events.  If the state is
    matched again before the timer expires, the old pending trigger is
    disabled and a fresh timer is started.

    Subclasses (:py:class:`entering.delay.Trigger`,
    :py:class:`exiting.delay.Trigger`) further restrict the match to
    state *entry* or *exit* transitions respectively.
    """

    def __init__(
        self,
        name: str,
        events: Iterable[home.Event],
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

        :param name: human-readable trigger name used in log messages
        :param events: events to deliver when the forked date trigger fires
        :param state: the :py:attr:`State.VALUE` string that must match
        :param timeout_seconds: delay in seconds before the forked trigger fires
        """
        super(Trigger, self).__init__(name, events, state)
        self._delay = Delay(
            "delay trigger for {}".format(name),
            events,
            timeout_seconds,
            self._timezone,
        )
        self._events = (
            []
        )  # this trigger has no events, wait for the forked trigger
        self._timeout = timeout_seconds
        self._logger = logging.getLogger(__name__)

    def __str__(self):
        s = ", state delay: %s" % self._timeout
        return super(Trigger, self).__str__() + s

    def fork(
        self, performer: home.Performer
    ) -> List[Tuple[home.Performer, "home.scheduler.Trigger"]]:
        """
        Create a one-shot :py:class:`date.resettable.Trigger` that will
        fire after the configured delay and deliver events to *performer*.

        If a previous forked trigger for the same performer is still
        pending, it is disabled before the new one is created.

        :param performer: the performer to notify when the timer expires
        :return: list containing one ``(performer, resettable_trigger)`` pair
        """
        return self._delay.fork(performer)
