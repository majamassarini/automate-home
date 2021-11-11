# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light.zone.state import State as Parent
from home.appliance.light.zone.state.alarmed.on import callable as alarmed_callable


class Mixin(object):
    def init_callables(self):

        callables = {
            type(home.event.presence.Event.On): alarmed_callable.Presence(
                off=self.off, on=self.on, alarmed_off=self.alarmed_off
            ),
            type(home.event.courtesy.Event.Off): alarmed_callable.Courtesy(
                off=self.off, on=self.on, alarmed_off=self.alarmed_off
            ),
            type(home.event.alarm.armed.Event.Off): alarmed_callable.Armed(
                off=self.off, on=self.on, alarmed_off=self.alarmed_off
            ),
            type(home.event.sun.brightness.Event.Bright): alarmed_callable.Brightness(
                off=self.off, on=self.on, alarmed_off=self.alarmed_off
            ),
            type(home.event.toggle.Event.On): alarmed_callable.Toggle(
                off=self.off, on=self.on, alarmed_off=self.alarmed_off
            ),
            self.forced_enum: alarmed_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsAlarmed, mixin.IsOn, Parent):

    VALUE = "Alarmed On"

    def __init__(self, events=None, events_disabled=None):
        self.on = home.appliance.light.zone.state.on.State
        self.off = home.appliance.light.zone.state.off.State
        self.alarmed_off = home.appliance.light.zone.state.alarmed.off.State
        self.forced_on = home.appliance.light.zone.state.forced.on.State
        self.forced_off = home.appliance.light.zone.state.forced.off.State
        self._is_on = True

        super(State, self).__init__(events, events_disabled)
