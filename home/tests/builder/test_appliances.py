# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.builder.appliances import Builder
from home.tests.builder.test_helper import Helper


class TestPerfomersBuilder(Helper):

    DATA = """
        !Appliances
         Tapparelle:
         - !curtain.outdoor.Appliance {name: "porta-finestra studio", events: []}
         - !curtain.outdoor.Appliance {name: "finestra studio", events: []}
         Luci:
         - !light.Appliance {name: "presa 1 primo piano salotto tv", events: []}
        """

    def _builder_fix(self):
        Builder.FILE_NAME = self._path
        return []

    def test_builder(self):
        b = Builder("")
        appliances = b.run()
        self.assertIn("Luci", appliances)
        self.assertIn("Tapparelle", appliances)
        self.assertEqual(len(appliances["Luci"]), 1)
        self.assertEqual(len(appliances["Tapparelle"]), 2)
        self.assertIsInstance(appliances.find("finestra studio"), home.Appliance)
