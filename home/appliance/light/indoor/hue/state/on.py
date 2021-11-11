# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.light import event
from home.appliance.light.indoor.dimmerable.state.on import Mixin
from home.appliance.light.indoor.hue.state import State as Parent


class State(
    Mixin,
    attribute.mixin.IsOn,
    attribute.mixin.IsNotCircadianRhythm,
    attribute.mixin.IsNotLuxBalancing,
    attribute.mixin.IsNotShowing,
    Parent,
):

    BRIGHTNESS_EVENT = event.brightness.Event

    def __init__(self, events=None, events_disabled=None):
        self.off = home.appliance.light.indoor.hue.state.off.State
        self.forced_on = home.appliance.light.indoor.hue.state.forced.on.State
        self.forced_show = home.appliance.light.indoor.hue.state.forced.show.State
        self.forced_circadian_rhythm = (
            home.appliance.light.indoor.hue.state.forced.circadian_rhythm.State
        )
        self.forced_lux_balance = (
            home.appliance.light.indoor.hue.state.forced.lux_balance.State
        )

        super(State, self).__init__(events, events_disabled)
