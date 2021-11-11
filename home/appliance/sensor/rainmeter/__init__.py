# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.sensor.rainmeter import state


class Appliance(Parent):
    """
    >>> import home
    >>> a  = home.appliance.sensor.rainmeter.Appliance("a meter", [])
    >>> str(a)
    'Appliance a meter in Not raining (computed from events: home.event.rain.Event.No) and disabled events set()'
    """

    def _init_state(self):
        return state.no.State()
