# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home import event
from home.appliance.sensor.state import State as Parent


class State(Parent):
    """
    >>> import home
    >>> state = home.appliance.sensor.motion.state.missed.State()
    >>> state.compute()
    'Missed'
    >>> state = state.next(home.event.motion.Event.Spotted)
    >>> state.compute()
    'Spotted'
    """

    DEFAULTS = [event.motion.Event.Missed]


from home.appliance.sensor.motion.state import missed
from home.appliance.sensor.motion.state import spotted
