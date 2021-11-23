# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.socket.presence.christmas import state


class Appliance(Parent):
    """
    A socket which is **by default on**. Designed to automate a socket with plugged in a tv, a voice controller,
    a Christmas tree ecc.

    It is automatically turned **off** when no one is supposed to be using it unless it is Christmas time.


    This socket model reacts to the following events:

    - **home.appliance.socket.event.forced.Event**: tells the system a user turned *on/off* the socket.

      - *home.appliance.socket.event.forced.Event.On* -> the system will un-force a forced on socket if no one is
        considered being using it.
      - *home.appliance.socket.event.forced.Event.Off* -> the system will never un-force a forced off socket,
        which is in a off state since off is the default state.

    - **home.event.presence.Event**: tells the system someone *could/could not* being using the socket

      - *home.event.presence.Event.On* -> the system will do nothing.
      - *home.event.presence.Event.Off* -> the system will un-force a forced on socket because nobody is supposed to be using
        the light.

    - **home.sun.brightness.Event.(Bright|Dark|DeepDark)**:  tells the system the *sun brightness* level.

      - *home.sun.brightness.Event.DeepDark* -> the system will turn *on* the socket even if nobody is supposed to be
        using it just at Christmas time.
      - *home.sun.brightness.Event.Dark* -> the system will do nothing.
      - *home.sun.brightness.Event.Bright* ->  the system will turn the light *off* if nobody is supposed to be using it.

    - **home.holiday.christmas.Event.(Over|Day|Eve|Time)**:  tells the system *is/is not christmas time/day*.

      - *home.holiday.christmas.Event.Over* -> the system will turn *off* the socket if nobody is supposed to be
        using it.
      - *home.holiday.christmas.Event.(Day|Eve)* -> the system will turn *on* the socket even if nobody is supposed to be
        using it or sun brightness level is high.
      - *home.holiday.christmas.Event.Time* -> the system will turn *on* the socket even if nobody is supposed to be
        using it if the sun brightness level is very low.

    - **home.holiday.san_silvester.Event.(Over|Day|Eve|Time)**:  tells the system *is/is not christmas time/day*.

      - *home.holiday.san_silvester.Event.Over* -> the system will turn *off* the socket if nobody is supposed to be
        using it.
      - *home.holiday.san_silvester.Event.(Day|Eve)* -> the system will turn *on* the socket even if nobody is supposed to be
        using it or sun brightness level is high.
      - *home.holiday.san_silvester.Event.Time* -> the system will turn *on* the socket even if nobody is supposed to be
        using it if the sun brightness level is very low.

    - **home.holiday.epiphany.Event.(Over|Day|Eve|Time)**:  tells the system *is/is not christmas time/day*.

      - *home.holiday.epiphany.Event.Over* -> the system will turn *off* the socket if nobody is supposed to be
        using it.
      - *home.holiday.epiphany.Event.(Day|Eve)* -> the system will turn *on* the socket even if nobody is supposed to be
        using it or sun brightness level is high.
      - *home.holiday.epiphany.Event.Time* -> the system will turn *on* the socket even if nobody is supposed to be
        using it if the sun brightness level is very low.

    Final states:

    - **Forced on**
    - **Forced off**
    - **On**
    - **Off**

    Default state is **On**.

    >>> import home
    >>> p = home.appliance.socket.presence.christmas.Appliance("a presence Christmas socket", [])
    >>> _, new = p.notify(home.event.holiday.christmas.Event.Time)
    >>> _, new = p.notify(home.event.sun.brightness.Event.DeepDark)
    >>> new.compute()
    'On'
    >>> _, new = p.notify(home.event.presence.Event.Off)
    >>> new.compute()
    'Off'
    >>> _, new = p.notify(home.event.holiday.christmas.Event.Over)
    >>> new.compute()
    'Off'
    """

    def _init_state(self):
        return state.on.State()
