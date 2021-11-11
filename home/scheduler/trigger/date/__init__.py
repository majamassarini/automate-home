# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from apscheduler.triggers.date import DateTrigger
from home.scheduler.trigger import Trigger as Parent

from typing import Iterable


class Trigger(Parent, DateTrigger):
    """
    An extension of the `APScheduler DateTrigger <https://apscheduler.readthedocs.io/en/stable/modules/triggers/date.html>`_.
    """

    def __init__(self, name: str, events: Iterable["home.Event"], *args, **kwargs):
        super(Trigger, self).__init__(name, events, *args, **kwargs)


from home.scheduler.trigger.date import resettable
