# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.socket.energy_guard.state import State as Parent
from home.appliance.socket.energy_guard.state.on import callable as on_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.power.consumption.Event.No): on_callable.Power(
                detachable=self.detachable
            ),
            type(
                home.event.power.consumption.duration.Event.Short
            ): on_callable.Duration(detachable=self.detachable),
            type(home.event.enable.Event.Off): on_callable.Enable(
                detachable=self.detachable
            ),
            self.forced_enum: on_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOn, mixin.IsNotDetachable, Parent):
    def __init__(self, events=None, events_disabled=None):
        self.detachable = home.appliance.socket.energy_guard.state.detachable.State
        self.forced_on = home.appliance.socket.energy_guard.state.forced.on.State
        self.forced_off = home.appliance.socket.energy_guard.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
