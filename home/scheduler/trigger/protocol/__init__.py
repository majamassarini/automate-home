# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import datetime

from typing import Iterable
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger import Trigger as Parent


class Trigger(Parent, BaseTrigger):
    """
    A **Scheduler Trigger** triggered when its **Protocol Trigger** is triggered.

    When triggered will notify given *events* plus the *protocol trigger events*.
    """

    @staticmethod
    @property
    def type(self):
        return "PROTOCOL EVENT"

    def __init__(
        self,
        name: str,
        events: Iterable["home.Events"],
        protocol_trigger: "home.protocol.Trigger",
        *args,
        **kwargs
    ):
        super(Trigger, self).__init__(name, events, *args, **kwargs)
        self._protocol_trigger = protocol_trigger

    def is_triggered(self, description: "home.protocol.Description") -> bool:
        """
        Check if the given protocol message description triggers
        the inner *Protocol Trigger*

        :param description: a message from a home.protocol.Gateway
        :return: if the *Protocol Trigger* is triggered
        """
        return self._protocol_trigger.is_triggered(description)

    def __str__(self):
        s = " protocol trigger: %s" % self._protocol_trigger
        return super(Trigger, self).__str__() + s

    def get_next_fire_time(self, _, now):
        """
        When the inner *Protocol Trigger* is triggered this
        *Scheduler Trigger* is armed to be *immediately triggered*.

        :param _:
        :param now: datetime now
        :return: datetime now
        """
        timedelta = datetime.timedelta(
            weeks=52
        )  # prevent scheduler from removing trigger
        result = datetime.datetime.now(self._timezone) + timedelta
        return result

    @property
    def events(self):
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
