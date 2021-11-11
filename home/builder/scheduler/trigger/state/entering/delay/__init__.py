# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.state.entering import Builder as Parent
from home.scheduler.trigger.state.entering.delay import Trigger


class Builder(Parent):
    """
    >>> import home
    >>> map = {
    ... "name": "toggle 2",
    ... "notify events": [home.event.toggle.Event.On],
    ... "when appliance state became": "Fade In",
    ... "and timeout expires": 1
    ... }
    >>> l = home.builder.scheduler.trigger.state.entering.delay.Builder()._run(map, [])
    >>> off = home.appliance.sound.player.state.off.State()
    >>> fade_in = home.appliance.sound.player.state.fade_in.State()
    >>> l[0].is_triggered(off, fade_in)
    True
    """

    TAG_NAME = "state.entering.delay.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        args = super(Builder, self)._build_args(mapping)
        args.append(mapping["and timeout expires"])
        return args


from home.builder.scheduler.trigger.state.entering.delay import duration
