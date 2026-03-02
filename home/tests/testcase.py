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
    """
    Base class for integration tests that involve a :py:class:`Process`
    and an ``AsyncIOScheduler``.

    Provides helpers to wire up a minimal in-process home with stub Redis
    and protocol gateways so that the full event-routing pipeline can be
    exercised in unit tests.
    """

    def setUp(self):
        super(TestCase, self).setUp()
        self.scheduler = None
        self.process = None
        self.counter = 0

    async def fake_connect(self):
        """Stub coroutine that simulates a short connection delay."""
        await asyncio.sleep(0.1)

    def make_process(self, myhome):
        """
        Create a :py:class:`Process` backed by stub Redis gateways.

        The Redis ``connect`` coroutine is replaced with an
        :py:class:`~unittest.mock.AsyncMock` so no real Redis server is
        needed.

        :param myhome: the :py:class:`MyHome` instance under test
        """
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
        """
        Create a fresh ``AsyncIOScheduler``, register all
        ``(performer, trigger)`` jobs, and start the process tasks.

        Must be called from within a running event loop, typically from
        ``asyncSetUp`` of an inner :py:class:`unittest.IsolatedAsyncioTestCase`.

        :param loop: the currently running :py:class:`asyncio.AbstractEventLoop`
        :param myhome: the :py:class:`MyHome` instance under test
        """
        self.scheduler = AsyncIOScheduler()
        myhome.schedule(self.scheduler, self.process.schedule)
        self.process.create_tasks(loop, self.scheduler)

    def enable_logging(self):
        """
        Enable ``DEBUG``-level logging for the home framework and related
        libraries, writing to ``stdout``.

        Useful when debugging a failing test.
        """
        for name in ("asyncio", "knx_stack", "knx_plugin", "home"):
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(logging.StreamHandler(sys.stdout))


class Description(home.protocol.Description):
    """
    Minimal :py:class:`home.protocol.Description` stub for tests.

    All instances with the same :py:attr:`NAME` compare as equal and
    share the same hash, so they can be used as dictionary keys in the
    performer lookup tables.
    """

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
    """
    Minimal :py:class:`home.protocol.Trigger` stub for tests.

    :py:meth:`is_triggered` always returns ``False``; subclasses in
    individual test modules override it to simulate specific bus events.
    """

    NAME = "A name for trigger"

    def __init__(self, description=None):
        super(Trigger, self).__init__(description)

    def is_triggered(self, another_description):
        return False


class Command(home.protocol.Command, Description):
    """
    Minimal :py:class:`home.protocol.Command` stub for tests.

    Both :py:meth:`make_msgs_from` and :py:meth:`execute` return empty
    lists, so no real protocol messages are produced during tests.
    """

    NAME = "A name for command"

    def __init__(self, description=None):
        super(Command, self).__init__(description)

    def make_msgs_from(self, old_state, new_state):
        return []

    def execute(self):
        return []
