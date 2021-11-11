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
    >>> state = home.appliance.sensor.scene.state.untriggered.State()
    >>> state.compute()
    'Untriggered'
    >>> state = state.next(home.event.scene.Event.Triggered)
    >>> state.compute()
    'Triggered'
    """

    DEFAULTS = [event.scene.Event.Untriggered]


from home.appliance.sensor.scene.state import triggered
from home.appliance.sensor.scene.state import untriggered
