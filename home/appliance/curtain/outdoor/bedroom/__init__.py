# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.curtain.outdoor.bedroom.state.opened import State
from home.appliance import Appliance as Parent


class Appliance(Parent):
    """
    An outdoor bedroom Curtain. Designed to model an outdoor automated curtain to be used in a bedroom.

    It is closed by the system when the sun (with an high brightness) hits the curtain's window or at sunset.

    It is opened by the system when it is time to wake up the user (after sunrise) or when the wind is strong.

    It could be forced opened or forced closed by a user.

    This curtain model reacts to the following events:

    - **home.appliance.curtain.event.forced.Event.(Opened|Closed)**: tells the system a user *opened/closed* the curtain.

      - *home.appliance.curtain.event.forced.Event.Opened* -> a user *forced opened* a closed curtain.
      - *home.appliance.curtain.event.forced.Event.Closed* -> a user *forced closed* an opened curtain.

    - **home.event.sun.brightness.Event.(DeepDark|Dark|Bright)**: tells the system the *sun brightness* level.

      - *home.event.sun.brightness.Event.(DeepDark|Dark)* -> the system will *open* a closed curtain unless the user
        forced closed it or the sun is already set.
      - *home.event.sun.brightness.Event.Bright* -> the system will *close* an opened curtain if the sun is hitting the
        curtain's window unless the user forced closed it or the wind is strong.

    - **home.event.sun.twilight.civil.Event.(Sunrise|Sunset)**: tells the system that it is *sunrise/sunset*.

      - *home.event.sun.twilight.civil.Event.Sunrise* -> the system will *open* the curtain if the user should not yet
        being asleep.
      - *home.event.sun.twilight.civil.Event.Sunset* -> the system will *close* the curtain unless it is windy.

    - **home.event.sun.hit.Event**: tells the system that the sun *is/is not hitting* the curtain's window.

      - *home.event.sun.hit.Event.On* -> the system will *close* the curtain if the sun brightness is high and
        the wind is not strong or a user forced it opened.
      - *home.event.sun.hit.Event.Off* -> the system will *open* a closed curtain unless sun was already set or
        a user forced it closed.

    - **home.event.sleepiness.Event.(Asleep|Awake|Sleepy)**: tells the system that the user should be *asleep/awake*.

      - *home.event.sleepiness.Event.(Asleep|Sleepy)* -> the system will do nothing.
      - *home.event.sleepiness.Event.Awake* -> the system will *open* the curtain if the sun is already rised.

    - **home.event.wind.Event.(Weak|Strong)**: tells the system that the wind is *weak/strong*.

      - *home.event.wind.Event.Weak* -> the system will *close* an opened curtain unless it was forced opened.
      - *home.event.wind.Event.Strong* -> the system will *open* a closed curtain unless it was forced closed.


    Final states:

    - **forced closed**
    - **forced opened**
    - **closed**
    - **opened**

    Default state is **opened**.

    >>> import home
    >>> c = home.appliance.curtain.outdoor.bedroom.Appliance("a curtain", [])
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


from home.appliance.curtain.outdoor.bedroom import state
