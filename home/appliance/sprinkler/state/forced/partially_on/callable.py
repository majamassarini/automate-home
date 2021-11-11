# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.sprinkler.state.forced.on import callable as forced_on


class SunPhase(forced_on.SunPhase):
    pass


class Forced(forced_on.Forced):
    pass
