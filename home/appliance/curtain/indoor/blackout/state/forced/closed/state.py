# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home

from home.appliance.attribute import mixin
from home.appliance.curtain.indoor.blackout.state import State as Parent
from home.appliance.curtain.indoor.blackout.state.forced.closed import (
    callable as forced_closed_callable,
)


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.sleepiness.Event.Awake): forced_closed_callable.Sleepiness(
                base=self.base, reset=self.reset
            ),
            type(
                home.event.sun.twilight.civil.Event.Sunrise
            ): forced_closed_callable.SunTwilight(base=self.base, reset=self.reset),
            self.forced_enum: forced_closed_callable.Forced(
                base=self.base, reset=self.reset
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsClosed, Parent):

    VALUE = "Forced Closed"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.curtain.indoor.blackout.state.closed.State
        self.base = home.appliance.curtain.indoor.blackout.state.opened.State

        super(State, self).__init__(events, events_disabled)
