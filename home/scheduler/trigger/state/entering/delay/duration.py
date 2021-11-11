# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.scheduler.trigger.state.entering import delay
from typing import Iterable


class Trigger(delay.Trigger):
    """
    A **Scheduler Trigger** triggered *timeout_seconds* (a value changing with the duration attribute of the new state)
    after a given **Appliance state** has been triggered.
    If an *Appliance state* has been triggered twice, the old scheduler trigger is disabled and a new one is started.
    """

    def __init__(self, name: str, events: Iterable["home.Event"], state: str):
        # timeout seconds is controlled by duration attribute in new state, read when triggered
        super(Trigger, self).__init__(name, events, state, 0)

    def is_triggered(
        self,
        old_state: "home.appliance.State",
        new_state: "home.appliance.attribute.mixin.Duration",
    ) -> bool:
        """
        When state is changed and its value is like those the trigger wants return True

        :param old_state: the old appliance state
        :param new_state: the new appliance state
        """
        triggered = super(Trigger, self).is_triggered(old_state, new_state)
        try:
            self._delay.timeout = new_state.duration
        except AttributeError as e:
            self._logger.debug("{} for {}".format(e, new_state))
        return triggered

    def __str__(self):
        s = ", entering state delay for given duration: %s" % self._timeout
        return super(Trigger, self).__str__() + s
