# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.event.saturation import Event as Parent


class Event(Parent):
    """
    An event carrying on show starting saturation data

    >>> Event(80)
    Show starting saturation: 80%
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._str = "Show starting saturation: {}%"
