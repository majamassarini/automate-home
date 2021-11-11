# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging

from typing import Iterable, Any, Tuple


class Performer(object):
    """
    The entity which links together an Appliance,
    its protocol commands and
    its protocol triggers.

    Through a *Performer* the physical devices are linked with their abstract *Appliance*.
    A *Performer* keep synchronized physical devices states and *Appliance* states.
    """

    def __init__(
        self,
        name: str,
        appliance: "home.Appliance",
        commands: Iterable["home.protocol.Command"],
        triggers: Iterable["home.protocol.Trigger"],
    ):
        self._name = name
        self._appliance = appliance
        self._commands = commands
        self._triggers = triggers

        for command in self._commands:
            command.label = "{}: {}".format(name, command.label)
        for trigger in self._triggers:
            trigger.label = "{}: {}".format(name, trigger.label)

        self._logger = logging.getLogger(__name__)

    def __str__(self):
        return self._name

    @property
    def name(self) -> str:
        return self._name

    @property
    def triggers(self) -> Iterable["home.protocol.Trigger"]:
        return self._triggers

    @property
    def commands(self) -> Iterable["home.protocol.Command"]:
        return self._commands

    @property
    def appliance(self) -> "home.Appliance":
        return self._appliance

    def has(self, description: "home.protocol.Description") -> bool:
        """
        The Performer has a trigger or command for the given
        protocol message description?

        :param description: A protocol message description
        :return: bool
        """
        return description in self.commands or description in self.triggers

    def is_for(self, appliance: "home.Appliance") -> bool:
        """
        The Performer is for the given Appliance?

        :param appliance: An Appliance to look for
        :return: bool
        """
        return self._appliance == appliance

    def execute(
        self, old_state: "home.appliance.State", new_state: "home.appliance.State"
    ) -> Iterable[Any]:
        """
        For every command in Performer make them
        create messages given old and new Appliance State.

        :param old_state: the old Appliance State
        :param new_state: the new Appliance State
        :return: a list of protocol messages to be send through the Gateway
        """
        result = []
        for command in self._commands:
            result.extend(command.make_msgs_from(old_state, new_state))
        return result

    def notify(
        self, events: Iterable["home.Event"]
    ) -> Tuple[Iterable[Any], "home.appliance.State", "home.appliance.State"]:
        """
        Notify to the contained Appliance the given Events.
        Create the protocol messages with old and new Appliance state.

        :param events: Events to be notified to the Appliance
        :return: protocol messages to be sent through the Gateway, \
        old Appliance State and new Appliance State
        """
        msgs = []
        old_old_state = None
        new_state = None
        for event in events:
            old_state, new_state = self._appliance.notify(event)
            msgs.extend(self.execute(old_state, new_state))
            log = "Performer {} has been notified event {} (will send {})".format(
                self.name, event, msgs
            )
            if msgs:
                self._logger.info(log)
            else:
                self._logger.debug(log)
            if old_old_state is None:
                old_old_state = old_state
        return msgs, old_old_state, new_state

    def is_notified(self, event: "home.Event") -> bool:
        """
        The given Event is already inside the Appliance State?

        :param event: an Event to look for
        :return: bool
        """
        return self._appliance.is_notified(event)

    def update_by(
        self, description: "home.protocol.Description"
    ) -> Tuple["home.appliance.State", "home.appliance.State"]:
        """
        Update the contained *Appliance State* through the given
        protocol message description.

        :param description: a protocol message description
        :return: (old Appliance State, new Appliance State)
        """
        old_states = list()
        new_states = list()
        for trigger in self._triggers:
            triggered = trigger.is_triggered(description)
            if triggered:
                old_state, new_state = self._appliance.update_by(trigger, description)
                old_states.append(old_state)
                new_states.append(new_state)
                try:
                    self._logger.info(
                        "Performer {} updated by Trigger {}".format(
                            self.name, trigger.name
                        )
                    )
                except AttributeError:
                    self._logger.info(
                        "Performer {} updated by Trigger {}".format(self.name, trigger)
                    )
        if old_states and new_states:
            return old_states[0], new_states[-1]
        else:
            return None, None


class Performers(list):
    def __init__(self, performers):
        super(Performers, self).__init__(performers)
        self._commands = [
            command for performer in performers for command in performer.commands
        ]
        self._triggers = [
            trigger for performer in performers for trigger in performer.triggers
        ]
        self._performers = performers

    def __str__(self):
        s = "Group of performers [{}]".format(self._performers)
        return s

    @property
    def commands(self):
        return self._commands

    @property
    def triggers(self):
        return self._triggers
