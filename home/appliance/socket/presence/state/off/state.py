# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.socket.presence.state import State as Parent
from home.appliance.socket.presence.state.off import callable as off_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): off_callable.Presence(),
            self.forced_enum: off_callable.Forced(forced_on=self.forced_on),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOff, Parent):
    def __init__(self, events=None, events_disabled=None):
        self.forced_on = home.appliance.socket.presence.state.forced.on.State

        super(State, self).__init__(events, events_disabled)
