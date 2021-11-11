# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging


class Client(object):

    PREFIX = "Appliance"

    def __init__(self, appliance, storage_connection, pubsub_connection):
        self._storage_connection = storage_connection
        self._pubsub_connection = pubsub_connection
        self._appliance = appliance
        self._id = "{} {}".format(self.PREFIX, self._appliance.name)

        self._logger = logging.getLogger(__name__)

    async def subscribe(self):
        await self._pubsub_connection.subscribe(self._id)

    def _update(self, new_appliance):
        if new_appliance:
            if not hasattr(new_appliance, "events"):
                self._logger.error(
                    "new_appliance: {} not correctly serialized".format(new_appliance)
                )
            else:
                for event in new_appliance.events_disabled:
                    self._appliance.enable(event)
                    self._appliance.notify(event)
                    self._appliance.disable(event)
                for event in new_appliance.events:
                    if not self._appliance.is_notified(event):
                        self._appliance.notify(event)

    async def notify(self, appliance):
        await self._pubsub_connection.write(self._id, appliance)

    async def save(self, appliance):
        await self._storage_connection.set(self._id, appliance)

    async def update(self):
        appliance = await self._storage_connection.get(self._id)
        self._update(appliance)
        return self._appliance

    async def get_history(self, num_of_events):
        history = await self._storage_connection.get_history(self._id, num_of_events)
        return history

    async def run(self, on_appliance_updated):
        appliance = await self._storage_connection.get(self._id)
        self._update(appliance)
        while True:
            appliance = await self._pubsub_connection.read(self._id)
            await on_appliance_updated(appliance)
