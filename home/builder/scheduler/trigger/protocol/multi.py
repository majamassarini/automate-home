# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger import Builder as Parent
from home.scheduler.trigger.protocol.multi import Trigger


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
    ... "name": "conditional scheduler trigger",
    ... "notify more events": [],
    ... "when A is triggered by performer": "performers triggering A",
    ... "and A is not reset by performer": "performers disabling triggering for A",
    ... "and B is triggered by performer": "performers triggering B",
    ... "and B is not reset by performer": "performers disabling triggering for B"
    ... }
    >>> l = home.builder.scheduler.trigger.protocol.multi.Builder()._run(map,
    ...       {
    ...        "performers triggering A": home.Performers(
    ...            [
    ...                home.Performer(
    ...                    "performer A",
    ...                    None,
    ...                    [],
    ...                    [T()],
    ...                )
    ...            ]
    ...        ),
    ...        "performers disabling triggering for A": home.Performers(
    ...            [
    ...                home.Performer(
    ...                    "performer not A",
    ...                    None,
    ...                    [],
    ...                    [T()],
    ...                )
    ...            ]
    ...         ),
    ...        "performers triggering B": home.Performers(
    ...            [
    ...                home.Performer(
    ...                    "performer B",
    ...                    None,
    ...                    [],
    ...                    [T()],
    ...                )
    ...            ]
    ...         ),
    ...        "performers disabling triggering for B": home.Performers(
    ...            [
    ...                home.Performer(
    ...                    "performer not B",
    ...                    None,
    ...                    [],
    ...                    [T()],
    ...                )
    ...            ]
    ...         ),
    ...         }
    ...     )
    >>> len(l)
    1
    """

    TAG_NAME = "protocol.multi.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _run(self, mapping, group_of_performers):
        positive_a = group_of_performers[mapping["when A is triggered by performer"]]
        negative_a = group_of_performers[mapping["and A is not reset by performer"]]
        positive_b = group_of_performers[mapping["and B is triggered by performer"]]
        negative_b = group_of_performers[mapping["and B is not reset by performer"]]
        scheduler_triggers = list()
        if (
            len(positive_a.triggers) != 1
            or len(negative_a.triggers) != 1
            or len(positive_b.triggers) != 1
            or len(negative_b.triggers) != 1
        ):
            raise AttributeError(
                "home.scheduler.protocol.multi.Trigger does not support more than one protocol trigger"
                "in a performer!"
            )

        scheduler_triggers.append(
            self.trigger(
                name=mapping["name"],
                events=mapping["notify more events"],
                positive_a=positive_a.triggers[0],
                negative_a=negative_a.triggers[0],
                positive_b=positive_b.triggers[0],
                negative_b=negative_b.triggers[0],
            )
        )
        return scheduler_triggers
