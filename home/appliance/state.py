# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import collections
import logging
import copy
from abc import ABCMeta, abstractmethod
from typing import Iterable, Type

registry_for_redis = list()


def register_class(target_class):
    klass = "{}.{}".format(target_class.__module__, target_class.__name__)
    registry_for_redis.append(klass)


class Registry(ABCMeta):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        if name not in registry_for_redis:
            register_class(cls)
        return cls


class State(metaclass=Registry):
    """
    An abstract Appliance State object.
    """

    VALUE = "None"
    DEFAULTS = ()

    def __init__(
        self,
        events: Iterable["home.Event"] = None,
        events_disabled: Iterable["home.Event"] = None,
    ):
        """
        :param events: list of events values which will initialize internal state
        :param events_disabled: list of events values, *used to initialize internal state*, which will never updated
        again
        """
        self._events = collections.OrderedDict()
        self._disabled = set()
        self._callables = {}
        self.init_callables()
        for event in self.DEFAULTS:
            self.update_by(event)
        if events:
            for event in events:
                self.update_by(event)
        if events_disabled:
            for event in events_disabled:
                self.update_by(event)
            self._disabled = set(events_disabled)

    @abstractmethod
    def init_callables(self) -> None:
        ...

    def _get_str_value(self):
        return self.VALUE.format()

    def __repr__(self, *args, **kwargs):
        events = ""
        for event in self._events.values():
            events += str(event)
            events += ", "
        events = events[0:-2]
        s = "{} (computed from events: {}) and disabled events {}".format(
            self._get_str_value(), events, self._disabled
        )
        return s

    def __eq__(self, other):
        events_are_equals = True
        for key, event in self._events.items():
            try:
                if event != other._events[key]:
                    events_are_equals = False
                    break
            except KeyError as e:
                logging.getLogger(__name__).error(
                    "self is {}, event is {} other is {}".format(self, event, other)
                )
                raise e
            except AttributeError as e:
                logging.getLogger(__name__).error(
                    "self is {}, event is {} other is none".format(self, event)
                )
                raise e
        events_disabled_are_equals = self.events_disabled == other.events_disabled
        return (
            self.__class__ == other.__class__
            and events_are_equals
            and events_disabled_are_equals
        )

    def __contains__(self, event):
        return event in self._events.values()

    def __sub__(self, other):
        return set(self._events.values()) - set(other._events.values())

    @property
    def events(self) -> Iterable["home.Event"]:
        """
        All Events already notified to the Appliance
        """
        return [v for v in self._events.values()]

    @property
    def events_disabled(self) -> Iterable["home.Event"]:
        """
        All Events disabled in this state machine
        """
        return self._disabled

    def is_enabled(self, event: "home.Event") -> bool:
        """
        Are event of given event type enabled?

        :param event: home.Event
        :return: bool
        """
        return type(event) not in [type(e) for e in self._disabled]

    def disable(self, event: "home.Event"):
        """
        Disable processing for events of the same type in the state machine.

        :param event: home.Event
        """
        if self.is_enabled(event):
            self._disabled.add(event)

    def enable(self, event: "home.Event"):
        """
        Enable processing for events of the same type in the state machine.

        :param event: home.Event
        """
        saved = None
        for e in self._disabled:
            if type(e) == type(event):
                saved = e
        if saved:
            self._disabled.remove(saved)

    @classmethod
    def make(
        cls,
        events: Iterable["home.Event"],
        events_disabled: Iterable["home.Event"] = None,
    ) -> "home.appliance.State":
        """
        :param events: to be processed by a new State
        :param events_disabled: list of events which will not be updated!
        :return: a brand new State
        """
        state = cls([], events_disabled)
        for event in events:
            state = state.next(event)
        return state

    def next(self, event: "home.Event") -> "home.appliance.State":
        """
        :param event: to be processed by this State
        :return: a brand new State (if necessary)
        """
        new_state = copy.deepcopy(self)
        new_state = new_state._next(event)
        if self != new_state:
            return new_state
        else:
            return self

    def update_by(self, event):
        if type(event) not in [type(e) for e in self._disabled]:
            if event in self.DEFAULTS:
                self._events[type(event)] = event
            elif type(event) in self._events:
                self._events[type(event)] = event

    def _next(self, event):
        new_state = self
        self.update_by(event)
        try:
            if type(event) not in [type(e) for e in self._disabled]:
                callback = self._callables[type(event)]
                new_state = callback.run(event, self)
        except KeyError:
            pass
        return new_state

    def compute(self) -> str:
        """
        :return: a str representation of this state
        """
        return self._get_str_value()

    @property
    @abstractmethod
    def forced_enum(self) -> Type["home.Event"]:
        ...

    def force(self, value: str) -> "home.appliance.State":
        """
        :param value: a value in forced Event Enum values
        :return: the related forced State
        """
        event = getattr(self.forced_enum, value)
        return self.next(event)

    def unforce(self) -> "home.appliance.State":
        """
        :return: a non forced State
        """
        event = getattr(self.forced_enum, "Not")
        return self.next(event)

    def is_forced(self) -> bool:
        event = getattr(self.forced_enum, "Not")
        if event in self._events:
            return True
        else:
            return False
