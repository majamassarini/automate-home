# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.sprinkler import event
from home.appliance.sprinkler.state import State as Parent
from home.appliance.sprinkler.state.forced.off import callable as _callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.sun.phase.Event.Sunrise): _callable.SunPhase(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: _callable.Forced(
                base=self.base,
                forced_on=self.forced_on,
                forced_partially_on=self.forced_partially_on,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, attribute.mixin.IsOff, Parent):

    VALUE = "Forced Off"

    DURATION_EVENT = event.duration.Event

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.sprinkler.state.off.State
        self.base = home.appliance.sprinkler.state.off.State
        self.off = home.appliance.sprinkler.state.off.State
        self.forced_on = home.appliance.sprinkler.state.forced.on.State
        self.forced_partially_on = (
            home.appliance.sprinkler.state.forced.partially_on.State
        )

        super(State, self).__init__(events, events_disabled)
