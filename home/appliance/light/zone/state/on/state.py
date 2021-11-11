# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light.zone.state import State as Parent
from home.appliance.light.zone.state.on import callable as on_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): on_callable.Presence(
                off=self.off, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.courtesy.Event.Off): on_callable.Courtesy(
                off=self.off, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.alarm.armed.Event.Off): on_callable.Armed(
                off=self.off, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.sun.brightness.Event.Bright): on_callable.Brightness(
                off=self.off, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.toggle.Event.On): on_callable.Toggle(
                off=self.off, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            self.forced_enum: on_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOn, mixin.IsNotAlarmed, Parent):

    VALUE = "On"

    def __init__(self, events=None, events_disabled=None):
        self.off = home.appliance.light.zone.state.off.State
        self.alarmed_on = home.appliance.light.zone.state.alarmed.on.State
        self.alarmed_off = home.appliance.light.zone.state.alarmed.off.State
        self.forced_on = home.appliance.light.zone.state.forced.on.State
        self.forced_off = home.appliance.light.zone.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
