# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.event.hue import Event as Parent


class Event(Parent):
    """
    An event carrying on show ending hue data

    >>> Event(80)
    Show ending hue: 80°
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._str = "Show ending hue: {}°"
