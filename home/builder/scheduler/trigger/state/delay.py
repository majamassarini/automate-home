# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.state import Builder as Parent
from home.scheduler.trigger.state.delay import Trigger


class Builder(Parent):
    TAG_NAME = "state.delay.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        args = super(Builder, self)._build_args(mapping)
        args.append(mapping["and timeout expires"])
        return args
