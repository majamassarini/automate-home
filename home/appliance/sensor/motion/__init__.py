# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.sensor.motion import state


class Appliance(Parent):
    """
    >>> import home
    >>> a  = home.appliance.sensor.motion.Appliance("a motion sensor", [])
    >>> str(a)
    'Appliance a motion sensor in Missed (computed from events: home.event.motion.Event.Missed) and disabled events set()'
    """

    def _init_state(self):
        return state.missed.State()
