# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home import event
from home.appliance.socket.event.forced.event import Event as Forced
from home.appliance.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.socket.presence.christmas.state.on.State()
    >>> state = state.next(home.event.holiday.christmas.Event.Time)
    >>> state = state.next(home.event.sun.brightness.Event.DeepDark)
    >>> state = state.next(home.event.presence.Event.Off)
    >>> state.compute()
    'On'
    >>> state = state.next(Forced.Off)
    >>> state.compute()
    'Forced Off'
    >>> state = state.unforce()
    >>> state.compute()
    'On'
    """

    DEFAULTS = [
        event.presence.Event.On,
        event.holiday.christmas.Event.Over,
        event.holiday.san_silvester.Event.Over,
        event.holiday.epiphany.Event.Over,
        event.sun.brightness.Event.Bright,
        Forced.Not,
    ]

    @property
    def forced_enum(self):
        return Forced


from home.appliance.socket.presence.christmas.state import on
from home.appliance.socket.presence.christmas.state import off
from home.appliance.socket.presence.christmas.state import forced
