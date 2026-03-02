# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import home

import copy
import datetime
from typing import Iterable, List, Tuple

from home.scheduler.trigger.date import enable_events as date_enable_events
from home.scheduler.trigger.protocol.delay import Delay
from home.scheduler.trigger.state.entering.delay import Trigger as Parent


class _EnableEventsDelay(Delay):
    """
    A :py:class:`Delay` variant that forks into a
    :py:class:`date.enable_events.Trigger` instead of the default
    :py:class:`date.resettable.Trigger`.

    When the forked trigger fires, the :py:class:`Process` recognises it
    as an ``enable_events`` trigger and calls
    :py:meth:`Appliance.enable` for each event, re-activating them in
    the appliance state machine.
    """

    def fork(
        self, performer: home.Performer
    ) -> List[Tuple[home.Performer, "home.scheduler.Trigger"]]:
        result = list()
        name = (
            "date.enable_events.Trigger for parent trigger"
            " {} and performer {}".format(self._trigger_name, performer.name)
        )
        run_date = datetime.datetime.now() + datetime.timedelta(
            seconds=self._timeout
        )
        if name in self._last_resettable_trigger:
            self._last_resettable_trigger[name].disable()
        self._last_resettable_trigger[name] = date_enable_events.Trigger(
            name,
            self._scheduler_trigger_events,
            run_date=run_date,
            timezone=self._timezone,
        )
        result.append((performer, self._last_resettable_trigger[name]))
        return result


class Trigger(Parent):
    """
    A scheduler trigger that, on entering the specified state, starts a
    timer and re-enables the given events in the appliance state machine
    once the timer expires.

    A typical use-case is suppressing an event (e.g. ``forced.Off``)
    immediately on state entry and automatically re-enabling it after a
    short grace period, so that spurious echoes from the bus are ignored
    while legitimate commands are still accepted afterwards.

    >>> import home
    >>> off = home.appliance.sound.player.state.off.State()
    >>> fade_in = home.appliance.sound.player.state.fade_in.State()
    >>> trigger = Trigger("re-enable forced off", [], 'Fade In', 1)
    >>> trigger.is_triggered(off, fade_in)
    True
    """

    def __init__(
        self,
        name: str,
        events: Iterable[home.Event],
        state: str,
        timeout_seconds: float,
    ):
        """
        :param name: human-readable trigger name used in log messages
        :param events: events to re-enable when the timer expires
        :param state: the :py:attr:`State.VALUE` string that starts the timer
        :param timeout_seconds: seconds to wait before re-enabling the events
        """
        super().__init__(name, events, state, timeout_seconds)
        self._delay = _EnableEventsDelay(
            "delay trigger for {}".format(name),
            copy.deepcopy(events),
            timeout_seconds,
            self._timezone,
        )
