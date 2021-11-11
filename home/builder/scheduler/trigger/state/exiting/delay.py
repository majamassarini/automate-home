# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.state.exiting import Builder as Parent
from home.scheduler.trigger.state.exiting.delay import Trigger


class Builder(Parent):
    """
    >>> import home
    >>> map = {
    ... "name": "toggle 2",
    ... "notify events": [home.event.toggle.Event.On],
    ... "when appliance state is no more": "Alarmed",
    ... "and timeout expires": 60
    ... }
    >>> l = home.builder.scheduler.trigger.state.exiting.delay.Builder()._run(map, [])
    >>> len(l)
    1
    """

    TAG_NAME = "state.exiting.delay.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        args = super(Builder, self)._build_args(mapping)
        args.append(mapping["and timeout expires"])
        return args
