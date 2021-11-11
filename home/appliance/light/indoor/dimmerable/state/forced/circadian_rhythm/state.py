# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light import event
from home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm import (
    callable as forced_circadian_rhythm,
)
from home.appliance.light.indoor.dimmerable.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): forced_circadian_rhythm.Presence(
                reset=self.reset, base=self.base
            ),
            type(
                home.event.sun.brightness.Event.Bright
            ): forced_circadian_rhythm.Brightness(reset=self.reset, base=self.base),
            self.forced_enum: forced_circadian_rhythm.Forced(
                reset=self.reset,
                base=self.base,
                forced_on=self.forced_on,
                forced_show=self.forced_show,
                forced_lux_balance=self.forced_lux_balance,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    mixin.IsOn,
    mixin.IsCircadianRhythm,
    mixin.IsNotLuxBalancing,
    mixin.IsNotShowing,
    Mixin,
    Parent,
):

    VALUE = "Forced Circadian Rhythm"
    BRIGHTNESS_EVENT = event.circadian_rhythm.brightness.Event

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.light.indoor.dimmerable.state.off.State
        self.base = home.appliance.light.indoor.dimmerable.state.off.State
        self.forced_on = home.appliance.light.indoor.dimmerable.state.forced.on.State
        self.forced_lux_balance = (
            home.appliance.light.indoor.dimmerable.state.forced.lux_balance.State
        )
        self.forced_show = (
            home.appliance.light.indoor.dimmerable.state.forced.show.State
        )

        super(State, self).__init__(events, events_disabled)
