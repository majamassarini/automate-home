# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import callable


class Presence(callable.Callable):
    def run(self, event, state):
        if event == home.event.presence.Event.Off:
            state = self.compute_new_state(state, "base", [state.forced_enum.On])
        return state


class Christmas(callable.Forced):
    pass


class SanSilvester(callable.Forced):
    pass


class Epiphany(callable.Forced):
    pass


class SunBrightness(callable.Forced):
    pass


class Forced(callable.Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        return state
