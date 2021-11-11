# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Scene(Callable):
    def run(self, event, state):
        if home.event.scene.Event.Untriggered == event:
            state = self.get_new_state(state, "untriggered")
        return state
