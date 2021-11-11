# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.data import Registry


class Int(metaclass=Registry):
    def __init__(self, value: int):
        self._value = value
        self._str = "An abstract int event: {}"

    def __eq__(self, other):
        if self.__class__ == other.__class__ and self.value == other.value:
            return True
        else:
            return False

    def __repr__(self):
        return self._str.format(self.value)

    def __str__(self):
        return self._str.format(self.value)

    def __hash__(self):
        return hash(str(self))

    @property
    def value(self):
        return self._value


class Float(Int):
    def __init__(self, value: float):
        self._value = value
        self._str = "An abstract float event: {}"


class Str(Int):
    def __init__(self, value: str):
        self._value = value
        self._str = "An abstract str event: {}"
