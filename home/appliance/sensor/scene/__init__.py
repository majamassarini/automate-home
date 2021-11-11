# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sensor.scene import state
from home.appliance import Appliance as Parent


class Appliance(Parent):
    """
    A scene Button.

    *Triggered* when the button is pressed.

    It could be made *Untriggered* few seconds later the button has been pressed.

    Or it could be made *Untriggered* when the running scene is ended.

    The scene is usually started when the old Appliance State is *Untriggered* and
    the new Appliance state is *Triggered*.

    >>> import home
    >>> s  = home.appliance.sensor.scene.Appliance("a scene", [])
    >>> old, new = s.notify(home.event.scene.Event.Triggered)
    >>> old.compute()
    'Untriggered'
    >>> new.compute()
    'Triggered'
    """

    def _init_state(self):
        return state.untriggered.State()
