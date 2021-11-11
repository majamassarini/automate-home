# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.presence import state
from home.appliance import Appliance as Parent


class Appliance(Parent):
    """
    A light automatically turned **off** when no one is supposed to be using it.
    Because, as an example, the alarm system is armed.
    This light model reacts to the following events:

    - **home.appliance.light.event.forced.Event**: tells the system a user turned *on/off* the light.

      - *home.appliance.light.event.forced.Event.On* -> the system will un-force a forced on light if no one is
        considered being using it.
      - *home.appliance.light.event.forced.Event.Off* -> the system will never un-force a forced off light,
        which is in a off state since off is the default state.

    - **home.event.presence.Event**: tells the system someone *could/could not* being using the light

      - *home.event.presence.Event.On* -> the system will do nothing.
      - *home.event.presence.Event.Off* -> the system will un-force a forced on light because nobody is supposed to be using
        the light.

    Final states:

    - **forced on**
    - **off**

    Default state is **off**.


    >>> import home
    >>> p = home.appliance.light.presence.Appliance("an indoor presence light", [])
    >>> _, new = p.notify(home.appliance.light.event.forced.Event.On)
    >>> new.compute()
    'Forced On'
    >>> _, new = p.notify(home.event.presence.Event.Off)
    >>> new.compute()
    'Off'
    >>> _, new = p.notify(home.event.presence.Event.On)
    >>> new.compute()
    'Off'
    """

    def _init_state(self):
        return state.off.State()
