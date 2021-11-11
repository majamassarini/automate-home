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
    >>> state = home.appliance.sensor.alarm.state.unarmed.State()
    >>> state.compute()
    'Unarmed'
    >>> state = state.next(home.event.alarm.armed.Event.On)
    >>> state.compute()
    'Armed'
    >>> state = state.next(home.event.alarm.triggered.Event.On)
    >>> state.compute()
    'Triggered'
    """

    DEFAULTS = [event.alarm.armed.Event.Off, event.alarm.triggered.Event.Off]


from home.appliance.sensor.alarm.state import armed
from home.appliance.sensor.alarm.state import unarmed
from home.appliance.sensor.alarm.state import triggered
