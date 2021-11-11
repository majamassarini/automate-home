# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.crawler.osmer_fvg.will_rain import Builder as Parent
from home.scheduler.trigger.crawler.osmer_fvg.will_rain.off import Trigger


class Builder(Parent):
    """
    >>> import home
    >>> import datetime
    >>> import unittest.mock
    >>> map = {
    ... "name": "forecast",
    ... "notify more events": [],
    ... "url": "https://dev.meteo.fvg.it/xml/previsioni/",
    ... "probability": 60,
    ... }
    >>> l = home.builder.scheduler.trigger.crawler.osmer_fvg.will_rain.on.Builder()._run(map, [])
    >>> on = l[0]
    >>> on._today = lambda : datetime.date(2021, 11, 8)
    >>> l = home.builder.scheduler.trigger.crawler.osmer_fvg.will_rain.off.Builder()._run(map, [])
    >>> off = l[0]
    >>> off._today = lambda : datetime.date(2021, 11, 8)
    >>> on.is_triggered()
    False
    >>> off.is_triggered()
    True
    """

    TAG_NAME = "crawler.osmer_fvg.will_rain.off.Trigger"

    @property
    def trigger(self):
        return Trigger
