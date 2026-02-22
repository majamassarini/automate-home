# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.scheduler.trigger.date.resettable import Trigger as Parent


class Trigger(Parent):
    """
    A resettable date trigger that, when fired, re-enables events
    in the Appliance state machine.
    """
