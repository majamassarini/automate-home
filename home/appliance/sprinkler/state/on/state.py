# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.sprinkler import event
from home.appliance.sprinkler.state import State as Parent
from home.appliance.sprinkler.state.on import callable as _callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.enable.Event.Off): _callable.Enable(
                off=self.off, partially_on=self.partially_on
            ),
            type(home.event.sun.phase.Event.Sunrise): _callable.SunPhase(
                off=self.off, partially_on=self.partially_on
            ),
            type(home.event.rain.in_the_past.Event.Off): _callable.HasRained(
                off=self.off, partially_on=self.partially_on
            ),
            type(home.event.rain.Event.No): _callable.IsRaining(
                off=self.off, partially_on=self.partially_on
            ),
            type(home.event.rain.forecast.Event.Off): _callable.WillRain(
                off=self.off, partially_on=self.partially_on
            ),
            self.forced_enum: _callable.Forced(
                forced_off=self.forced_off,
                forced_partially_on=self.forced_partially_on,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, attribute.mixin.IsOn, Parent):

    VALUE = "On"

    DURATION_EVENT = event.duration.Event

    def __init__(self, events=None, events_disabled=None):
        self.forced_off = home.appliance.sprinkler.state.forced.off.State
        self.forced_partially_on = (
            home.appliance.sprinkler.state.forced.partially_on.State
        )
        self.off = home.appliance.sprinkler.state.off.State
        self.partially_on = home.appliance.sprinkler.state.partially_on.State

        super(State, self).__init__(events, events_disabled)
