# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.thermostat.presence.event.setpoint import Event as Parent


class Event(Parent):
    """
    An event carrying on setpoint data in keeping mode

    >>> Event(40.5)
    Keeping mode setpoint: 40.5°
    """

    def __init__(self, value: float):
        super(Event, self).__init__(value)
        self._str = "Keeping mode setpoint: {}°"
