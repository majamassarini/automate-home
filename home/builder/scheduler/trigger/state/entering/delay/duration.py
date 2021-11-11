# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.state import Builder as Parent
from home.scheduler.trigger.state.entering.delay.duration import Trigger


class Builder(Parent):
    """
    >>> import home
    >>> map = {
    ... "name": "disabilita irrigatore (forced on state)",
    ... "notify events": [home.appliance.sprinkler.event.forced.Event.Not],
    ... "when appliance state became (and appliance state duration elapsed)": "Forced On"}
    >>> l = home.builder.scheduler.trigger.state.entering.delay.duration.Builder()._run(map, [])
    >>> len(l)
    1
    """

    TAG_NAME = "state.entering.delay.duration.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_args(self, mapping):
        name = mapping["name"]
        events = mapping["notify events"]
        state = (
            mapping[
                "when appliance state became (and appliance state duration elapsed)"
            ],
        )
        return [name, events, state]
