# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from apscheduler.triggers.interval import IntervalTrigger
from home.scheduler.trigger import Trigger as Parent

from typing import Iterable


class Trigger(Parent, IntervalTrigger):
    """
    An extension of the `APScheduler IntervalTrigger <https://apscheduler.readthedocs.io/en/stable/modules/triggers/interval.html>`_.
    """

    def __init__(self, name: str, events: Iterable["home.Event"], *args, **kwargs):
        super(Trigger, self).__init__(name, events, *args, **kwargs)
