# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import abstractmethod
from typing import Tuple, Iterable, Callable

import home


def get_event_value(obj):
    return obj.value


def lookup(
    event: type, events: Iterable[Tuple[type, home.event.Event]]
) -> home.event.Event:
    for klass, obj in events:
        if klass == event:
            return klass


def lookup_value(
    event: type, events: Iterable[Tuple[type, home.event.Event]], fun: Callable = None
) -> home.event.Event:
    if not fun:
        fun = get_event_value
    for klass, obj in events:
        if klass == event:
            if obj:
                return fun(obj)


class IsOn:

    VALUE = "On"

    @property
    def is_on(self) -> bool:
        return True


class IsOff:

    VALUE = "Off"

    @property
    def is_on(self) -> bool:
        return False


class IsAlarmed:

    VALUE = "Alarmed"

    @property
    def is_alarmed(self) -> bool:
        return True

    @abstractmethod
    def toggle(self) -> None:
        ...


class IsNotAlarmed:
    @property
    def is_alarmed(self) -> bool:
        return False


class IsShowing:

    VALUE = "Show"

    @property
    def is_showing(self) -> bool:
        return True


class IsNotShowing:
    @property
    def is_showing(self) -> bool:
        return False


class IsOpened:
    @property
    def is_opened(self) -> bool:
        return True


class IsClosed:
    @property
    def is_opened(self) -> bool:
        return False


class IsTriggered:

    VALUE = "Triggered"

    @property
    def is_triggered(self) -> bool:
        return True


class IsNotTriggered:
    @property
    def is_triggered(self) -> bool:
        return False


class IsKeeping:

    VALUE = "Keeping"

    @property
    def is_keeping(self) -> bool:
        return True


class IsNotKeeping:
    @property
    def is_keeping(self) -> bool:
        return False


class IsDetachable:

    VALUE = "Detachable"

    @property
    def is_detachable(self) -> bool:
        return True


class IsNotDetachable:
    @property
    def is_detachable(self) -> bool:
        return False


class IsCircadianRhythm:

    VALUE = "Circadian Rhythm"

    @property
    def is_circadian_rhythm(self) -> bool:
        return True


class IsNotCircadianRhythm:
    @property
    def is_circadian_rhythm(self) -> bool:
        return False


class IsLuxBalancing:

    VALUE = "Lux Balancing"

    @property
    def is_lux_balancing(self) -> bool:
        return True


class IsNotLuxBalancing:
    @property
    def is_lux_balancing(self) -> bool:
        return False


class IsFading:
    @property
    def is_fading(self) -> bool:
        return True


class IsNotFading:
    @property
    def is_fading(self) -> bool:
        return False


class Brightness:
    @property
    def brightness(self) -> int:
        return lookup_value(self.BRIGHTNESS_EVENT, self._events.items())

    @brightness.setter
    def brightness(self, value: int):
        event = lookup(self.BRIGHTNESS_EVENT, self._events.items())
        self.update_by(event(value))


class Hue:
    @property
    def hue(self) -> int:
        return lookup_value(self.HUE_EVENT, self._events.items())

    @hue.setter
    def hue(self, value: int):
        event = lookup(self.HUE_EVENT, self._events.items())
        self.update_by(event(value))


class Saturation:
    @property
    def saturation(self) -> int:
        return lookup_value(self.SATURATION_EVENT, self._events.items())

    @saturation.setter
    def saturation(self, value: int):
        event = lookup(self.SATURATION_EVENT, self._events.items())
        self.update_by(event(value))


class Temperature:
    @property
    def temperature(self) -> float:
        return lookup_value(self.TEMPERATURE_EVENT, self._events.items())

    @temperature.setter
    def temperature(self, value: float):
        event = lookup(self.TEMPERATURE_EVENT, self._events.items())
        self.update_by(event(value))


