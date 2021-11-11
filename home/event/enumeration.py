# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import enum
import functools

registry = dict()


def register_class(target_class):
    klass = "{}.{}".format(
        target_class.__module__.replace(".definition", "").replace(
            "forced.event", "forced"
        ),
        target_class.__name__,
    )
    for value in dir(target_class):
        if "__" not in value:
            registry["{}.{}".format(klass, value)] = target_class


class Registry(enum.EnumMeta):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        if name not in registry:
            register_class(cls)
        return cls


class Enum(enum.Enum, metaclass=Registry):
    def __str__(self):
        ss = super(Enum, self).__str__().split(".")
        return functools.reduce(lambda s, i: s + "." + i, ss, str(self.__module__))
