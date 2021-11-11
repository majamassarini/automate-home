# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.socket.presence.christmas.state import State as Parent
from home.appliance.socket.presence.christmas.state.on import callable as on_callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.presence.Event.On): on_callable.Presence(off=self.off),
            type(home.event.holiday.christmas.Event.Over): on_callable.Christmas(
                off=self.off
            ),
            type(home.event.holiday.san_silvester.Event.Over): on_callable.SanSilvester(
                off=self.off
            ),
            type(home.event.holiday.epiphany.Event.Over): on_callable.Epiphany(
                off=self.off
            ),
            type(home.event.sun.brightness.Event.Bright): on_callable.SunBrightness(
                off=self.off
            ),
            self.forced_enum: on_callable.Forced(
                forced_off=self.forced_off, forced_on=self.forced_on
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsOn, Parent):
    def __init__(self, events=None, events_disabled=None):
        self.off = home.appliance.socket.presence.christmas.state.off.State
        self.forced_on = home.appliance.socket.presence.christmas.state.forced.on.State
        self.forced_off = (
            home.appliance.socket.presence.christmas.state.forced.off.State
        )

        super(State, self).__init__(events, events_disabled)
