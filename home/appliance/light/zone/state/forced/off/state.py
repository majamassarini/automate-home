# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light.zone.state.forced.off import callable as forced_off_callable
from home.appliance.light.zone.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): forced_off_callable.Presence(
                reset=self.reset, base=self.base
            ),
            type(home.event.courtesy.Event.Off): forced_off_callable.Courtesy(
                reset=self.reset, base=self.base
            ),
            type(
                home.event.sun.brightness.Event.Bright
            ): forced_off_callable.Brightness(reset=self.reset, base=self.base),
            type(home.event.alarm.armed.Event.Off): forced_off_callable.Armed(
                reset=self.reset, base=self.base
            ),
            type(home.event.toggle.Event.On): forced_off_callable.Toggle(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: forced_off_callable.Forced(
                reset=self.reset, base=self.base
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(mixin.IsOff, mixin.IsNotAlarmed, Mixin, Parent):

    VALUE = "Forced Off"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.light.zone.state.off.State
        self.base = home.appliance.light.zone.state.off.State

        super(State, self).__init__(events, events_disabled)
