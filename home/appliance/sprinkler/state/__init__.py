# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home import event as home_event
from home.appliance import attribute
from home.appliance.sprinkler import event
from home.appliance.state import State as Parent
from home.appliance.callable import DoNothing


class Duration(DoNothing):
    pass


class PartiallyOnDuration(DoNothing):
    pass


class Enable(DoNothing):
    pass


class SunPhase(DoNothing):
    pass


class HasRained(DoNothing):
    pass


class IsRaining(DoNothing):
    pass


class WillRain(DoNothing):
    pass


class Mixin(object):
    def init_callables(self):
        callables = {
            type(event.duration.Event(1200)): Duration(),
            type(event.partially_on.duration.Event(350)): PartiallyOnDuration(),
            type(home_event.rain.in_the_past.Event.Off): HasRained(),
            type(home_event.rain.Event.No): IsRaining(),
            type(home_event.rain.forecast.Event.Off): WillRain(),
            type(home_event.enable.Event.Off): Enable(),
            type(home_event.sun.phase.Event.Sunrise): SunPhase(),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Parent, Mixin, attribute.mixin.Duration):
    """
    >>> import home
    >>> state = home.appliance.sprinkler.state.off.State()
    >>> state = state.force("On")
    >>> state.compute()
    'Forced On'
    >>> state = state.force("Off")
    >>> state.compute()
    'Off'
    """

    DEFAULTS = [
        event.duration.Event(1200),
        event.partially_on.duration.Event(350),
        home_event.rain.in_the_past.Event.Off,
        home_event.rain.Event.No,
        home_event.rain.forecast.Event.Off,
        home_event.enable.Event.Off,
        home_event.sun.phase.Event.Sunrise,
        event.forced.Event.Not,
    ]

    @property
    def forced_enum(self):
        return event.forced.Event


from home.appliance.sprinkler.state import off, on, partially_on, forced
