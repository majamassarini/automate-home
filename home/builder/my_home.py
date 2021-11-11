# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home.builder
from home import MyHome


class Yaml(MyHome):
    def __init__(self, yaml_dir):
        self._yaml_dir = yaml_dir
        super(Yaml, self).__init__()

    def _build_appliances(self):
        return home.builder.appliances.Builder(self._yaml_dir).run()

    def _build_performers(self):
        return home.builder.performers.Builder(self._yaml_dir, self._appliances).run()

    def _build_group_of_performers(self):
        return home.builder.group_of_performers.Builder(
            self._yaml_dir, self._performers
        ).run()

    def _build_scheduler_triggers(self):
        return home.builder.scheduler_triggers.Builder(
            self._yaml_dir, self._group_of_performers
        ).run()

    def _build_schedule_infos(self):
        return home.builder.schedule_infos.Builder(
            self._yaml_dir, self._group_of_performers, self._scheduler_triggers_by_name
        ).run()

    def dump_for_ws(self, filename):
        appliances = home.builder.appliances.Builder(self._yaml_dir).run()
        home.builder.performers.Builder(self._yaml_dir, appliances).dump(filename)
