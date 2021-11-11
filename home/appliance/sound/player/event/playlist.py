# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.event import Str


class Event(Str):
    """
    An event carrying a playlist

    >>> Event("a wonderful playlist")
    Playlist: a wonderful playlist
    """

    def __init__(self, value: str):
        super(Event, self).__init__(value)
        self._str = "Playlist: {}"
