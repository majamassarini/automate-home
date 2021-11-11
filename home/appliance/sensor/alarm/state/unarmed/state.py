# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.sensor.alarm.state import State as Parent
from home.appliance.sensor.alarm.state.unarmed import callable as alarm_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.alarm.armed.Event.Off): alarm_callable.Armed(
                armed=self.armed, triggered=self.triggered
            ),
            type(home.event.alarm.triggered.Event.Off): alarm_callable.Triggered(
                triggered=self.triggered
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOff, mixin.IsNotTriggered, Parent):

    VALUE = "Unarmed"

    def __init__(self, events=None, events_disabled=None):
        self.armed = home.appliance.sensor.alarm.state.armed.State
        self.triggered = home.appliance.sensor.alarm.state.triggered.State

        super(State, self).__init__(events, events_disabled)
