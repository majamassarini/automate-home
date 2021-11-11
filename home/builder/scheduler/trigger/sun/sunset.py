# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.sun import Builder as Parent
from home.scheduler.trigger.sun.sunset import Trigger


class Builder(Parent):
    TAG_NAME = "sun.sunset.Trigger"

    @property
    def trigger(self):
        return Trigger
