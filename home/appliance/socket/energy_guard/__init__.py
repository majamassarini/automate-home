# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.socket.energy_guard import state


class Appliance(Parent):
    """
    A socket which is **by default on**. Designed to let the system control the home's power consumption.
    This socket is supposed to have plugged in a load like a dishwasher.

    A energy guard socket enters a **detachable** state when its detach logic is enabled and power
    consuming levels are too much high.

    A energy guard socket enters an **off** state when its detach logic is enabled and power consuming
    levels are too much high for too much time.

    When power consuming levels lower down it will be turned **on** again by the system.

    You could have more energy guard sockets. A socket can enable the detach logic of another socket
    when turning itself off.

    This will design a priority level between sockets.

      1) when a socket is turned off then it will enable the detach logic of another socket A -> enables -> B -> enables -> C -> enables -> D
      2) when a socket is turned on then it will disable its detach logic by itself,
      3) when power consuming levels are high again than will be enabled the detach logic for the lowest priority socket


    This socket model reacts to the following events:

    - **home.appliance.socket.event.forced.Event**: tells the system a user turned *on/off* the socket.

      - *home.appliance.socket.event.forced.Event.On* -> a user *forced on* an off socket.
      - *home.appliance.socket.event.forced.Event.Off* -> a user *forced off* an on socket.

    - **home.event.enable.Event**: tells the system that the detachable logic for this socket *could/could not* being enabled

      - *home.event.enable.Event.On* -> the system will let this socket be put in a detachable state.
      - *home.event.enable.Event.Off* -> the system will not let this socket be put in a detachable state.

    - **home.event.power.consumption.Event.(No|Low|High)**:  tells the system how is the *power consumption* level in the home.

      - *home.event.power.consumption.Event.(No|Low)* -> the system will turn *on* the socket.
      - *home.event.power.consumption.Event.(High)* -> the system will turn *off* the socket if it is in a detachable
        state and the high power consumption last from long time.

    - **home.event.power.consumption.duration.Event.(Short|Long)**:  tells the system *how long last* the
      *high power consumption* level in the home.

      - *home.event.power.consumption.duration.Event.Short* -> the system will do nothing.
      - *home.event.power.consumption.duration.Event.Long* -> the system will turn *off* the socket if it is in a detachable
        state and the power consumption level is high.

    Final states:

    - **Forced off**
    - **Forced on**
    - **Off**
    - **On**
    - **Detachable**

    Default state is **On**.

    >>> import home
    >>> p = home.appliance.socket.energy_guard.Appliance("a energy guard socket", [])
    >>> old, new = p.notify(home.event.enable.Event.On)
    >>> old.compute()
    'On'
    >>> new.compute()
    'On'
    >>> _, new = p.notify(home.event.power.consumption.Event.High)
    >>> _, new = p.notify(home.event.power.consumption.duration.Event.Long)
    >>> new.compute()
    'Off'
    >>> _, new = p.notify(home.event.power.consumption.Event.No)
    >>> new.compute()
    'On'
    >>> _, new = p.notify(home.event.power.consumption.Event.High)
    >>> new.compute()
    'On'
    >>> _, new = p.notify(home.event.enable.Event.On)
    >>> _, new = p.notify(home.event.power.consumption.duration.Event.Long)
    >>> new.compute()
    'Off'
    >>> _, new = p.notify(home.event.power.consumption.Event.No)
    >>> new.compute()
    'On'
    >>> _, new = p.notify(home.appliance.socket.event.forced.Event.Off)
    >>> new.compute()
    'Forced Off'
    """

    def _init_state(self):
        return state.on.State()
