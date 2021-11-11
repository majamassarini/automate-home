# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sensor.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.sensor.powermeter.State(0.0)
    >>> state.compute()
    '0.0 W'
    """

    DEFAULTS = [
        0.0,
    ]

    def _get_str_value(self):
        return "{} W".format(self.value)
