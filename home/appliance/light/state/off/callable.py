# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable
from home.appliance.light.state.on import callable as on_callable


class Courtesy(Callable):
    def run(self, event, state):
        if event == home.event.courtesy.Event.On:
            if home.event.sun.brightness.Event.DeepDark in state:
                state = self.get_new_state(state, "on")
        return state


class Brightness(Callable):
    def run(self, event, state):
        if event == home.event.sun.brightness.Event.DeepDark:
            if home.event.courtesy.Event.On in state:
                state = self.get_new_state(state, "on")
        return state


class Forced(on_callable.Forced):
    def run(self, event, state):
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
