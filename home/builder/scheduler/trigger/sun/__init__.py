# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger import Builder as Parent
from typing import List, Any


class Builder(Parent):
    TAG_NAME = "sun.follow.Trigger"

    def _build_args(self, mapping) -> List[Any]:
        name = mapping["name"]
        events = mapping["notify more events"]
        longitude = mapping["longitude"]
        latitude = mapping["latitude"]
        elevation = mapping["elevation"]
        return [name, events, latitude, longitude, elevation]

    def _run(self, mapping, group_of_performers):
        args = self._build_args(mapping)
        return [self.trigger(*args)]


from home.builder.scheduler.trigger.sun import sunhit
from home.builder.scheduler.trigger.sun import sunleft
from home.builder.scheduler.trigger.sun import sunrise
from home.builder.scheduler.trigger.sun import sunset
from home.builder.scheduler.trigger.sun import twilight
