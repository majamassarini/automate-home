# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.sensor.scene.state import State as Parent
from home.appliance.sensor.scene.state.triggered import callable as triggered_callable


class State(Parent):

    VALUE = "Triggered"

    def init_callables(self):
        callables = {
            type(home.event.scene.Event.Untriggered): triggered_callable.Scene(
                untriggered=home.appliance.sensor.scene.state.untriggered.State
            )
        }

        self._callables.update(callables)
