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
from home.scheduler.trigger.sun import follow


class Trigger(follow.Trigger, BaseTrigger):
    """
    A *Trigger* triggered by the **sunrise**.

    When triggered will notify a **home.event.sun.phase.Event.Sunrise** plus
    other given *events*.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        latitude: float,
        longitude: float,
        elevation: int,
    ):
        super(Trigger, self).__init__(name, events, latitude, longitude, elevation)

        self._events.append(sun.phase.Event.Sunrise)
        self._next_fire_time = self._get_next_fire_time(
            None, self._timezone.localize(datetime.datetime.now())
        )

    def _get_next_fire_time(self, _, now: datetime.datetime) -> datetime.datetime:
        """
        >>> import datetime
        >>> s = Trigger("sunrise", [], 45.20, 13.20, 280)
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=16)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2000, 12, 2, 7, 29)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=1)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 10, 19, 7, 29)

        :param _:
        :param now: now datetime
        :return: next rising sun datetime
        """
        self._observer.date = now.astimezone(pytz.timezone("UTC"))
        next_rising = self._observer.next_rising(self._sun, use_center=True).datetime()
        next_rising = next_rising.replace(tzinfo=pytz.timezone("UTC"))
        next_rising = next_rising.astimezone(tz=self._timezone)
        self._logger.info(
            "next rising is at %s (now: %s, zone: %s)"
            % (str(next_rising), str(now), str(now.tzinfo))
        )
        return next_rising
