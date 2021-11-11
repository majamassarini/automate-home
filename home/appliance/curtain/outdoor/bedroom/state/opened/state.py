# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home

from home.appliance.attribute import mixin
from home.appliance.curtain.outdoor import state
from home.appliance.curtain.outdoor.bedroom.state import State as Parent
from home.appliance.curtain.outdoor.bedroom.state.opened import (
    callable as opened_callable,
)


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.wind.Event.Weak): opened_callable.Wind(closed=self.closed),
            type(home.event.sleepiness.Event.Awake): opened_callable.Sleepiness(
                closed=self.closed
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(state.opened.Mixin, Mixin, mixin.IsOpened, Parent):

    VALUE = "Opened"

    def __init__(self, events=None, events_disabled=None):
        self.closed = home.appliance.curtain.outdoor.bedroom.state.closed.State
        self.forced_opened = (
            home.appliance.curtain.outdoor.bedroom.state.forced.opened.State
        )
        self.forced_closed = (
            home.appliance.curtain.outdoor.bedroom.state.forced.closed.State
        )

        super(State, self).__init__(events, events_disabled)
