Energy Guard Sockets Project Example
====================================

This example project automates one kind of *Appliance* an **energy guard socket**.
The automated devices are 2 knx switches.

The **energy guard socket** is a :ref:`socket.energy_guard.Appliance Appliance <socket.energy_guard.Appliance>`.

Once the detach logic for a socket is turned on (and the socket goes into a *detachable* state) a warning message is sent to the user through home assistant.

The sockets are turned off one by one when energy consumption is too high for too much time.

There are two levels of allowed overconsumption; the lower level of overconsumption is allowed for a longer period of time.

To automate the sockets a power sensor is used: :ref:`sensor.powermeter.Appliance Appliance <sensor.powermeter.Appliance>`.

The *protocol triggers* and *protocol commands* in this example project are **inverted** because *the loads* are on when the switches are off and *the loads* are off when the switches are on.

.. raw:: latex

    \clearpage


Directories/files structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  example-lights

    :ref:`configuration.ini <configuration_energy.ini>`

    :ref:`appliances.yaml <appliances_energy.yaml>`

    performer

      sensors

         :ref:`power.yaml <power_energy.yaml>`

      sockets

           :ref:`energy_guard.yaml <energy_guard.yaml>`

    performers

      :ref:`energy_guard.yaml <energy_guard_performers.yaml>`

    scheduler_triggers

      :ref:`energy_guard_scheduler_triggers.yaml <energy_guard_scheduler_triggers.yaml>`

    scheduler

      :ref:`energy_guard_scheduler.yaml <energy_guard_scheduler.yaml>`

.. raw:: latex

    \clearpage

Files
^^^^^

configuration.ini
"""""""""""""""""

.. _configuration_energy.ini:

.. literalinclude:: ../../../homino/example-energy-guard/configuration.ini

appliances.yaml
"""""""""""""""

.. _appliances_energy.yaml:

.. literalinclude:: ../../../homino/example-energy-guard/appliances.yaml

performer/sensors/power.yaml
"""""""""""""""""""""""""""""

.. _power_energy.yaml:

.. literalinclude:: ../../../homino/example-energy-guard/performer/sensors/power.yaml

performer/sockets/energy_guard.yaml
"""""""""""""""""""""""""""""""""""""""

.. _energy_guard.yaml:

.. literalinclude:: ../../../homino/example-energy-guard/performer/sockets/energy_guard.yaml

performers/energy_guard.yaml
""""""""""""""""""""""""""""

.. _energy_guard_performers.yaml:

.. literalinclude:: ../../../homino/example-energy-guard/performers/energy_guard.yaml

scheduler_triggers/energy_guard.yaml
"""""""""""""""""""""""""""""""""""""

.. _energy_guard_scheduler_triggers.yaml:

.. literalinclude:: ../../../homino/example-energy-guard/scheduler_triggers/energy_guard.yaml

scheduler/energy_guard.yaml
""""""""""""""""""""""""""""""

.. _energy_guard_scheduler.yaml:

.. literalinclude:: ../../../homino/example-energy-guard/scheduler/energy_guard.yaml

