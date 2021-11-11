# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.socket.energy_guard.state.forced.on import (
    callable as forced_on_callable,
)
from home.appliance.socket.energy_guard.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.power.consumption.Event.No): forced_on_callable.Power(
                reset=self.reset, base=self.base
            ),
            type(
                home.event.power.consumption.duration.Event.Short
            ): forced_on_callable.Duration(reset=self.reset, base=self.base),
            type(home.event.enable.Event.Off): forced_on_callable.Enable(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: forced_on_callable.Forced(
                reset=self.reset, base=self.base
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(mixin.IsOn, mixin.IsNotDetachable, Mixin, Parent):

    VALUE = "Forced On"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.socket.energy_guard.state.on.State
        self.base = home.appliance.socket.energy_guard.state.on.State

        super(State, self).__init__(events, events_disabled)
