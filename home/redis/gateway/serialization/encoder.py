# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import logging
import json

import home
from home.redis.gateway.serialization import (
    performer,
    appliance,
    state,
    enumeration,
    brightness,
    hue,
    temperature,
    saturation,
    volume,
    sleepy_volume,
    playlist,
    circadian_rhythm,
    lux_balancing,
    show,
    fade_in,
    fade_out,
    duration,
    partially_on,
    setpoint,
    keep,
)


class Encoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super(Encoder, self).__init__(*args, **kwargs)
        self._events_serializers = {
            k: v
            for k, v in (
                (home.appliance.light.event.brightness.Event, brightness.Serializer()),
                (
                    home.appliance.light.event.circadian_rhythm.brightness.Event,
                    circadian_rhythm.brightness.Serializer(),
                ),
                (
                    home.appliance.light.event.lux_balancing.brightness.Event,
                    lux_balancing.brightness.Serializer(),
                ),
                (
                    home.appliance.light.event.show.starting_brightness.Event,
                    show.starting_brightness.Serializer(),
                ),
                (
                    home.appliance.light.event.show.ending_brightness.Event,
                    show.ending_brightness.Serializer(),
                ),
                (home.appliance.light.event.hue.Event, hue.Serializer()),
                (
                    home.appliance.light.event.circadian_rhythm.hue.Event,
                    circadian_rhythm.hue.Serializer(),
                ),
                (
                    home.appliance.light.event.show.starting_hue.Event,
                    show.starting_hue.Serializer(),
                ),
                (
                    home.appliance.light.event.show.ending_hue.Event,
                    show.ending_hue.Serializer(),
                ),
                (home.appliance.light.event.saturation.Event, saturation.Serializer()),
                (
                    home.appliance.light.event.circadian_rhythm.saturation.Event,
                    circadian_rhythm.saturation.Serializer(),
                ),
                (
                    home.appliance.light.event.show.starting_saturation.Event,
                    show.starting_saturation.Serializer(),
                ),
                (
                    home.appliance.light.event.show.ending_saturation.Event,
                    show.ending_saturation.Serializer(),
                ),
                (
                    home.appliance.light.event.temperature.Event,
                    temperature.Serializer(),
                ),
                (
                    home.appliance.light.event.circadian_rhythm.temperature.Event,
                    circadian_rhythm.temperature.Serializer(),
                ),
                (
                    home.appliance.light.event.show.cycles.Event,
                    show.cycles.Serializer(),
                ),
                (
                    home.appliance.light.event.show.period.Event,
                    show.period.Serializer(),
                ),
                (home.appliance.sound.player.event.volume.Event, volume.Serializer()),
                (
                    home.appliance.sound.player.event.sleepy_volume.Event,
                    sleepy_volume.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.fade_in.volume.Event,
                    fade_in.volume.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.fade_out.volume.Event,
                    fade_out.volume.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.playlist.Event,
                    playlist.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event,
                    circadian_rhythm.playlist_a.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event,
                    circadian_rhythm.playlist_b.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event,
                    circadian_rhythm.playlist_c.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.fade_in.playlist.Event,
                    fade_in.playlist.Serializer(),
                ),
                (
                    home.appliance.sound.player.event.fade_out.playlist.Event,
                    fade_out.playlist.Serializer(),
                ),
                (home.appliance.sprinkler.event.duration.Event, duration.Serializer()),
                (
                    home.appliance.sprinkler.event.partially_on.duration.Event,
                    partially_on.duration.Serializer(),
                ),
                (
                    home.appliance.thermostat.presence.event.setpoint.Event,
                    setpoint.Serializer(),
                ),
                (
                    home.appliance.thermostat.presence.event.keep.setpoint.Event,
                    keep.setpoint.Serializer(),
                ),
            )
        }
        self._performer = performer.Serializer()
        self._appliance = appliance.Serializer()
        self._state = state.Serializer()
        self._enum = enumeration.Serializer()

    def default(self, obj):
        try:
            return self._events_serializers[type(obj)].run(obj)
        except KeyError:
            pass
        try:
            if isinstance(obj, home.event.Enum):
                return self._enum.run(obj)
            elif isinstance(obj, home.Appliance):
                return self._appliance.run(obj)
            elif isinstance(obj, home.Performer):
                return self._performer.run(obj)
            elif isinstance(obj, home.appliance.State):
                return self._state.run(obj)
            return json.JSONEncoder.default(self, obj)
        except AttributeError as e:
            logging.error(e)
