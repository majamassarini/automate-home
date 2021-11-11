# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sound.player.state.forced.on import callable as forced_on
from home.appliance.callable import Callable


class Presence(forced_on.Presence):
    pass


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Not:
            state = self.compute_new_state(state, "base", [event])
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        if event == state.forced_enum.CircadianRhythm:
            state = self.get_new_state(state, "forced_circadian_rhythm")
        return state
