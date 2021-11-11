# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Enable(Callable):
    def run(self, event, state):
        if event == home.event.enable.Event.Off:
            state = self.get_new_state(state, "off")
        return state


class SunPhase(Callable):
    def run(self, event, state):
        if event == home.event.sun.phase.Event.Sunrise:
            state = self.get_new_state(state, "off")
        return state


class HasRained(Callable):
    def run(self, event, state):
        if event == home.event.rain.in_the_past.Event.On:
            if (
                home.event.rain.Event.No in state
                and home.event.rain.forecast.Event.Off in state
            ):
                state = self.get_new_state(state, "partially_on")
            else:
                state = self.get_new_state(state, "off")
        return state


class WillRain(Callable):
    def run(self, event, state):
        if event == home.event.rain.forecast.Event.On:
            if (
                home.event.rain.Event.No in state
                and home.event.rain.in_the_past.Event.Off in state
                and home.event.enable.Event.On
            ):
                state = self.get_new_state(state, "partially_on")
            else:
                state = self.get_new_state(state, "off")
        return state


class IsRaining(Callable):
    def run(self, event, state):
        if event == home.event.rain.Event.Gentle:
            state = self.get_new_state(state, "off")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Off:
            state = self.get_new_state(state, "forced_off")
        elif event == state.forced_enum.PartiallyOn:
            state = self.get_new_state(state, "forced_partially_on")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
