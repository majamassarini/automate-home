# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.event import alarm
from home.event import clima
from home.event import courtesy
from home.event import holiday
from home.event import motion
from home.event import power
from home.event import rain
from home.event import scene
from home.event import show
from home.event import sleepiness
from home.event import sun
from home.event import temperature
from home.event import wind
from home.event import enable
from home.event import presence
from home.event import waveform
from home.event import elapsed
from home.event import user
from home.event import toggle
from home.event.enumeration import Enum
from home.event.enumeration import registry

from typing import TypeVar

Event = TypeVar(
    int,
    float,
    str,
    "home.Enum",
    "home.appliance.light.event.hue.Event",
    "home.appliance.light.event.brightness.Event",
    "home.appliance.light.event.saturation.Event",
    "home.appliance.light.event.temperature.Event",
    "home.appliance.light.show.cycles.Event",
    "home.appliance.light.show.ending_brightness.Event",
    "home.appliance.light.show.ending_hue.Event",
    "home.appliance.light.show.period.Event",
    "home.appliance.light.show.starting_brightness.Event",
    "home.appliance.light.show.starting_hue.Event",
    "home.appliance.light.event.lux_balancing.brightness.Event",
    "home.appliance.light.event.circadian_rhythm.brightness.Event",
    "home.appliance.light.event.circadian_rhythm.hue.Event",
    "home.appliance.light.event.circadian_rhythm.saturation.Event",
    "home.appliance.light.event.circadian_rhythm.temperature.Event",
    "home.appliance.sound.player.event.volume.Event",
    "home.appliance.sound.player.event.sleepy_volume.Event",
    "home.appliance.sound.player.event.playlist.Event",
    "home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event",
    "home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event",
    "home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event",
    "home.appliance.sound.player.event.fade_in.volume.Event",
    "home.appliance.sound.player.event.fade_in.playlist.Event",
    "home.appliance.sound.player.event.fade_out.volume.Event",
    "home.appliance.sound.player.event.fade_out.playlist.Event",
)
