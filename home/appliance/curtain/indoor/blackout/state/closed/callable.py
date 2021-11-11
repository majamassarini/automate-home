# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Sleepiness(Callable):
    def run(self, event, state):
        if event in (
            home.event.sleepiness.Event.Awake,
            home.event.sleepiness.Event.Sleepy,
        ):
            if home.event.sun.twilight.civil.Event.Sunset not in state:
                state = self.get_new_state(state, "opened")
        return state


class SunTwilight(Callable):
    def run(self, event, state):
        if event == home.event.sun.twilight.civil.Event.Sunrise and (
            home.event.sleepiness.Event.Awake in state
            or home.event.sleepiness.Event.Sleepy in state
        ):
            state = self.get_new_state(state, "opened")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Opened:
            state = self.get_new_state(state, "forced_opened")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
