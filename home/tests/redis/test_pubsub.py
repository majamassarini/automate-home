# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

"""Unit tests for home.redis.gateway.client.pubsub.Connection.

Tests focus on the shared-PubSub / asyncio.Queue dispatch design:
- subscribe() creates one Queue per channel and registers it on all
  per-node PubSubs.
- dispatch() strips the " from <node>" suffix, looks up the base channel
  name in _queues, and puts the decoded message there.
- Channels that were never subscribed are silently dropped.
- Messages from multiple other-nodes are each routed to the same queue.
- Two distinct channels never bleed into each other's queue.
"""

import asyncio
import json
import unittest

from home.redis.gateway.client.pubsub import Connection


# ---------------------------------------------------------------------------
# Minimal fakes
# ---------------------------------------------------------------------------


class _FakePubSub:
    """Fake aioredis PubSub that returns a pre-loaded sequence of messages."""

    def __init__(self, messages=()):
        self._iter = iter(messages)
        self.subscribed = []

    async def subscribe(self, channel):
        self.subscribed.append(channel)

    async def get_message(self, *, ignore_subscribe_messages, timeout):
        await asyncio.sleep(
            0
        )  # yield so other tasks can run, mirroring real I/O
        try:
            return next(self._iter)
        except StopIteration:
            return None

    async def aclose(self):
        pass


def _raw(channel, payload):
    """Build a fake Redis pub/sub message dict."""
    return {"channel": channel, "data": json.dumps(payload)}


def _make_conn(other_nodes):
    """Return a Connection without calling connect()."""
    return Connection(
        host="localhost",
        port=6379,
        encoder=None,
        decoder=None,
        my_node_name="me",
        other_nodes_names=other_nodes,
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestSubscribe(unittest.IsolatedAsyncioTestCase):
    async def test_creates_queue(self):
        conn = _make_conn(["n1"])
        ps = _FakePubSub()
        conn._pubsubs["n1"] = ps

        await conn.subscribe("ch")

        self.assertIn("ch", conn._queues)

    async def test_registers_suffixed_channel_on_every_node(self):
        conn = _make_conn(["n1", "n2"])
        ps1, ps2 = _FakePubSub(), _FakePubSub()
        conn._pubsubs["n1"] = ps1
        conn._pubsubs["n2"] = ps2

        await conn.subscribe("lights")

        self.assertIn("lights from n1", ps1.subscribed)
        self.assertIn("lights from n2", ps2.subscribed)

    async def test_each_channel_gets_its_own_queue(self):
        conn = _make_conn(["n1"])
        conn._pubsubs["n1"] = _FakePubSub()

        await conn.subscribe("ch_a")
        await conn.subscribe("ch_b")

        self.assertIsNot(conn._queues["ch_a"], conn._queues["ch_b"])


class TestDispatch(unittest.IsolatedAsyncioTestCase):
    async def _run_dispatch_until(self, conn, queue, timeout=1.0):
        """Run dispatch() as a background task; cancel it after queue gets an item."""
        task = asyncio.create_task(conn.dispatch())
        try:
            item = await asyncio.wait_for(queue.get(), timeout=timeout)
        except asyncio.TimeoutError:
            self.fail("dispatch() did not deliver message within timeout")
        finally:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        return item

    async def test_routes_message_to_correct_queue(self):
        conn = _make_conn(["n1"])
        payload = {"k": "v"}
        conn._pubsubs["n1"] = _FakePubSub([_raw("ch from n1", payload)])
        conn._queues["ch"] = asyncio.Queue()

        item = await self._run_dispatch_until(conn, conn._queues["ch"])

        self.assertEqual(item, payload)

    async def test_other_channel_queue_stays_empty(self):
        conn = _make_conn(["n1"])
        conn._pubsubs["n1"] = _FakePubSub([_raw("ch_a from n1", {"x": 1})])
        conn._queues["ch_a"] = asyncio.Queue()
        conn._queues["ch_b"] = asyncio.Queue()

        await self._run_dispatch_until(conn, conn._queues["ch_a"])

        self.assertEqual(conn._queues["ch_b"].qsize(), 0)

    async def test_unknown_channel_is_dropped(self):
        conn = _make_conn(["n1"])
        payload = {"x": 1}
        conn._pubsubs["n1"] = _FakePubSub([_raw("ghost from n1", payload)])
        conn._queues["known"] = asyncio.Queue()

        task = asyncio.create_task(conn.dispatch())
        await asyncio.sleep(0.2)
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        self.assertNotIn("ghost", conn._queues)
        self.assertEqual(conn._queues["known"].qsize(), 0)

    async def test_messages_from_two_nodes_both_routed(self):
        conn = _make_conn(["n1", "n2"])
        conn._pubsubs["n1"] = _FakePubSub([_raw("ch from n1", {"src": "n1"})])
        conn._pubsubs["n2"] = _FakePubSub([_raw("ch from n2", {"src": "n2"})])
        conn._queues["ch"] = asyncio.Queue()

        task = asyncio.create_task(conn.dispatch())
        received = []
        try:
            for _ in range(2):
                item = await asyncio.wait_for(
                    conn._queues["ch"].get(), timeout=1.0
                )
                received.append(item)
        except asyncio.TimeoutError:
            self.fail("dispatch() did not deliver messages from both nodes")
        finally:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

        self.assertIn({"src": "n1"}, received)
        self.assertIn({"src": "n2"}, received)

    async def test_multiple_messages_on_same_channel(self):
        conn = _make_conn(["n1"])
        conn._pubsubs["n1"] = _FakePubSub(
            [
                _raw("ch from n1", {"i": 0}),
                _raw("ch from n1", {"i": 1}),
                _raw("ch from n1", {"i": 2}),
            ]
        )
        conn._queues["ch"] = asyncio.Queue()

        task = asyncio.create_task(conn.dispatch())
        received = []
        try:
            for _ in range(3):
                item = await asyncio.wait_for(
                    conn._queues["ch"].get(), timeout=1.0
                )
                received.append(item)
        except asyncio.TimeoutError:
            self.fail("dispatch() did not deliver all messages")
        finally:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

        self.assertEqual(received, [{"i": 0}, {"i": 1}, {"i": 2}])


class TestRead(unittest.IsolatedAsyncioTestCase):
    async def test_read_returns_item_placed_by_dispatch(self):
        conn = _make_conn(["n1"])
        payload = {"hello": "world"}
        conn._pubsubs["n1"] = _FakePubSub([_raw("ch from n1", payload)])
        conn._queues["ch"] = asyncio.Queue()

        dispatch_task = asyncio.create_task(conn.dispatch())
        try:
            result = await asyncio.wait_for(conn.read("ch"), timeout=1.0)
        except asyncio.TimeoutError:
            self.fail("read() timed out waiting for dispatched message")
        finally:
            dispatch_task.cancel()
            try:
                await dispatch_task
            except asyncio.CancelledError:
                pass

        self.assertEqual(result, payload)
