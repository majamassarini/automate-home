# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import datetime

from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger import date
from home.scheduler.trigger.protocol import Trigger as Parent


class Trigger(Parent, BaseTrigger):
    """
    Notify protocol trigger events and other events (events) when protocol trigger is triggered.
    Start another trigger which will be triggered (timeouts_seconds) later
    with new events (stop_timer_events) to be notified to performers (stop_timer_performers)
    >>> import home
    >>> class PT(home.protocol.Trigger):
    ...     def is_triggered(self):
    ...         return False
    ...     @property
    ...     def events(self):
    ...         return [home.event.scene.Event.Triggered]
    ...     def make(self):
    ...         ...
    ...     def make_from(cls, msg):
    ...         ...
    >>> t = Trigger("a timer trigger", [], PT(object), 10, [home.event.scene.Event.Untriggered], [])
    >>> tt = t.fork(None)
    """

    def __init__(
        self,
        name,
        events,
        protocol_trigger,
        timeout_seconds,
        stop_timer_events,
        stop_timer_performers,
        *args,
        **kwargs
    ):
        super(Trigger, self).__init__(name, events, protocol_trigger, *args, **kwargs)
        self._timeout = timeout_seconds
        self._stop_timer_events = stop_timer_events
        self._stop_timer_performers = stop_timer_performers

    def __str__(self):
        s = ", timeout: %s, stop_timer_actions: %s" % (
            self._timeout,
            self._stop_timer_events,
        )
        return super(Trigger, self).__str__() + s

    def fork(self, performer):
        result = list()
        for another_performer in self._stop_timer_performers:
            name = "stop trigger for trigger %s and %s" % (
                self._name,
                another_performer,
            )
            run_date = datetime.datetime.now() + datetime.timedelta(
                seconds=self._timeout
            )
            result.append(
                (
                    another_performer,
                    date.Trigger(
                        name,
                        self._stop_timer_events,
                        run_date=run_date,
                        timezone=self._timezone,
                    ),
                )
            )
        return result
