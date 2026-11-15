# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sound.player.event.volume_scale import Event
from home.redis.gateway.serialization.volume import Deserializer as DParent
from home.redis.gateway.serialization.volume import Serializer as SParent

KEY = "home.appliance.sound.player.event.volume_scale.Event"


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
