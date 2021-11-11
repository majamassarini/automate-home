# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home


class Event(home.event.Enum):
    On = "On"
    Off = "Off"
    CircadianRhythm = "CircadianRhythm"
    LuxBalance = "LuxBalance"
    Show = "Show"
    Not = "Not"
