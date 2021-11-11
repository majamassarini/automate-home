# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from typing import Iterable
from apscheduler.triggers.base import BaseTrigger
from home.scheduler.trigger.protocol import Trigger as Parent


class Trigger(Parent, BaseTrigger):
    """
    A **Scheduler Trigger** triggered when both trigger_positive_a and trigger_positive_b **Protocol Triggers**
    are triggered.

    When triggered will notify given *events* plus all the *protocol triggers events*.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"],
        positive_a: "home.protocol.Trigger",
        negative_a: "home.protocol.Trigger",
        positive_b: "home.protocol.Trigger",
        negative_b: "home.protocol.Trigger",
    ):
        """
        >>> import home
        >>> class PositiveA(home.protocol.Trigger):
        ...     DEFAULT_EVENTS = ["positive a"]
        ...     def __init__(self, description, events):
        ...         super(PositiveA, self).__init__(description, events)
        ...         self._values = [True, False, False, True ]
        ...         self._values.reverse()
        ...     def is_triggered(self, another_description):
        ...         return self._values.pop()
        ...     def make(self):
        ...         ...
        ...     def make_from(cls, msg):
        ...         ...
        >>> class NegativeA(home.protocol.Trigger):
        ...     def __init__(self, description, events):
        ...         super(NegativeA, self).__init__(description, events)
        ...         self._values = [False, True, False, False ]
        ...         self._values.reverse()
        ...     def is_triggered(self, another_description):
        ...         return self._values.pop()
        ...     def make(self):
        ...         ...
        ...     def make_from(cls, msg):
        ...         ...
        >>> class PositiveB(home.protocol.Trigger):
        ...     DEFAULT_EVENTS = ["positive b"]
        ...     def __init__(self, description, events):
        ...         super(PositiveB, self).__init__(description, events)
        ...         self._values = [False, False, True, False ]
        ...         self._values.reverse()
        ...     def is_triggered(self, another_description):
        ...         return self._values.pop()
        ...     def make(self):
        ...         ...
        ...     def make_from(cls, msg):
        ...         ...
        >>> class NegativeB(home.protocol.Trigger):
        ...     def __init__(self, description, events):
        ...         super(NegativeB, self).__init__(description, events)
        ...         self._values = [False, False, False, False ]
        ...         self._values.reverse()
        ...     def is_triggered(self, another_description):
        ...         return self._values.pop()
        ...     def make(self):
        ...         ...
        ...     def make_from(cls, msg):
        ...         ...
        >>> t = home.scheduler.trigger.protocol.multi.Trigger("AND trigger",
        ...       ["another event to send"],
        ...       PositiveA("something", []),
        ...       NegativeA("something", []),
        ...       PositiveB("something", []),
        ...       NegativeB("something", []))
        >>> t.is_triggered("something")
        False
        >>> t.is_triggered(object)
        False
        >>> t.is_triggered(object)
        False
        >>> t.is_triggered(object)
        True

        :param name: the scheduler trigger name
        :param events: events to be notified
        :param positive_a: a *Protocol Trigger* to wait for
        :param negative_a: a *Protocol Trigger* which reset the positive_a triggered state
        :param positive_b: a *Protocol Trigger* to wait for
        :param negative_b: a *Protocol Trigger* which reset the positive_b triggered state
        """
        super(Trigger, self).__init__(name, events, positive_a)
        self._events.extend(positive_b.events)
        self._events.extend(events)
        self._positive_a = positive_a
        self._negative_a = negative_a
        self._positive_b = positive_b
        self._negative_b = negative_b
        self._triggered_a = False
        self._triggered_b = False

    def is_triggered(self, description: "home.protocol.Description"):
        """
        Check if the given protocol message description triggers
        the last untriggered *Protocol Trigger*

        :param description: a message from a home.protocol.Gateway
        :return: if all the *Protocol Triggers* are triggered
        """
        if self._positive_a.is_triggered(description):
            self._triggered_a = True
        elif self._negative_a.is_triggered(description):
            self._triggered_a = False

        if self._positive_b.is_triggered(description):
            self._triggered_b = True
        elif self._negative_b.is_triggered(description):
            self._triggered_b = False

        result = self._triggered_a and self._triggered_b
        if result:  # it should be triggered just once
            self._triggered_a = False
            self._triggered_b = False
        return result

    def __str__(self):
        s = " AND protocol trigger: positive a {}, negative a {}, positive b {}, negative {}".format(
            self._positive_a, self._negative_a, self._positive_b, self._negative_b
        )
        return super(Trigger, self).__str__() + s
