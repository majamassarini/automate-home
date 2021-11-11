# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from typing import Type
import abc

from home.redis.gateway.serialization import deserializer
from home.redis.gateway.serialization import serializer


class Serializer(serializer.Serializer):
    @property
    @abc.abstractmethod
    def key(self) -> str:
        ...

    def run(self, obj):
        serialization = obj.value
        return {self.key: serialization}


class Deserializer(deserializer.Deserializer):
    @property
    @abc.abstractmethod
    def key(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def klass(self) -> Type:
        ...

    def check(self, serialization):
        if self.key in serialization:
            return True
