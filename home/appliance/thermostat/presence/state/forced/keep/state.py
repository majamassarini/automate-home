# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.thermostat.presence import event
from home.appliance.thermostat.presence.state.forced.keep import (
    callable as forced_keep_callable,
)
from home.appliance.thermostat.presence.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.clima.command.Event.Off): forced_keep_callable.Command(
                reset=self.reset, base=self.base
            ),
            type(home.event.presence.Event.Off): forced_keep_callable.Presence(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: forced_keep_callable.Forced(
                reset=self.reset,
                base=self.base,
                forced_on=self.forced_on,
                forced_off=self.forced_off,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(mixin.IsOn, mixin.IsKeeping, mixin.Setpoint, Mixin, Parent):

    SETPOINT_EVENT = event.keep.setpoint.Event

    VALUE = "Forced Keeping"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.thermostat.presence.state.keep.State
        self.base = home.appliance.thermostat.presence.state.keep.State
        self.forced_on = home.appliance.thermostat.presence.state.forced.on.State
        self.forced_off = home.appliance.thermostat.presence.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
