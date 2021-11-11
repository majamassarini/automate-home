# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from apscheduler.triggers.cron import CronTrigger
from home.scheduler.trigger import Trigger as Parent

from typing import List


class Trigger(Parent, CronTrigger):
    """
    An extension of the `APScheduler CronTrigger <https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html>`_.
    """

    def __init__(self, name: str, events: List["home.Event"], *args, **kwargs):
        super(Trigger, self).__init__(name, events, *args, **kwargs)
