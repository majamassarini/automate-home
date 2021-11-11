# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import os
import tempfile

import home
from home.builder.schedule_infos import Builder
from home.tests.builder.test_helper import Helper


class Trigger(home.protocol.Trigger):
    def __init__(self):
        self._label = "Trigger"

    @classmethod
    def make_from_yaml(cls):
        return Trigger()

    @classmethod
    def make_from(cls, msg):
        pass

    def make_new_state_from(self, another_description, old_state):
        pass

    def is_triggered(self, another_description):
        pass

    @property
    def events(self):
        return []


class TestSchedulerTriggersBuilder(Helper):

    DATA = """
        - !schedule
           trigger: "a trigger"
           for performers: "some performers"
        """

    def _builder_fix(self):
        Builder.SUBDIRS = [""]
        Builder.FILE_EXTENSION = self._path

        self._group_of_performers = {
            "some performers": home.Performers(
                [
                    home.Performer(
                        "a performer",
                        home.appliance.light.Appliance("for light", []),
                        [],
                        [Trigger()],
                    ),
                    home.Performer(
                        "another performer",
                        home.appliance.light.Appliance("for another light", []),
                        [],
                        [Trigger()],
                    ),
                ]
            )
        }
        self._scheduler_triggers = {
            "a trigger": [
                home.scheduler.trigger.state.entering.delay.Trigger(
                    "stay in state", [], state="On", timeout_seconds=3
                )
            ]
        }

        self._out_fd, self._out_path = tempfile.mkstemp()
        self._out_file = os.fdopen(self._out_fd, "w")
        return [self._out_file]

    def test_builder(self):
        b = Builder(
            self.get_temporary_dir(),
            self._group_of_performers,
            self._scheduler_triggers,
        )
        schedule_infos = b.run()
        self.assertEqual(len(schedule_infos), 1)
