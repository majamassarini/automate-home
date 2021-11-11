# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.light.event.forced.event import Event as Forced
from home.appliance.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.light.state.off.State()
    >>> state = state.next(home.event.sun.phase.Event.Sunset)
    >>> state = state.next(home.event.sun.twilight.civil.Event.Sunset)
    >>> state = state.next(home.event.sun.brightness.Event.Dark)
    >>> state = state.next(home.event.courtesy.Event.On)
    >>> state.compute()
    'On'
    >>> state = state.next(Forced.Off)
    >>> state.compute()
    'Off'
    >>> state = state.unforce()
    >>> state.compute()
    'On'
    >>> state = state.force("Off")
    >>> state.compute()
    'Off'
    >>> state = state.make_from("On", "Sunset", "DeepDark", "Not")
    >>> state.compute()
    'On'
    >>> home.appliance.light.state.on.State().compute() == state.compute()
    True
    """

    DEFAULTS = [
        home.event.courtesy.Event.Off,
        home.event.sun.brightness.Event.Bright,
        Forced.Not,
    ]

    @property
    def forced_enum(self):
        return Forced


from home.appliance.light.state import forced
from home.appliance.light.state import off
from home.appliance.light.state import on
