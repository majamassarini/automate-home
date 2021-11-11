# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.event.temperature import Event as Parent


class Event(Parent):
    """
    An event carrying on circadian saturation data

    >>> Event(80)
    Circadian temperature: 80° kelvin
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._str = "Circadian temperature: {}° kelvin"
