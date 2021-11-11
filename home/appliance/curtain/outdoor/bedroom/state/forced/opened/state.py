# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home

from home.appliance.attribute import mixin
from home.appliance.curtain.outdoor.state import forced
from home.appliance.curtain.outdoor.bedroom.state.forced.opened import (
    callable as forced_opened_callable,
)
from home.appliance.curtain.outdoor.bedroom.state import State as Parent


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.sleepiness.Event.Awake): forced_opened_callable.Sleepiness(
                base=self.base, reset=self.reset
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(forced.opened.Mixin, Mixin, mixin.IsOpened, Parent):

    VALUE = "Forced Opened"

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.curtain.outdoor.bedroom.state.opened.State
        self.base = home.appliance.curtain.outdoor.bedroom.state.opened.State

        super(State, self).__init__(events, events_disabled)
