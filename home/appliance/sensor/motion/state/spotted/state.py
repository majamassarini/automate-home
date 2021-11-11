# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.sensor.motion.state import State as Parent
from home.appliance.sensor.motion.state.spotted import callable as spotted_callable


class State(Parent):

    VALUE = "Spotted"

    def init_callables(self):
        callables = {
            type(home.event.motion.Event.Missed): spotted_callable.Motion(
                missed=home.appliance.sensor.motion.state.missed.State
            )
        }

        self._callables.update(callables)
