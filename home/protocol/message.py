# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import copy
from abc import ABC, ABCMeta, abstractmethod
from typing import Any, List

registry = list()


def register_class(target_class):
    klass = "{}.{}".format(
        target_class.__module__.replace(".definition", ""), target_class.__name__
    )
    registry.append(klass)


class Registry(ABCMeta):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        if name not in registry:
            register_class(cls)
        return cls


class Description(metaclass=Registry):
    """
    An abstract Description for a protocol message
    """

    PROTOCOL = "a_protocol_identifier_name"

    def __init__(self, description):
        """
        :param description: a description of a protocol message
        """
        ...

    @property
    def type(self) -> str:
        """
        :return: a protocol identifier
        """
        return self.PROTOCOL

    @property
    def label(self) -> str:
        """
        :return: the label attached to this protocol description
        """
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        """
        Attach a label to the protocol description

        :param value: a label
        """
        self._label = value

    @classmethod
    def make(cls, *args, **kwargs) -> "home.protocol.Description":
        """
        Make a protocol message Description given the arguments.

        :param args:
        :param kwargs:
        :return: a protocol message Description
        """
        ...

    @classmethod
    def make_from_yaml(cls, *args, **kwargs) -> "home.protocol.Description":
        """
        Make a protocol message Description given the yaml arguments.

        :param args:
        :param kwargs:
        :return: a protocol message Description
        """
        ...

    @classmethod
    def make_from(cls, msg: Any) -> "home.protocol.Description":
        """
        Make a protocol message Description given the protocol message

        :param msg: a protocol message
        :return: a protocol message Description
        """
        ...


class Trigger(Description, ABC):
    """
    An abstract Trigger for a protocol message.
    """

    DEFAULT_EVENTS = []

    def __init__(self, description: Any, events: List["home.Event"] = None):
        """

        :param events: A list of events to be notified when this Trigger is triggered
        """
        super(Trigger, self).__init__(description)
        self._events = events if events else []
        self._events.extend(self.DEFAULT_EVENTS)

    @abstractmethod
    def is_triggered(self, another_description: "home.protocol.Description") -> bool:
        """
        This trigger is triggered by the given protocol message Description?

        :param another_description: a protocol message description
        :return: bool
        """
        return self.PROTOCOL == another_description.PROTOCOL

    @property
    def events(self) -> List["home.Event"]:
        """
        Events to be notified when this Trigger is triggered.

        :return: a list of Events to be notified
        """
        return self._events

    def make_new_state_from(
        self,
        another_description: "home.protocol.Description",
        old_state: "home.appliance.State",
    ) -> "home.appliance.State":
        """
        Given the protocol message Description, if this Trigger is
        triggered, notify Trigger's Events to the given state
        and return new state.

        :param another_description: a protocol message Description
        :param old_state: an Appliance State to be updated
        :return: an updated Appliance State
        """
        if self.is_triggered(another_description):
            new_state = copy.deepcopy(old_state)
            for event in self.events:
                new_state = new_state.next(event)
            return new_state
        else:
            return old_state


class Unknown(Trigger):
    def is_triggered(self, another_description: "home.protocol.Description") -> bool:
        return False


class Command(Description, ABC):
    """
    An abstract Command for a protocol.
    """

    def __init__(self, description):
        """

        :param events: A list of events to be notified when this Trigger is triggered
        """
        super(Command, self).__init__(description)

    @abstractmethod
    def execute(self):
        """
        Build one or more messages for the protocol Gateway,
        using the internal protocol message representation

        :return: a list of protocol messages
        """
        ...

    @abstractmethod
    def make_msgs_from(
        self, old_state: "home.appliance.State", new_state: "home.appliance.State"
    ) -> List[Any]:
        """
        Update the internal protocol message representation and
        call execute to build one or more messages for
        the protocol Gateway

        :param old_state: the old *Appliance State*
        :param new_state: the new *Appliance State*
        :return: a list of protocol messages
        """
        ...


class Wait(Command):
    class Msg(dict):
        pass

    PROTOCOL = "sleepy"

    def __init__(self, seconds):
        self._seconds = seconds

    @classmethod
    def make(cls, seconds):
        return cls(seconds)

    @classmethod
    def make_from(cls, msg):
        raise NotImplementedError

    def update_from(self, msg):
        raise NotImplementedError

    def execute(self):
        pass

    def make_msgs_from(self, _, __):
        msg = self.Msg()
        msg["type"] = self.PROTOCOL
        msg["seconds"] = self._seconds
        return [msg]

    def __str__(self):
        return "Wait for {} seconds".format(self._seconds)