class Cycles:
    @property
    def cycles(self) -> int:
        return lookup_value(self.CYCLES_EVENT, self._events.items())

    @cycles.setter
    def cycles(self, value: int):
        event = lookup(self.CYCLES_EVENT, self._events.items())
        self.update_by(event(value))


class Period:
    @property
    def period(self) -> int:
        return lookup_value(self.PERIOD_EVENT, self._events.items())

    @period.setter
    def period(self, value: int):
        event = lookup(self.PERIOD_EVENT, self._events.items())
        self.update_by(event(value))


class StartingBrightness:
    @property
    def starting_brightness(self) -> int:
        return lookup_value(self.STARTING_BRIGHTNESS_EVENT, self._events.items())

    @starting_brightness.setter
    def starting_brightness(self, value: int):
        event = lookup(self.STARTING_BRIGHTNESS_EVENT, self._events.items())
        self.update_by(event(value))


class StartingHue:
    @property
    def starting_hue(self) -> int:
        return lookup_value(self.STARTING_HUE_EVENT, self._events.items())

    @starting_hue.setter
    def starting_hue(self, value: int):
        event = lookup(self.STARTING_HUE_EVENT, self._events.items())
        self.update_by(event(value))


class StartingSaturation:
    @property
    def starting_saturation(self) -> int:
        return lookup_value(self.STARTING_SATURATION_EVENT, self._events.items())

    @starting_saturation.setter
    def starting_saturation(self, value: int):
        event = lookup(self.STARTING_SATURATION_EVENT, self._events.items())
        self.update_by(event(value))


class EndingBrightness:
    @property
    def ending_brightness(self) -> int:
        return lookup_value(self.ENDING_BRIGHTNESS_EVENT, self._events.items())

    @ending_brightness.setter
    def ending_brightness(self, value: int):
        event = lookup(self.ENDING_BRIGHTNESS_EVENT, self._events.items())
        self.update_by(event(value))


class EndingHue:
    @property
    def ending_hue(self) -> int:
        return lookup_value(self.ENDING_HUE_EVENT, self._events.items())

    @ending_hue.setter
    def ending_hue(self, value: int):
        event = lookup(self.ENDING_HUE_EVENT, self._events.items())
        self.update_by(event(value))


class EndingSaturation:
    @property
    def ending_saturation(self) -> int:
        return lookup_value(self.ENDING_SATURATION_EVENT, self._events.items())

    @ending_saturation.setter
    def ending_saturation(self, value: int):
        event = lookup(self.ENDING_SATURATION_EVENT, self._events.items())
        self.update_by(event(value))


class Waveform:
    @property
    def waveform(self) -> str:
        return lookup_value(self.WAVEFORM_EVENT, self._events.items(), lambda obj: obj)


class Volume:
    @property
    def volume(self) -> int:
        return lookup_value(self.VOLUME_EVENT, self._events.items())

    @volume.setter
    def volume(self, value: int):
        event = lookup(self.VOLUME_EVENT, self._events.items())
        self.update_by(event(value))

    # @todo REMOVE!
    def next_volume(self, value: int) -> "home.appliance.State":
        if home.event.sleepiness.Event.Sleepy in self.events:
            return self.next(self.VOLUME_EVENT(value))


class Setpoint:
    @property
    def setpoint(self) -> float:
        return lookup_value(self.SETPOINT_EVENT, self._events.items())

    @setpoint.setter
    def setpoint(self, value: float):
        event = lookup(self.SETPOINT_EVENT, self._events.items())
        self.update_by(event(value))


class Playlist:
    @property
    def playlist(self) -> str:
        return lookup_value(self.PLAYLIST_EVENT, self._events.items())

    @playlist.setter
    def playlist(self, value: str):
        event = lookup(self.PLAYLIST_EVENT, self._events.items())
        self.update_by(event(value))


class Duration:
    @property
    def duration(self) -> int:
        return lookup_value(self.DURATION_EVENT, self._events.items())

    @duration.setter
    def duration(self, value: int):
        event = lookup(self.DURATION_EVENT, self._events.items())
        self.update_by(event(value))
