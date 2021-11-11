# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance import attribute
from home.appliance.sound.player import event
from home.appliance.sound.player.state import State as Parent
from home.appliance.sound.player.state.forced.circadian_rhythm import (
    callable as _callable,
)


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
                forced_on=self.forced_on,
                forced_off=self.forced_off,
            ),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    Mixin,
    attribute.mixin.IsOn,
    attribute.mixin.IsNotFading,
    attribute.mixin.IsCircadianRhythm,
    Parent,
):

    VALUE = "Forced Circadian Rhythm"

    VOLUME_EVENT = event.volume.Event
    PLAYLIST_EVENT = None

    def __init__(self, events=None, events_disabled=None):
        self.reset = home.appliance.sound.player.state.off.State
        self.base = home.appliance.sound.player.state.off.State
        self.forced_on = home.appliance.sound.player.state.forced.on.State
        self.forced_off = home.appliance.sound.player.state.forced.off.State
        self.forced_circadian_rhythm = (
            home.appliance.sound.player.state.forced.circadian_rhythm.State
        )
        self.fade_out = home.appliance.sound.player.state.fade_out.State

        super(State, self).__init__(events, events_disabled)

    @property
    def playlist(self):
        lookup = None
        if home.event.user.Event.A in self.events:
            lookup = (
                home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event
            )
        elif home.event.user.Event.B in self.events:
            lookup = (
                home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event
            )
        elif home.event.user.Event.C in self.events:
            lookup = (
                home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event
            )
        if lookup:
            for klass, obj in self._events.items():
                if klass == lookup:
                    return obj.value
        else:
            return "None was found"

    @property
    def volume(self):
        if home.event.sleepiness.Event.Sleepy in self.events:
            for klass, obj in self._events.items():
                if klass == home.appliance.sound.player.event.sleepy_volume.Event:
                    return obj.value
        else:
            return super(State, self).volume

    def next_volume(self, value):
        if home.event.sleepiness.Event.Sleepy in self.events:
            return self.next(event.sleepy_volume.Event(value))
        else:
            return self.next(event.volume.Event(value))
