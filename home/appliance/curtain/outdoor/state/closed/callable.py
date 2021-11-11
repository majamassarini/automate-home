# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable
from home.appliance.curtain.outdoor.state.opened import callable as opened_callable


class Wind(Callable):
    def run(self, event, state):
        if event == home.event.wind.Event.Strong:
            state = self.get_new_state(state, "opened")
        return state


class Brightness(Callable):
    def run(self, event, state):
        if event in (
            home.event.sun.brightness.Event.Dark,
            home.event.sun.brightness.Event.DeepDark,
        ):
            if home.event.sun.twilight.civil.Event.Sunset not in state:
                state = self.get_new_state(state, "opened")
        return state


class SunTwilight(Callable):
    def run(self, event, state):
        if event == home.event.sun.twilight.civil.Event.Sunrise:
            if home.event.sun.hit.Event.Sunhit not in state:
                state = self.get_new_state(state, "opened")
            else:
                if home.event.sun.brightness.Event.Bright not in state:
                    state = self.get_new_state(state, "opened")
        return state


class SunHit(Callable):
    def run(self, event, state):
        if event == home.event.sun.hit.Event.Sunleft:
            if home.event.sun.twilight.civil.Event.Sunset not in state:
                state = self.get_new_state(state, "opened")
        return state


class Forced(opened_callable.Forced):
    def run(self, event, state):
        if event == state.forced_enum.Opened:
            state = self.get_new_state(state, "forced_opened")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
