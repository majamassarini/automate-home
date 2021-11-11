# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.callable import Callable


class Presence(Callable):
    def run(self, event, state):
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
