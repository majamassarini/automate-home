# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini


from home.appliance import Appliance as Parent
from home.appliance.sound.player import event
from home.appliance.sound.player import state


class Appliance(Parent):
    """
    A sound player wich can be forced by the user in **two** different states.

      - It can follow *circadian rhythm* events when in a **forced circadian rhythm** state.
        A scheduler trigger will notify *circadian rhythm playlist events* during the day
        making the sound player adjusting the played playlist.
        The playlists, when in a circadian rhythm state, could be associated to three different users: A, B, C.
        A user will choose which are the associated playlist he wants to listen to.
      - It can have an almost *fixed* playlist and volume when in a **forced on** state.
        The playlist and volume will be adjusted only by the user.

    The system puts the sound player in a **fade in** state when its time to wake up the user.

    The system puts the sound player in a **fade out** state if the sound player is forced on or forced in a circadian
    rhythm state and its time for the user to go to bed.


    This sound player model reacts to the following events:

    - **home.appliance.sound.player.event.forced.Event**: tells the system a user turned in a forced
      **on/circadian rhythm** state the sound player.

      - *home.appliance.light.event.forced.Event.On* -> the system will put the sound player in a *forced on* state.
      - *home.appliance.light.event.forced.Event.CircadianRhythm* -> the system will put the sound player in a
        *forced circadian rhythm* state.
      - *home.appliance.light.event.forced.Event.Off* -> the system will put the sound player in a *forced off* state which is
        an *off* state.

    - **home.event.presence.Event**: tells the system someone *could/could not* being using the sound player

      - *home.event.presence.Event.On* -> the system will do nothing.
      - *home.event.presence.Event.Off* -> the system will un-force a forced sound player because
        nobody is supposed to be using it.

    - **home.event.sleepiness.Event.(Asleep|Awake|Sleepy)**: tells the system if the user should be *asleep/awake/sleepy*

      - *home.event.sleepiness.Event.Asleep* -> the system will put the sound player in a *fade out* state if already
        forced on or forced circadian rhythm.
      - *home.event.sleepiness.Event.Awake* -> the system will put the sound player in a *fade in* state.
      - *home.event.sleepiness.Event.Sleepy* -> the system will use the sleepy volume if forced on or forced in a
        circadian rhythm.

    - **home.event.user.Event.(A|B|C)**: tells the system which *user profile use*, when in a
      *forced circadian rhythm* state

    - **home.appliance.sound.player.event.playlist.Event**: tells the system the playlist to be used,
      when the sound player is in a *forced on* state

    - **home.appliance.sound.player.event.volume.Event**: tells the system the volume to be used,
      when the sound player is in a *forced on/circadian rhythm* state

    - **home.appliance.sound.player.event.sleepy_volume.Event**: tells the system the volume to be used,
      when the sound player is in a *forced on/circadian rhythm* state and the user is supposed to be sleepy,
      like in the evening.

    - **home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event**: tells the system the playlist
      to be used for user A, when the sound player is in a *forced circadian rhythm* state

    - **home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event**: tells the system the playlist
      to be used for user B, when the sound player is in a *forced circadian rhythm* state

    - **home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event**: tells the system the playlist
      to be used for user C, when the sound player is in a *forced circadian rhythm* state

    - **home.appliance.sound.player.event.fade_in.playlist.Event**: tells the system the playlist to be used,
      when the sound player is in a *fade in* state

    - **home.appliance.sound.player.event.fade_in.volume.Event**: tells the system the volume to be used,
      when the sound player is in a *fade in* state

    - **home.appliance.sound.player.event.fade_out.playlist.Event**: tells the system the playlist to be used,
      when the sound player is in a *fade out* state

    - **home.appliance.sound.player.event.fade_out.volume.Event**: tells the system the volume to be used,
      when the sound player is in a *fade out* state


    Final states:

    - **Forced on**
    - **Forced circadian rhythm**
    - **Fade in**
    - **Fade out**
    - **Off**

    Default state is **Off**.

    >>> import home
    >>> p = home.appliance.sound.player.Appliance("a player", [])
    >>> old, new = p.notify(home.appliance.sound.player.event.forced.Event.On)
    >>> old.compute()
    'Off'
    >>> new.compute()
    'Forced On'
    >>> old, new = p.notify(home.appliance.sound.player.event.forced.Event.Not)
    >>> new.compute()
    'Off'
    """

    def _init_state(self):
        return state.off.State()
