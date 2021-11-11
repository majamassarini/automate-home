# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home

from home.appliance.attribute import mixin
from home.appliance.curtain.outdoor import state
from home.appliance.curtain.outdoor.bedroom.state.closed import (
    callable as closed_callable,
)
from home.appliance.curtain.outdoor.bedroom.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.sleepiness.Event.Awake): closed_callable.Sleepiness(
                opened=self.opened
            ),
            type(home.event.sun.brightness.Event.Dark): closed_callable.Brightness(
                opened=self.opened
            ),
            type(
                home.event.sun.twilight.civil.Event.Sunrise
            ): closed_callable.SunTwilight(opened=self.opened),
            type(home.event.sun.hit.Event.Sunleft): closed_callable.SunHit(
                opened=self.opened
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(state.closed.Mixin, Mixin, mixin.IsClosed, Parent):

    VALUE = "Closed"

    def __init__(self, events=None, events_disabled=None):
        self.opened = home.appliance.curtain.outdoor.bedroom.state.opened.State
        self.forced_opened = (
            home.appliance.curtain.outdoor.bedroom.state.forced.opened.State
        )
        self.forced_closed = (
            home.appliance.curtain.outdoor.bedroom.state.forced.closed.State
        )

        super(State, self).__init__(events, events_disabled)
