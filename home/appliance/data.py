# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

registry = list()


def register_class(target_class):
    klass = "{}.{}".format(
        target_class.__module__.replace(".definition", "").replace(
            "home.appliance.", ""
        ),
        target_class.__name__,
    )
    registry.append(klass)


class Registry(type):
    def __new__(mcs, name, bases, class_dict):
        cls = super().__new__(mcs, name, bases, class_dict)
        if name not in registry:
            register_class(cls)
        return cls
