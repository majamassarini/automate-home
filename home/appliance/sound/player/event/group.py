# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.event import Str


class Event(Str):
    """
    An event carrying the name of the player to group with
    (the group coordinator); an empty name means no group

    >>> Event("Kitchen")
    Group: Kitchen
    >>> Event("").value
    ''
    """

    def __init__(self, value: str):
        super(Event, self).__init__(value)
        self._str = "Group: {}"
