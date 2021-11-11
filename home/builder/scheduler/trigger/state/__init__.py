# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from typing import List, Any
from home.builder.scheduler.trigger import Builder as Parent


class Builder(Parent):
    TAG_NAME = "state.Trigger"

    def _build_args(self, mapping) -> List[Any]:
        name = mapping["name"]
        events = mapping["notify events"]
        state = mapping["when appliance is"]
        return [name, events, state]

    def _run(self, mapping, group_of_performers):
        args = self._build_args(mapping)
        return [self.trigger(*args)]


from home.builder.scheduler.trigger.state import entering, exiting
