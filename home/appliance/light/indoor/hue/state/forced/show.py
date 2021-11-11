# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.light.indoor.dimmerable.state.forced.show import Mixin
from home.appliance.light.indoor.hue.state import State as Parent


class State(
    attribute.mixin.IsOn,
    attribute.mixin.IsShowing,
    attribute.mixin.IsNotCircadianRhythm,
    attribute.mixin.IsNotLuxBalancing,
    Mixin,
    Parent,
):

    VALUE = "Forced Show"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.light.indoor.hue.state.off.State
        self.base = home.appliance.light.indoor.hue.state.off.State
        self.forced_circadian_rhythm = (
            home.appliance.light.indoor.hue.state.forced.circadian_rhythm.State
        )
        self.forced_lux_balance = (
            home.appliance.light.indoor.hue.state.forced.lux_balance.State
        )
        self.forced_on = home.appliance.light.indoor.hue.state.forced.on.State

        super(State, self).__init__(events, events_disabled)
