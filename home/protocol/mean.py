# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import abstractmethod


class Mixin:
    @abstractmethod
    def get_value(self, description: "home.protocol.Description") -> float:
        ...
