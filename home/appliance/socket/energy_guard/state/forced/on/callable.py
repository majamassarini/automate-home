# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import callable


class Power(callable.Callable):
    """
    A Power event will not automatically unlock a Forced Socket
    """

    def run(self, event, state):
        return state


class Duration(Power):
    pass


class Enable(callable.Forced):
    pass


class Forced(callable.Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        return state
