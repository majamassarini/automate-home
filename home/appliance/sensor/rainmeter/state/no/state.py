# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.sensor.rainmeter.state import State as Parent
from home.appliance.sensor.rainmeter.state.no import callable as no_callable


class State(Parent):

    VALUE = "Not raining"

    def init_callables(self):
        callables = {
            type(home.event.rain.Event.No): no_callable.Rain(
                gentle=home.appliance.sensor.rainmeter.state.gentle.State
            )
        }

        self._callables.update(callables)
