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
    A scheduler trigger that fires when the appliance *remains* in the
    specified state (i.e. old state and new state are identical and both
    equal to the configured state value).

    Use :py:class:`entering.Trigger` if you want to react to the
    *transition* into a state rather than to its steady presence.
    """

    type = "APPLIANCE STATE"

    def __init__(self, name: str, events: Iterable[home.Event], state: str):
        """
        :param name: human-readable trigger name used in log messages
        :param events: events to deliver when this trigger fires
        :param state: the :py:attr:`State.VALUE` string that must match
        """
        super(Trigger, self).__init__(name, events)
        self._state = state

    def is_triggered(
        self, old_state: home.appliance.State, new_state: home.appliance.State
    ) -> bool:
        """
        Return ``True`` when the state has not changed and equals the
        configured state value.

        :param old_state: the appliance state before the last event
        :param new_state: the appliance state after the last event
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
        """
        Return a fire time far in the future so that APScheduler never
        removes this trigger from the scheduler.

        State-based triggers are fired manually (via
        :py:meth:`Process._schedule_by_appliance_state`) whenever the
        appliance state changes; they are not supposed to fire on their own.
        """
        timedelta = datetime.timedelta(
            weeks=52
        )  # prevent scheduler from removing trigger
        result = datetime.datetime.now(self._timezone) + timedelta
        return result


from home.scheduler.trigger.state import delay, entering, exiting
