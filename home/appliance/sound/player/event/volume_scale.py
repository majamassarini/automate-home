# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.event import Int


class Event(Int):
    """
    An event carrying on the percentage of the sleepy volume actually played,
    used to fade a sleepy forced on sound player without losing its sleepy volume

    >>> Event(75)
    Sleepy Volume Scale: 75%
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._value = value % 101
        self._str = "Sleepy Volume Scale: {}%"
