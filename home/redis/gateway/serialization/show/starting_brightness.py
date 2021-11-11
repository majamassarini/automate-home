# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.event.show.starting_brightness import Event
from home.redis.gateway.serialization.brightness import Deserializer as DParent
from home.redis.gateway.serialization.brightness import Serializer as SParent

KEY = "home.appliance.light.event.show.starting_brightness.Event"


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
