# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home


class Event(home.event.Enum):
    Off = "Off"
    On = "On"
    Keep = "Keep"
    Not = "Not"
