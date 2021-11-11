# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger import Builder as Parent
from home.scheduler.trigger.interval import Trigger


class Builder(Parent):
    TAG_NAME = "interval.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _run(self, mapping, group_of_performers):
        weeks = mapping["weeks"] if "weeks" in mapping else 0
        days = mapping["days"] if "days" in mapping else 0
        hours = mapping["hours"] if "hours" in mapping else 0
        minutes = mapping["minutes"] if "minutes" in mapping else 0
        seconds = mapping["seconds"] if "seconds" in mapping else 0
        start_date = mapping["start_date"] if "start_date" in mapping else None
        end_date = mapping["end_date"] if "end_date" in mapping else None
        timezone = mapping["timezone"] if "timezone" in mapping else None
        kwargs = {
            "weeks": weeks,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "start_date": start_date,
            "end_date": end_date,
            "timezone": timezone,
        }
        return [
            self.trigger(
                name=mapping["name"], events=mapping["notify events"], **kwargs
            )
        ]
