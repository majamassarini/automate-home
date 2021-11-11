# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.scheduler.trigger.state import delay


class Trigger(delay.Trigger):
    """
    >>> import home
    >>> off = home.appliance.sound.player.state.off.State()
    >>> fade_in = home.appliance.sound.player.state.fade_in.State()
    >>> trigger = home.scheduler.trigger.state.entering.delay.Trigger("adjust volume", [], 'Fade In', 1)
    >>> trigger.is_triggered(off, fade_in)
    True
    """

    def is_triggered(
        self, old_state: "home.appliance.State", new_state: "home.appliance.State"
    ) -> bool:
        """
        When state is changed and its value is like those the trigger wants return True

        :param old_state: the old appliance state
        :param new_state: the new appliance state
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
