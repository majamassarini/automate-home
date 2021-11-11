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
from home.appliance.light.state import State as Parent


class Brightness(Callable):
    def run(self, event, state):
        return state


class CircadianBrightness(Callable):
    def run(self, event, state):
        return state


class BalancedBrightness(Callable):
    def run(self, event, state):
        return state


class ShowStartingBrightness(Callable):
    def run(self, event, state):
        return state


class ShowEndingBrightness(Callable):
    def run(self, event, state):
        return state


class ShowWaveform(Callable):
    def run(self, event, state):
        return state


class ShowPeriod(Callable):
    def run(self, event, state):
        return state


class ShowCycles(Callable):
    def run(self, event, state):
        return state


class State(
    Parent,
    attribute.mixin.Brightness,
    attribute.mixin.StartingBrightness,
    attribute.mixin.EndingBrightness,
    attribute.mixin.Waveform,
    attribute.mixin.Period,
    attribute.mixin.Cycles,
):
    """
    >>> import home
    >>> state = home.appliance.light.indoor.dimmerable.state.off.State()
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

    BRIGHTNESS_EVENT = event.brightness.Event
    STARTING_BRIGHTNESS_EVENT = event.show.starting_brightness.Event
    ENDING_BRIGHTNESS_EVENT = event.show.ending_brightness.Event
    PERIOD_EVENT = event.show.period.Event
    CYCLES_EVENT = event.show.cycles.Event
    WAVEFORM_EVENT = home_event.waveform.Event

    DEFAULTS = [
        event.show.period.Event(1000),
        event.show.cycles.Event(100),
        event.show.ending_brightness.Event(100),
        event.show.starting_brightness.Event(10),
        event.lux_balancing.brightness.Event(100),
        event.circadian_rhythm.brightness.Event(100),
        event.brightness.Event(100),
        home_event.waveform.Event.Sine,
        home_event.presence.Event.Off,
        home_event.sun.brightness.Event.Bright,
        forced_event.Event.Not,
    ]

    def __init__(self, *args):
        super(State, self).__init__(*args)

        callables = {
            type(event.brightness.Event): Brightness(),
            type(event.circadian_rhythm.brightness.Event): CircadianBrightness(),
            type(event.lux_balancing.brightness.Event): BalancedBrightness(),
            type(event.show.starting_brightness.Event): ShowStartingBrightness(),
            type(event.show.ending_brightness.Event): ShowEndingBrightness(),
            type(event.show.cycles.Event): ShowCycles(),
            type(event.show.period.Event): ShowPeriod(),
            type(home_event.waveform.Event): ShowWaveform(),
        }
        self._callables.update(callables)

    @property
    def forced_enum(self):
        return forced_event.Event


from home.appliance.light.indoor.dimmerable.state import on
from home.appliance.light.indoor.dimmerable.state import off
from home.appliance.light.indoor.dimmerable.state import forced
