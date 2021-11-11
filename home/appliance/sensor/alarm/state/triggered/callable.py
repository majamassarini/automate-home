# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Armed(Callable):
    def run(self, event, state):
        if home.event.alarm.armed.Event.Off == event:
            state = self.get_new_state(state, "unarmed")
        return state


class Triggered(Callable):
    def run(self, event, state):
        if home.event.alarm.triggered.Event.Off == event:
            if home.event.alarm.armed.Event.On in state:
                state = self.get_new_state(state, "armed")
            else:
                state = self.get_new_state(state, "unarmed")
        return state
