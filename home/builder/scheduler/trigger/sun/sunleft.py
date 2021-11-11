# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.sun import Builder as Parent
from home.scheduler.trigger.sun.sunleft import Trigger


class Builder(Parent):
    TAG_NAME = "sun.sunleft.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        args = super(Builder, self)._build_args(mapping)
        position = mapping["position"]
        args.append(position)
        return args
