# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Armed(Callable):
    def run(self, event, state):
        if home.event.alarm.armed.Event.On == event:
            if home.event.alarm.triggered.Event.On not in state:
                state = self.get_new_state(state, "armed")
            else:
                state = self.get_new_state(state, "triggered")
        return state


class Triggered(Callable):
    def run(self, event, state):
        return state
