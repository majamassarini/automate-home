# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sensor.callable import Callable
from home.appliance.state import State as Parent


class State(Parent):
    def force(self, state_str):
        return self

    def unforce(self):
        return self

    def init_callables(self):
        callables = {self.DEFAULTS[0]: Callable()}
        self._callables.update(callables)

    @property
    def forced_str(self):
        return None

    @property
    def forced_enum(self):
        return []

    @property
    def value(self):
        return self._events[type(self.DEFAULTS[0])]
