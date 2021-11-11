# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.crawler.osmer_fvg.will_rain import Builder as Parent
from home.scheduler.trigger.crawler.osmer_fvg.will_rain.on import Trigger


class Builder(Parent):
    TAG_NAME = "crawler.osmer_fvg.will_rain.on.Trigger"

    @property
    def trigger(self):
        return Trigger
