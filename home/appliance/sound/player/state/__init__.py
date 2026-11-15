# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home import event as home_event
from home.appliance import attribute
from home.appliance.sound.player import event
from home.appliance.state import State as Parent
from home.appliance.callable import DoNothing


class FadeInPlaylist(DoNothing):
    pass


class FadeInVolume(DoNothing):
    pass


class FadeOutPlaylist(DoNothing):
    pass


class FadeOutVolume(DoNothing):
    pass


class FadeInVolumeScale(DoNothing):
    pass


class FadeOutVolumeScale(DoNothing):
    pass


class CircadianPlaylistC(DoNothing):
    pass


class CircadianPlaylistB(DoNothing):
    pass


class CircadianPlaylistA(DoNothing):
    pass


class Playlist(DoNothing):
    pass


class PlayMode(DoNothing):
    pass


class SleepyPlayMode(DoNothing):
    pass


class FadeInPlayMode(DoNothing):
    pass


class FadeOutPlayMode(DoNothing):
    pass


class CircadianPlayMode(DoNothing):
    pass


class Group(DoNothing):
    pass


class User(DoNothing):
    pass


class Volume(DoNothing):
    pass


class SleepyVolume(DoNothing):
    pass


class VolumeScale(DoNothing):
    pass


class Elapsed(DoNothing):
    pass


class Presence(DoNothing):
    pass


class Sleepiness(DoNothing):
    pass


class Mixin(object):
    def init_callables(self):
        callables = {
            type(event.fade_in.playlist.Event("unknown")): FadeInPlaylist(),
            type(event.fade_in.volume.Event(20)): FadeInVolume(),
            type(event.fade_out.playlist.Event("unknown")): FadeOutPlaylist(),
            type(event.fade_out.volume.Event(20)): FadeOutVolume(),
            type(event.fade_in.volume_scale.Event(100)): FadeInVolumeScale(),
            type(event.fade_out.volume_scale.Event(100)): FadeOutVolumeScale(),
            type(
                event.forced.circadian_rhythm.playlist_c.Event("unknown")
            ): CircadianPlaylistC(),
            type(
                event.forced.circadian_rhythm.playlist_b.Event("unknown")
            ): CircadianPlaylistB(),
            type(
                event.forced.circadian_rhythm.playlist_a.Event("unknown")
            ): CircadianPlaylistA(),
            type(event.playlist.Event("unknown")): Playlist(),
            event.play_mode.Event: PlayMode(),
            event.sleepy_play_mode.Event: SleepyPlayMode(),
            event.fade_in.play_mode.Event: FadeInPlayMode(),
            event.fade_out.play_mode.Event: FadeOutPlayMode(),
            event.forced.circadian_rhythm.play_mode.Event: CircadianPlayMode(),
            event.group.Event: Group(),
            type(event.volume.Event(30)): Volume(),
            type(event.sleepy_volume.Event(10)): SleepyVolume(),
            type(event.volume_scale.Event(100)): VolumeScale(),
            type(home_event.user.Event.A): User(),
            type(home_event.elapsed.Event.Off): Elapsed(),
            type(home_event.sleepiness.Event.Awake): Sleepiness(),
            type(home_event.presence.Event.Off): Presence(),
        }

        self._callables.update(callables)

        super(Mixin, self).init_callables()


class State(
    Parent,
    Mixin,
    attribute.mixin.Volume,
    attribute.mixin.Playlist,
    attribute.mixin.PlayMode,
    attribute.mixin.Group,
):
    """
    >>> import home
    >>> state = home.appliance.sound.player.state.off.State()
    >>> state = state.force("On")
    >>> state.compute()
    'Sleepy Forced On'
    >>> state = state.force("Off")
    >>> state.compute()
    'Off'
    """

    DEFAULTS = [
        event.fade_in.playlist.Event("Fade in"),
        event.fade_in.volume.Event(30),
        event.fade_out.playlist.Event("Fade out"),
        event.fade_out.volume.Event(20),
        event.fade_in.volume_scale.Event(100),
        event.fade_out.volume_scale.Event(100),
        event.forced.circadian_rhythm.playlist_c.Event("User C"),
        event.forced.circadian_rhythm.playlist_b.Event("User B"),
        event.forced.circadian_rhythm.playlist_a.Event("User A"),
        event.playlist.Event("Common"),
        event.volume.Event(20),
        event.sleepy_volume.Event(10),
        event.volume_scale.Event(100),
        event.play_mode.Event.RepeatAll,
        event.sleepy_play_mode.Event.RepeatAll,
        event.fade_in.play_mode.Event.RepeatAll,
        event.fade_out.play_mode.Event.RepeatAll,
        event.forced.circadian_rhythm.play_mode.Event.Shuffle,
        event.group.Event(""),
        home_event.user.Event.A,
        home_event.sleepiness.Event.Sleepy,
        home_event.presence.Event.Off,
        home_event.elapsed.Event.Off,
        event.forced.Event.Not,
    ]

    GROUP_EVENT = event.group.Event

    @property
    def forced_enum(self):
        return event.forced.Event


from home.appliance.sound.player.state import forced, off, fade_in, fade_out
