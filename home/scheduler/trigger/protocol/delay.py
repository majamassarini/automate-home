# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import home

import datetime
import logging
import copy

from typing import Any, Dict, Iterable, List, Tuple
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger import date
from home.scheduler.trigger.protocol import Trigger as Parent


class Delay:
    """
    Helper that manages the creation and reset of one-shot
    :py:class:`date.resettable.Trigger` instances on behalf of delay
    triggers.

    Each call to :py:meth:`fork` creates a new resettable trigger
    scheduled to fire ``timeout_seconds`` from now and disables the
    previous one (if any) for the same performer, so that only the most
    recent timer is active at any time.

    Subclasses (e.g. :py:class:`_EnableEventsDelay`) can override
    :py:meth:`fork` to produce a different kind of date trigger.
    """

    def __init__(
        self,
        name: str,
        events: Iterable[home.Event],
        timeout_seconds: float,
        timezone,
    ):
        """
        :param name: label used when naming the forked triggers
        :param events: events the forked trigger will deliver
        :param timeout_seconds: delay in seconds before the forked trigger fires
        :param timezone: pytz timezone used to compute the run date
        """
        self._trigger_name = name
        self._scheduler_trigger_events: List[home.Event] = list(events)
        self._protocol_trigger_events: List[home.Event] = []
        self._timeout = timeout_seconds
        self._timezone = timezone
        self._logger = logging.getLogger(__name__)
        self._last_resettable_trigger: Dict[str, Any] = {}  # one per performer

    @property
    def timeout(self) -> float:
        """Delay in seconds before the forked trigger fires."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: float):
        self._timeout = value

    @property
    def protocol_trigger_events(self) -> List:
        """Extra events contributed by the owning protocol trigger."""
        return self._protocol_trigger_events

    @protocol_trigger_events.setter
    def protocol_trigger_events(self, value: List[home.Event]):
        self._protocol_trigger_events = value  # type: ignore[assignment]

    def fork(
        self, performer: home.Performer
    ) -> List[Tuple[home.Performer, "home.scheduler.Trigger"]]:
        """
        Create a new :py:class:`date.resettable.Trigger` scheduled to
        fire ``timeout`` seconds from now and deliver events to
        *performer*.

        If a previous forked trigger for the same performer is still
        pending, it is disabled before the new one is scheduled.

        :param performer: the performer to notify when the timer fires
        :return: a list containing one ``(performer, resettable_trigger)`` pair
        """
        result = list()
        name = "date.resettable.Trigger for parent trigger {} and performer {}".format(
            self._trigger_name, performer.name
        )
        run_date = datetime.datetime.now() + datetime.timedelta(
            seconds=self._timeout
        )
        if name in self._last_resettable_trigger:
            self._last_resettable_trigger[name].disable()
        self._last_resettable_trigger[name] = date.resettable.Trigger(
            name,
            (self._scheduler_trigger_events + self.protocol_trigger_events),
            run_date=run_date,
            timezone=self._timezone,
        )
        result.append((performer, self._last_resettable_trigger[name]))
        return result


class Trigger(Parent, BaseTrigger):
    """
    A scheduler trigger that fires *timeout_seconds* after its protocol
    trigger is activated.

    The trigger itself carries no events (``events`` is always ``[]``);
    the actual events are delivered by the forked
    :py:class:`date.resettable.Trigger` and include both the configured
    events and those from the protocol trigger.  If the protocol trigger
    fires again before the timer expires, the old pending trigger is
    disabled and a new timer is started.
    """

    def __init__(
        self,
        name: str,
        events: Iterable[home.Event],
        protocol_trigger: home.protocol.Trigger,
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

        :param name: human-readable trigger name used in log messages
        :param events: events to include in the forked trigger's payload
        :param protocol_trigger: the protocol trigger that starts the timer
        :param timeout_seconds: delay in seconds before the forked trigger fires
        """
        super(Trigger, self).__init__(name, events, protocol_trigger)
        self._delay = Delay(
            self.name, copy.deepcopy(events), timeout_seconds, self._timezone
        )
        self._timeout = timeout_seconds
        self._logger = logging.getLogger(__name__)

    @property
    def events(self):
        # Events are delivered by the forked date trigger, not this one.
        return []

    def __str__(self):
        s = ", delay: %s" % self._timeout
        return super(Trigger, self).__str__() + s

    def fork(
        self, performer: home.Performer
    ) -> List[Tuple[home.Performer, "home.scheduler.Trigger"]]:
        """
        Snapshot the current protocol trigger events and delegate to the
        :py:class:`Delay` helper to create a one-shot resettable trigger.

        :param performer: the performer to notify when the timer fires
        :return: list containing one ``(performer, resettable_trigger)`` pair
        """
        self._delay.protocol_trigger_events = self._protocol_trigger.events  # type: ignore[assignment]
        return self._delay.fork(performer)
