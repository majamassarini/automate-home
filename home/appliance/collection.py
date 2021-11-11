# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini


class Collection(dict):
    """
    >>> class Appliance(object):
    ...     def __init__(self, name):
    ...         self.name = name
    ...     def __repr__(self):
    ...         return self.name+" object"

    >>> collections = Collection()
    >>> collections["pippoli"] = list([Appliance("pip"), Appliance("poli")])
    >>> collections["boboli"] = list([Appliance("bo"), Appliance("boli")])
    >>> collections.find("bo")
    bo object
    >>> collections.find("pip")
    pip object
    """

    def __init__(self, *args, **kwargs):
        super(Collection, self).__init__(self, *args, **kwargs)
        self._appliances = {}
        for collection in self:
            self._update_appliances(self[collection])

    def __setitem__(self, name, collection):
        super(Collection, self).__setitem__(name, collection)
        self._update_appliances(collection)

    def _update_appliances(self, collection):
        for appliance in collection:
            self._appliances[appliance.name] = appliance

    def find(self, name):
        return self._appliances[name]

    def collection_for(self, appliance):
        for name, collection in self.items():
            if appliance in collection:
                return name
