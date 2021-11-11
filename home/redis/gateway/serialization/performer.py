# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.redis.gateway.serialization import deserializer
from home.redis.gateway.serialization import serializer


class ApplianceDecodingException(Exception):
    pass


class Serializer(serializer.Serializer):

    KEY = "home.Performer"

    def run(self, obj):
        serialization = {"name": obj.name, "appliance": obj.appliance}
        return {Serializer.KEY: serialization}


class Deserializer(deserializer.Deserializer):
    def check(self, serialization):
        if Serializer.KEY in serialization:
            return True

    def run(self, serialization):
        return home.Performer(
            serialization[Serializer.KEY]["name"],
            serialization[Serializer.KEY]["appliance"],
            [],
            [],
        )
