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
    A *Trigger* triggered by the **sunset**.

    When triggered will notify a **home.event.sun.phase.Event.Sunset** plus
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

        self._events.append(sun.phase.Event.Sunset)
        self._next_fire_time = self._get_next_fire_time(
            None, datetime.datetime.now(tz=self._timezone)
        )

    def _get_next_fire_time(self, _, now: datetime.datetime) -> datetime.datetime:
        """
        >>> import datetime
        >>> s = Trigger("sunset", [], 45.20, 13.20, 280)
        >>> s._timezone = pytz.timezone('Europe/Rome')
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2000, month=12, day=1, hour=6)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2000, 12, 1, 16, 24)
        >>> d = s.get_next_fire_time(None, pytz.timezone('Europe/Rome').localize(datetime.datetime(year=2018, month=10, day=19, hour=6)))
        >>> (d.year, d.month, d.day, d.hour, d.minute)
        (2018, 10, 19, 18, 13)

        :param _:
        :param now: datetime now
        :return: next sunset datetime
        """
        self._observer.date = now.astimezone(pytz.timezone("UTC"))
        next_setting = self._observer.next_setting(
            self._sun, use_center=True
        ).datetime()
        next_setting = next_setting.replace(tzinfo=pytz.timezone("UTC"))
        next_setting = next_setting.astimezone(tz=self._timezone)
        self._logger.info(
            "next setting is at %s (now: %s, zone: %s)"
            % (str(next_setting), str(now), str(now.tzinfo))
        )
        return next_setting
