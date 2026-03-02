# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import home

from home.scheduler.trigger.state.entering import delay
from typing import Iterable


class Trigger(delay.Trigger):
    """
    A delayed entering trigger whose timeout is read from the new state's
    ``duration`` attribute at the moment the transition is detected.

    This is useful for appliances (e.g. sprinklers) whose active-state
    duration is part of their configuration rather than a fixed constant.
    If the appliance enters the same state again before the timer expires,
    the previous pending trigger is disabled and a new timer is started
    with the duration of the new state.
    """

    def __init__(self, name: str, events: Iterable[home.Event], state: str):
        # timeout_seconds is 0 here; the real value is read from
        # new_state.duration each time is_triggered() fires.
        super(Trigger, self).__init__(name, events, state, 0)

    def is_triggered(
        self,
        old_state: home.appliance.State,
        new_state: home.appliance.State,
    ) -> bool:
        """
        Return ``True`` when the state changes and the new state matches
        the configured state value, and update the delay timeout from
        ``new_state.duration``.

        :param old_state: the appliance state before the last event
        :param new_state: the appliance state after the last event
        """
        triggered = super(Trigger, self).is_triggered(old_state, new_state)
        try:
            self._delay.timeout = new_state.duration  # type: ignore[attr-defined]
        except AttributeError as e:
            self._logger.debug("{} for {}".format(e, new_state))
        return triggered

    def __str__(self):
        s = ", entering state delay for given duration: %s" % self._timeout
        return super(Trigger, self).__str__() + s
