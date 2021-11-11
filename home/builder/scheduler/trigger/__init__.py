# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import ABCMeta, abstractmethod
from typing import Type, List
from home.scheduler import Trigger


registry = dict()


def register_class(tag, a_tuple):
    registry[tag] = a_tuple


class Registry(ABCMeta):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        if name not in registry:
            register_class(cls.TAG_NAME, (cls.__module__ + "." + cls.__name__, cls))
        return cls


class Builder(metaclass=Registry):

    TAG_NAME = "No tag name given"

    @property
    @abstractmethod
    def trigger(self) -> Type:
        ...

    def _run(self, mapping, group_of_performers) -> List[Type[Trigger]]:
        return [self.trigger(**mapping)]

    def run(self, loader, node, group_of_performers) -> List[Type[Trigger]]:
        mapping = loader.construct_mapping(node, deep=True)
        return self._run(mapping, group_of_performers)


from home.builder.scheduler.trigger import cron
from home.builder.scheduler.trigger import date
from home.builder.scheduler.trigger import interval
from home.builder.scheduler.trigger import protocol
from home.builder.scheduler.trigger import state
from home.builder.scheduler.trigger import sun
from home.builder.scheduler.trigger import circadian_rhythm
from home.builder.scheduler.trigger import crawler
