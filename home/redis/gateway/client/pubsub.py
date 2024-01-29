# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import logging
import json
import aioredis


class Connection(object):
    def __init__(self, host, port, encoder, decoder, my_node_name, other_nodes_names):
        self._host = host
        self._port = port
        self._encoder = encoder
        self._decoder = decoder
        self._other_nodes_names = other_nodes_names
        self._my_node_name = my_node_name

        self._publisher = None
        self._subscriptions = dict()
        self._channels = dict()

        self._logger = logging.getLogger(__name__)

    async def connect(self):
        self._publisher = await aioredis.create_redis(
            address=(self._host, self._port), encoding="utf-8"
        )
        for other_node_name in self._other_nodes_names:
            self._subscriptions[other_node_name] = await aioredis.create_redis(
                address=(self._host, self._port), encoding="utf-8"
            )

    async def disconnect(self):
        for subscription in self._subscriptions.values():
            subscription.close()
        if self._publisher:
            self._publisher.close()

    async def subscribe(self, channel):
        self._channels[channel] = list()
        for other_node_name, subscription in self._subscriptions.items():
            channel_subscription = await subscription.subscribe(
                "{} from {}".format(channel, other_node_name)
            )
            self._logger.debug(
                "subscribed channel {} for subscription {}".format(
                    channel, other_node_name
                )
            )
            self._channels[channel].append(channel_subscription)

    async def read(self, channel):
        for channel_subscription in self._channels[channel]:
            while await channel_subscription[0].wait_message():
                data = await channel_subscription[0].get(encoding="utf-8")
                if data:
                    msg = json.loads(data, object_hook=self._decoder)
                    self._logger.debug("read {} from channel {}".format(data, channel))
                    return msg

    async def write(self, channel, data):
        if data:
            msg = json.dumps(data, cls=self._encoder)
            if self._publisher:
                await self._publisher.publish(
                    "{} from {}".format(channel, self._my_node_name), msg
                )
                self._logger.debug("written {} to channel {}".format(msg, channel))
            else:
                self._logger.warning("Redis publisher not ready yet")


class Stub(Connection):
    async def read(self, channel):
        self._logger.debug("read nothing on redis stub")
        await asyncio.sleep(86400)  # one day
        return json.loads("", object_hook=self._decoder)

    async def write(self, channel, data):
        msg = json.dumps(data, cls=self._encoder)
        self._logger.debug("written {}".format(str(msg)))
