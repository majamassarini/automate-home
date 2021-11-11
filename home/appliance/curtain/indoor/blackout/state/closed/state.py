# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home

from home.appliance.attribute import mixin
from home.appliance.curtain.indoor.blackout.state.closed import (
    callable as closed_callable,
)
from home.appliance.curtain.indoor.blackout.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(
                home.event.sun.twilight.civil.Event.Sunrise
            ): closed_callable.SunTwilight(opened=self.opened),
            type(home.event.sleepiness.Event.Awake): closed_callable.Sleepiness(
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
        self.opened = home.appliance.curtain.indoor.blackout.state.opened.State
        self.forced_opened = (
            home.appliance.curtain.indoor.blackout.state.forced.opened.State
        )
        self.forced_closed = (
            home.appliance.curtain.indoor.blackout.state.forced.closed.State
        )

        super(State, self).__init__(events, events_disabled)
