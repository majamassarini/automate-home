# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import os
import sys
import copy
import logging

import yaml

from abc import ABC, abstractmethod


class Builder(ABC):
    def __init__(self, yaml_dir, *args, **kwargs):
        self._yaml_dir = yaml_dir
        self._logging = logging.getLogger(__name__)

    @abstractmethod
    def run(self):
        pass

    def find_in_dirs(self, yaml_dir, subdirs, extension):
        dirs = copy.copy(subdirs)
        while dirs:
            dir_name = dirs.pop()
            try:
                for file_name in os.listdir(os.path.join(yaml_dir, dir_name)):
                    path = os.path.join(yaml_dir, dir_name, file_name)
                    if os.path.isdir(path):
                        dirs.append(os.path.join(dir_name, file_name))
                    elif path.endswith(extension):
                        with open(path, mode="r") as stream:
                            yield yaml.load(stream, Loader=yaml.Loader)
            except PermissionError as e:
                self._logging.error(str(e))

    @staticmethod
    def _get_klass(root_space, klass_name):
        namespace = klass_name.split(".")
        space = root_space
        for name in namespace:
            try:
                space = getattr(space, name)
            except AttributeError:
                space = space[name]
        return space

    def data_constructor(self, prefix, loader, node):
        klass = Builder._get_klass(prefix, node.tag[1:])
        mapping = loader.construct_mapping(node, deep=True)
        try:
            return klass(**mapping)
        except TypeError as e:
            raise e

    def event_constructor(self, loader, node):
        namespace = node.tag[1:].split(".")
        space = sys.modules[namespace[0]]
        for name in namespace[1:]:
            try:
                space = getattr(space, name)
            except Exception as e:
                log = logging.getLogger(__name__)
                log.error(str(e))
        return space


from home.builder import appliances
from home.builder import group_of_performers
from home.builder import my_home
from home.builder import performers
from home.builder import schedule_infos
from home.builder import scheduler_triggers
from home.builder import listener
from home.builder import scheduler
