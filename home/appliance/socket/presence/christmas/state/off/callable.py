# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Presence(Callable):
    def run(self, event, state):
        if event == home.event.presence.Event.On:
            if (
                home.event.holiday.christmas.Event.Over not in state
                or home.event.holiday.san_silvester.Event.Over not in state
                or home.event.holiday.epiphany.Event.Over not in state
            ):
                if (
                    home.event.sun.brightness.Event.Dark in state
                    or home.event.sun.brightness.Event.DeepDark in state
                ):
                    state = self.get_new_state(state, "on")
            else:
                state = self.get_new_state(state, "on")
        return state


class Christmas(Callable):
    def run(self, event, state):
        if event == home.event.holiday.christmas.Event.Time:
            if home.event.sun.brightness.Event.DeepDark in state:
                state = self.get_new_state(state, "on")
        elif event == home.event.holiday.christmas.Event.Over:
            if home.event.presence.Event.On in state:
                state = self.get_new_state(state, "on")
        elif (
            event == home.event.holiday.christmas.Event.Eve
            or event == home.event.holiday.christmas.Event.Day
        ):
            state = self.get_new_state(state, "on")
        return state


class SanSilvester(Callable):
    def run(self, event, state):
        if (
            event == home.event.holiday.san_silvester.Event.Eve
            or event == home.event.holiday.san_silvester.Event.Day
        ):
            state = self.get_new_state(state, "on")
        return state


class Epiphany(Callable):
    def run(self, event, state):
        if (
            event == home.event.holiday.epiphany.Event.Eve
            or event == home.event.holiday.epiphany.Event.Day
        ):
            state = self.get_new_state(state, "on")
        return state


class SunBrightness(Callable):
    def run(self, event, state):
        if event == home.event.sun.brightness.Event.DeepDark:
            if (
                home.event.holiday.christmas.Event.Time in state
                or home.event.holiday.christmas.Event.Day in state
                or home.event.holiday.christmas.Event.Eve in state
                or home.event.holiday.san_silvester.Event.Day in state
                or home.event.holiday.san_silvester.Event.Eve in state
                or home.event.holiday.epiphany.Event.Day in state
                or home.event.holiday.epiphany.Event.Eve in state
            ):
                state = self.get_new_state(state, "on")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.On:
            state = self.get_new_state(state, "forced_on")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
