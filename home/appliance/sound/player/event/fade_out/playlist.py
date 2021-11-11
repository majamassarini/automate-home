# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sound.player.event.playlist import Event as Parent


class Event(Parent):
    """
    An event carrying on playlist for fade out state

    >>> Event("a wonderful playlist")
    Fade out playlist: a wonderful playlist
    """

    def __init__(self, value: str):
        super(Event, self).__init__(value)
        self._str = "Fade out playlist: {}"
