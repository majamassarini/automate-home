# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sound.player.event.playlist import Event as Parent


class Event(Parent):
    """
    An event carrying playlist for user A

    >>> Event("a wonderful playlist")
    Playlist for user A: a wonderful playlist
    """

    def __init__(self, value: str):
        super(Event, self).__init__(value)
        self._str = "Playlist for user A: {}"
