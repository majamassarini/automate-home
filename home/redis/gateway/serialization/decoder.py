# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.redis.gateway.serialization import (
    enumeration,
    appliance,
    performer,
    brightness,
    hue,
    temperature,
    saturation,
    circadian_rhythm,
    lux_balancing,
    show,
    volume,
    sleepy_volume,
    playlist,
    fade_in,
    fade_out,
    duration,
    partially_on,
    state,
    setpoint,
    keep,
)


class Decoder:
    def __init__(self):
        self._events_deserializers = {
            d.key: d.run
            for d in [
                brightness.Deserializer(),
                circadian_rhythm.brightness.Deserializer(),
                lux_balancing.brightness.Deserializer(),
                show.starting_brightness.Deserializer(),
                show.ending_brightness.Deserializer(),
                hue.Deserializer(),
                circadian_rhythm.hue.Deserializer(),
                show.starting_hue.Deserializer(),
                show.ending_hue.Deserializer(),
                saturation.Deserializer(),
                circadian_rhythm.saturation.Deserializer(),
                show.starting_saturation.Deserializer(),
                show.ending_saturation.Deserializer(),
                temperature.Deserializer(),
                circadian_rhythm.temperature.Deserializer(),
                show.cycles.Deserializer(),
                show.period.Deserializer(),
                volume.Deserializer(),
                sleepy_volume.Deserializer(),
                fade_in.volume.Deserializer(),
                fade_out.volume.Deserializer(),
                playlist.Deserializer(),
                circadian_rhythm.playlist_a.Deserializer(),
                circadian_rhythm.playlist_b.Deserializer(),
                circadian_rhythm.playlist_c.Deserializer(),
                fade_in.playlist.Deserializer(),
                fade_out.playlist.Deserializer(),
                duration.Deserializer(),
                partially_on.duration.Deserializer(),
                setpoint.Deserializer(),
                keep.setpoint.Deserializer(),
            ]
        }

        self._performer = performer.Deserializer()
        self._appliance = appliance.Deserializer()
        self._state = state.Deserializer()
        self._enumeration = enumeration.Deserializer()

    def run(self, serialization):
        try:
            return self._events_deserializers[[k for k in serialization.keys()][0]](
                serialization
            )
        except KeyError:
            pass

        if self._appliance.check(serialization):
            return self._appliance.run(serialization)
        elif self._enumeration.check(serialization):
            return self._enumeration.run(serialization)
        elif self._state.check(serialization):
            return self._state.run(serialization)
        elif self._performer.check(serialization):
            return self._performer.run(serialization)
        else:
            return serialization
