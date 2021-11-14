# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home import event as home_event
from home.appliance import attribute
from home.appliance.sound.player import event
from home.appliance.sound.player.state import State as Parent
from home.appliance.sound.player.state.forced.on import callable as _callable


class Mixin(object):
    def init_callables(self):
        callables = {
            type(home.event.sleepiness.Event.Awake): _callable.Sleepiness(
                fade_out=self.fade_out
            ),
            type(home.event.presence.Event.Off): _callable.Presence(
                reset=self.reset, base=self.base
            ),
            self.forced_enum: _callable.Forced(
                base=self.base,
                forced_off=self.forced_off,
                forced_circadian_rhythm=self.forced_circadian_rhythm,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    Mixin,
    attribute.mixin.IsOn,
    attribute.mixin.IsNotFading,
    attribute.mixin.IsNotCircadianRhythm,
    Parent,
):

    VALUE = "Forced On"

    VOLUME_EVENT = event.volume.Event
    PLAYLIST_EVENT = event.playlist.Event

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.sound.player.state.off.State
        self.base = home.appliance.sound.player.state.off.State
        self.off = home.appliance.sound.player.state.off.State
        self.forced_off = home.appliance.sound.player.state.forced.off.State
        self.forced_circadian_rhythm = (
            home.appliance.sound.player.state.forced.circadian_rhythm.State
        )
        self.fade_out = home.appliance.sound.player.state.fade_out.State

        super(State, self).__init__(events, events_disabled)

    @attribute.mixin.Volume.volume.getter
    def volume(self) -> int:
        if home_event.sleepiness.Event.Sleepy in self.events:
            for klass, obj in self._events.items():
                if klass == event.sleepy_volume.Event:
                    return obj.value
        else:
            return super(State, self).volume
