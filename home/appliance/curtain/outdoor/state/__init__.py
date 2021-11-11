# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.curtain.event.forced.event import Event as Forced
from home.appliance.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.curtain.outdoor.state.opened.State()
    >>> state.compute()
    'Opened'
    >>> state = state.next(home.appliance.curtain.event.forced.Event.Closed)
    >>> state.compute()
    'Forced Closed'
    >>> state = state.unforce()
    >>> state.compute()
    'Opened'
    >>> state = state.next(home.event.sun.twilight.civil.Event.Sunset)
    >>> state.compute()
    'Closed'
    >>> state = state.next(home.event.sun.twilight.civil.Event.Sunrise)
    >>> state.compute()
    'Opened'
    """

    DEFAULTS = [
        home.event.wind.Event.Weak,
        home.event.sun.brightness.Event.Dark,
        home.event.sun.twilight.civil.Event.Sunrise,
        home.event.sun.hit.Event.Sunleft,
        Forced.Not,
    ]

    @property
    def forced_enum(self):
        return Forced


from home.appliance.curtain.outdoor.state import closed
from home.appliance.curtain.outdoor.state import forced
from home.appliance.curtain.outdoor.state import opened
