# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging
from home.builder.scheduler.trigger import Builder as Parent
from home.scheduler.trigger.protocol import Trigger


class Builder(Parent):
    TAG_NAME = "protocol.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _build_kwargs(self, mapping):
        return {
            "name": mapping["name"],
            "events": mapping["notify more events"],
        }

    def _run(self, mapping, group_of_performers):
        logger = logging.getLogger(__name__)
        kwargs = self._build_kwargs(mapping)
        try:
            performers = group_of_performers[mapping["when triggered performers"]]
        except KeyError as e:
            logger.error(e)
            return list()
        scheduler_triggers = list()
        if not performers.triggers:
            logger.error(
                "{} have no triggers, could not be used as scheduler trigger performers".format(
                    performers
                ),
            )
        for protocol_trigger in performers.triggers:
            scheduler_triggers.append(
                self.trigger(
                    **kwargs,
                    protocol_trigger=protocol_trigger,
                )
            )
        return scheduler_triggers


from home.builder.scheduler.trigger.protocol import delay
from home.builder.scheduler.trigger.protocol import multi
from home.builder.scheduler.trigger.protocol import timer
from home.builder.scheduler.trigger.protocol import mean
from home.builder.scheduler.trigger.protocol import enum
