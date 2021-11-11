# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging
import os
import yaml
import abc

from home import builder
from home import redis


class Builder(builder.performers.Builder):

    PERFORMERS_FILENAME = "performer_for_listeners.yaml"

    def run(self):
        yaml.add_constructor(
            "!Performer", lambda loader, node: self.performer_constructor(loader, node)
        )
        performers = yaml.load(
            open(os.path.join(self._yaml_dir, self.PERFORMERS_FILENAME), mode="r"),
            Loader=yaml.Loader,
        )
        if performers:
            return performers
        else:
            return list()


class EmptyPerformers(builder.performers.Builder):
    def performer_constructor(self, loader, node):
        return self._performer_constructor(loader, node, empty=True)


class MyHome(builder.my_home.Yaml):
    def _build_performers(self):
        return EmptyPerformers(self._yaml_dir, self._appliances).run()

    def _build_scheduler_triggers(self):
        return []

    def _build_schedule_infos(self):
        return []


class Resources(object):
    def __init__(
        self, yaml_dir, redis_host, redis_port, my_node_name, other_nodes_names
    ):
        self._myhome = MyHome(yaml_dir)
        self._brain_home = builder.my_home.Yaml(yaml_dir)
        self._redis_gateway = redis.Gateway(
            redis_host,
            redis_port,
            redis.gateway.serialization.Encoder,
            redis.gateway.serialization.Decoder().run,
            self._myhome.appliances,
            self._myhome.performers,
            redis.gateway.client.storage.Connection,
            redis.gateway.client.pubsub.Connection,
            my_node_name,
            other_nodes_names,
        )
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.json_encoder = redis.gateway.serialization.Encoder

    @property
    def brain_performers(self):
        return self._brain_home.performers

    @property
    def brain_group_of_performers(self):
        return self._brain_home.group_of_performers

    @property
    def brain_scheduler_triggers(self):
        return self._brain_home.scheduler_triggers

    @property
    def brain_schedule_infos(self):
        return self._brain_home.schedule_infos

    @property
    def performers(self):
        return self._myhome.performers

    @property
    def appliances(self):
        return self._myhome.appliances

    @property
    def redis_gateway(self):
        return self._redis_gateway


class OnRedisMsg(abc.ABC):
    def __init__(self, websocket_handler, home_resources):
        self._home_resources = home_resources
        self._websocket_handler = websocket_handler

    async def on_appliance_updated(self, new_appliance):
        ...

    def on_performer_updated(self, performer, old_state, new_state):
        ...
