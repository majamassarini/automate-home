# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.date import Builder as Parent
from home.scheduler.trigger.date.resettable import Trigger


class Builder(Parent):
    TAG_NAME = "date.resettable.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _get_kwargs(self, mapping):
        kwargs = super(Builder, self)._get_kwargs(mapping)
        kwargs["resettable events"] = mapping["resettable events"]
        return kwargs
