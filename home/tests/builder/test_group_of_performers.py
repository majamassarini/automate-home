# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.builder.group_of_performers import Builder
from home.tests.builder.test_helper import Helper


class TestGroupOfPerfomersBuilder(Helper):

    DATA = """
        prese muro:
        - "presa 1"
        - "presa 2"
        """

    def _builder_fix(self):
        Builder.SUBDIRS = [""]
        Builder.FILE_EXTENSION = self._path
        self._performers = [
            home.Performer(
                "presa 1", home.appliance.light.Appliance("presa 1", []), [], []
            ),
            home.Performer(
                "presa 2", home.appliance.light.Appliance("presa 2", []), [], []
            ),
        ]
        return []

    def test_builder(self):
        b = Builder(self.get_temporary_dir(), self._performers)
        group_of_performers = b.run()
        self.assertIn("prese muro", group_of_performers)
        self.assertEqual(len(group_of_performers["prese muro"]), 2)
