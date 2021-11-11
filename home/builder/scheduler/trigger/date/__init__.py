# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger import Builder as Parent
from home.scheduler.trigger.date import Trigger


class Builder(Parent):
    TAG_NAME = "date.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _get_kwargs(self, mapping):
        run_date = mapping["run_date"]
        timezone = mapping["timezone"] if "timezone" in mapping else None
        return {"run_date": run_date, "timezone": timezone}

    def _run(self, mapping, group_of_performers):
        kwargs = self._get_kwargs(mapping)
        return [self.trigger(**kwargs)]


from home.builder.scheduler.trigger.date import resettable
