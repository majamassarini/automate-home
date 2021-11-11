# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable
from home.appliance.socket.energy_guard.state.on import callable as on_callable


class Power(Callable):
    def run(self, event, state):
        if (
            event != home.event.power.consumption.Event.High
            and home.event.enable.Event.On in state
        ):
            state = self.get_new_state(state, "on")
            state = state.next(home.event.enable.Event.Off)
        return state


class Duration(Callable):
    def run(self, event, state):
        return state


class Enable(Callable):
    def run(self, event, state):
        return state


class Forced(on_callable.Forced):
    def run(self, event, state):
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
