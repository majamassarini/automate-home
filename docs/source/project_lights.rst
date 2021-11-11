Lights Project Example
======================

This example project automates 4 different *Appliances*.
The automated devices are 2 knx switches, 1 knx dimmer and 1 lifx bulb (switched on/off by one more knx switch).

  1. **an indoor presence light** is a :ref:`light.presence.Appliance Appliance <light.presence.Appliance>`. An *indoor* light which
  is turned off by the system when no one is supposed to be using the light because, as an example, the alarm was armed.
  It is turned off by the system even if the light was *forced on*.

  2. **an indoor courtesy light** is a :ref:`light.zone.Appliance Appliance <light.zone.Appliance>`. An *indoor* light which
  is turned on by the system when, as an example, a sensor not far from the light has been triggered.

  3. **an indoor dimmerable light** is a :ref:`light.indoor.dimmerable.Appliance Appliance <light.indoor.dimmerable.Appliance>`.
  It can work in 4 differents modes:

  - it can work with a **circadian rhythm**: during the day it will adjust its brightness accordingly to received,
    through a *circadian rhythm scheduler trigger*, brightness events
  - it can work **balancing the lux**: a protocol scheduler trigger linked to a lux sensor notifies lux balancing
    brightness events to the dimmer that will adjust its brightness
  - it can work like in a **show**: a *show* scheduler trigger notifies new brightness events when, as an example,
    a button is pressed
  - it can work with an almost *fixed* brightness value, only the user will change it

  Multiple buttons can make the dimmer switching between its operating modes.
  When the user forces the brightness, the mode is always switched to the fixed one (*forced on*).

  4. **a indoor hue light** is an :ref:`light.indoor.hue.Appliance Appliance <light.indoor.hue.Appliance>`. An *indoor* hue light.
  It can work in 4 differents modes:

  - it can work with a **circadian rhythm**: during the day it will adjust its hue, saturation, lightness and
    temperature accordingly to received, through a *circadian rhythm scheduler trigger*, events
  - it can work **balancing the lux**: a protocol scheduler trigger linked to a lux sensor creates lux balancing
    brightness events and notifies them to the hue light that will adjust its lightness
  - it can work like in a **show**: it will change its hue, saturation, lightness and temperature with given waveforms
    as speedy as specified by period and cycles events. The show parameters can be adjusted, during the day, using a
    circadian rhythm scheduler trigger.
  - it can work with an almost *fixed* hue, saturation, lightness and temperature: changing only through the
    user interaction

  Multiple buttons can make the hue light switching between its operating modes.

To automate the lights two sensors, other than the buttons, are used and modeled:

  2. **lux** is a :ref:`sensor.luxmeter.Appliance Appliance <sensor.luxmeter.Appliance>`. It is used to calculate balanced brightness,
     through a specific protocol trigger.

  3. **alarm** is a :ref:`sensor.alarm.Appliance Appliance <sensor.alarm.Appliance>`. It is used to guess presence state.

The lifx bulb, an *indoor hue Light Appliance*, is controlled using scheduler triggers with some delay seconds;
it is turned on/off through a knx switch and it takes 7/8 seconds to be ready to listen and execute new commands.

.. raw:: latex

    \clearpage

UI
^^

.. image:: ../../../homino/example-lights/gui/last_events.png

.. image:: ../../../homino/example-lights/gui/collections.png

.. image:: ../../../homino/example-lights/gui/lights.png

.. image:: ../../../homino/example-lights/gui/presence_light.png

.. _light widget:

.. image:: ../../../homino/example-lights/gui/zone_light.png

.. image:: ../../../homino/example-lights/gui/indoor_dimmerable_light.png

.. image:: ../../../homino/example-lights/gui/indoor_hue_light.png


