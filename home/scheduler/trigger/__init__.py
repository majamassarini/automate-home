# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import home

from abc import ABCMeta
import datetime
import logging
import pytz
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
    Base class for all scheduler triggers.

    When fired by APScheduler, the configured *events* are delivered to
    every *Performer* that has been associated with this trigger via
    :py:meth:`MyHome.schedule_performer`.
    """

    type = "SCHEDULER EVENT"

    def __init__(
        self, name: str, events: Iterable[home.Event], *args, **kwargs
    ):
        """
        :param name: human-readable trigger name used in log messages
        :param events: events to deliver when this trigger fires
        """
        super(Trigger, self).__init__(*args, **kwargs)
        self._name = name
        self._events: List[home.Event] = list()
        self._events.extend(events)
        self._timedelta_fire = datetime.timedelta(weeks=52)
        tz = get_localzone()
        # Convert ZoneInfo to pytz for APScheduler compatibility
        if hasattr(tz, "key"):
            # ZoneInfo timezone - convert to pytz
            self._timezone = pytz.timezone(tz.key)
        else:
            # Already a pytz timezone
            self._timezone = tz  # type: ignore[assignment]
        self._logger = logging.getLogger(__name__)

    def __str__(self):
        s = "scheduler.Trigger name: %s, events: %s, %s" % (
            self._name,
            str(self._events),
            super(Trigger, self).__str__(),
        )
        return s

    def _localize(self, dt: datetime.datetime) -> datetime.datetime:
        """
        Localize a naive datetime to the trigger's timezone.
        Handles both pytz and ZoneInfo timezones.

        :param dt: naive datetime to localize
        :return: timezone-aware datetime
        """
        if hasattr(self._timezone, "localize"):
            # pytz timezone
            return self._timezone.localize(dt)
        else:
            # ZoneInfo timezone
            return dt.replace(tzinfo=self._timezone)

    def fork(
        self, performer: home.Performer
    ) -> List[Tuple[home.Performer, "home.scheduler.Trigger"]]:
        """
        Produce derived triggers that will notify *performer* after a delay.

        The base implementation returns an empty list. Subclasses that
        carry a delay (e.g. :py:class:`state.delay.Trigger`) override this
        to create and return a one-shot
        :py:class:`date.resettable.Trigger` scheduled to fire after the
        configured timeout.

        :param performer: the performer to notify when the derived trigger fires
        :return: list of (performer, trigger) pairs to register with APScheduler
        """
        return []

    @property
    def is_enabled(self) -> bool:
        """
        Whether this trigger is still active.

        Returns ``False`` for :py:class:`date.resettable.Trigger` instances
        that have been explicitly disabled (e.g. because a newer fork
        supersedes them).  The base implementation always returns ``True``.
        """
        return True

    @property
    def name(self) -> str:
        """
        :return: the *Scheduler Trigger* name
        """
        return self._name

    @property
    def events(self) -> Iterable[home.Event]:
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
