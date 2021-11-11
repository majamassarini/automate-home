# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Power(Callable):
    def run(self, event, state):
        if (
            event == home.event.power.consumption.Event.High
            and home.event.enable.Event.On in state
        ):
            state = self.get_new_state(state, "detachable")
        return state


class Duration(Callable):
    def run(self, event, state):
        return state


class Enable(Callable):
    def run(self, event, state):
        if (
            event == home.event.enable.Event.On
            and home.event.power.consumption.Event.High in state
        ):
            state = self.get_new_state(state, "detachable")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Off:
            state = self.get_new_state(state, "forced_off")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
