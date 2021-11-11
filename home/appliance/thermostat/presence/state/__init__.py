# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home import event as home_event
from home.appliance.state import State as Parent
from home.appliance.thermostat.presence import event as thermostat_event
from home.appliance.thermostat.presence.event.forced.event import Event as Forced


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.thermostat.presence.state.keep.State()
    >>> state.compute()
    'Keeping'
    >>> state = state.next(home.event.clima.command.Event.On)
    >>> state = state.next(home.event.presence.Event.On)
    >>> state.compute()
    'On'
    >>> state = state.next(home.event.presence.Event.Off)
    >>> state.compute()
    'Keeping'
    """

    SETPOINT_EVENT = thermostat_event.setpoint.Event

    DEFAULTS = [
        0.0,  # temperature
        thermostat_event.setpoint.Event(22.5),
        thermostat_event.keep.setpoint.Event(21.5),
        home_event.clima.season.Event.Winter,
        home_event.clima.command.Event.Keep,
        home_event.presence.Event.Off,
        Forced.Not,
    ]

    def update_by(self, event):
        super(State, self).update_by(event)
        if type(event) is self.SETPOINT_EVENT:
            self._setpoint = event
        elif type(event) is home_event.clima.season.Event:
            self._season = event
        elif type(event) is home_event.clima.command.Event:
            self._mode = event

    @property
    def setpoint(self):
        return self._setpoint

    @property
    def season(self):
        return self._season

    @property
    def mode(self):
        return self._mode

    @property
    def forced_enum(self):
        return Forced


from home.appliance.thermostat.presence.state import on
from home.appliance.thermostat.presence.state import off
from home.appliance.thermostat.presence.state import keep
from home.appliance.thermostat.presence.state import forced
