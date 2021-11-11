# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.appliance.light.indoor.dimmerable.state.forced.on import callable


class Presence(callable.Presence):
    pass


class Brightness(callable.Brightness):
    pass


class Forced(callable.Forced):
    pass
