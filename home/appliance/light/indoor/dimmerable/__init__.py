# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light import Appliance as Parent
from home.appliance.light.indoor.dimmerable import event
from home.appliance.light.indoor.dimmerable import state


class Appliance(Parent):
    """
    A light which can work in **four** different modes and in every moment it can switch between its working modes.

      - It can follow circadian rhythm events when in a **forced circadian rhythm** state.
        A scheduler trigger will notify circadian rhythm brightness/temperature
        events during the day making the light adjusting its settings.
      - It can follow lux balancing events when in a **forced lux balancing** state.
        A scheduler trigger linked to a *sun lux balancing protocol trigger*
        will notify lux balancing brightness events making the light
        adjusting its brightness accordingly to the sun brightness.
        The less bright will be the sun the more bright will be the light.
      - It can automatically change its brightness and temperature
        with a given period of time, for a given number of cycles,
        starting and ending from given show colors when in a **forced show** state.
      - It can have a fixed brightness when in a **forced on** state.
        Its brightness/temperature will be adjusted only by the user.


    This light model reacts to the following events:

    - **home.appliance.light.event.forced.Event**: tells the system a user turned in a forced
      **on/circadian rhythm/lux balancing/show** state the light.

      - *home.appliance.light.event.forced.Event.On* -> the system will put the light in a *forced on* state.
      - *home.appliance.light.event.forced.Event.CircadianRhythm* -> the system will put the light in a
        *forced circadian rhythm* state.
      - *home.appliance.light.event.forced.Event.LuxBalancing* -> the system will put the light in a
        *forced lux balancing* state.
      - *home.appliance.light.event.forced.Event.Show* -> the system will put the light in a
        *forced show* state.
      - *home.appliance.light.event.forced.Event.Off* -> the system will put the light in a *forced off* state which is
        an *off* state.

    - **home.event.presence.Event**: tells the system someone *could/could not* being using the light

      - *home.event.presence.Event.On* -> the system will do nothing.
      - *home.event.presence.Event.Off* -> the system will un-force a forced on light because nobody is supposed to be using
        the light.

    - **home.appliance.event.brightness.Event**: tells the system the user desired brightness,
      used by the system when the light is in a *forced on* state

    - **home.appliance.event.circadian_rhythm.brightness.Event**: tells the system the actual circadian rhythm brightness,
      used by the system when the light is in a *forced circadian rhythm* state

    - **home.appliance.event.lux_balancing.brightness.Event**: tells the system the actual lux balancing brightness,
      used by the system when the light is in a *forced lux balancing* state

    - **home.appliance.event.show.starting_brightness.Event**: tells the system the show have to start with show starting brightness,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.ending_brightness.Event**: tells the system the show have to end with show ending brightness,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.period.Event**: tells the system the show have to last for *period event*,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.period.Event**: tells the system the show have to repeat itself for *cycles event*,
      used by the system when the light is in a *forced show* state

    - **home.event.waveform.Event**: tells the system the show transition from starting to ending brightness
      have to be in the form of *waveform event*,
      used by the system when the light is in a *forced show* state

    Final states:

    - **Forced on**
    - **Forced circadian rhythm**
    - **Forced lux balancing**
    - **Forced show**
    - **Off**

    Default state is **Off**.


    >>> import home
    >>> l = home.appliance.light.indoor.dimmerable.Appliance("a light", [])
    >>> old, new = l.notify(home.appliance.light.indoor.dimmerable.event.forced.Event.On)
    >>> old.compute()
    'Off'
    >>> new.compute()
    'Forced On'
    >>> old, new = l.notify(home.appliance.light.indoor.dimmerable.event.forced.Event.Off)
    >>> new.compute()
    'Off'
    """

    def _init_state(self):
        return state.off.State()
