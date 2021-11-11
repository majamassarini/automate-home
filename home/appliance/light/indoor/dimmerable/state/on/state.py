# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.light.indoor.dimmerable.state import State as Parent
from home.appliance.light.indoor.dimmerable.state.on import callable as on_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): on_callable.Presence(off=self.off),
            type(home.event.sun.brightness.Event.Bright): on_callable.Brightness(
                off=self.off
            ),
            self.forced_enum: on_callable.Forced(
                forced_on=self.forced_on,
                forced_show=self.forced_show,
                forced_circadian_rhythm=self.forced_circadian_rhythm,
                forced_lux_balance=self.forced_lux_balance,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    Mixin,
    attribute.mixin.IsOn,
    attribute.mixin.IsNotCircadianRhythm,
    attribute.mixin.IsNotLuxBalancing,
    attribute.mixin.IsNotShowing,
    Parent,
):
    def __init__(self, events=None, events_disabled=None):
        self.off = home.appliance.light.indoor.dimmerable.state.off.State
        self.forced_on = home.appliance.light.indoor.dimmerable.state.forced.on.State
        self.forced_circadian_rhythm = (
            home.appliance.light.indoor.dimmerable.state.forced.circadian_rhythm.State
        )
        self.forced_lux_balance = (
            home.appliance.light.indoor.dimmerable.state.forced.lux_balance.State
        )
        self.forced_show = (
            home.appliance.light.indoor.dimmerable.state.forced.show.State
        )

        super(State, self).__init__(events, events_disabled)
