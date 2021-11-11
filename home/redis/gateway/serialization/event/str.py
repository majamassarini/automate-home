# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.redis.gateway.serialization.event import Deserializer as Parent


class Deserializer(Parent):
    def run(self, serialization):
        return self.klass(str(serialization[self.key]))
