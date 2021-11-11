# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light import Appliance as Parent
from home.appliance.light.indoor.hue.state import off


class Appliance(Parent):
    """
    A light wich can work in *four* different modes at the same time and
    in every moment it can switch between its working modes.

      - it can follow *circadian rhythm* events when in a **forced circadian rhythm** state.
        A **circadian rhythm** scheduler trigger will notify *circadian rhythm brightness/hue/saturation/temperature
        events* during the day making the hue light adjusting its settings.
      - it can follow *lux balancing* events when in a **forced lux balancing** state.
        A *protocol scheduler trigger* linked to a *sun lux balancing
        protocol trigger* will notify *lux balancing brightness events* making the
        hue light adjusting its brightness accordingly to the sun brightness.
        The less bright will be the sun the more bright will be the dimmerable light.
      - it can automatically change its **hue, saturation, brightness and temperature** with a
        given *period* and for a *cycles* times, starting and ending from given show events
        when in a **forced show** state.
      - it can have an almost **fixed** brightness when in a *forced on* state.
        Its brightness/hue/saturation/temperature will be adjusted only by the user.

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

      - *home.event.presence.On* -> the system will do nothing.
      - *home.event.presence.Off* -> the system will un-force a forced on light because nobody is supposed to be using
        the light.

    - **home.appliance.event.brightness.Event**: tells the system the user desired brightness,
      used by the system when the light is in a *forced on* state

    - **home.appliance.event.hue.Event**: tells the system the user desired hue,
      used by the system when the light is in a *forced on* state

    - **home.appliance.event.saturation.Event**: tells the system the user desired saturation,
      used by the system when the light is in a *forced on* state

    - **home.appliance.event.temperature.Event**: tells the system the user desired temperature,
      used by the system when the light is in a *forced on* state

    - **home.appliance.event.circadian_rhythm.brightness.Event**: tells the system the actual circadian rhythm brightness,
      used by the system when the light is in a *forced circadian rhythm* state

    - **home.appliance.event.circadian_rhythm.hue.Event**: tells the system the actual circadian rhythm hue,
      used by the system when the light is in a *forced circadian rhythm* state

    - **home.appliance.event.circadian_rhythm.saturation.Event**: tells the system the actual circadian rhythm saturation,
      used by the system when the light is in a *forced circadian rhythm* state

    - **home.appliance.event.circadian_rhythm.temperature.Event**: tells the system the actual circadian rhythm temperature,
      used by the system when the light is in a *forced circadian rhythm* state

    - **home.appliance.event.lux_balancing.brightness.Event**: tells the system the actual lux balancing brightness,
      used by the system when the light is in a *forced lux balancing* state

    - **home.appliance.event.show.starting_brightness.Event**: tells the system the show have to start with show starting brightness,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.starting_hue.Event**: tells the system the show have to start with show starting hue,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.ending_brightness.Event**: tells the system the show have to end with show ending brightness,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.ending_hue.Event**: tells the system the show have to end with show ending hue,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.period.Event**: tells the system the show have to last for *period event*,
      used by the system when the light is in a *forced show* state

    - **home.appliance.event.show.period.Event**: tells the system the show have to repeat itself for *cycles event*,
      used by the system when the light is in a *forced show* state

    - **home.event.waveform.Event**: tells the system the show transition from starting to ending brightness
      have to be in the form of *waveform event*,
      used by the system when the light is in a *forced show* state

    Final states:

    - **forced on**
    - **forced circadian rhythm**
    - **forced lux balancing**
    - **forced show**
    - **off**

    Default state is **off**.

    >>> import home
    >>> l = home.appliance.light.indoor.hue.Appliance("a light", [])
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
        return off.State()


from home.appliance.light.indoor.hue import state
