# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import datetime

from typing import Iterable
from home.event import sun
from home.scheduler.trigger.sun import sunrise


class Trigger(sunrise.Trigger):
    """
    A *Trigger* triggered when starts the *morning civil twilight*

    When triggered will notify a **home.event.sun.twilight.civil.Event.Sunrise** plus
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
        """
        >>> import datetime
        >>> import pytz
        >>> s = Trigger("sunrise", [], 46.201685, 13.209001, 280)
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=16)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2000, 12, 2, 6, 55)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=1)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 10, 19, 6, 58)
        """
        super(Trigger, self).__init__(name, events, latitude, longitude, elevation)
        self._events.append(sun.twilight.civil.Event.Sunrise)
        self._observer.horizon = "-6"  # civil twilight
        self._next_fire_time = self._get_next_fire_time(
            None, self._timezone.localize(datetime.datetime.now())
        )
