Sound Player Project Example
============================

This example project automates one kind of *Appliance* an **sound player**.
The automated device is one sonos device.

The **sound player** is a :ref:`sound.player.Appliance Appliance <sound.player.Appliance>`.

.. raw:: latex

    \clearpage

UI
^^

.. image:: ../../../homino/example-sound-player/gui/last_events.png

.. image:: ../../../homino/example-sound-player/gui/sound_player.png

.. image:: ../../../homino/example-sound-player/gui/history.png

Directories/files structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  example-sound-player

    :ref:`configuration.ini <configuration_sound.ini>`

    :ref:`appliances.yaml <appliances_sound.yaml>`

    performer

      sound

         :ref:`player.yaml <player.yaml>`

    scheduler_triggers

      :ref:`buttons.yaml <st_buttons_sp.yaml>`

      :ref:`circadian_rhythm.yaml <st_circadian_rhythm_sp.yaml>`

      :ref:`fade.yaml <st_fade_sp.yaml>`

      :ref:`sleepiness.yaml <st_sleepiness_sp.yaml>`

    scheduler

      :ref:`buttons.yaml <s_buttons_sp.yaml>`

      :ref:`circadian_rhythm.yaml <s_circadian_rhythm_sp.yaml>`

      :ref:`fade.yaml <s_fade_sp.yaml>`

      :ref:`sleepiness.yaml <s_sleepiness_sp.yaml>`

.. raw:: latex

    \clearpage

Files
^^^^^

configuration.ini
"""""""""""""""""

.. _configuration_sound.ini:

.. literalinclude:: ../../../homino/example-sound-player/configuration-dev-mac.ini

appliances.yaml
"""""""""""""""

.. _appliances_sound.yaml:

.. literalinclude:: ../../../homino/example-sound-player/appliances.yaml

performer/sound/player.yaml
"""""""""""""""""""""""""""

.. _player.yaml:

.. literalinclude:: ../../../homino/example-sound-player/performer/sound/player.yaml

scheduler_triggers/buttons.yaml
"""""""""""""""""""""""""""""""

.. _st_buttons_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler_triggers/buttons.yaml

scheduler_triggers/circadian_rhythm.yaml
""""""""""""""""""""""""""""""""""""""""

.. _st_circadian_rhythm_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler_triggers/circadian_rhythm.yaml

scheduler_triggers/fade.yaml
""""""""""""""""""""""""""""

.. _st_fade_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler_triggers/fade.yaml

scheduler_triggers/sleepiness.yaml
""""""""""""""""""""""""""""""""""

.. _st_sleepiness_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler_triggers/sleepiness.yaml


scheduler/buttons.yaml
""""""""""""""""""""""

.. _s_buttons_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler/buttons.yaml

scheduler/circadian_rhythm.yaml
"""""""""""""""""""""""""""""""

.. _s_circadian_rhythm_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler/circadian_rhythm.yaml

scheduler/fade.yaml
"""""""""""""""""""

.. _s_fade_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler/fade.yaml

scheduler/sleepiness.yaml
"""""""""""""""""""""""""

.. _s_sleepiness_sp.yaml:

.. literalinclude:: ../../../homino/example-sound-player/scheduler/sleepiness.yaml
