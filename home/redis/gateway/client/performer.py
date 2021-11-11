# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging


class Client(object):

    PREFIX = "Performer"

    def __init__(self, performer, storage_connection, pubsub_connection):
        self._storage_connection = storage_connection
        self._pubsub_connection = pubsub_connection
        self._performer = performer
        self._id = "{} {}".format(self.PREFIX, self._performer.name)

        self._logger = logging.getLogger(__name__)

    async def subscribe(self):
        await self._pubsub_connection.subscribe(self._id)

    async def notify(self, performer, old_state, new_state):
        obj = {"performer": performer, "old_state": old_state, "new_state": new_state}
        await self._pubsub_connection.write(self._id, obj)

    async def run(self, on_performer_updated):
        while True:
            obj = await self._pubsub_connection.read(self._id)
            if obj:
                await on_performer_updated(
                    obj["performer"], obj["old_state"], obj["new_state"]
                )
