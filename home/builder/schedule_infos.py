# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging
import yaml

from home.performer import Performers
from home.protocol.message import Unknown
from home.builder import Builder as Parent


class Builder(Parent):

    SUBDIRS = ["scheduler"]
    FILE_EXTENSION = ".yaml"

    def __init__(self, yaml_dir, group_of_performers, scheduler_triggers):
        super(Builder, self).__init__(yaml_dir)
        self._group_of_performers = group_of_performers
        self._scheduler_triggers = scheduler_triggers
        self._logging = logging.getLogger(__name__)

    def run(self):
        yaml.add_constructor("!schedule", self.schedule_constructor)

        scheduler = list()
        for scheduler_ in self.find_in_dirs(
            self._yaml_dir, self.SUBDIRS, self.FILE_EXTENSION
        ):
            scheduler.extend(scheduler_)

        return scheduler

    def schedule_constructor(self, loader, node):
        mapping = loader.construct_mapping(node, deep=True)
        try:
            performers = self._group_of_performers[mapping["for performers"]]
        except KeyError as e:
            self._logging.error(e)
            performers = Performers([])
        try:
            trigger = self._scheduler_triggers[mapping["trigger"]]
        except KeyError as e:
            self._logging.error(e)
            trigger = [Unknown(None, [])]

        return (performers, trigger)
