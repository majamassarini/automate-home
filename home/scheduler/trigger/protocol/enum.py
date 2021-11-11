# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import enum
import logging

from typing import Iterable
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger.protocol import Trigger as Parent


class Direction(enum.Enum):
    previous = ("previous",)
    next = ("next",)


class Trigger(Parent, BaseTrigger):
    """
    A **Scheduler Trigger** triggered by a **Protocol Trigger**,
    when triggered will remove selected Event and add the next or previous
    Event chosen in the given enum Event class.
    The chosen Event will be added to the list of events to be notified.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        selected: "home.enum.definition.Event",
        direction: str,
        protocol_trigger: "home.protocol.Trigger",
    ):
        """
        >>> import home
        >>> class PT(home.protocol.Trigger):
        ...     def is_triggered(self, description):
        ...         return True
        ...     @property
        ...     def events(self):
        ...         return [3]
        ...     def make(self):
        ...         ...
        ...     def make_from(cls, msg):
        ...         ...
        >>> t = Trigger("an enum scheduler trigger", [1, 2], home.event.user.Event.A, 'next', PT(object))
        >>> t.events
        [1, 2, 3, <Event.A: 'A'>]
        >>> r = t.is_triggered(object)
        >>> t.events
        [1, 2, 3, <Event.B: 'B'>]
        >>> r = t.is_triggered(object)
        >>> t.events
        [1, 2, 3, <Event.C: 'C'>]
        >>> r = t.is_triggered(object)
        >>> t.events
        [1, 2, 3, <Event.A: 'A'>]
        >>> t = Trigger("an enum scheduler trigger", [1, 2], home.event.user.Event.A, 'previous', PT(object))
        >>> r = t.is_triggered(object)
        >>> t.events
        [1, 2, 3, <Event.C: 'C'>]

        :param name: the scheduler trigger name
        :param events: events to be notified
        :param selected: an Event taken from a enum list with other Events choices
        :param direction: choose the next or previous Event in the list of enum choices?
        :param protocol_trigger: a protocol trigger
        """
        super(Trigger, self).__init__(name, events, protocol_trigger)
        self._selected = selected
        self._direction = Direction[direction]
        self._logger = logging.getLogger(__name__)

    @property
    def events(self) -> Iterable["home.Event"]:
        _events = self._events.copy()
        _events.append(self._selected)
        return _events

    def __str__(self):
        s = ", enum scheduler trigger: %s" % self._selected
        return super(Trigger, self).__str__() + s

    def _next_or_previous_event(self):
        events = [e for e in self._selected.__class__]
        index = events.index(self._selected)
        if self._direction == Direction.next:
            index = (index + 1) % len(events)
        else:
            index = (index - 1) % len(events)
        return events[index]

    def is_triggered(self, description: "home.protocol.Description") -> bool:
        if self._protocol_trigger.is_triggered(description):
            self._selected = self._next_or_previous_event()
            return True
