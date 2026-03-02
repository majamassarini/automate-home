# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini


class Event:
    """
    Base class for all events in the system.

    There are two concrete families:
    - Enum-based events (home.event.Enum subclasses): carry no numeric value,
      e.g. presence.Event.On, sleepiness.Event.Sleepy
    - Value-based events (home.appliance.event.Int/Float/Str subclasses): carry
      a numeric or string payload, e.g. brightness.Event(80), volume.Event(50)
    """

    pass
