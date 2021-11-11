# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.event.hue import Event as Parent


class Event(Parent):
    """
    An event carrying on circadian hue data

    >>> Event(80)
    Circadian hue: 80°
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._str = "Circadian hue: {}°"
