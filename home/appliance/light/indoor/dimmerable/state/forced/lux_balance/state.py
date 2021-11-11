# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light import event
from home.appliance.light.indoor.dimmerable.state.forced.lux_balance import (
    callable as forced_lux_balance,
)
from home.appliance.light.indoor.dimmerable.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): forced_lux_balance.Presence(
                reset=self.reset, base=self.base
            ),
            type(home.event.sun.brightness.Event.Bright): forced_lux_balance.Brightness(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: forced_lux_balance.Forced(
                reset=self.reset,
                base=self.base,
                forced_show=self.forced_show,
                forced_circadian_rhythm=self.forced_circadian_rhythm,
                forced_on=self.forced_on,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    mixin.IsOn,
    mixin.IsLuxBalancing,
    mixin.IsNotCircadianRhythm,
    mixin.IsNotShowing,
    Mixin,
    Parent,
):

    VALUE = "Forced Lux Balancing"
    BRIGHTNESS_EVENT = event.lux_balancing.brightness.Event

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.light.indoor.dimmerable.state.off.State
        self.base = home.appliance.light.indoor.dimmerable.state.off.State
        self.forced_circadian_rhythm = (
            home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm.State
        )
        self.forced_on = home.appliance.light.indoor.dimmerable.state.forced.on.State
        self.forced_show = (
            home.appliance.light.indoor.dimmerable.state.forced.show.State
        )

        super(State, self).__init__(events, events_disabled)
