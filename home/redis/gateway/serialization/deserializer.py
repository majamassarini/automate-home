# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import abc


class Deserializer:
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def check(self, serialization):
        ...

    @abc.abstractmethod
    def run(self, serialization):
        ...
