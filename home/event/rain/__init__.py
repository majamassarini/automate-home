# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.event.enumeration import Enum


class Event(Enum):
    No = "No"
    Mist = "Mist"
    Gentle = "Gentle"
    Heavy = "Heavy"
    Storm = "Storm"


from home.event.rain import forecast, in_the_past
