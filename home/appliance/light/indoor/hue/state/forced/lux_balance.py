# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.light import event
from home.appliance.light.indoor.dimmerable.state.forced.lux_balance import Mixin
from home.appliance.light.indoor.hue.state import State as Parent


class State(
    attribute.mixin.IsOn,
    attribute.mixin.IsLuxBalancing,
    attribute.mixin.IsNotCircadianRhythm,
    attribute.mixin.IsNotShowing,
    Mixin,
    Parent,
):

    VALUE = "Forced Lux Balancing"
    BRIGHTNESS_EVENT = event.lux_balancing.brightness.Event

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.light.indoor.hue.state.off.State
        self.base = home.appliance.light.indoor.hue.state.off.State
        self.forced_on = home.appliance.light.indoor.hue.state.forced.on.State
        self.forced_show = home.appliance.light.indoor.hue.state.forced.show.State
        self.forced_circadian_rhythm = (
            home.appliance.light.indoor.hue.state.forced.circadian_rhythm.State
        )

        super(State, self).__init__(events, events_disabled)
