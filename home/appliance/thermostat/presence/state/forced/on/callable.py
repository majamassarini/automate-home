# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import callable


class Presence(callable.Forced):
    pass


class Command(callable.Forced):
    pass


class Forced(callable.Callable):
    def run(self, event, state):
        if event == state.forced_enum.Off:
            state = self.get_new_state(state, "forced_off")
        elif event == state.forced_enum.Keep:
            state = self.get_new_state(state, "forced_keep")
        elif event == state.forced_enum.Not:
            state = self.compute_new_state(state, "base", [event])
        return state
