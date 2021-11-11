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
    >>> state = home.appliance.socket.presence.state.off.State()
    >>> state = state.next(Forced.On)
    >>> state.compute()
    'Forced On'
    >>> state = state.next(home.event.presence.Event.Off)
    >>> state.compute()
    'Off'
    >>> state = state.unforce()
    >>> state.compute()
    'Off'
    """

    DEFAULTS = [event.presence.Event.On, Forced.Not]

    @property
    def forced_enum(self):
        return Forced


from home.appliance.socket.presence.state import off
from home.appliance.socket.presence.state import forced
