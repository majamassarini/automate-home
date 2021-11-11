# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Presence(Callable):
    def run(self, event, state):
        if event == home.event.presence.Event.Off:
            if (
                home.event.holiday.christmas.Event.Day not in state
                and home.event.holiday.christmas.Event.Eve not in state
                and home.event.holiday.san_silvester.Event.Day not in state
                and home.event.holiday.san_silvester.Event.Eve not in state
                and home.event.holiday.epiphany.Event.Day not in state
                and home.event.holiday.epiphany.Event.Eve not in state
            ):
                state = self.get_new_state(state, "off")
        return state


class Christmas(Callable):
    def run(self, event, state):
        if event == home.event.holiday.christmas.Event.Time:
            if (
                home.event.sun.brightness.Event.Bright in state
                or home.event.sun.brightness.Event.Dark in state
            ):
                if (
                    home.event.holiday.san_silvester.Event.Over in state
                    and home.event.holiday.epiphany.Event.Over in state
                ):
                    state = self.get_new_state(state, "off")
        elif event == home.event.holiday.christmas.Event.Over:
            if home.event.presence.Event.Off in state:
                if (
                    home.event.holiday.san_silvester.Event.Over in state
                    and home.event.holiday.epiphany.Event.Over in state
                ):
                    state = self.get_new_state(state, "off")
        return state


class SanSilvester(Callable):
    def run(self, event, state):
        if home.event.holiday.san_silvester.Event.Over == event:
            if home.event.holiday.christmas.Event.Time in state and (
                home.event.holiday.epiphany.Event.Day not in state
                and home.event.holiday.epiphany.Event.Eve not in state
            ):
                if (
                    home.event.sun.brightness.Event.Bright in state
                    or home.event.sun.brightness.Event.Dark in state
                ):
                    state = self.get_new_state(state, "off")
            elif home.event.presence.Event.Off in state:
                if (
                    home.event.holiday.epiphany.Event.Day not in state
                    and home.event.holiday.epiphany.Event.Eve not in state
                ):
                    state = self.get_new_state(state, "off")
        return state


class Epiphany(Callable):
    def run(self, event, state):
        if home.event.holiday.epiphany.Event.Over == event:
            if home.event.holiday.christmas.Event.Time in state and (
                home.event.holiday.san_silvester.Event.Day not in state
                and home.event.holiday.san_silvester.Event.Eve not in state
            ):
                if (
                    home.event.sun.brightness.Event.Bright in state
                    or home.event.sun.brightness.Event.Dark in state
                ):
                    state = self.get_new_state(state, "off")
            elif home.event.presence.Event.Off in state:
                if (
                    home.event.holiday.san_silvester.Event.Day not in state
                    and home.event.holiday.san_silvester.Event.Eve not in state
                ):
                    state = self.get_new_state(state, "off")

        return state


class SunBrightness(Callable):
    def run(self, event, state):
        if (
            event == home.event.sun.brightness.Event.Bright
            or event == home.event.sun.brightness.Event.Dark
        ):
            if home.event.holiday.christmas.Event.Time in state:
                if (
                    home.event.holiday.epiphany.Event.Day not in state
                    and home.event.holiday.epiphany.Event.Eve not in state
                    and home.event.holiday.san_silvester.Event.Day not in state
                    and home.event.holiday.san_silvester.Event.Eve not in state
                ):
                    state = self.get_new_state(state, "off")
        return state


class Forced(Callable):
    def run(self, event, state):
        if event == state.forced_enum.Off:
            state = self.get_new_state(state, "forced_off")
        elif event != state.forced_enum.Not:
            state = state.unforce()
        return state
