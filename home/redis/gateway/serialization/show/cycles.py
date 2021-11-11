# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.event.show.cycles import Event
from home.redis.gateway.serialization.event.int import Deserializer as DParent
from home.redis.gateway.serialization.event import Serializer as SParent

KEY = "home.appliance.light.event.show.cycles.Event"


class Serializer(SParent):
    @property
    def key(self):
        return KEY


class Deserializer(DParent):
    @property
    def key(self):
        return KEY

    @property
    def klass(self):
        return Event
