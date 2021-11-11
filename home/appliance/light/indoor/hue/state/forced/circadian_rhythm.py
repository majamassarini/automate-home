# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.light import event
from home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm import Mixin
from home.appliance.light.indoor.hue.state import State as Parent


class State(
    attribute.mixin.IsOn,
    attribute.mixin.IsCircadianRhythm,
    attribute.mixin.IsNotLuxBalancing,
    attribute.mixin.IsNotShowing,
    Mixin,
    Parent,
):

    VALUE = "Forced Circadian Rhythm"

    HUE_EVENT = event.circadian_rhythm.hue.Event
    BRIGHTNESS_EVENT = event.circadian_rhythm.brightness.Event
    SATURATION_EVENT = event.circadian_rhythm.saturation.Event
    TEMPERATURE_EVENT = event.circadian_rhythm.temperature.Event

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.light.indoor.hue.state.off.State
        self.base = home.appliance.light.indoor.hue.state.off.State
        self.forced_on = home.appliance.light.indoor.hue.state.forced.on.State
        self.forced_show = home.appliance.light.indoor.hue.state.forced.show.State
        self.forced_lux_balance = (
            home.appliance.light.indoor.hue.state.forced.lux_balance.State
        )

        super(State, self).__init__(events, events_disabled)
