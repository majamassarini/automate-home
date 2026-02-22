# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from home.scheduler.trigger.state.entering import Trigger as Parent


class Trigger(Parent):
    """
    A **Scheduler Trigger** that, when entering the specified state,
    disables the specified events in the Appliance state machine.
    """
