# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Sleepiness(Callable):
    def run(self, event, state):
        if home.event.wind.Event.Strong not in state:
            if event == home.event.sleepiness.Event.Asleep:
                state = self.get_new_state(state, "closed")
        return state


class Wind(Callable):
    def _run(self, state):
        if (
            home.event.sun.twilight.civil.Event.Sunset in state
            or home.event.sleepiness.Event.Asleep in state
        ):
            state = self.get_new_state(state, "closed")
        if home.event.sun.brightness.Event.Bright in state:
            if home.event.sun.hit.Event.Sunhit in state:
                state = self.get_new_state(state, "closed")
        return state

    def run(self, event, state):
        if event == home.event.wind.Event.Weak:
            state = self._run(state)
        return state
