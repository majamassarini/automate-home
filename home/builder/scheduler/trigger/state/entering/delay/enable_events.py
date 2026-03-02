# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.state.entering.delay import (
    Builder as Parent,
)
from home.scheduler.trigger.state.entering.delay.enable_events import Trigger


class Builder(Parent):
    TAG_NAME = "state.entering.delay.enable_events.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        name = mapping["name"]
        events = mapping["enable events"]
        state = mapping["when appliance state became"]
        timeout = mapping["and timeout expires"]
        return [name, events, state, timeout]
