# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.event import Float


class Event(Float):
    """
    An event carrying on setpoint data

    >>> Event(40.5)
    Setpoint: 40.5°
    """

    def __init__(self, value: float):
        super(Event, self).__init__(value)
        self._setpoint = value % 50
        self._str = "Setpoint: {}°"
