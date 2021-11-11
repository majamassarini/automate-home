# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Presence(Callable):
    def run(self, event, state):
        return state


class Courtesy(Callable):
    def run(self, event, state):
        return state


class Brightness(Callable):
    def run(self, event, state):
        return state


class Toggle(Callable):
    def run(self, event, state):
        if event == home.event.toggle.Event.Off:
            state = self.get_new_state(state, "alarmed_off")
        return state


class Armed(Callable):
    def run(self, event, state):
        if event == home.event.alarm.armed.Event.Off:
            if (
                home.event.presence.Event.On in state
                or home.event.courtesy.Event.On in state
            ) and home.event.sun.brightness.Event.Bright not in state:
                state = self.get_new_state(state, "on")
            else:
                state = self.get_new_state(state, "off")
        return state


class Forced(Callable):
    """
    An alarmed light does not react to Forced Off events!!!
    """

    def run(self, event, state):
        if event != state.forced_enum.Not:
            state = state.unforce()
        return state
