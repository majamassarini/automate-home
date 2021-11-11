# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light.state.forced.on import callable as forced_on_callable
from home.appliance.light.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.courtesy.Event.Off): forced_on_callable.Courtesy(
                reset=self.reset, base=self.base
            ),
            type(home.event.sun.brightness.Event.Bright): forced_on_callable.Brightness(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: forced_on_callable.Forced(
                reset=self.reset, base=self.base
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(mixin.IsOn, Mixin, Parent):

    VALUE = "Forced On"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.light.state.on.State
        self.base = home.appliance.light.state.off.State

        super(State, self).__init__(events, events_disabled)
