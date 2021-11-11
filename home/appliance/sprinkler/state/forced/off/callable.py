# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sprinkler.state.forced.on import callable as forced_on
from home.appliance.callable import Callable


class SunPhase(forced_on.SunPhase):
    pass


class Forced(Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        if event == state.forced_enum.PartiallyOn:
            state = self.get_new_state(state, "forced_partially_on")
        return state
