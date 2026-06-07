# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable
from home.appliance.sound.player.state.forced.on import callable as forced_on


class Sleepiness(Callable):
    def run(self, event, state):
        if event == home.event.sleepiness.Event.Awake:
            state = self.get_new_state(state, "forced_on")
        elif event == home.event.sleepiness.Event.Asleep:
            if home.event.presence.Event.On in state:
                state = self.compute_new_state(
                    state, "fade_out", [state.forced_enum.On]
                )
        return state


class Presence(forced_on.Presence):
    pass


class Forced(Callable):
    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.get_new_state(state, "base")
        elif event == state.forced_enum.CircadianRhythm:
            state = self.get_new_state(state, "forced_circadian_rhythm")
        return state
