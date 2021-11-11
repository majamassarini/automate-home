# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import os

import home.appliance
import yaml
from home.builder import Builder as Parent


class Builder(Parent):

    FILE_NAME = "appliances.yaml"

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

        for tag in home.appliance.registry:
            yaml.add_constructor("!{}".format(tag), self.appliance_constructor)
        yaml.add_constructor("!Appliances", self.appliances_constructor)
        appliances = {}
        with open(os.path.join(self._yaml_dir, self.FILE_NAME), mode="r") as stream:
            appliances = yaml.load(stream, Loader=yaml.Loader)
        return appliances

    def appliance_constructor(self, loader, node):
        mapping = loader.construct_mapping(node, deep=True)
        klass = Builder._get_klass(home.appliance, node.tag[1:])
        appliance = klass(**mapping)
        return appliance

    def appliances_constructor(self, loader, node):
        mapping = loader.construct_mapping(node, deep=True)
        appliances = home.appliance.Collection()
        for key, value in mapping.items():
            appliances[key] = list(value)
        return appliances
