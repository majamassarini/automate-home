# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import ABC, abstractmethod

from typing import Iterable, Any, Callable


class WrongMsg(Exception):
    pass


class Gateway(ABC):
    """
    An Abstract *Protocol Gateway*.

    The entity which can send and receive protocol messages to/from the protocol bus.
    """

    PROTOCOL = "a_protocol_identifier_name"

    @abstractmethod
    def associate_commands(self, descriptions: "home.protocol.Description") -> Any:
        """
        Connect the *Protocol Commands* with the *Gateway*, if needed.

        Only connected commands should go through the *Gateway* to the bus.

        :param descriptions: a protocol message description
        :return: an association object, if any
        """
        ...

    @abstractmethod
    def associate_triggers(self, descriptions: "home.protocol.Description"):
        """
        Connect the *Protocol Triggers* with the *Gateway*, if needed.

        Only connected triggers should go through the *Gateway* from the bus.

        :param descriptions: a protocol message description
        :return: an association object, if any
        """
        ...

    @abstractmethod
    async def run(self, tasks: Iterable[Callable]):
        """
        Create an asynchronous task capable of receiving messages from the bus.

        Every received message becomes a **Protocol Trigger**.

        Every created *Protocol Trigger* goes through given tasks to be processed.

        :param tasks: a function capable of process a *Protocol Trigger*
        """
        ...

    @abstractmethod
    async def writer(self, msgs: Iterable[Any], *args):
        """
        A function capable of sending protocol messages to the bus.

        :param msgs: a protocol messages
        :param args:
        """
        ...

    @staticmethod
    def make_trigger(msg: Any) -> "home.protocol.Trigger":
        """
        Make a *Protocol Trigger* from a protocol message.

        :param msg: a protocol message
        :return: a *Protocol Trigger*
        """
        ...

    def _wrap_tasks(self, tasks: Iterable[Callable]):
        wrapped_tasks = [lambda msg: task(self.make_trigger(msg)) for task in tasks]
        return wrapped_tasks
