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
    def run(self, obj):
        serialization = {"name": obj.name, "state": obj.state}
        key = obj.__class__.__module__ + "." + obj.__class__.__name__
        return {key: serialization}


class Deserializer(deserializer.Deserializer):
    def __init__(self):
        self._clss = list()
        self._clss.extend(home.appliance.registry_for_redis)

    def check(self, serialization):
        for cls in self._clss:
            if cls in serialization:
                return True

    def run(self, serialization):
        for cls in self._clss:
            if cls in serialization:
                packages = cls.split(".")
                if packages[0] == "home":
                    space = home
                    for name in packages[1:]:
                        try:
                            space = getattr(space, name)
                        except AttributeError:
                            raise ApplianceDecodingException(
                                "home.Appliance  package {} is unknown ({})".format(
                                    name, serialization
                                )
                            )
                    appliance = space.make(
                        serialization[cls]["name"], serialization[cls]["state"]
                    )
                    return appliance
