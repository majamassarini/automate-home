# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.sensor.alarm.state import State as Parent
from home.appliance.sensor.alarm.state.triggered import callable as triggered_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.alarm.armed.Event.On): triggered_callable.Armed(
                unarmed=self.unarmed
            ),
            type(home.event.alarm.triggered.Event.Off): triggered_callable.Triggered(
                armed=self.armed, unarmed=self.unarmed
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOn, mixin.IsTriggered, Parent):

    VALUE = "Triggered"

    def __init__(self, events=None, events_disabled=None):
        self.armed = home.appliance.sensor.alarm.state.armed.State
        self.unarmed = home.appliance.sensor.alarm.state.unarmed.State

        super(State, self).__init__(events, events_disabled)
