# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.protocol import Builder as Parent
from home.scheduler.trigger.protocol.mean import GreaterThan


class Builder(Parent):
    TAG_NAME = "protocol.mean.GreaterThan"

    @property
    def trigger(self):
        return GreaterThan

    def _build_kwargs(self, mapping):
        d = super(Builder, self)._build_kwargs(mapping)
        num_of_samples = int(mapping["num of samples"])
        hit_value = float(mapping["hit value"])
        timeout_seconds = float(mapping["timeout seconds"])
        d["num_of_samples"] = num_of_samples
        d["hit_value"] = hit_value
        d["timeout_seconds"] = timeout_seconds
        return d
