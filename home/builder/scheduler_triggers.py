# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import yaml

import home.appliance
import home.event
import home.scheduler

from home.builder import Builder as Parent
from home.builder.scheduler.trigger import registry


class Builder(Parent):

    SUBDIRS = ["scheduler_triggers"]
    FILE_EXTENSION = ".yaml"

    def __init__(self, yaml_dir, group_of_performers):
        super(Builder, self).__init__(yaml_dir)
        self._group_of_performers = group_of_performers

    def run(self):
        for tag in home.appliance.data.registry:
            yaml.add_constructor(
                "!{}".format(tag),
                lambda loader, node: self.data_constructor(
                    home.appliance, loader, node
                ),
            )

        for tag in home.event.registry:
            yaml.add_constructor("!{}".format(tag), self.event_constructor)
        yaml.add_constructor(
            "!Position",
            lambda loader, node: self.data_constructor(
                home.scheduler.trigger.sun,
                loader,
                node,
            ),
        )

        for tag_ in set(home.scheduler.trigger.registry) - set(
            [
                "home.scheduler.trigger.Trigger",
            ]
        ):

            def scheduler_trigger_constructor(loader, node, tag=tag_):
                str_, cls_ = registry[tag]
                try:
                    return cls_().run(loader, node, self._group_of_performers)
                except TypeError as e:
                    self._logging.error(e)
                return []

            yaml.add_constructor("!{}".format(tag_), scheduler_trigger_constructor)

        scheduler_triggers = list()
        for scheduler_triggers_ in self.find_in_dirs(
            self._yaml_dir, self.SUBDIRS, self.FILE_EXTENSION
        ):
            scheduler_triggers.extend(scheduler_triggers_)

        result = list()
        for triggers in scheduler_triggers:
            result.extend(triggers)
        return result
