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
    A **Scheduler Trigger** triggered when the Appliance is already in the specified state.
    """

    @staticmethod
    @property
    def type(self):
        return "APPLIANCE STATE"

    def __init__(self, name: str, events: Iterable["home.Events"], state: str):
        """
        :param name: the scheduler trigger name
        :param events: events to be notified
        :param state: a str representing a state
        """
        super(Trigger, self).__init__(name, events)
        self._state = state

    def is_triggered(
        self, old_state: "home.appliance.State", new_state: "home.appliance.State"
    ) -> bool:
        """
        When Appliance state is already in the specified state returns True

        :param old_state: the old appliance state
        :param new_state: the new appliance state
        """
        triggered = False
        if (old_state and new_state) and (old_state.VALUE == new_state.VALUE):
            triggered = old_state.VALUE == self._state
        if triggered:
            self._logger.info(
                "Trigger {} triggered by old state {} and new state {}".format(
                    self.name, old_state.VALUE, new_state.VALUE
                )
            )
        else:
            self._logger.debug(
                "Trigger {} not triggered by old state {} and new state {}".format(
                    self, old_state.VALUE, new_state.VALUE
                )
            )
        return triggered

    def __str__(self):
        s = " state trigger: %s" % self._state
        return super(Trigger, self).__str__() + s

    def get_next_fire_time(self, previous_fire_time, now):
        timedelta = datetime.timedelta(
            weeks=52
        )  # prevent scheduler from removing trigger
        result = datetime.datetime.now(self._timezone) + timedelta
        return result


from home.scheduler.trigger.state import delay, entering, exiting
