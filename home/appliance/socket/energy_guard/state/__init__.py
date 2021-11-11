# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.socket.event.forced.event import Event as Forced
from home.appliance.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.socket.energy_guard.state.on.State()
    >>> state = state.next(home.event.power.consumption.Event.High)
    >>> state = state.next(home.event.enable.Event.On)
    >>> state.compute()
    'Off'
    >>> state = state.next(Forced.On)
    >>> state.compute()
    'Forced On'
    >>> state = state.unforce()
    >>> state.compute()
    'Off'
    """

    DEFAULTS = [
        home.event.enable.Event.Off,
        home.event.power.consumption.Event.No,
        home.event.power.consumption.duration.Event.Short,
        Forced.Not,
    ]

    @property
    def forced_enum(self):
        return Forced


from home.appliance.socket.energy_guard.state import on
from home.appliance.socket.energy_guard.state import off
from home.appliance.socket.energy_guard.state import detachable
from home.appliance.socket.energy_guard.state import forced
