# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import logging
import sys
import unittest
import home
from unittest.mock import AsyncMock
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class TestCase(unittest.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.scheduler = None
        self.process = None
        self.counter = 0

    async def fake_connect(self):
        await asyncio.sleep(0.1)

    def make_process(self, myhome):
        redis_gateway = home.redis.Gateway(
            None,
            None,
            home.redis.gateway.serialization.Encoder,
            home.redis.gateway.serialization.Decoder().run,
            myhome.appliances,
            myhome.performers,
            home.redis.gateway.client.storage.Stub,
            home.redis.gateway.client.pubsub.Stub,
            "my node",
            ["other node", "another node"],
        )
        redis_gateway.connect = AsyncMock()
        self.process = home.Process(myhome, redis_gateway)

    def create_tasks(self, loop, myhome):
        self.scheduler = AsyncIOScheduler()
        myhome.schedule(self.scheduler, self.process.schedule)
        self.process.create_tasks(loop, self.scheduler)

    def enable_logging(self):
        for name in ("asyncio", "knx_stack", "knx_plugin", "home"):
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(logging.StreamHandler(sys.stdout))


class Description(home.protocol.Description):

    NAME = "A name for description"

    def __init__(self, description=None):
        super(Description, self).__init__(description)
        self._name = self.NAME
        self._label = self._name

    @classmethod
    def make_from_yaml(cls):
        return cls()

    @classmethod
    def make_from(cls, msg):
        return cls()

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Trigger(home.protocol.Trigger, Description):

    NAME = "A name for trigger"

    def __init__(self, description=None):
        super(Trigger, self).__init__(description)

    def is_triggered(self, another_description):
        return False


class Command(home.protocol.Command, Description):

    NAME = "A name for command"

    def __init__(self, description=None):
        super(Command, self).__init__(description)

    def make_msgs_from(self, old_state, new_state):
        return []

    def execute(self):
        return []
