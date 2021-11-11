# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.sensor.scene.state import State as Parent
from home.appliance.sensor.scene.state.untriggered import (
    callable as untriggered_callable,
)


class State(Parent):

    VALUE = "Untriggered"

    def init_callables(self):
        callables = {
            type(home.event.scene.Event.Untriggered): untriggered_callable.Scene(
                triggered=home.appliance.sensor.scene.state.triggered.State
            )
        }

        self._callables.update(callables)
