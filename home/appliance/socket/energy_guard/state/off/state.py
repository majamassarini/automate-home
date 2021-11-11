# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.socket.energy_guard.state import State as Parent
from home.appliance.socket.energy_guard.state.off import callable as off_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.power.consumption.Event.No): off_callable.Power(on=self.on),
            type(
                home.event.power.consumption.duration.Event.Short
            ): off_callable.Duration(on=self.on),
            type(home.event.enable.Event.Off): off_callable.Enable(on=self.on),
            self.forced_enum: off_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOff, mixin.IsNotDetachable, Parent):
    def __init__(self, events=None, events_disabled=None):

        self.on = home.appliance.socket.energy_guard.state.on.State
        self.forced_on = home.appliance.socket.energy_guard.state.forced.on.State
        self.forced_off = home.appliance.socket.energy_guard.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
