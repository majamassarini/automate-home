# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.event.enumeration import Enum


class Event(Enum):
    Sunset = "Sunset"
    Sunrise = "Sunrise"
