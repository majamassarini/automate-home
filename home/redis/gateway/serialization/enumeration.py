# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
import logging
from home.redis.gateway.serialization import deserializer
from home.redis.gateway.serialization import serializer


class EnumDecodingException(Exception):
    pass


class Serializer(serializer.Serializer):

    KEY = "home.event.Enum"

    def run(self, obj):
        return {Serializer.KEY: str(obj)}


class Deserializer(deserializer.Deserializer):
    def check(self, serialization):
        if Serializer.KEY in serialization:
            return True

    def run(self, serialization):
        logger = logging.getLogger(__name__)
        packages = serialization[Serializer.KEY].split(".")
        if packages[0] == "home":
            space = home
            for name in packages[1:]:
                try:
                    space = getattr(space, name)
                except AttributeError:
                    logger.error(
                        "home.Enum event package {} is unknown ({})".format(
                            name, serialization
                        )
                    )
            return space
        else:
            raise logger.error(
                "home.Enum event package {} is unknown ({})".format(
                    packages[0], serialization
                )
            )
