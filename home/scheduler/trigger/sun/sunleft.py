# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import datetime
import pytz

from typing import Iterable
from apscheduler.triggers.base import BaseTrigger
from home.event import sun
from home.scheduler.trigger.sun import sunhit


class Trigger(sunhit.Trigger, BaseTrigger):
    """
    Triggered when an object, with the given *Position*, is no more hit by the sun.

    When triggered will notify a **home.event.sun.hit.Event.Sunleft** plus
    other given *events*.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        latitude: float,
        longitude: float,
        elevation: int,
        position: "home.scheduler.trigger.sun.Position",
    ):
        super(Trigger, self).__init__(
            name, events, latitude, longitude, elevation, position
        )

        self._events.append(sun.hit.Event.Sunleft)
        self._position = position
        self._timedelta = datetime.timedelta(seconds=self.TIMEDELTA)

        self._next_fire_time = self._get_next_fire_time(
            None, datetime.datetime.now(self._timezone)
        )

    def _get_next_fire_time(self, _, now):
        """
        >>> import home
        >>> s = Trigger("follower", [], 46.201685, 13.209001, 280, home.scheduler.trigger.sun.Position(20, 90, 120, 240))
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=8, day=1, hour=6)))
        datetime.datetime(2000, 8, 1, 15, 47, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=8, day=30, hour=18)))
        datetime.datetime(2000, 8, 31, 16, 12, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=8, day=30, hour=14)))
        datetime.datetime(2000, 8, 30, 16, 11, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)

        >>> s = Trigger("follower", [], 46.201685, 13.209001, 280, home.scheduler.trigger.sun.Position(20, 90, 20, 130)) # est
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=4)))
        datetime.datetime(2018, 10, 19, 11, 46, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=1, day=19, hour=4)))
        datetime.datetime(2018, 1, 26, 5, 1, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=4, day=19, hour=4)))
        datetime.datetime(2018, 4, 19, 10, 56, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=7, day=19, hour=4)))
        datetime.datetime(2018, 7, 19, 11, 29, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)

        >>> s = Trigger("follower", [], 46.201685, 13.209001, 280, home.scheduler.trigger.sun.Position(20, 90, 120, 240)) # sud
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=4)))
        datetime.datetime(2018, 10, 19, 15, 59, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=1, day=19, hour=4)))
        datetime.datetime(2018, 1, 19, 13, 56, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=4, day=19, hour=4)))
        datetime.datetime(2018, 4, 19, 16, 2, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=7, day=19, hour=4)))
        datetime.datetime(2018, 7, 19, 15, 37, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)

        >>> s = Trigger("follower", [], 46.201685, 13.209001, 280, home.scheduler.trigger.sun.Position(20, 90, 240, 290)) # ovest
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=4)))
        datetime.datetime(2018, 10, 26, 6, 1, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=1, day=19, hour=4)))
        datetime.datetime(2018, 1, 26, 5, 1, tzinfo=<DstTzInfo 'Europe/Rome' CET+1:00:00 STD>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=4, day=19, hour=4)))
        datetime.datetime(2018, 4, 19, 17, 59, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)
        >>> s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=7, day=19, hour=4)))
        datetime.datetime(2018, 7, 19, 18, 44, tzinfo=<DstTzInfo 'Europe/Rome' CEST+2:00:00 DST>)

        :param _:
        :param now: datetime now
        :return: when the object is no more hit by the sun
        """
        sunhit = self._is_sun_over(now)
        timedelta = self._timedelta
        if not sunhit:
            now = super(Trigger, self)._get_next_fire_time(None, now)
            now = now.replace(tzinfo=pytz.timezone("UTC")).astimezone(self._timezone)
            sunhit = self._is_sun_over(now)
        while sunhit and timedelta < datetime.timedelta(days=1):
            timedelta = timedelta + self._timedelta
            sunhit = self._is_sun_over(now + timedelta)

        if not sunhit:
            next_hit = now + timedelta
        else:
            next_hit = now + datetime.timedelta(
                days=7
            )  # prevent scheduler from removing it

        self._logger.info(
            "next sunleft is at %s (now: %s, zone: %s) for position %s"
            % (str(next_hit), str(now), str(now.tzinfo), str(self._position))
        )
        return next_hit
