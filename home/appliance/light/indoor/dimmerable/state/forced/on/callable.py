# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import callable


class Presence(callable.Forced):
    """
    Just a event.presence.Event.Off event will unlock a Forced Light
    """

    def run(self, event, state):
        if event == home.event.presence.Event.Off:
            return super(Presence, self).run(event, state)
        else:
            return state


class Brightness(callable.Forced):
    """
    A Brightness event will not automatically unlock a Forced Light
    """

    def run(self, event, state):
        return state


class Forced(callable.Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        return state
