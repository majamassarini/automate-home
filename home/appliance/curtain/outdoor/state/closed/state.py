# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.attribute import mixin
from home.appliance.curtain.outdoor.state.closed import callable as closed_callable
from home.appliance.curtain.outdoor.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.wind.Event.Weak): closed_callable.Wind(opened=self.opened),
            type(home.event.sun.brightness.Event.Dark): closed_callable.Brightness(
                opened=self.opened
            ),
            type(
                home.event.sun.twilight.civil.Event.Sunrise
            ): closed_callable.SunTwilight(opened=self.opened),
            type(home.event.sun.hit.Event.Sunleft): closed_callable.SunHit(
                opened=self.opened
            ),
            self.forced_enum: closed_callable.Forced(
                forced_closed=self.forced_closed, forced_opened=self.forced_opened
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(Mixin, mixin.IsClosed, Parent):

    VALUE = "Closed"

    def __init__(self, events=None, events_disabled=None):
        self.opened = home.appliance.curtain.outdoor.state.opened.State
        self.forced_opened = home.appliance.curtain.outdoor.state.forced.opened.State
        self.forced_closed = home.appliance.curtain.outdoor.state.forced.closed.State

        super(State, self).__init__(events, events_disabled)
