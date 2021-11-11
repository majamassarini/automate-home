# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import callable


class Presence(callable.Forced):
    pass


class Courtesy(callable.Forced):
    pass


class Brightness(callable.Forced):
    pass


class Armed(callable.Forced):
    pass


class Toggle(callable.Forced):
    pass


class Forced(callable.Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.On):
            state = self.compute_new_state(state, "base", [event])
        return state
