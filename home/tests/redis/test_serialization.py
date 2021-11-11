# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import json
import unittest

import home


class TestSerialization(unittest.TestCase):
    def setUp(self):
        super(TestSerialization, self).setUp()
        self._encoder = home.redis.gateway.serialization.Encoder
        self._decoder = home.redis.gateway.serialization.Decoder().run

    def test_appliances_serializations(self):
        appliances = list()
        appliances.append(home.appliance.curtain.indoor.blackout.Appliance("", []))
        appliances.append(home.appliance.curtain.outdoor.Appliance("", []))
        appliances.append(home.appliance.curtain.outdoor.bedroom.Appliance("", []))
        appliances.append(home.appliance.thermostat.presence.Appliance("", []))
        appliances.append(home.appliance.sensor.alarm.Appliance("", []))
        appliances.append(home.appliance.sensor.anemometer.Appliance("", []))
        appliances.append(home.appliance.sensor.crepuscular.Appliance("", []))
        appliances.append(home.appliance.sensor.luxmeter.Appliance("", []))
        appliances.append(home.appliance.sensor.motion.Appliance("", []))
        appliances.append(home.appliance.sensor.powermeter.Appliance("", []))
        appliances.append(home.appliance.sensor.rainmeter.Appliance("", []))
        appliances.append(home.appliance.sensor.scene.Appliance("", []))
        appliances.append(home.appliance.sensor.thermometer.Appliance("", []))
        appliances.append(home.appliance.light.Appliance("", []))
        appliances.append(home.appliance.light.presence.Appliance("", []))
        appliances.append(home.appliance.light.zone.Appliance("", []))
        appliances.append(home.appliance.light.indoor.dimmerable.Appliance("", []))
        appliances.append(home.appliance.light.indoor.hue.Appliance("", []))
        appliances.append(home.appliance.sound.player.Appliance("", []))
        appliances.append(home.appliance.sprinkler.Appliance("", []))

        for appliance in appliances:
            serialization = json.dumps(appliance, cls=self._encoder)
            a = json.loads(serialization, object_hook=self._decoder)
            self.assertIsInstance(a, home.Appliance)

    def test_curtain_deserialization(self):
        curtain = home.appliance.curtain.outdoor.Appliance("", [])
        serialization = json.dumps(curtain, cls=self._encoder)
        a = json.loads(serialization, object_hook=self._decoder)
        self.assertEqual(a.state.compute(), "Opened")

    def test_hue_deserialization(self):
        hue = home.appliance.light.indoor.hue.Appliance("", [])
        serialization = json.dumps(hue, cls=self._encoder)
        a = json.loads(serialization, object_hook=self._decoder)
        self.assertEqual(a.state.compute(), "Off")

    def test_performer_serialization(self):
        performer = home.Performer("", home.appliance.light.Appliance("", []), [], [])
        serialization = json.dumps(performer, cls=self._encoder)
        p = json.loads(serialization, object_hook=self._decoder)
        self.assertIsInstance(p, home.Performer)

    def test_thermometer_serialization(self):
        state = home.appliance.sensor.thermometer.State()
        state = state.next(-1.6)
        serialization = json.dumps(state, cls=self._encoder)
        s = json.loads(serialization, object_hook=self._decoder)
        self.assertIsInstance(s, home.appliance.State)
