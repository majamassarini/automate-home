Curtains Project Example
========================

This example project automates 3 different *Appliances*.
The automated devices are 3 equals knx actuators for blind/shutters which understand just an *opened* and a *closed command*.

  1. **indoor blackout curtain** is an :ref:`indoor.blackout.Curtain Appliance <curtain.indoor.blackout.Appliance>`.
  It is an *indoor* curtain which completely obscure the room.
  It is closed by the user when he goes to bed; in the morning is opened by
  the system to wake up the user at the desired time. The *Performer* bound with this
  *Appliance* **does not know how to close the curtain** since it is dangerous: the window
  could be left opened by the user and the system could not know when it happens,
  thus it is safer if the system does not close this indoor curtain.

  2. **outdoor curtain** is an :ref:`outdoor.Curtain Appliance <curtain.outdoor.Appliance>`.
  It is an *outdoor* curtain which partially obscure the room.
  It is closed at sunset (for enhancing the room privacy), opened at
  sunrise (for the benefit of the plants in the room), closed when the sun enters through
  the window (for preserving the room's furniture), opened when the wind is strong.

  3. **outdoor bedroom curtain** is an :ref:`outdoor.bedroom.Curtain Appliance <curtain.outdoor.bedroom.Appliance>`.
  It is like *outdoor curtain* but should not be raised
  at sunrise unless the user is to be wake up. It is used with the indoor.blackout.Curtain
  to gentle wake up the user in the morning at the desired time.

To automate the curtains 2 sensors are used:

  2. **lux** is a :ref:`sensor.luxmeter.Appliance Appliance <sensor.luxmeter.Appliance>`. Has a changing lux value.

  3. **wind** is a :ref:`sensor.anemometer.Appliance Appliance <sensor.anemometer.Appliance>`. Has a changing wind value.


.. raw:: latex

    \clearpage


UI
^^

.. image:: ../../../homino/example-curtains/gui/last_events.png

.. image:: ../../../homino/example-curtains/gui/collections.png

.. image:: ../../../homino/example-curtains/gui/curtains.png

.. image:: ../../../homino/example-curtains/gui/indoor_blackout_curtain.png

.. _curtain widget:

.. image:: ../../../homino/example-curtains/gui/outdoor_curtain.png

.. _event disable widget:

.. image:: ../../../homino/example-curtains/gui/outdoor_bedroom_curtain.png


Directories/files structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  example-curtains

    :ref:`configuration.ini <configuration.ini>`

    :ref:`appliances.yaml <appliances.yaml>`

    performer

      curtains

         :ref:`indoor_blackout.yaml <indoor_blackout.yaml>`

         :ref:`outdoor.yaml <outdoor.yaml>`

         :ref:`outdoor_bedroom.yaml <outdoor.yaml>`

     sensors

         :ref:`lux.yaml <lux.yaml>`

         :ref:`wind.yaml <wind.yaml>`

    performers

      :ref:`curtains.yaml <curtains.yaml>`

    scheduler_triggers

      :ref:`calendar.yaml <st_calendar.yaml>`

      :ref:`sensors.yaml <st_sensors.yaml>`

      :ref:`sun.yaml <st_sun.yaml>`

    scheduler

      :ref:`calendar.yaml <s_calendar.yaml>`

      :ref:`sensors.yaml <s_sensors.yaml>`

      :ref:`sun.yaml <s_sun.yaml>`

.. raw:: latex

    \clearpage

Files
^^^^^

configuration.ini
"""""""""""""""""

.. _configuration.ini:

.. literalinclude:: ../../../homino/example-curtains/configuration.ini

appliances.yaml
"""""""""""""""

.. _appliances.yaml:

.. literalinclude:: ../../../homino/example-curtains/appliances.yaml

performer/curtains/indoor_blackout.yaml
"""""""""""""""""""""""""""""""""""""""

.. _indoor_blackout.yaml:

.. literalinclude:: ../../../homino/example-curtains/performer/curtains/indoor_blackout.yaml

performer/curtains/outdoor.yaml
""""""""""""""""""""""""""""""""""""""""

.. _outdoor.yaml:

.. literalinclude:: ../../../homino/example-curtains/performer/curtains/outdoor.yaml

performer/curtains/outdoor_bedroom.yaml
""""""""""""""""""""""""""""""""""""""""

.. _outdoor_bedroom.yaml:

.. literalinclude:: ../../../homino/example-curtains/performer/curtains/outdoor_bedroom.yaml

performer/sensors/lux.yaml
"""""""""""""""""""""""""""

.. _lux.yaml:

.. literalinclude:: ../../../homino/example-curtains/performer/sensors/lux.yaml

performer/sensors/wind.yaml
"""""""""""""""""""""""""""

.. _wind.yaml:

.. literalinclude:: ../../../homino/example-curtains/performer/sensors/wind.yaml

performers/curtains.yaml
""""""""""""""""""""""""

.. _curtains.yaml:

.. literalinclude:: ../../../homino/example-curtains/performers/curtains.yaml


scheduler_triggers/calendar.yaml
""""""""""""""""""""""""""""""""

.. _st_calendar.yaml:

.. literalinclude:: ../../../homino/example-curtains/scheduler_triggers/calendar.yaml

scheduler_triggers/sensors.yaml
""""""""""""""""""""""""""""""""

.. _st_sensors.yaml:

.. literalinclude:: ../../../homino/example-curtains/scheduler_triggers/sensors.yaml

scheduler_triggers/sun.yaml
""""""""""""""""""""""""""""""""

.. _st_sun.yaml:

.. literalinclude:: ../../../homino/example-curtains/scheduler_triggers/sun.yaml

scheduler/calendar.yaml
""""""""""""""""""""""""""""""""

.. _s_calendar.yaml:

.. literalinclude:: ../../../homino/example-curtains/scheduler/calendar.yaml

scheduler/sensors.yaml
""""""""""""""""""""""""""""""""

.. _s_sensors.yaml:

.. literalinclude:: ../../../homino/example-curtains/scheduler/sensors.yaml

scheduler/sun.yaml
""""""""""""""""""""""""""""""""

.. _s_sun.yaml:

.. literalinclude:: ../../../homino/example-curtains/scheduler/sun.yaml

.. raw:: latex

    \clearpage

