# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Presence(Callable):
    def run(self, event, state):
        if event == home.event.presence.Event.Off:
            if home.event.clima.command.Event.On in state:
                state = self.get_new_state(state, "keep")
        return state


class Command(Callable):
    def run(self, event, state):
        if event == home.event.clima.command.Event.Keep:
            state = self.get_new_state(state, "keep")
        if event == home.event.clima.command.Event.Off:
            state = self.get_new_state(state, "off")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Off:
            state = self.get_new_state(state, "forced_off")
        elif event == state.forced_enum.Keep:
            state = self.get_new_state(state, "forced_keep")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
