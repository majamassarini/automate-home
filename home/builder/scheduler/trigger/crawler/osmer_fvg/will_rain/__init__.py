# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.builder.scheduler.trigger import Builder as Parent


class Builder(Parent):
    def _get_kwargs(self, mapping):
        name = mapping["name"]
        events = mapping["notify more events"]
        url = mapping["url"] if "url" in mapping else None
        zone = mapping["zone"] if "zone" in mapping else None
        probability = mapping["probability"] if "probability" in mapping else None
        return {
            "name": name,
            "events": events,
            "url": url,
            "zone": zone,
            "probability": probability,
        }

    def _run(self, mapping, group_of_performers):
        kwargs = self._get_kwargs(mapping)
        return [self.trigger(**kwargs)]


from home.builder.scheduler.trigger.crawler.osmer_fvg.will_rain import on
from home.builder.scheduler.trigger.crawler.osmer_fvg.will_rain import off
