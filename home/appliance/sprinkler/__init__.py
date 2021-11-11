# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.sprinkler import event
from home.appliance.sprinkler import state


class Appliance(Parent):
    """
    A sprinkler automatically turned **on** by a scheduler event just after sunset and if is not raining.
    Automatically turned **off** by a scheduler event.
    After sunrise is turned **off** even if someone *forced it on*.
    If has rained or will rain, in the forecast, than it is turned in a state called **partially on**.

    - **home.appliance.sprinkler.event.forced.Event**: tells the system a user turned on/off the sprinkler.

      - *home.appliance.sprinkler.event.forced.Event.On* -> the system will un-force a forced on sprinkler
        if it is raining or sun just rised.
      - *home.appliance.sprinkler.event.forced.Event.Off* -> the system will un-force a forced off sprinkler at sun set.

    - **home.event.enable.Event**: tells the system to enable/disable sprinkling.

      - *home.event.enable.Event.On* -> the system will turn the sprinkler *on* if the sun is set, is not raining,
        has not rained or will not rain. If has rained or will it rain than the system puts the sprinkler in a
        *partially on* state.
      - *home.event.enable.Event.Off* -> the system will turn the sprinkler *off* only if it was not *forced on*.

    - **home.event.sun.phase.Event.(Sunset|Sunrise)**: tells the system the sun *is set/is raised*.

      - *home.event.sun.phase.Event.Sunset* -> the system will turn the sprinkler *on* if it is enabled and
        has not rained or will not rain. If it is enabled and has rained and will rain the system does nothing.
        If it is enabled and has rained or will rain the system puts the sprinkler in a *partially on* state.
        The system will put the light in an *alarmed* state if the alarm in the light zone was armed.
      - *home.event.presence.Event.Sunrise* -> the system will turn the sprinkler *off*.

    - **home.event.rain.Event.(No|Gentle)**: tells the system is/is not raining.

      - *home.event.rain.Event.Gentle* -> the system will turn the sprinkler *off* even if it was forced on.
      - *home.event.rain.Event.No* -> the system will turn the sprinkler *partially on* if will no more rain and logic
        is enabled.

    - **home.event.rain.forecast.Event**: tells the system will/will not rain.

      - *home.event.forecast.rain.Event.On* -> the system will turn the sprinkler *on* if is no raining and has not
        rained. Otherwise will turn it *partially on* only if has not rained and is not raining.
      - *home.event.forecast.rain.Event.Off* -> the system will turn the sprinkler *partially on* if will no more
        rain and logic is enabled.

    - **home.event.rain.in_the_past.Event**: tells the system has/has not rained.

      - *home.event.in_the_past.rain.Event.On* -> the system will turn the sprinkler *on* if is no raining and will not
        rain. Otherwise will turn it *partially on* only if will not rained and is not raining.
      - *home.event.in_the_past.rain.Event.Off* -> the system will turn the sprinkler *partially on* if has not rained
        and logic is enabled.

    - **home.appliance.sprinkler.event.duration.Event**: tells the system how long sprinkling should last when in a *on*
      state.

    - **home.appliance.sprinkler.event.partially_on.duration.Event**: tells the system how long sprinkling should last
      when in a *partially on* state.

    Final states:

    - **forced on**
    - **forced partially on**
    - **forced off**
    - **on**
    - **partially on**
    - **off**

    Default state is **off**.

    >>> import home
    >>> l = home.appliance.sprinkler.Appliance("a sprinkler", [])
    >>> _, new = l.notify(home.event.enable.Event.On)
    >>> new.compute()
    'Off'
    >>> _, new = l.notify(home.event.sun.phase.Event.Sunset)
    >>> new.compute()
    'On'
    """

    def _init_state(self):
        return state.off.State()
