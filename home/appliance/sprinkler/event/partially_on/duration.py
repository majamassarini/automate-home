# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sprinkler.event.duration import Event as Parent


class Event(Parent):
    """
    An event carrying on partially on sprinkling duration

    >>> Event(80)
    Partially on duration: 80 seconds
    """

    def __init__(self, value: int):
        super(Event, self).__init__(value)
        self._str = "Partially on duration: {} seconds"
