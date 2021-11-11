# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.sound.player.state.forced.on import callable as forced_on
from home.appliance.callable import Callable


class Sleepiness(Callable):
    def run(self, event, state):
        if home.event.presence.Event.On in state:
            if event == home.event.sleepiness.Event.Asleep:
                state = self.compute_new_state(
                    state, "fade_out", [state.forced_enum.CircadianRhythm]
                )
        return state


class Presence(forced_on.Presence):
    pass


class Forced(forced_on.Forced):
    pass
