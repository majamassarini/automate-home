# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import home


class Event(home.event.Enum):
    """
    The play mode (repeat, shuffle) of a sleepy forced on sound player

    >>> import home
    >>> home.appliance.sound.player.event.sleepy_play_mode.Event.RepeatAll.value
    'RepeatAll'
    """

    Normal = "Normal"
    RepeatAll = "RepeatAll"
    RepeatOne = "RepeatOne"
    Shuffle = "Shuffle"
    ShuffleNoRepeat = "ShuffleNoRepeat"
    ShuffleRepeatOne = "ShuffleRepeatOne"
