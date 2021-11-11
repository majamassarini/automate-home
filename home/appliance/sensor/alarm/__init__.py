# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.sensor.alarm import state


class Appliance(Parent):
    """
    >>> import home
    >>> a  = home.appliance.sensor.alarm.Appliance("an alarm", [])
    >>> str(a)
    'Appliance an alarm in Unarmed (computed from events: home.event.alarm.armed.Event.Off, home.event.alarm.triggered.Event.Off) and disabled events set()'
    """

    def _init_state(self):
        return state.unarmed.State()
