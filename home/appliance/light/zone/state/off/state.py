# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.light.zone.state import State as Parent
from home.appliance.light.zone.state.off import callable as off_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): off_callable.Presence(
                on=self.on, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.courtesy.Event.Off): off_callable.Courtesy(
                on=self.on, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.alarm.armed.Event.Off): off_callable.Armed(
                on=self.on, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.sun.brightness.Event.Bright): off_callable.Brightness(
                on=self.on, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            type(home.event.toggle.Event.On): off_callable.Toggle(
                on=self.on, alarmed_on=self.alarmed_on, alarmed_off=self.alarmed_off
            ),
            self.forced_enum: off_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOff, mixin.IsNotAlarmed, Parent):

    VALUE = "Off"

    def __init__(self, events=None, events_disabled=None):

        self.on = home.appliance.light.zone.state.on.State
        self.alarmed_on = home.appliance.light.zone.state.alarmed.on.State
        self.alarmed_off = home.appliance.light.zone.state.alarmed.off.State
        self.forced_on = home.appliance.light.zone.state.forced.on.State
        self.forced_off = home.appliance.light.zone.state.forced.off.State

        super(State, self).__init__(events, events_disabled)
