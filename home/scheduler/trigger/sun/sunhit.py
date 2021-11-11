# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import collections
import datetime
import pytz

from typing import Iterable
from apscheduler.triggers.base import BaseTrigger
from home.event import sun
from home.scheduler.trigger.sun import follow


class Trigger(follow.Trigger, BaseTrigger):
    """
    Triggered when an object, with the given *Position*, is hit by the sun.

    When triggered will notify a **home.event.sun.hit.Event.Sunhit** plus
    other given *events*.
    """

    TIMEDELTA = 60

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        latitude: float,
        longitude: float,
        elevation: int,
        position: "home.scheduler.trigger.sun.Position",
    ):
        super(Trigger, self).__init__(name, events, latitude, longitude, elevation)

        self._events.append(sun.hit.Event.Sunhit)
        self._position = position
        self._timedelta = datetime.timedelta(seconds=self.TIMEDELTA)

        self._next_fire_time = self._get_next_fire_time(
            None, datetime.datetime.now(self._timezone)
        )

    def _is_sun_over(self, now):
        self._observer.date = now.astimezone(pytz.timezone("UTC"))
        self._sun.compute(self._observer)
        altitude = str(self._sun.alt)
        azimuth = str(self._sun.az)
        altitude = int(altitude.split(":")[0])
        azimuth = int(azimuth.split(":")[0])
        Position = collections.namedtuple("Position", "altitude azimuth")
        position = Position(altitude, azimuth)
        is_sun_over = self._position.is_sun_over(position)
        self._logger.debug(
            "at %s sun is in %s and is %s over"
            % (str(now), str(position), "not" if not is_sun_over else "")
        )
        return is_sun_over

    def _get_next_fire_time(self, _, now: datetime.datetime) -> datetime.datetime:
        """
        >>> import home
        >>> s = Trigger("sunhit", [], 46.201685, 13.209001, 280,
        ... home.scheduler.trigger.sun.Position(20, 90, 120, 240))
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=6)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2000, 12, 1, 10, 44)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=11, day=30, hour=18)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2000, 12, 1, 10, 44)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=11, day=30, hour=12)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2000, 12, 1, 10, 44)
        >>> s = Trigger("sunhit", [], 46.201685, 13.209001, 280,
        ... home.scheduler.trigger.sun.Position(20, 90, 20, 130)) # est
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 10, 19, 9, 45)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=1, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 1, 26, 4, 0)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=4, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 4, 19, 8, 16)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=7, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 7, 19, 7, 44)

        >>> s = Trigger("sunhit", [], 46.201685, 13.209001, 280,
        ... home.scheduler.trigger.sun.Position(20, 90, 120, 240)) # sud
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 10, 19, 9, 45)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=1, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 1, 19, 10, 41)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=4, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 4, 19, 10, 16)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=7, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 7, 19, 10, 55)

        >>> s = Trigger("sunhit", [], 46.201685, 13.209001, 280,
        ... home.scheduler.trigger.sun.Position(20, 90, 240, 290)) # ovest
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 10, 26, 4, 0)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=1, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 1, 26, 4, 0)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=4, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 4, 19, 15, 58)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=7, day=19, hour=4)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 7, 19, 15, 33)

        :param _:
        :param now: datetime now
        :return: when the object is hit by the sun again
        """
        sunhit = self._is_sun_over(now)
        if sunhit:  # wait next transit over the window
            now = self._observer.next_rising(self._sun, use_center=True).datetime()
            now = now.replace(tzinfo=pytz.timezone("UTC")).astimezone(self._timezone)
        timedelta = self._timedelta
        sunhit = False
        while not sunhit and timedelta < datetime.timedelta(days=1):
            timedelta = timedelta + self._timedelta
            sunhit = self._is_sun_over(now + timedelta)

        if sunhit:
            next_hit = now + timedelta
        else:
            next_hit = now + datetime.timedelta(
                days=7
            )  # prevent scheduler from removing it

        self._logger.info(
            "next sunhit is at %s (now: %s, zone: %s) for position %s"
            % (str(next_hit), str(now), str(now.tzinfo), str(self._position))
        )
        return next_hit
