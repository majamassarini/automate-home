# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.thermostat.presence import event
from home.appliance.thermostat.presence.state import State as Parent
from home.appliance.thermostat.presence.state.on import callable as on_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.clima.command.Event.Off): on_callable.Command(
                off=self.off, keep=self.keep
            ),
            type(home.event.presence.Event.Off): on_callable.Presence(
                off=self.off, keep=self.keep
            ),
            self.forced_enum: on_callable.Forced(
                forced_on=self.forced_on,
                forced_keep=self.forced_keep,
                forced_off=self.forced_off,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOn, mixin.IsNotKeeping, mixin.Setpoint, Parent):

    SETPOINT_EVENT = event.setpoint.Event

    def __init__(self, events=None, events_disabled=None):
        self.off = home.appliance.thermostat.presence.state.off.State
        self.keep = home.appliance.thermostat.presence.state.keep.State
        self.forced_on = home.appliance.thermostat.presence.state.forced.on.State
        self.forced_off = home.appliance.thermostat.presence.state.forced.off.State
        self.forced_keep = home.appliance.thermostat.presence.state.forced.keep.State

        super(State, self).__init__(events, events_disabled)
