# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light.state import State as Parent
from home.appliance.light.state.off import callable as off_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.courtesy.Event.Off): off_callable.Courtesy(on=self.on),
            type(home.event.sun.brightness.Event.Bright): off_callable.Brightness(
                on=self.on
            ),
            self.forced_enum: off_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOff, Parent):

    VALUE = "Off"

    def __init__(self, events=None, events_disabled=None):

        self.on = home.appliance.light.state.on.State
        self.forced_on = home.appliance.light.state.forced.on.State
        self.forced_off = home.appliance.light.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
