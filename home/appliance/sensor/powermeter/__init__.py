# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.sensor.powermeter.state import State


class Appliance(Parent):
    """
    >>> import home
    >>> a  = home.appliance.sensor.powermeter.Appliance("a meter", [])
    >>> str(a)
    'Appliance a meter in 0.0 W (computed from events: 0.0) and disabled events set()'
    """

    def _init_state(self):
        return State()
