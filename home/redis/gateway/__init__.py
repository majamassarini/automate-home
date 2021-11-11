# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import asyncio

from home.redis.gateway import serialization
from home.redis.gateway import client as c


class Gateway(object):
    def __init__(
        self,
        host,
        port,
        encoder,
        decoder,
        appliances,
        performers,
        storage_client,
        pubsub_client,
        my_node_name,
        other_nodes_names,
    ):
        self._storage_connection = storage_client(host, port, encoder, decoder)
        self._pubsub_connection = pubsub_client(
            host, port, encoder, decoder, my_node_name, other_nodes_names
        )
        self._host = host
        self._port = port
        self._my_node_name = my_node_name
        self._other_nodes_names = other_nodes_names

        self._appliances = {
            appliance: c.appliance.Client(
                appliance, self._storage_connection, self._pubsub_connection
            )
            for collections in appliances.values()
            for appliance in collections
        }
        self._performers = {
            performer: c.performer.Client(
                performer, self._storage_connection, self._pubsub_connection
            )
            for performer in performers
        }

    async def connect(self):
        await self._storage_connection.connect()
        await self._pubsub_connection.connect()
        for appliance in self._appliances.values():
            await appliance.subscribe()
        for performer in self._performers.values():
            await performer.subscribe()

    async def disconnect(self):
        await self._storage_connection.disconnect()
        await self._pubsub_connection.disconnect()

    def _get_client(self, obj):
        client = None
        if obj in self._appliances:
            client = self._appliances[obj]
        elif obj in self._performers:
            client = self._performers[obj]

        return client

    async def save(self, obj):
        client = self._get_client(obj)
        if client:
            await client.save(obj)

    async def update(self, obj):
        client = self._get_client(obj)
        if client:
            await client.update()

    async def notify(self, obj, *args, **kwargs):
        client = self._get_client(obj)
        if client:
            await client.notify(obj, *args, **kwargs)

    async def get_history(self, obj, num_of_events):
        client = self._get_client(obj)
        history = await client.get_history(num_of_events)
        return history

    async def on_appliance_updated_by_process(self, appliance, old_state, new_state):
        if old_state != new_state:
            await self.save(appliance)
            await self.notify(appliance)

    async def on_performer_updated_by_process(self, performer, old_state, new_state):
        if old_state != new_state:
            await self.save(performer.appliance)
            await self.notify(performer.appliance)
            # await self.notify(performer, old_state, new_state)

    def create_tasks(
        self, loop, on_appliance_updated_by_redis, on_performer_updated_by_redis
    ):
        for client in self._appliances.values():
            asyncio.get_event_loop().create_task(
                client.run(on_appliance_updated_by_redis)
            )
        for client in self._performers.values():
            asyncio.get_event_loop().create_task(
                client.run(on_performer_updated_by_redis)
            )
