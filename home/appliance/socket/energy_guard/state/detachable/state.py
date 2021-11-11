# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.socket.energy_guard.state import State as Parent
from home.appliance.socket.energy_guard.state.detachable import (
    callable as detachable_callable,
)


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.power.consumption.Event.No): detachable_callable.Power(
                off=self.off, on=self.on
            ),
            type(
                home.event.power.consumption.duration.Event.Short
            ): detachable_callable.Duration(off=self.off, on=self.on),
            type(home.event.enable.Event.Off): detachable_callable.Enable(
                off=self.off, on=self.on
            ),
            self.forced_enum: detachable_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsDetachable, mixin.IsOn, Parent):
    """
    This State has been introduced  because of the *is_detachable* property
    (found in mixin.IsDetachable).

    Through the is_detachable property messages of advice could be sent to the
    user when entering or staying into the detachable State.
    """

    def __init__(self, events=None, events_disabled=None):
        self.off = home.appliance.socket.energy_guard.state.off.State
        self.on = home.appliance.socket.energy_guard.state.on.State
        self.forced_on = home.appliance.socket.energy_guard.state.forced.on.State
        self.forced_off = home.appliance.socket.energy_guard.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
