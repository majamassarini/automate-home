# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.callable import Callable
from home.appliance.light.presence.state.off import callable


class Presence(callable.Presence):
    pass


class Brightness(Callable):
    def run(self, event, state):
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        elif event == state.forced_enum.CircadianRhythm:
            state = self.get_new_state(state, "forced_circadian_rhythm")
        elif event == state.forced_enum.LuxBalance:
            state = self.get_new_state(state, "forced_lux_balance")
        elif event == state.forced_enum.Show:
            state = self.get_new_state(state, "forced_show")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
