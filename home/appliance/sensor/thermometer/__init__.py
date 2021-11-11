# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sensor.thermometer.state import State
from home.appliance import Appliance as Parent


class Appliance(Parent):
    """
    >>> import home
    >>> a  = home.appliance.sensor.thermometer.Appliance("a meter", [])
    >>> str(a)
    'Appliance a meter in 0.0 centigrade (computed from events: 0.0) and disabled events set()'
    """

    def _init_state(self):
        return State()
