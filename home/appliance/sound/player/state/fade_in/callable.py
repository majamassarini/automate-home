# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Elapsed(Callable):
    def run(self, event, state):
        if event == home.event.elapsed.Event.On:
            state = self.get_new_state(state, "off")
        return state


class Presence(Callable):
    def run(self, event, state):
        if event == home.event.presence.Event.Off:
            state = self.get_new_state(state, "off")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        # otherwise do not override this status
        return state
