# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.sound.player import event
from home.appliance.sound.player.state import State as Parent
from home.appliance.sound.player.state.fade_out import callable as _callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.elapsed.Event.Off): _callable.Elapsed(off=self.off),
            type(home.event.presence.Event.Off): _callable.Presence(off=self.off),
            self.forced_enum: _callable.Forced(
                forced_off=self.forced_off,
                forced_on=self.forced_on,
                forced_circadian_rhythm=self.forced_circadian_rhythm,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    Mixin,
    attribute.mixin.IsOn,
    attribute.mixin.IsFading,
    attribute.mixin.IsNotCircadianRhythm,
    Parent,
):

    VALUE = "Fade Out"

    VOLUME_EVENT = event.fade_out.volume.Event
    PLAYLIST_EVENT = event.fade_out.playlist.Event

    def __init__(self, events=None, events_disabled=None):
        self.off = home.appliance.sound.player.state.off.State
        self.forced_on = home.appliance.sound.player.state.forced.on.State
        self.forced_off = home.appliance.sound.player.state.forced.off.State
        self.forced_circadian_rhythm = (
            home.appliance.sound.player.state.forced.circadian_rhythm.State
        )

        super(State, self).__init__(events, events_disabled)
