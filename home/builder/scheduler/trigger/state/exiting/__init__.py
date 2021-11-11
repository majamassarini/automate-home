# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.state import Builder as Parent
from home.scheduler.trigger.state.exiting import Trigger


class Builder(Parent):
    TAG_NAME = "state.exiting.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        name = mapping["name"]
        events = mapping["notify events"]
        state = mapping["when appliance state is no more"]
        return [name, events, state]


from home.builder.scheduler.trigger.state.exiting import delay
