# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from abc import abstractmethod
from typing import Any, ClassVar, Optional, Tuple, Iterable, Callable

import home


def get_event_value(obj):
    return obj.value


def lookup(
    event: type, events: Iterable[Tuple[type, home.event.Event]]
) -> Optional[Any]:
    for klass, obj in events:
        if klass == event:
            return klass
    return None


def lookup_value(
    event: type,
    events: Iterable[Tuple[type, home.event.Event]],
    fun: Callable = None,
) -> Optional[Any]:
    if not fun:
        fun = get_event_value
    for klass, obj in events:
        if klass == event:
            if obj:
                return fun(obj)
    return None


class IsOn:

    VALUE: ClassVar[str] = "On"

    @property
    def is_on(self) -> bool:
        return True


class IsOff:

    VALUE: ClassVar[str] = "Off"

    @property
    def is_on(self) -> bool:
        return False


class IsAlarmed:

    VALUE: ClassVar[str] = "Alarmed"

    @property
    def is_alarmed(self) -> bool:
        return True

    @abstractmethod
    def toggle(self) -> None: ...


class IsNotAlarmed:
    @property
    def is_alarmed(self) -> bool:
        return False


class IsShowing:

    VALUE: ClassVar[str] = "Show"

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

    VALUE: ClassVar[str] = "Triggered"

    @property
    def is_triggered(self) -> bool:
        return True


class IsNotTriggered:
    @property
    def is_triggered(self) -> bool:
        return False


class IsKeeping:

    VALUE: ClassVar[str] = "Keeping"

    @property
    def is_keeping(self) -> bool:
        return True


class IsNotKeeping:
    @property
    def is_keeping(self) -> bool:
        return False


class IsDetachable:

    VALUE: ClassVar[str] = "Detachable"

    @property
    def is_detachable(self) -> bool:
        return True


class IsNotDetachable:
    @property
    def is_detachable(self) -> bool:
        return False


class IsCircadianRhythm:

    VALUE: ClassVar[str] = "Circadian Rhythm"

    @property
    def is_circadian_rhythm(self) -> bool:
        return True


class IsNotCircadianRhythm:
    @property
    def is_circadian_rhythm(self) -> bool:
        return False


class IsLuxBalancing:

    VALUE: ClassVar[str] = "Lux Balancing"

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
        return lookup_value(self.BRIGHTNESS_EVENT, self._events.items())  # type: ignore[attr-defined]

    @brightness.setter
    def brightness(self, value: int):
        event = lookup(self.BRIGHTNESS_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Hue:
    @property
    def hue(self) -> int:
        return lookup_value(self.HUE_EVENT, self._events.items())  # type: ignore[attr-defined]

    @hue.setter
    def hue(self, value: int):
        event = lookup(self.HUE_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Saturation:
    @property
    def saturation(self) -> int:
        return lookup_value(self.SATURATION_EVENT, self._events.items())  # type: ignore[attr-defined]

    @saturation.setter
    def saturation(self, value: int):
        event = lookup(self.SATURATION_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Temperature:
    @property
    def temperature(self) -> float:
        return lookup_value(self.TEMPERATURE_EVENT, self._events.items())  # type: ignore[attr-defined]

    @temperature.setter
    def temperature(self, value: float):
        event = lookup(self.TEMPERATURE_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Cycles:
    @property
    def cycles(self) -> int:
        return lookup_value(self.CYCLES_EVENT, self._events.items())  # type: ignore[attr-defined]

    @cycles.setter
    def cycles(self, value: int):
        event = lookup(self.CYCLES_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Period:
    @property
    def period(self) -> int:
        return lookup_value(self.PERIOD_EVENT, self._events.items())  # type: ignore[attr-defined]

    @period.setter
    def period(self, value: int):
        event = lookup(self.PERIOD_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class StartingBrightness:
    @property
    def starting_brightness(self) -> int:
        return lookup_value(self.STARTING_BRIGHTNESS_EVENT, self._events.items())  # type: ignore[attr-defined]

    @starting_brightness.setter
    def starting_brightness(self, value: int):
        event = lookup(self.STARTING_BRIGHTNESS_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class StartingHue:
    @property
    def starting_hue(self) -> int:
        return lookup_value(self.STARTING_HUE_EVENT, self._events.items())  # type: ignore[attr-defined]

    @starting_hue.setter
    def starting_hue(self, value: int):
        event = lookup(self.STARTING_HUE_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class StartingSaturation:
    @property
    def starting_saturation(self) -> int:
        return lookup_value(self.STARTING_SATURATION_EVENT, self._events.items())  # type: ignore[attr-defined]

    @starting_saturation.setter
    def starting_saturation(self, value: int):
        event = lookup(self.STARTING_SATURATION_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class EndingBrightness:
    @property
    def ending_brightness(self) -> int:
        return lookup_value(self.ENDING_BRIGHTNESS_EVENT, self._events.items())  # type: ignore[attr-defined]

    @ending_brightness.setter
    def ending_brightness(self, value: int):
        event = lookup(self.ENDING_BRIGHTNESS_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class EndingHue:
    @property
    def ending_hue(self) -> int:
        return lookup_value(self.ENDING_HUE_EVENT, self._events.items())  # type: ignore[attr-defined]

    @ending_hue.setter
    def ending_hue(self, value: int):
        event = lookup(self.ENDING_HUE_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class EndingSaturation:
    @property
    def ending_saturation(self) -> int:
        return lookup_value(self.ENDING_SATURATION_EVENT, self._events.items())  # type: ignore[attr-defined]

    @ending_saturation.setter
    def ending_saturation(self, value: int):
        event = lookup(self.ENDING_SATURATION_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Waveform:
    @property
    def waveform(self) -> str:
        return lookup_value(self.WAVEFORM_EVENT, self._events.items(), lambda obj: obj)  # type: ignore[attr-defined]


class Volume:
    @property
    def volume(self) -> int:
        return lookup_value(self.VOLUME_EVENT, self._events.items())  # type: ignore[attr-defined]

    @volume.setter
    def volume(self, value: int):
        event = lookup(self.VOLUME_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Setpoint:
    @property
    def setpoint(self) -> float:
        return lookup_value(self.SETPOINT_EVENT, self._events.items())  # type: ignore[attr-defined]

    @setpoint.setter
    def setpoint(self, value: float):
        event = lookup(self.SETPOINT_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Playlist:
    @property
    def playlist(self) -> str:
        return lookup_value(self.PLAYLIST_EVENT, self._events.items())  # type: ignore[attr-defined]

    @playlist.setter
    def playlist(self, value: str):
        event = lookup(self.PLAYLIST_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]


class Duration:
    @property
    def duration(self) -> int:
        return lookup_value(self.DURATION_EVENT, self._events.items())  # type: ignore[attr-defined]

    @duration.setter
    def duration(self, value: int):
        event = lookup(self.DURATION_EVENT, self._events.items())  # type: ignore[attr-defined]
        self.update_by(event(value))  # type: ignore[attr-defined]
