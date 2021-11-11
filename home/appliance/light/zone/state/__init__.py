# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home import event
from home.appliance.light.event.forced.event import Event as Forced
from home.appliance.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.light.zone.state.off.State()
    >>> state = state.next(home.event.sun.brightness.Event.DeepDark)
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
        event.presence.Event.Off,
        event.courtesy.Event.Off,
        event.alarm.armed.Event.Off,
        event.sun.brightness.Event.Bright,
        event.toggle.Event.On,
        Forced.Not,
    ]

    @property
    def forced_enum(self):
        return Forced


from home.appliance.light.zone.state import forced
from home.appliance.light.zone.state import off
from home.appliance.light.zone.state import on
from home.appliance.light.zone.state import alarmed
