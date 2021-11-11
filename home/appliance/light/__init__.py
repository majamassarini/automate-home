# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.light.state import off


class Appliance(Parent):
    """
    >>> import home
    >>> p = home.appliance.light.Appliance("a light", [])
    >>> _, new = p.notify(home.event.sun.brightness.Event.DeepDark)
    >>> old, new = p.notify(home.appliance.light.event.forced.Event.On)
    >>> old.compute()
    'Off'
    >>> new.compute()
    'Forced On'
    >>> _, new = p.notify(home.event.courtesy.Event.On)
    >>> new.compute()
    'Forced On'
    >>> _, new = p.notify(home.event.courtesy.Event.Off)
    >>> new.compute()
    'Forced On'
    >>> old, new = p.notify(home.appliance.light.event.forced.Event.Not)
    >>> new.compute()
    'Off'
    """

    def _init_state(self):
        return off.State()


from home.appliance.light import indoor
from home.appliance.light import event
from home.appliance.light import zone
from home.appliance.light import presence
from home.appliance.light import state
