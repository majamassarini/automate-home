# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.event import Int


class Event(Int):
    """
    An event carrying on sprinkling duration

    >>> Event(80)
    "Duration: 80 seconds"
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._str = "Duration: {} seconds"
