# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import callable


class Wind(callable.Forced):
    pass


class Brightness(callable.Callable):
    """
    A Brightness event will not automatically unlock a Forced Curtain
    """

    def run(self, event, state):
        return state


class SunTwilight(callable.Forced):
    pass


class SunHit(callable.Forced):
    pass


class Forced(callable.Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Closed):
            state = self.compute_new_state(state, "base", [event])
        return state