Directories/files structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  example-lights

    :ref:`configuration.ini <configuration_lights.ini>`

    :ref:`appliances.yaml <appliances_lights.yaml>`

    performer

      sensors

         :ref:`alarm.yaml <alarm_lights.yaml>`

         :ref:`lux.yaml <lux_lights.yaml>`

      lights

           :ref:`presence.yaml <presence.yaml>`

           :ref:`zone.yaml <zone.yaml>`

           :ref:`dimmer.yaml <dimmer.yaml>`

           :ref:`hue.yaml <hue.yaml>`

    performers

      :ref:`lights.yaml <lights.yaml>`

    scheduler_triggers

      :ref:`alarm.yaml <st_alarm_lights.yaml>`

      :ref:`hue.yaml <st_hue.yaml>`

      :ref:`sensor.yaml <st_sensor_lights.yaml>`

      :ref:`circadian_rhythm.yaml <st_circadian_rhythm.yaml>`

    scheduler

      :ref:`alarm.yaml <s_alarm_lights.yaml>`

      :ref:`hue.yaml <s_hue.yaml>`

      :ref:`sensor.yaml <s_sensor_lights.yaml>`

      :ref:`circadian_rhythm.yaml <s_circadian_rhythm.yaml>`

.. raw:: latex

    \clearpage

Files
^^^^^

configuration.ini
"""""""""""""""""

.. _configuration_lights.ini:

.. literalinclude:: ../../../homino/example-lights/configuration.ini

appliances.yaml
"""""""""""""""

.. _appliances_lights.yaml:

.. literalinclude:: ../../../homino/example-lights/appliances.yaml

performer/sensors/alarm.yaml
""""""""""""""""""""""""""""

.. _alarm_lights.yaml:

.. literalinclude:: ../../../homino/example-lights/performer/sensors/alarm.yaml

performer/sensors/lux.yaml
"""""""""""""""""""""""""""

.. _lux_lights.yaml:

.. literalinclude:: ../../../homino/example-lights/performer/sensors/lux.yaml

performer/lights/presence.yaml
"""""""""""""""""""""""""""""""""""""""

.. _presence.yaml:

.. literalinclude:: ../../../homino/example-lights/performer/lights/presence.yaml

performer/lights/zone.yaml
"""""""""""""""""""""""""""""""""""""""

.. _zone.yaml:

.. literalinclude:: ../../../homino/example-lights/performer/lights/zone.yaml

performer/lights/dimmer.yaml
"""""""""""""""""""""""""""""""""""""""

.. _dimmer.yaml:

.. literalinclude:: ../../../homino/example-lights/performer/lights/dimmer.yaml

performer/lights/hue.yaml
"""""""""""""""""""""""""""""""""""""""

.. _hue.yaml:

.. literalinclude:: ../../../homino/example-lights/performer/lights/hue.yaml

performers/lights.yaml
""""""""""""""""""""""""

.. _lights.yaml:

.. literalinclude:: ../../../homino/example-lights/performers/lights.yaml

scheduler_triggers/sensor.yaml
""""""""""""""""""""""""""""""

.. _st_sensor_lights.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler_triggers/sensor.yaml

scheduler_triggers/hue.yaml
""""""""""""""""""""""""""""""""

.. _st_hue.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler_triggers/hue.yaml

scheduler_triggers/circadian_rhythm.yaml
""""""""""""""""""""""""""""""""""""""""

.. _st_circadian_rhythm.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler_triggers/circadian_rhythm.yaml

scheduler_triggers/alarm.yaml
""""""""""""""""""""""""""""""""

.. _st_alarm_lights.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler_triggers/alarm.yaml

scheduler/alarm.yaml
""""""""""""""""""""""""""""""

.. _s_alarm_lights.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler/alarm.yaml

scheduler/circadian_rhythm.yaml
""""""""""""""""""""""""""""""""

.. _s_circadian_rhythm.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler/circadian_rhythm.yaml

scheduler/hue.yaml
""""""""""""""""""""""""""""""""

.. _s_hue.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler/hue.yaml

scheduler/sensor.yaml
""""""""""""""""""""""""""""""""

.. _s_sensor_lights.yaml:

.. literalinclude:: ../../../homino/example-lights/scheduler/sensor.yaml

.. raw:: latex

    \clearpage

