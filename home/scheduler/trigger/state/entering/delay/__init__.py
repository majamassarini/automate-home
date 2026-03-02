# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import home

from home.scheduler.trigger.state import delay


class Trigger(delay.Trigger):
    """
    A delayed scheduler trigger that fires *timeout_seconds* after the
    appliance *enters* the specified state.

    If the appliance enters the same state again before the timer expires,
    the previous pending trigger is disabled and a new timer is started.

    >>> import home
    >>> off = home.appliance.sound.player.state.off.State()
    >>> fade_in = home.appliance.sound.player.state.fade_in.State()
    >>> trigger = home.scheduler.trigger.state.entering.delay.Trigger("adjust volume", [], 'Fade In', 1)
    >>> trigger.is_triggered(off, fade_in)
    True
    """

    def is_triggered(
        self, old_state: home.appliance.State, new_state: home.appliance.State
    ) -> bool:
        """
        Return ``True`` when the state changes and the new state matches
        the configured state value.

        :param old_state: the appliance state before the last event
        :param new_state: the appliance state after the last event
        """
        triggered = False
        if (old_state and new_state) and (old_state.VALUE != new_state.VALUE):
            triggered = new_state.VALUE == self._state
        if triggered:
            self._logger.info(
                "Trigger {} triggered by old state {} and new state {}".format(
                    self.name, old_state.VALUE, new_state.VALUE
                )
            )
        else:
            self._logger.debug(
                "Trigger {} not triggered by old state {} and new state {}".format(
                    self.name, old_state.VALUE, new_state.VALUE
                )
            )
        return triggered

    def __str__(self):
        s = ", entering state delay: %s" % self._timeout
        return super(Trigger, self).__str__() + s


from home.scheduler.trigger.state.entering.delay import duration
from home.scheduler.trigger.state.entering.delay import enable_events
