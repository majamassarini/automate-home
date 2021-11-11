# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import callable


class Power(callable.Callable):
    """
    A Power event will not automatically unlock a Forced Light
    """

    def run(self, event, state):
        return state


class Duration(Power):
    pass


class Enable(callable.Forced):
    def run(self, event, state):
        if "reset" in self._output_states:
            new_state = self.compute_new_state(
                state, "base", [f for f in state.forced_enum]
            )
            if new_state.__class__ == self._output_states["reset"]:
                state = state.unforce()
        return state


class Forced(callable.Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.On):
            state = self.compute_new_state(state, "base", [event])
        return state
