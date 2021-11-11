# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.curtain.event.forced import Event as Forced
from home.appliance.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.curtain.indoor.blackout.state.opened.State()
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
    >>> state = state.next(home.event.sleepiness.Event.Asleep)
    >>> state.compute()
    'Closed'
    >>> state = state.next(home.event.sun.twilight.civil.Event.Sunrise)
    >>> state.compute()
    'Closed'
    >>> state = state.next(home.event.sleepiness.Event.Awake)
    >>> state.compute()
    'Opened'
    """

    DEFAULTS = [
        home.event.sun.twilight.civil.Event.Sunrise,
        home.event.sleepiness.Event.Awake,
        Forced.Not,
    ]

    @property
    def forced_enum(self):
        return Forced


from home.appliance.curtain.indoor.blackout.state import opened
from home.appliance.curtain.indoor.blackout.state import closed
from home.appliance.curtain.indoor.blackout.state import forced
