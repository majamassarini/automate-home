# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging

from apscheduler.triggers.date import DateTrigger
from home.scheduler.trigger import Trigger as Parent


class Trigger(Parent, DateTrigger):
    """
    A one-shot APScheduler date trigger that can be disabled before it fires.

    Created by :py:class:`Delay.fork` to represent a pending timer.  If a
    newer timer supersedes it (because the same state or protocol trigger
    fires again), :py:meth:`disable` is called so that when APScheduler
    eventually invokes :py:meth:`Process.schedule`, the event is silently
    dropped by the ``if trigger.is_enabled`` check in
    :py:meth:`Process._run`.
    """

    def __init__(self, name, events, run_date, *args, **kwargs):
        """
        :param name: human-readable trigger name used in log messages
        :param events: events to deliver when this trigger fires
        :param run_date: the datetime at which APScheduler should fire this job
        """
        super(Trigger, self).__init__(name, events, run_date, *args, **kwargs)
        self._logger = logging.getLogger(__name__)
        self._is_enabled = True

    @property
    def is_enabled(self) -> bool:
        """``False`` if :py:meth:`disable` has been called, ``True`` otherwise."""
        return self._is_enabled

    def disable(self):
        """Mark this trigger as inactive so its events are ignored when it fires."""
        self._is_enabled = False
