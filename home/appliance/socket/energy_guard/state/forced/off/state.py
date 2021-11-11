# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.socket.energy_guard.state.forced.off import (
    callable as forced_off_callable,
)
from home.appliance.socket.energy_guard.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.power.consumption.Event.No): forced_off_callable.Power(
                reset=self.reset, base=self.base
            ),
            type(
                home.event.power.consumption.duration.Event.Short
            ): forced_off_callable.Duration(reset=self.reset, base=self.base),
            type(home.event.enable.Event.Off): forced_off_callable.Enable(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: forced_off_callable.Forced(
                reset=self.reset, base=self.base
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(mixin.IsOff, mixin.IsNotDetachable, Mixin, Parent):

    VALUE = "Forced Off"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.socket.energy_guard.state.off.State
        self.base = home.appliance.socket.energy_guard.state.on.State

        super(State, self).__init__(events, events_disabled)
