# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.redis.gateway.serialization import deserializer
from home.redis.gateway.serialization import serializer


class StateDecodingException(Exception):
    pass


class Serializer(serializer.Serializer):
    def run(self, obj):
        serialization = {
            "events": obj.events,
            "events_disabled": list(obj.events_disabled),
        }
        key = obj.__class__.__module__ + "." + obj.__class__.__name__
        return {key: serialization}


class Deserializer(deserializer.Deserializer):
    def __init__(self):
        self._clss = list()
        self._clss.extend(home.appliance.state.registry_for_redis)

    def check(self, serialization):
        for cls in self._clss:
            for key in serialization.keys():
                if cls in key:
                    return True

    def run(self, serialization):
        for cls in self._clss:
            for key in serialization.keys():
                if cls in key:
                    packages = key.split(".")
                    if packages[0] == "home":
                        space = home
                        for name in packages[1:]:
                            try:
                                space = getattr(space, name)
                            except AttributeError:
                                raise StateDecodingException(
                                    "home.Appliance  package {} is unknown ({})".format(
                                        name, serialization
                                    )
                                )
                        state = space(
                            serialization[cls]["events"],
                            serialization[cls]["events_disabled"],
                        )
                        return state
