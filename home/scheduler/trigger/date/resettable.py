# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging

from apscheduler.triggers.date import DateTrigger
from home.scheduler.trigger import Trigger as Parent


class Trigger(Parent, DateTrigger):
    """A date trigger which events could be disabled by someone else."""

    def __init__(self, name, events, run_date, *args, **kwargs):
        super(Trigger, self).__init__(name, events, run_date, *args, **kwargs)
        self._logger = logging.getLogger(__name__)
        self._is_enabled = True

    @property
    def is_enabled(self):
        return self._is_enabled

    def disable(self):
        self._is_enabled = False
