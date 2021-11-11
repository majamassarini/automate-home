# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.sensor.luxmeter.state import State


class Appliance(Parent):
    """
    A Lux sensor.

    Has just one state with an always changing lux value expressed in lux.

    >>> import home
    >>> l  = home.appliance.sensor.luxmeter.Appliance("lux sensor", [])
    >>> old, new = l.notify(6000.0)
    >>> old.compute()
    '0.0 lux'
    >>> new.compute()
    '6000.0 lux'
    """

    def _init_state(self):
        return State()
