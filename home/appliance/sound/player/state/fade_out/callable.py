# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.callable import Callable
from home.appliance.sound.player.state.fade_in import callable as fade_in


class Elapsed(fade_in.Elapsed):
    pass


class Presence(fade_in.Presence):
    pass


class Forced(Callable):
    """
    A fading out state starts always from a forced state; when someone un-force the state
    it wants that the sound player exits from the fading out state too.
    """

    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        return state
