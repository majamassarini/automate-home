# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.scheduler.trigger.state import delay


class Trigger(delay.Trigger):
    def is_triggered(
        self, old_state: "home.appliance.State", new_state: "home.appliance.State"
    ) -> bool:
        """
        When state is changed and its value is no more like those the trigger wants return True

        :param old_state: the old appliance state
        :param new_state: the new appliance state
        """
        triggered = False
        if (old_state and new_state) and (old_state.VALUE != new_state.VALUE):
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
                    self.name, old_state.VALUE, new_state.VALUE
                )
            )
        return triggered

    def __str__(self):
        s = ", exiting state delay: %s" % self._timeout
        return super(Trigger, self).__str__() + s
