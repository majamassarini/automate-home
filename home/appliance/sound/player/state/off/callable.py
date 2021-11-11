# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Sleepiness(Callable):
    def run(self, event, state):
        if event == home.event.sleepiness.Event.Awake:
            if home.event.elapsed.Event.On not in state:
                state = self.get_new_state(state, "fade_in")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        elif event == state.forced_enum.CircadianRhythm:
            state = self.get_new_state(state, "forced_circadian_rhythm")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
