# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.sound.player import event
from home.appliance.sound.player.state import State as Parent
from home.appliance.sound.player.state.off import callable as _callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.sleepiness.Event.Awake): _callable.Sleepiness(
                fade_in=self.fade_in
            ),
            self.forced_enum: _callable.Forced(
                forced_on=self.forced_on,
                forced_circadian_rhythm=self.forced_circadian_rhythm,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    Mixin,
    attribute.mixin.IsOff,
    attribute.mixin.IsNotFading,
    attribute.mixin.IsNotCircadianRhythm,
    Parent,
):

    VALUE = "Off"

    VOLUME_EVENT = event.volume.Event
    PLAYLIST_EVENT = event.playlist.Event

    def __init__(self, events=None, events_disabled=None):
        self.forced_on = home.appliance.sound.player.state.forced.on.State
        self.forced_circadian_rhythm = (
            home.appliance.sound.player.state.forced.circadian_rhythm.State
        )
        self.fade_in = home.appliance.sound.player.state.fade_in.State

        super(State, self).__init__(events, events_disabled)
