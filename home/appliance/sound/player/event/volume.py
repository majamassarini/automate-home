# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.event import Int


class Event(Int):
    """
    An event carrying on sound player volume

    >>> Event(80)
    Volume: 80%
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._value = value % 101
        self._str = "Volume: {}%"
