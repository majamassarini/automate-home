# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import os
import tempfile

from home.tests.builder.test_helper import Helper

import home
from home.builder.performers import Builder


class Command(home.protocol.Command):
    def __init__(self):
        self._label = "Command"

    @classmethod
    def make_from_yaml(cls):
        return Command()

    def execute(self):
        pass

    def make_msgs_from(self, old_state, new_state):
        pass


class TestPerfomersBuilder(Helper):

    DATA = """
        - !Performer
          name: "luce"
          for appliance: "luce"
          commands:
          - !home.tests.builder.test_performers.Command {}
          triggers: []
        """

    def _builder_fix(self):
        Builder.SUBDIRS = [""]
        Builder.FILE_EXTENSION = self._path
        self._appliances = home.appliance.Collection()
        self._appliances["luci"] = set([home.appliance.light.Appliance("luce", [])])

        self._out_fd, self._out_path = tempfile.mkstemp()
        self._out_file = os.fdopen(self._out_fd, "w")
        return [self._out_file]

    def test_builder(self):
        from home.tests import builder  # noqa

        b = Builder(self.get_temporary_dir(), self._appliances)
        performers = b.run()
        self.assertEqual(len(performers), 1)

    def test_dump(self):
        b = Builder(self.get_temporary_dir(), self._appliances)
        b.dump(self._out_path)
        with open(self._out_path, "r") as outfile:
            data = outfile.readlines()
            self.assertIn("  for appliance: luce\n", data)
