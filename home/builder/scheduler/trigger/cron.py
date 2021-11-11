# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger import Builder as Parent
from home.scheduler.trigger.cron import Trigger


class Builder(Parent):
    TAG_NAME = "cron.Trigger"

    @property
    def trigger(self):
        return Trigger

    def _run(self, mapping, group_of_performers):
        """
        >>> import home
        >>> map = {
        ... "name": "giorni feriali wakeup time 1",
        ... "notify events": [home.event.sleepiness.Event.Awake],
        ... "day_of_week": "mon-fri",
        ... "hour": "7",
        ... "minute": "15",
        ... "month": "2-11"}
        >>> l = home.builder.scheduler.trigger.cron.Builder()._run(map, [])
        >>> len(l)
        1
        """
        year = mapping["year"] if "year" in mapping else None
        month = mapping["month"] if "month" in mapping else None
        day = mapping["day"] if "day" in mapping else None
        week = mapping["week"] if "week" in mapping else None
        day_of_week = mapping["day_of_week"] if "day_of_week" in mapping else None
        hour = mapping["hour"] if "hour" in mapping else None
        minute = mapping["minute"] if "minute" in mapping else None
        second = mapping["second"] if "second" in mapping else None
        start_date = mapping["start_date"] if "start_date" in mapping else None
        end_date = mapping["end_date"] if "end_date" in mapping else None
        timezone = mapping["timezone"] if "timezone" in mapping else None
        kwargs = {
            "year": year,
            "month": month,
            "day": day,
            "week": week,
            "day_of_week": day_of_week,
            "hour": hour,
            "minute": minute,
            "second": second,
            "start_date": start_date,
            "end_date": end_date,
            "timezone": timezone,
        }
        return [
            self.trigger(
                name=mapping["name"], events=mapping["notify events"], **kwargs
            )
        ]
