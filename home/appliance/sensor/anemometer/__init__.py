# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sensor.anemometer.state import State
from home.appliance import Appliance as Parent


class Appliance(Parent):
    """
    A Wind sensor.

    Has just one state with an always changing wind value expressed in wsp.

    >>> import home
    >>> a  = home.appliance.sensor.anemometer.Appliance("wind sensor", [])
    >>> old, new = a.notify(4.5)
    >>> old.compute()
    '0.0 wsp'
    >>> new.compute()
    '4.5 wsp'
    """

    def _init_state(self):
        return State()
