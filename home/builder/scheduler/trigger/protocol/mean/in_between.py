# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.protocol import Builder as Parent
from home.scheduler.trigger.protocol.mean import InBetween


class Builder(Parent):
    TAG_NAME = "protocol.mean.InBetween"

    @property
    def trigger(self):
        return InBetween

    def _build_kwargs(self, mapping):
        d = super(Builder, self)._build_kwargs(mapping)
        num_of_samples = int(mapping["num of samples"])
        min_value = float(mapping["min value"])
        max_value = float(mapping["max value"])
        timeout_seconds = float(mapping["timeout seconds"])
        d["num_of_samples"] = num_of_samples
        d["min_value"] = min_value
        d["max_value"] = max_value
        d["timeout_seconds"] = timeout_seconds
        return d
