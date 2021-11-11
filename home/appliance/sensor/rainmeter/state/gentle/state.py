# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.sensor.rainmeter.state import State as Parent
from home.appliance.sensor.rainmeter.state.gentle import callable as gentle_callable


class State(Parent):

    VALUE = "Gentle raining"

    def init_callables(self):
        callables = {
            type(home.event.rain.Event.No): gentle_callable.Rain(
                no=home.appliance.sensor.rainmeter.state.no.State
            )
        }

        self._callables.update(callables)
