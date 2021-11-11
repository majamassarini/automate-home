# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable
from home.appliance.light.zone.state.alarmed.on import callable as on_callable


class Presence(on_callable.Presence):
    pass


class Courtesy(on_callable.Courtesy):
    pass


class Brightness(on_callable.Brightness):
    pass


class Toggle(Callable):
    def run(self, event, state):
        if event == home.event.toggle.Event.On:
            state = self.get_new_state(state, "alarmed_on")
        return state


class Armed(on_callable.Armed):
    pass


class Forced(on_callable.Forced):
    pass
