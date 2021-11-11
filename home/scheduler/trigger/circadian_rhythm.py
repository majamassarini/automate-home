# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import datetime

from typing import Iterable, List
from home.scheduler.trigger import Trigger as Parent
from apscheduler.triggers.base import BaseTrigger


class Trigger(Parent, BaseTrigger):
    """
    A **Scheduler Trigger** triggered every **24*60 minutes / num of events_in_a_day**.

    Once every **24*60 minutes / num of events_in_a_day** this trigger will notify one event in *events_in_a_day*.
    Starting from midnight.

    Every time the trigger is triggered it will notify all the events specified in *events*.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        events_in_a_day: List["home.Event"],
    ):
        """
        >>> import datetime
        >>> import pytz
        >>> t = Trigger("circadian rhythm", ["e1"], ["e2", "e3", "e4"])
        >>> t._timezone = pytz.timezone('Europe/Rome')
        >>> t.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=0)))
        datetime.datetime(2000, 12, 1, 8, 0, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> t.events
        ['e1', 'e2']
        >>> t.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=1)))
        datetime.datetime(2000, 12, 1, 8, 0, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> t.events
        ['e1', 'e2']
        >>> t.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=8)))
        datetime.datetime(2000, 12, 1, 16, 0, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> t.events
        ['e1', 'e3']
        >>> t.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=9)))
        datetime.datetime(2000, 12, 1, 16, 0, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> t.events
        ['e1', 'e3']
        >>> t.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=16)))
        datetime.datetime(2000, 12, 2, 0, 0, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> t.events
        ['e1', 'e4']
        >>> t.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=17)))
        datetime.datetime(2000, 12, 2, 0, 0, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> t.events
        ['e1', 'e4']

        :param name: trigger identifier name
        :param events: events to be notified anytime trigger is triggered
        :param events_in_a_day: events to be notified one a day
        """
        super(Trigger, self).__init__(name, events)

        self._events_in_a_day = events_in_a_day
        self._interval = (24 * 60) / len(events_in_a_day)
        self._timedelta = datetime.timedelta(minutes=((24 * 60) / len(events_in_a_day)))
        self._iterator = None

        self._next_fire_time = self._get_next_fire_time(
            None, self._timezone.localize(datetime.datetime.now())
        )

    @property
    def events(self) -> Iterable["home.Event"]:
        """
        :return: *Events* to be notified
        """
        a_list = list()
        a_list.extend(self._events)
        a_list.append(self._events_in_a_day[self._iterator])
        return a_list

    def _get_next_fire_time(self, _, now: datetime.datetime) -> datetime.datetime:
        """
        Next *datetime* when new event taken from list *events in a day* will be notified
        together with all the events in *events*.

        :param _:
        :param now: now datetime
        :return: next datetime at which an event will be notified
        """
        midnight = self._timezone.localize(
            datetime.datetime(
                year=now.year, month=now.month, day=now.day, hour=0, minute=0
            )
        )
        next_fire_time = midnight
        for e in range(len(self._events_in_a_day)):
            self._iterator = e
            next_fire_time = next_fire_time + self._timedelta
            if next_fire_time > now:
                return next_fire_time
        return next_fire_time

    def get_next_fire_time(self, previous_fire_time, now):
        self._next_fire_time = self._get_next_fire_time(previous_fire_time, now)
        return self._next_fire_time
