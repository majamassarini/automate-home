# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import copy
import logging
from abc import ABCMeta, abstractmethod
from typing import Tuple, Iterable

registry = list()
registry_for_redis = list()


def register_class(target_class):
    klass = "{}.{}".format(
        target_class.__module__.replace(".definition", "").replace(
            "home.appliance.", ""
        ),
        target_class.__name__,
    )
    registry.append(klass)
    klass = "{}.{}".format(target_class.__module__, target_class.__name__)
    registry_for_redis.append(klass)


class Registry(ABCMeta):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        if name not in registry:
            register_class(cls)
        return cls


class Appliance(metaclass=Registry):
    """An abstract representation of a device.
    An appliance has a state which is changed by notified events.
    """

    def __init__(
        self,
        name: str,
        events: Iterable["home.Event"] = None,
        events_disabled: Iterable["home.Event"] = None,
    ):
        """
        :param name: the Appliance identifier string name
        :param events: a list of events which decide the Appliance initial state
        :param events_disabled: a list of events which are disabled and will not be used to calculate next appliance state
        """
        self._name = name
        self._state = self._init_state()
        if events_disabled:
            for event in events_disabled:
                self._state.disable(event)
        if events:
            for event in events:
                self._state = self._state.next(event)
        self._logger = logging.getLogger(__name__)

    @classmethod
    def make(cls, name, state):
        appliance = cls(name)
        appliance._state = state
        return appliance

    @abstractmethod
    def _init_state(self) -> "home.appliance.State":
        ...

    def __str__(self):
        return "Appliance %s in %s" % (self.name, self._state)

    def __repr__(self):
        return "%s in %s" % (self.name, self._state)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and (self._name == other.name)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __sub__(self, other):
        return self.state - other.state

    @property
    def name(self) -> str:
        """The Appliance name"""
        return self._name

    @property
    def events(self) -> Iterable["home.Event"]:
        """A list of Events already notified to the Appliance"""
        return self._state.events

    @property
    def events_disabled(self) -> Iterable["home.Event"]:
        """A list of Events disabled in the Appliance state machine"""
        return self._state.events_disabled

    @property
    def state(self) -> "home.appliance.State":
        """The Appliance state"""
        return self._state

    @property
    def forced_enum(self) -> "home.Event":
        """An Event capable of making the Appliance forced (if any)"""
        return self._state.forced_enum

    def _update(self, state) -> None:
        if self._state != state:
            self._logger.info("Appliance %s updated in %s" % (self.name, state))
            self._state = state

    def update(
        self, other: "home.Appliance"
    ) -> Tuple["home.appliance.State", "home.appliance.State"]:
        """
        Update state using events taken from another Appliance

        :param other: look for new events in another Appliance and use them to update Appliance state
        :return: *(old_state, new_state)* a tuple with the old state, the state before updating, \
        and the new state, the one after the update.
        """
        old_state = self._state
        new_state = self._state
        enable = list()
        disable = list()
        for event in self.events_disabled:
            enable.append(event)
        [self.enable(event) for event in enable]
        for event in other.events_disabled:
            disable.append(event)
        [self.disable(event) for event in disable]
        for event in other.state - old_state:
            new_state = new_state.next(event)
        if (
            new_state.VALUE != other.state.VALUE
        ):  # no event, could be a reset from a forced state
            new_state = other.state.make(other.state.events, other.events_disabled)
        self._update(new_state)
        return old_state, new_state

    def update_by(
        self, trigger: "home.protocol.Trigger", description: "home.protocol.Description"
    ) -> Tuple["home.appliance.State", "home.appliance.State"]:
        """
        Update state using trigger.
        A trigger is capable of creating a new state using its method make_new_state_from.

        :param trigger: a trigger capable of making a new state from an old one.
        :param description: a message description taken from a *bus event*, \
        it carries updated data used to make the new state
        :return: *(old_state, new_state)* a tuple with the old state, the state before updating, \
        and the new state, the one after the update.
        """
        old_state = copy.deepcopy(self._state)
        new_state = trigger.make_new_state_from(description, self._state)
        if self._state != new_state:
            self._update(new_state)
        return old_state, new_state

    def notify(
        self, event: "home.Event"
    ) -> Tuple["home.appliance.State", "home.appliance.State"]:
        """
        Notify a new event to the Appliance

        :param event: an event
        :return: *(old_state, new_state)* a tuple with the old state, the state before notifying event, \
        and the new state, the one after the notify.
        """
        old_state = self._state
        new_state = self._state.next(event)
        self._update(new_state)
        return old_state, new_state

    def is_notified(self, event: "home.Event") -> bool:
        """
        Event has been notified to the Appliance?

        :param event: an event
        :return: bool
        """
        return event in self._state

    def is_enabled(self, event: "home.Event") -> bool:
        """
        Events of the same given type are enabled in the state machine?

        :param event: an event
        :return: bool
        """
        return self._state.is_enabled(event)

    def enable(self, event: "home.Event"):
        """
        Enable events of the same given type in the state machine

        :param event: an event
        :return: bool
        """
        self._state.enable(event)

    def disable(self, event: "home.Event"):
        """
        Disable events of the same given type in the state machine

        :param event: an event
        :return: bool
        """
        self._state.disable(event)


from home.appliance.state import State
from home.appliance import attribute
from home.appliance import (
    data,
    light,
    curtain,
    thermostat,
    sensor,
    sound,
    socket,
    sprinkler,
)
from home.appliance.callable import Callable
from home.appliance.collection import Collection
