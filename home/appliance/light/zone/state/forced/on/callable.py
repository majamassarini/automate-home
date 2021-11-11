# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import callable


class Presence(callable.Forced):
    """
    A Presence event will not automatically unlock a Forced Light
    """

    def run(self, event, state):
        return state


class Courtesy(callable.Forced):
    """
    A Courtesy event will not automatically unlock a Forced Light
    """

    def run(self, event, state):
        return state


class Brightness(callable.Forced):
    """
    Just a sun brightness high event will automatically unlock a Forced Light
    """

    def run(self, event, state):
        if event == home.event.sun.brightness.Event.Bright:
            return super(Brightness, self).run(event, state)
        else:
            return state


class Armed(callable.Forced):
    def run(self, event, state):
        if event == home.event.alarm.armed.Event.On:
            return super(Armed, self).run(event, state)
        else:
            return state


class Toggle(callable.Forced):
    """
    A Toggle event will not automatically unlock a Forced Light
    """

    def run(self, event, state):
        return state


class Forced(callable.Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        return state
