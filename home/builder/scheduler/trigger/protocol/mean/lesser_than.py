# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.protocol.mean.greater_than import Builder as Parent
from home.scheduler.trigger.protocol.mean import LesserThan


class Builder(Parent):
    TAG_NAME = "protocol.mean.LesserThan"

    @property
    def trigger(self):
        return LesserThan
