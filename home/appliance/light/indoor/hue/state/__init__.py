# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home import event as home_event
from home.appliance import attribute
from home.appliance.callable import Callable
from home.appliance.light import event
from home.appliance.light.indoor.dimmerable.event import forced as forced_event
from home.appliance.light.indoor.dimmerable.state import State as Parent


class Hue(Callable):
    def run(self, event, state):
        return state


class CircadianHue(Callable):
    def run(self, event, state):
        return state


class Saturation(Callable):
    def run(self, event, state):
        return state


class CircadianSaturation(Callable):
    def run(self, event, state):
        return state


class Temperature(Callable):
    def run(self, event, state):
        return state


class CircadianTemperature(Callable):
    def run(self, event, state):
        return state


class ShowStartingHue(Callable):
    def run(self, event, state):
        return state


class ShowStartingSaturation(Callable):
    def run(self, event, state):
        return state


class ShowEndingHue(Callable):
    def run(self, event, state):
        return state


class ShowEndingSaturation(Callable):
    def run(self, event, state):
        return state


class State(
    Parent,
    attribute.mixin.Hue,
    attribute.mixin.Saturation,
    attribute.mixin.Temperature,
    attribute.mixin.StartingHue,
    attribute.mixin.StartingSaturation,
    attribute.mixin.EndingHue,
    attribute.mixin.EndingSaturation,
):
    """
    >>> import home
    >>> state = home.appliance.light.indoor.hue.state.off.State()
    >>> state = state.next(home.event.sun.brightness.Event.Dark)
    >>> state.compute()
    'Off'
    >>> state = state.next(home.appliance.light.event.brightness.Event(50))
    >>> state.compute()
    'Off'
    >>> state = state.next(home.appliance.light.indoor.dimmerable.event.forced.Event.On)
    >>> state.compute()
    'Forced On'
    >>> state = state.unforce()
    >>> state.compute()
    'Off'
    >>> state.brightness
    50
    """

    HUE_EVENT = event.hue.Event
    SATURATION_EVENT = event.saturation.Event
    TEMPERATURE_EVENT = event.temperature.Event
    STARTING_HUE_EVENT = event.show.starting_hue.Event
    STARTING_SATURATION_EVENT = event.show.starting_saturation.Event
    ENDING_HUE_EVENT = event.show.ending_hue.Event
    ENDING_SATURATION_EVENT = event.show.ending_saturation.Event

    DEFAULTS = [
        event.show.period.Event(120000),
        event.show.cycles.Event(1000),
        event.show.ending_hue.Event(360),
        event.show.ending_brightness.Event(100),
        event.show.ending_saturation.Event(0),
        event.show.starting_hue.Event(90),
        event.show.starting_brightness.Event(20),
        event.show.starting_saturation.Event(0),
        event.lux_balancing.brightness.Event(100),
        event.circadian_rhythm.temperature.Event(2500),
        event.circadian_rhythm.saturation.Event(0),
        event.circadian_rhythm.hue.Event(360),
        event.circadian_rhythm.brightness.Event(100),
        event.temperature.Event(2500),
        event.saturation.Event(0),
        event.hue.Event(360),
        event.brightness.Event(100),
        home_event.waveform.Event.Sine,
        home_event.presence.Event.Off,
        home_event.sun.brightness.Event.Bright,
        forced_event.Event.Not,
    ]

    def __init__(self, *args):
        super(State, self).__init__(*args)

        callables = {
            type(event.show.starting_hue.Event): ShowStartingHue(),
            type(event.show.starting_saturation.Event): ShowStartingSaturation(),
            type(event.show.ending_hue.Event): ShowEndingHue(),
            type(event.show.ending_saturation.Event): ShowEndingSaturation(),
            type(event.hue.Event): Hue(),
            type(event.circadian_rhythm.hue.Event): CircadianHue(),
            type(event.saturation.Event): Saturation(),
            type(event.circadian_rhythm.saturation.Event): CircadianSaturation(),
            type(event.temperature.Event): Temperature(),
            type(event.circadian_rhythm.temperature.Event): CircadianTemperature(),
        }
        self._callables.update(callables)


from home.appliance.light.indoor.hue.state import forced
from home.appliance.light.indoor.hue.state import off
from home.appliance.light.indoor.hue.state import on
