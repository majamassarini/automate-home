# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sound.player.event.volume import Event as Parent


class Event(Parent):
    """
    An event carrying on fade out volume

    >>> Event(80)
    Fade out volume: 80%
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._value = value % 101
        self._str = "Fade out volume: {}%"
