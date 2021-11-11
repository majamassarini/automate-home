# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable, Forced as Parent


class SunPhase(Parent):
    def run(self, event, state):
        if event == home.event.sun.phase.Event.Sunset:
            return state
        else:
            return super(SunPhase, self).run(event, state)


class Forced(Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        return state
