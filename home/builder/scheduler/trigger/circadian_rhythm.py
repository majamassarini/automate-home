# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger import Builder as Parent
from home.scheduler.trigger.circadian_rhythm import Trigger


class Builder(Parent):
    """
    >>> import home
    >>> map ={
    ... "name": "adjust saturation during the day: bagno",
    ... "events": [],
    ... "events_in_a_day": [home.appliance.light.event.circadian_rhythm.saturation.Event(0)]}
    >>> l = home.builder.scheduler.trigger.circadian_rhythm.Builder()._run(map, [])
    >>> len(l)
    1
    """

    TAG_NAME = "circadian_rhythm.Trigger"

    @property
    def trigger(self):
        return Trigger
