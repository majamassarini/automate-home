# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio
import logging
import json
import time

import aioredis


class Connection(object):
    def __init__(self, host, port, encoder, decoder):
        self._host = host
        self._port = port
        self._encoder = encoder
        self._decoder = decoder
        self._connection = None

        self._logger = logging.getLogger(__name__)

    async def connect(self):
        self._connection = await aioredis.create_connection((self._host, self._port))

    async def disconnect(self):
        if self._connection:
            self._connection.close()

    async def get(self, key):
        if self._connection:
            serializations = await self._connection.execute(
                "zrange", key, -1, -1, encoding="utf-8"
            )
            for entry in serializations:
                serialization = entry[entry.find(":") + 1 :]
                obj = json.loads(serialization, object_hook=self._decoder)
                self._logger.debug("get key {} -> {}".format(key, obj))
                return obj
        else:
            self._logger.warning("Redis connection not ready yet")

    async def get_history(self, key, num_of_events):
        if self._connection:
            serializations = await self._connection.execute(
                "zrange", key, -num_of_events, -1, encoding="utf-8"
            )
            history = list()
            for entry in serializations:
                entry.find(":")
                colon = entry.find(":")
                t = entry[0:colon]
                serialization = entry[colon + 1 :]
                deserialization = json.loads(serialization, object_hook=self._decoder)
                history.append((t, deserialization))
            history.reverse()
            self._logger.debug("get_history for key {} -> {}".format(key, history))
            return history
        else:
            self._logger.warning("Redis connection not ready yet")

    async def set(self, key, obj):
        if self._connection:
            if obj:
                s = json.dumps(obj, cls=self._encoder)
                entry = "{}:{}".format(time.time(), s)
                await self._connection.execute("zadd", key, 0, entry)
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
