# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger.protocol import Builder as Parent
from home.scheduler.trigger.protocol.timer import Trigger


class Builder(Parent):
    TAG_NAME = "protocol.timer.Trigger"

    @property
    def trigger(self):
        return Trigger

    def run(self, loader, node, group_of_performers):
        mapping = loader.construct_mapping(node, deep=True)
        performers = group_of_performers[mapping["when triggered performers"]]
        stop_timer_performers = group_of_performers[mapping["to performers"]]
        scheduler_triggers = list()
        for protocol_trigger in performers.triggers:
            scheduler_triggers.append(
                self.trigger(
                    name=mapping["name"],
                    events=mapping["notify more events"],
                    protocol_trigger=protocol_trigger,
                    timeout_seconds=mapping["wait for seconds"],
                    stop_timer_events=mapping["and notify new events"],
                    stop_timer_performers=stop_timer_performers,
                )
            )
        return scheduler_triggers
