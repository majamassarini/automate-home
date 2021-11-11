# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import abstractmethod
from typing import Iterable, Dict


class Callable(object):
    """
    A single transaction used to build up a non deterministic state machine.
    """

    def __init__(self, **kwargs: Dict[str, "home.appliance.State"]) -> "Callable":
        """
        This single transaction can result in one of the states listed in given dictionary.

        :param kwargs: A dictionary of named states.
        """
        self._output_states = {}
        for key, value in kwargs.items():
            self._output_states[key] = value

    @abstractmethod
    def run(
        self, event: "home.Event", state: "home.appliance.State"
    ) -> "home.appliance.State":
        """
        Do a transaction.
        From given state, processing given event, choose a final state.

        :param event: An event to be processed
        :param state: A state from which transaction starts
        :return: the input state or another one (from those used to build up the transaction)
        """
        ...

    def get_new_state(
        self, old_state: "home.appliance.State", new_state_key: str
    ) -> "home.appliance.State":
        """
        Get the internal named *new_state_key* state . Build it using events taken from given *old_state*.

        :param old_state: Take events from this state when creating new state
        :param new_state_key: Choose the internal state using this name
        :return: The new choose state instance.
        """
        klass = self._output_states[new_state_key]
        state = klass(old_state.events, old_state.events_disabled)
        return state

    def compute_new_state(
        self,
        old_state: "home.appliance.State",
        new_state_key: str,
        events: Iterable["home.Event"],
    ):
        """
        Get the internal named *new_state_key* state . Build it using events taken from given *old_state*,
        excluding those specified in given *events*.

        :param old_state: Take events from this state when creating new state
        :param new_state_key: Choose the internal state using this name
        :param events: Exclude thi events when creating new state.
        :return: The new choose state instance.
        """
        klass = self._output_states[new_state_key]
        state = klass.make(
            [e for e in old_state.events if e not in events], old_state.events_disabled
        )
        return state


class Forced(Callable):
    def run(self, event: "home.Event", state: "home.appliance.State"):
        if "reset" in self._output_states:
            new_state = self.compute_new_state(
                state, "base", [f for f in state.forced_enum]
            )
            if new_state.__class__ == self._output_states["reset"]:
                state = state.unforce()
        return state


class DoNothing(Callable):
    def run(self, event, state):
        return state
