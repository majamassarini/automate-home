# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import home

import datetime

from typing import Iterable
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger import Trigger as Parent


class Trigger(Parent, BaseTrigger):
    """
    A scheduler trigger that fires whenever its associated protocol
    trigger is activated by an incoming bus message.

    When fired, it delivers the union of its own *events* and the events
    carried by the protocol trigger to the associated performers.
    """

    type = "PROTOCOL EVENT"

    def __init__(
        self,
        name: str,
        events: Iterable[home.Event],
        protocol_trigger: home.protocol.Trigger,
        *args,
        **kwargs,
    ):
        """
        :param name: human-readable trigger name used in log messages
        :param events: extra events to deliver in addition to those from
            the protocol trigger
        :param protocol_trigger: the protocol-level trigger that activates
            this scheduler trigger
        """
        super(Trigger, self).__init__(name, events, *args, **kwargs)
        self._protocol_trigger = protocol_trigger

    def is_triggered(self, description: home.protocol.Description) -> bool:
        """
        Return ``True`` when the given protocol message description
        activates the inner protocol trigger.

        :param description: a message description received from a protocol gateway
        :return: ``True`` if the protocol trigger matches the description
        """
        return self._protocol_trigger.is_triggered(description)

    def __str__(self):
        s = " protocol trigger: %s" % self._protocol_trigger
        return super(Trigger, self).__str__() + s

    def get_next_fire_time(self, _, now):
        """
        Return a fire time far in the future so that APScheduler never
        removes this trigger from the scheduler.

        Protocol-based triggers are fired manually (via
        :py:meth:`Process._schedule_by_protocol_trigger`) whenever the
        matching protocol message arrives; they are not supposed to fire
        on their own.

        :param _: previous fire time (unused)
        :param now: current datetime (unused)
        :return: a datetime 52 weeks from now
        """
        timedelta = datetime.timedelta(
            weeks=52
        )  # prevent scheduler from removing trigger
        result = datetime.datetime.now(self._timezone) + timedelta
        return result

    @property
    def events(self):
        """
        Return the combined list of this trigger's own events and those
        carried by the inner protocol trigger.
        """
        lst = self._events.copy()
        if self._protocol_trigger:
            try:
                lst.extend(self._protocol_trigger.events)
            except TypeError as e:
                raise e
        else:
            raise AttributeError
        return lst


from home.scheduler.trigger.protocol import delay
from home.scheduler.trigger.protocol import multi
from home.scheduler.trigger.protocol import timer
from home.scheduler.trigger.protocol import mean
from home.scheduler.trigger.protocol import enum
