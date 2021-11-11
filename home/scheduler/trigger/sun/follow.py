# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import abstractmethod

import ephem
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger import Trigger as Parent


class Trigger(Parent, BaseTrigger):
    def __init__(self, name, events, latitude, longitude, elevation, *args, **kwargs):
        super(Trigger, self).__init__(name, events, *args, **kwargs)

        self._observer = ephem.Observer()
        self._observer.lon = str(longitude)
        try:
            self._observer.lat = str(latitude)
        except ValueError:
            pass
        self._observer.elev = elevation
        self._sun = ephem.Sun()

        self._next_fire_time = None

    @abstractmethod
    def _get_next_fire_time(self, previous_fire_time, now):
        ...

    def get_next_fire_time(self, previous_fire_time, now):
        self._next_fire_time = self._get_next_fire_time(previous_fire_time, now)
        return self._next_fire_time
