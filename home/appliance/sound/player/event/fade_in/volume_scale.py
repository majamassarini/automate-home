# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sound.player.event.volume_scale import Event as Parent


class Event(Parent):
    """
    An event carrying on the percentage of the fade in volume actually played,
    used to step a fade in without losing its fade in volume

    >>> Event(20)
    Fade in Volume Scale: 20%
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._str = "Fade in Volume Scale: {}%"
