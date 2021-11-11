# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.protocol import Builder as Parent
from home.scheduler.trigger.protocol.delay import Trigger


class Builder(Parent):
    """
    >>> import home
    >>> class T(home.protocol.Trigger):
    ...     def __init__(self):
    ...         self._label = "Trigger"
    ...     @classmethod
    ...     def make_from_yaml(cls):
    ...         return Trigger()
    ...     @classmethod
    ...     def make_from(cls, msg):
    ...         pass
    ...     def make_new_state_from(self, another_description, old_state):
    ...         pass
    ...     def is_triggered(self, another_description):
    ...         pass
    ...     @property
    ...     def events(self):
    ...         return []
    >>> map = {
    ... "name": "1 minuto di consumi esagerati",
    ... "notify more events": [home.event.power.consumption.duration.Event.Long],
    ... "when triggered performers": "trigger consumi esagerati",
    ... "and timeout expires": 60,
    ... }
    >>> l = home.builder.scheduler.trigger.protocol.delay.Builder()._run(map,
    ...       {
    ...        "trigger consumi esagerati": home.Performers(
    ...            [
    ...                home.Performer(
    ...                    "a performer",
    ...                    None,
    ...                    [],
    ...                    [T()],
    ...                )
    ...            ]
    ...        )}
    ...     )
    >>> len(l)
    1
    """

    TAG_NAME = "protocol.delay.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_kwargs(self, mapping):
        d = super(Builder, self)._build_kwargs(mapping)
        d["timeout_seconds"] = mapping["and timeout expires"]
        return d
