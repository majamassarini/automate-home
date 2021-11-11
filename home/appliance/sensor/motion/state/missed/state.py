# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.sensor.motion.state import State as Parent
from home.appliance.sensor.motion.state.missed import callable as missed_callable


class State(Parent):

    VALUE = "Missed"

    def init_callables(self):
        callables = {
            type(home.event.motion.Event.Missed): missed_callable.Motion(
                spotted=home.appliance.sensor.motion.state.spotted.State
            )
        }

        self._callables.update(callables)
