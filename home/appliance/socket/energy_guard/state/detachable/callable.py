# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Power(Callable):
    def run(self, event, state):
        if event in (
            home.event.power.consumption.Event.Low,
            home.event.power.consumption.Event.No,
        ):
            state = self.get_new_state(state, "on")
        return state


class Duration(Callable):
    def run(self, event, state):
        if event == home.event.power.consumption.duration.Event.Long:
            state = self.get_new_state(state, "off")
        return state


class Enable(Callable):
    def run(self, event, state):
        if event == home.event.enable.Event.Off:
            state = self.get_new_state(state, "on")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Off:
            state = self.get_new_state(state, "forced_off")
        elif event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
