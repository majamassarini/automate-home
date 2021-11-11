# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.sprinkler import event
from home.appliance.sprinkler.state import State as Parent
from home.appliance.sprinkler.state.forced.partially_on import callable as _callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.sun.phase.Event.Sunrise): _callable.SunPhase(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: _callable.Forced(
                base=self.base,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, attribute.mixin.IsOn, Parent):

    VALUE = "Forced Partially On"

    DURATION_EVENT = event.partially_on.duration.Event

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.sprinkler.state.off.State
        self.base = home.appliance.sprinkler.state.off.State
        self.forced_on = home.appliance.sprinkler.state.forced.on.State
        self.forced_off = home.appliance.sprinkler.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
