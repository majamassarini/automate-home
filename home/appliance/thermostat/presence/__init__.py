# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.thermostat.presence import event
from home.appliance.thermostat.presence import state


class Appliance(Parent):
    """
    >>> import home
    >>> p = home.appliance.thermostat.presence.Appliance("a thermostat", [])
    >>> old, new = p.notify(home.appliance.thermostat.presence.event.forced.Event.On)
    >>> old.compute()
    'Keeping'
    >>> new.compute()
    'Forced On'
    >>> old, new = p.notify(home.appliance.thermostat.presence.event.forced.Event.Off)
    >>> new.compute()
    'Forced Off'
    >>> old, new = p.notify(home.appliance.thermostat.presence.event.forced.Event.Not)
    >>> new.compute()
    'Keeping'
    """

    def _init_state(self):
        return state.keep.State()
