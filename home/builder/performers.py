# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import sys
import logging

import home.protocol
import yaml
from home import Performer
from home.builder import Builder as Parent


class Empty(home.appliance.State):
    def init_callables(self):
        pass

    def forced_enum(self):
        return home.Event


class Unknown(home.appliance.Appliance):
    def _init_state(self):
        return Empty()


class NoDetailYamlPerformer(yaml.YAMLObject, dict):

    yaml_tag = u"!Performer"

    def __init__(self, name, appliance_name):
        self.name = name
        self.for_appliance = appliance_name
        self.commands = []
        self.triggers = []
        self._logger = logging.getLogger(__name__)

    def __repr__(self):
        return "{}(name={}, for appliance={}, commands={}, triggers={})".format(
            self.__class__.__name__,
            self.name,
            self.for_appliance.name,
            self.commands,
            self.triggers,
        )


class Builder(Parent):

    SUBDIRS = ["performer"]
    FILE_EXTENSION = ".yaml"

    def __init__(self, yaml_dir, appliances):
        super(Builder, self).__init__(yaml_dir)

        self._appliances = appliances

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

        for tag in home.protocol.message.registry:
            yaml.add_constructor("!{}".format(tag), self.message_constructor)
        yaml.add_constructor(
            "!Performer", lambda loader, node: self.performer_constructor(loader, node)
        )
        performers = list()
        for performers_ in self.find_in_dirs(
            self._yaml_dir, self.SUBDIRS, self.FILE_EXTENSION
        ):
            performers.extend(performers_)
        return performers

    def message_constructor(self, loader, node):
        mapping = loader.construct_mapping(node, deep=True)
        klass = Builder._get_klass(sys.modules, node.tag[1:])
        try:
            return klass.make_from_yaml(**mapping)
        except Exception as e:
            raise e

    def _performer_constructor(self, loader, node, empty=False):
        try:
            mapping = loader.construct_mapping(node, deep=True)
        except yaml.constructor.ConstructorError as e:
            self._logging.error(e)
            return Performer("unknown performer", Unknown("appliance"), [], [])
        try:
            appliance = self._appliances.find(mapping["for appliance"])
        except KeyError as e:
            self._logging.error(e)
            return Performer(mapping["name"], Unknown("appliance"), [], [])
        if empty:
            return Performer(mapping["name"], appliance, [], [])
        else:
            return Performer(
                mapping["name"], appliance, mapping["commands"], mapping["triggers"]
            )

    def performer_constructor(self, loader, node):
        return self._performer_constructor(loader, node, empty=False)

    def dump(self, filename):
        nodetail_yaml_performers = [
            NoDetailYamlPerformer(performer.name, performer.appliance.name)
            for performer in self.run()
        ]
        with open(filename, "w") as outfile:
            data = yaml.dump(nodetail_yaml_performers, default_flow_style=False)
            data = data.replace("for_appliance", "for appliance")
            outfile.write(data)
            outfile.flush()
