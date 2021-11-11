# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class SunTwilight(Callable):
    def run(self, event, state):
        if event == home.event.sun.twilight.civil.Event.Sunset:
            state = self.get_new_state(state, "closed")
        return state


class Sleepiness(Callable):
    def run(self, event, state):
        if event == home.event.sleepiness.Event.Asleep:
            state = self.get_new_state(state, "closed")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Closed:
            state = self.get_new_state(state, "forced_closed")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
