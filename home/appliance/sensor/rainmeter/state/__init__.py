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
    >>> state = home.appliance.sensor.rainmeter.state.no.State()
    >>> state.compute()
    'Not raining'
    >>> state = state.next(home.event.rain.Event.Gentle)
    >>> state.compute()
    'Gentle raining'
    """

    DEFAULTS = [event.rain.Event.No]


from home.appliance.sensor.rainmeter.state import gentle
from home.appliance.sensor.rainmeter.state import no
