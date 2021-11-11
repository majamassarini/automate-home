# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder import Builder as Parent


class Builder(Parent):

    SUBDIRS = ["performers"]
    FILE_EXTENSION = ".yaml"

    def __init__(self, yaml_dir, performers):
        super(Builder, self).__init__(yaml_dir)
        self._performers = performers

    def run(self):
        _group_of_performers = dict()
        for groups in self.find_in_dirs(
            self._yaml_dir, self.SUBDIRS, self.FILE_EXTENSION
        ):
            _group_of_performers.update(groups)

        group_of_performers = {}
        for key, value in _group_of_performers.items():
            group_of_performers[key] = [
                performer
                for performer in self._performers
                for a_name in value
                if performer.name == a_name
            ]

        return group_of_performers
