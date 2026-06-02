# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import logging
import json
import time

import redis.asyncio as aioredis


class Connection(object):
    def __init__(self, host, port, encoder, decoder):
        self._host = host
        self._port = port
        self._encoder = encoder
        self._decoder = decoder
        self._connection = None

        self._logger = logging.getLogger(__name__)

    async def connect(self):
        self._connection = aioredis.Redis(
            host=self._host,
            port=self._port,
            decode_responses=True,
            max_connections=200,
        )

    async def disconnect(self):
        if self._connection:
            await self._connection.aclose()

    async def get(self, key):
        if self._connection:
            serializations = await self._connection.zrange(key, -1, -1)
            for entry in serializations:
                serialization = entry[entry.find(":") + 1 :]
                obj = json.loads(serialization, object_hook=self._decoder)
                self._logger.debug("get key {} -> {}".format(key, obj))
                return obj
        else:
            self._logger.warning("Redis connection not ready yet")

    async def get_history(self, key, num_of_events):
        if self._connection:
            serializations = await self._connection.zrange(
                key, -num_of_events, -1
            )
            history = list()
            for entry in serializations:
                colon = entry.find(":")
                t = entry[0:colon]
                serialization = entry[colon + 1 :]
                deserialization = json.loads(
                    serialization, object_hook=self._decoder
                )
                history.append((t, deserialization))
            history.reverse()
            self._logger.debug(
                "get_history for key {} -> {}".format(key, history)
            )
            return history
        else:
            self._logger.warning("Redis connection not ready yet")

    async def get_history_range(self, key, start_ts: float, end_ts: float):
        if self._connection:
            serializations = await self._connection.zrange(key, 0, -1)
            history = []
            for entry in serializations:
                colon = entry.find(":")
                try:
                    t = float(entry[0:colon])
                except ValueError:
                    continue
                if start_ts <= t <= end_ts:
                    serialization = entry[colon + 1 :]
                    deserialization = json.loads(
                        serialization, object_hook=self._decoder
                    )
                    history.append((entry[0:colon], deserialization))
            history.reverse()
            return history
        else:
            self._logger.warning("Redis connection not ready yet")
            return []

    async def set(self, key, obj):
        if self._connection:
            if obj:
                s = json.dumps(obj, cls=self._encoder)
                entry = "{}:{}".format(time.time(), s)
                await self._connection.zadd(key, {entry: 0})
                self._logger.debug("set key {} -> {}".format(key, entry))
        else:
            self._logger.warning("Redis connection not ready yet")


class Stub(Connection):
    async def get(self, key):
        self._logger.debug("read nothing on redis stub")
        await asyncio.sleep(86400)  # one day
        return json.loads("", object_hook=self._decoder)

    async def set(self, key, obj):
        s = json.dumps(obj, cls=self._encoder)
        entry = "{}:{}".format(time.time(), s)
        self._logger.debug("set key {} -> {}".format(key, entry))
