# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.sun import Builder as Parent
from home.scheduler.trigger.sun.sunhit import Trigger


class Builder(Parent):
    """
    >>> import home
    >>> map = {
    ... "name": "sunhit finestre a sud",
    ... "notify more events": [],
    ... "latitude": 46.201685,
    ... "longitude": 13.209001,
    ... "elevation": 280,
    ... "position": home.scheduler.trigger.sun.Position (10, 90, 145, 270)
    ... }
    >>> l = home.builder.scheduler.trigger.sun.sunhit.Builder()._run(map, [])
    >>> len(l)
    1
    """

    TAG_NAME = "sun.sunhit.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        args = super(Builder, self)._build_args(mapping)
        position = mapping["position"]
        args.append(position)
        return args
