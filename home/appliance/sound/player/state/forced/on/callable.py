# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable, Forced as Parent


class Sleepiness(Callable):
    def run(self, event, state):
        if home.event.presence.Event.On in state:
            if event == home.event.sleepiness.Event.Asleep:
                state = self.compute_new_state(
                    state, "fade_out", [state.forced_enum.On]
                )
        return state


class Presence(Parent):
    def run(self, event, state):
        if event == home.event.presence.Event.On:
            return state
        else:
            return super(Presence, self).run(event, state)


class Forced(Callable):
    """
    Do not automatically switch between a forced circadian rhythm state and a forced on state.
    *If the protocol used does not distinguish between a confirmation and an indication
    there is no way to understand if the status given back by the device is related with
    the system changing the device or a user changing it*.
    If, as an example, the status message is associated to a forced on message,
    when the system puts the Appliance in a circadian state it will receive back a status message
    and thus the Appliance will be switched by the system to a forced on state!

    To switch between forced state, not distinguishable from a device perspective,
    force the Appliance to go through a non forced state!

    When receiving a status message send a forced on event, which will have effect only if the device is turned off
    When receiving a message from push button 1 send a not forced event and a forced on event, which will have always the effect to put the device in a forced on state
    When receiving a message from push button 2 send a not forced event and a forced circadian rhythm event, which will have always the effect to put the device in a forced circadian rhythm state
    """

    def run(self, event, state):
        if event in (state.forced_enum.Not, state.forced_enum.Off):
            state = self.compute_new_state(state, "base", [event])
        return state
