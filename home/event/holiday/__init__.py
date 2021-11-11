# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.event.enumeration import Enum


class Event(Enum):
    Vacation = "Vacation"
    Over = "Over"


from home.event.holiday import christmas
from home.event.holiday import easter
from home.event.holiday import epiphany
from home.event.holiday import san_silvester
