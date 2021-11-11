# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home
from home.appliance.callable import Callable


class Sleepiness(Callable):
    def run(self, event, state):
        if event == home.event.sleepiness.Event.Awake:
            if home.event.sun.twilight.civil.Event.Sunset not in state:
                if home.event.sun.hit.Event.Sunhit not in state:
                    state = self.get_new_state(state, "opened")
                else:
                    if home.event.sun.brightness.Event.Bright not in state:
                        state = self.get_new_state(state, "opened")
        return state


class Brightness(Callable):
    def run(self, event, state):
        if event in (
            home.event.sun.brightness.Event.Dark,
            home.event.sun.brightness.Event.DeepDark,
        ):
            if (
                home.event.sun.twilight.civil.Event.Sunset not in state
                and home.event.sleepiness.Event.Asleep not in state
            ):
                state = self.get_new_state(state, "opened")
        return state


class SunHit(Callable):
    def run(self, event, state):
        if event == home.event.sun.hit.Event.Sunleft:
            if (
                home.event.sun.twilight.civil.Event.Sunset not in state
                and home.event.sleepiness.Event.Asleep not in state
            ):
                state = self.get_new_state(state, "opened")
        return state


class SunTwilight(Callable):
    def run(self, event, state):
        if event == home.event.sun.twilight.civil.Event.Sunrise and (
            home.event.sleepiness.Event.Awake in state
            or home.event.sleepiness.Event.Sleepy in state
        ):
            if home.event.sun.hit.Event.Sunhit not in state:
                state = self.get_new_state(state, "opened")
            else:
                if home.event.sun.brightness.Event.Bright not in state:
                    state = self.get_new_state(state, "opened")
        return state
