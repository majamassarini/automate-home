# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import logging
import json

import redis.asyncio as aioredis


class Connection(object):
    def __init__(
        self, host, port, encoder, decoder, my_node_name, other_nodes_names
    ):
        self._host = host
        self._port = port
        self._encoder = encoder
        self._decoder = decoder
        self._other_nodes_names = other_nodes_names
        self._my_node_name = my_node_name

        self._publisher = None
        self._subscriptions = dict()
        self._pubsubs = (
            dict()
        )  # one PubSub per other-node, shared across all channels
        self._queues = dict()  # one asyncio.Queue per subscribed channel

        self._logger = logging.getLogger(__name__)

    async def connect(self):
        self._publisher = aioredis.Redis(
            host=self._host, port=self._port, decode_responses=True
        )
        for other_node_name in self._other_nodes_names:
            connection = aioredis.Redis(
                host=self._host, port=self._port, decode_responses=True
            )
            self._subscriptions[other_node_name] = connection
            self._pubsubs[other_node_name] = connection.pubsub()

    async def disconnect(self):
        for pubsub in self._pubsubs.values():
            await pubsub.aclose()
        for connection in self._subscriptions.values():
            await connection.aclose()
        if self._publisher:
            await self._publisher.aclose()

    async def subscribe(self, channel):
        self._queues[channel] = asyncio.Queue()
        for other_node_name, pubsub in self._pubsubs.items():
            await pubsub.subscribe(
                "{} from {}".format(channel, other_node_name)
            )
            self._logger.debug(
                "subscribed channel {} for subscription {}".format(
                    channel, other_node_name
                )
            )

    async def dispatch(self):
        while True:
            for other_node_name, pubsub in self._pubsubs.items():
                msg = await pubsub.get_message(
                    ignore_subscribe_messages=True, timeout=0.1
                )
                if msg:
                    raw_channel = msg["channel"]
                    suffix = " from {}".format(other_node_name)
                    if raw_channel.endswith(suffix):
                        channel = raw_channel[: -len(suffix)]
                        if channel in self._queues:
                            data = msg["data"]
                            obj = json.loads(data, object_hook=self._decoder)
                            self._logger.debug(
                                "read {} from channel {}".format(
                                    data, raw_channel
                                )
                            )
                            await self._queues[channel].put(obj)

    async def read(self, channel):
        return await self._queues[channel].get()

    async def write(self, channel, data):
        if data:
            msg = json.dumps(data, cls=self._encoder)
            if self._publisher:
                await self._publisher.publish(
                    "{} from {}".format(channel, self._my_node_name), msg
                )
                self._logger.debug(
                    "written {} to channel {}".format(msg, channel)
                )
            else:
                self._logger.warning("Redis publisher not ready yet")


class Stub(Connection):
    async def dispatch(self):
        await asyncio.sleep(86400)

    async def read(self, channel):
        self._logger.debug("read nothing on redis stub")
        await asyncio.sleep(86400)  # one day
        return json.loads("", object_hook=self._decoder)

    async def write(self, channel, data):
        msg = json.dumps(data, cls=self._encoder)
        self._logger.debug("written {}".format(str(msg)))
