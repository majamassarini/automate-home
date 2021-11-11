# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance import Appliance as Parent
from home.appliance.light.zone import state


class Appliance(Parent):
    """
    A light automatically turned **on** when someone is arriving in the light zone or is already there.
    Automatically turned **off** when no one is in the light zone or near it unless it was forced on by the user.
    If the alarm system is armed and someone is coming the light becomes **alarmed** and starts blinking.
    This light model reacts to the following events:

    - **home.appliance.light.event.forced.Event**: tells the system a user turned on/off the light.

      - *home.appliance.light.event.forced.Event.On* -> the system will un-force a forced on light only if
        in the light zone the brightness is high or no one is in there.
      - *home.appliance.light.event.forced.Event.Off* -> the system will probably un-force a forced off light when
        one of the following events arrive: *courtesy, presence, alarm armed, sun brightness*.

    - **home.event.courtesy.Event**: tells the system someone *is/is not near* the light zone.

      - *home.event.courtesy.Event.On* -> the system will turn the light *on*, as a courtesy, if the sun brightness in the light
        zone is very low. The system will put the light in an *alarmed* state if the alarm in the light zone was armed.
      - *home.event.courtesy.Event.Off* -> the system will turn the light *off* only if there is nobody both near the zone light
        and in the zone light and the light was not forced on.

    - **home.event.presence.Event**: tells the system someone *is/is not in* the light zone.

      - *home.event.presence.Event.On* -> the system will turn the light *on* if the brightness in the light zone is very low.
        The system will put the light in an *alarmed* state if the alarm in the light zone was armed.
      - *home.event.presence.Event.Off* -> the system will turn the light *off* if the light is not alarmed or forced on.

    - **home.event.alarm.armed.Event**: tells the system the alarm is/is not armed in the light zone.

      - *home.event.alarm.armed.Event.On* -> the system will turn the light *off* even if it was forced on
        since no one should be in the light zone.
      - *home.event.alarm.armed.Event.Off* -> the system will turn the light *off*
        if it were turned on by a the triggered alarm.

    - **home.sun.brightness.Event.(Bright|Dark|DeepDark)**:  tells the system the sun brightness in the light zone is
      *very low/low/high*.

      - *home.sun.brightness.Event.DeepDark* -> the system will turn *on* the light in the above cases.
      - *home.sun.brightness.Event.Dark* -> the system will do nothing.
      - *home.sun.brightness.Event.Bright* ->  the system will turn the light *off* even if it was forced on.

    - **home.toggle.Event.(On|Off)**:  tells the system to toggle on/off when in alarmed state.

    Final states:

    - **forced on**
    - **forced off**
    - **on**
    - **off**
    - **alarmed on**
    - **alarmed off**

    Default state is **off**.

    >>> import home
    >>> l = home.appliance.light.zone.Appliance("a zone light", [])
    >>> _, new = l.notify(home.event.sun.brightness.Event.DeepDark)
    >>> new.compute()
    'Off'
    >>> _, new = l.notify(home.event.presence.Event.On)
    >>> new.compute()
    'On'
    >>> _, new = l.notify(home.event.presence.Event.Off)
    >>> new.compute()
    'Off'
    >>> l.disable(home.event.presence.Event.On)
    >>> l.is_enabled(home.event.presence.Event.Off)
    False
    >>> _, new = l.notify(home.event.presence.Event.On)
    >>> new.compute()
    'Off'
    >>> l.enable(home.event.presence.Event.On)
    >>> new.compute()
    'Off'
    >>> _, new = l.notify(home.event.alarm.armed.Event.On)
    >>> new.compute()
    'Off'
    >>> _, new = l.notify(home.event.presence.Event.On)
    >>> new.compute()
    'Alarmed On'
    >>> _, new = l.notify(home.appliance.light.event.forced.Event.Off)
    >>> new.compute()
    'Alarmed On'
    """

    def _init_state(self):
        return state.off.State()