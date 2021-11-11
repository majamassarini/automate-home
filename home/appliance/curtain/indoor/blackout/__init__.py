# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.curtain.indoor.blackout.state.opened import State
from home.appliance import Appliance as Parent


class Appliance(Parent):
    """
    An indoor blackout Curtain. Designed to model an indoor automated curtain in a bedroom.

    This curtain model reacts to the following events:

    - **home.appliance.curtain.event.forced.Event.(Opened|Closed)**: tells the system a user *opened/closed* the curtain.

      - *home.appliance.curtain.event.forced.Event.Opened* -> a user *forced opened* a closed curtain.
      - *home.appliance.curtain.event.forced.Event.Closed* -> a user *forced closed* an opened curtain.

    - **home.event.sun.twilight.civil.Event.(Sunrise|Sunset)**: tells the system that it is *sunrise/sunset*.

      - *home.event.sun.twilight.civil.Event.Sunrise* -> the system will *open* the curtain if the user should not yet
        being asleep.
      - *home.event.sun.twilight.civil.Event.Sunset* -> the system will *close* the curtain.

    - **home.event.sleepiness.Event.(Asleep|Awake|Sleepy)**: tells the system that the user should be *asleep/awake*.

      - *home.event.sleepiness.Event.(Asleep|Sleepy)* -> the system will do nothing.
      - *home.event.sleepiness.Event.Awake* -> the system will *open* the curtain if the sun is already rised.


    Final states:

    - **forced closed**
    - **forced opened**
    - **closed**
    - **opened**

    Default state is **opened**.

    >>> import home
    >>> c = home.appliance.curtain.indoor.blackout.Appliance("a curtain", [])
    >>> old, new = c.notify(home.event.sun.twilight.civil.Event.Sunset)
    >>> new.compute()
    'Closed'
    >>> old, new = c.notify(home.event.sleepiness.Event.Asleep)
    >>> old, new = c.notify(home.event.sun.twilight.civil.Event.Sunrise)
    >>> new.compute()
    'Closed'
    >>> old, new = c.notify(home.event.sleepiness.Event.Awake)
    >>> new.compute()
    'Opened'
    """

    def _init_state(self):
        return State()


from home.appliance.curtain.indoor.blackout import state
