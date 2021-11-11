# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sensor.crepuscular import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.sensor.luxmeter.State(0.0)
    >>> state.compute()
    '0.0 lux'
    """
