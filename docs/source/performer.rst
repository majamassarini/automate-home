Performer and Protocols
=======================

A **Performer** is the entity that binds together an *Appliance*, its **protocol commands** and its **protocol triggers**.

**Protocol commands** create protocol messages for one or more physical devices realizing the *Appliance*.
**Protocol triggers** map protocol messages from one or more physical devices to *events* for the realized *Appliance*.

*Performers* translate received protocol messages to **events** for an *Appliance* through *protocol triggers*.
When an *Appliance* has changed its *State*, *Performers* translate the **transaction** from an
*old Appliance State* to a *new Appliance State* in a list of protocol messages through *protocol commands*.

.. tip::
  Many commands and triggers can be grouped together inside the same *Performer*.

  When a trigger inside a *Performer* is triggered then the commands belonging to the same *Performer* are executed::

    - !Performer
      name: "sonos relative volume command up"
      for appliance: "a sound player"
      triggers:
      - !knx_plugin.trigger.dpt_control_dimming.step.up.Trigger {addresses: [0x0C09]}
      commands:
        - !soco_plugin.command.volume.relative.Command {addresses: ["Bath"], fields: {"delta": 10}}

    - !Performer
      name: "sonos relative volume command down"
      for appliance: "a sound player"
      triggers:
      - !knx_plugin.trigger.dpt_control_dimming.step.down.Trigger {addresses: [0x0C09]}
      commands:
        - !soco_plugin.command.volume.relative.Command {addresses: ["Bath"], fields: {"delta": -10}}

The above yaml syntax groups together an appliance named *a sound player* with some *KNX* protocol triggers and some
*Sonos* protocol commands (using the soco library).

When a KNX push button, with address 0x0C09, is pressed to send a DPT_Control_Dimming step up then the *Performer* named
*sonos relative volume command up* will create a message to increase volume by 10 for a Sonos device named *Bath*.

When a KNX push button, with address 0x0C09, is pressed to send a DPT_Control_Dimming step down message then the *Performer* named
*sonos relative volume command down* will create a message to decrease volume by 10 for a Sonos device named *Bath*.

.. tip::
  Yaml syntax uses *Performers* to define :ref:`Scheduler triggers<scheduler-triggers>`
  it is easier to use and re-use a *Performer* when it has few triggers or commands.

  Use multiple *Performers* instead of grouping together many commands and triggers when
  the *Performers* are thought to be used by *Scheduler Triggers*.

.. note::
  The **home** package has only an **abstract definition for every entity in the home.protocol package**.

Implementations are found in external packages, one for every protocol.

Right now, available protocol plugins are:

    - knx_plugin
    - lifx_plugin
    - sonos_plugin
    - home_assistant_plugin

.. raw:: latex

    \clearpage

Performer (Class Diagram)
-------------------------

.. raw:: latex
    :file: ./latex/performer_class_diagram.tex

.. only:: html

  .. figure:: ./latex/performer_class_diagram.tex.svg
    :align: center

.. raw:: latex

    \clearpage


Protocol Triggers
-----------------

Every time the system receives a message through one of its *Protocol Gateways* the message is checked against compatible *Protocol Triggers*.

When a *Protocol Trigger* is triggered all the *Performers* which own it will
potentially notify related **events** to their *Appliances*.

*Protocol Triggers* can be triggered for many different reasons:

 - a defined **kind** of protocol message is arrived
 - a **number** of defined **kinds** of protocol messages are arrived
 - a **mean** value for some protocol messages values has been reached
 - a protocol message value is **greater than**, **smaller than** or **in between** some other given value
 - a mix of the above conditions is met
 - and so on

A *Protocol Trigger* owns a list of *Events* which are used when it has been triggered.

Returned *Events* can be obtained applying functions to data collected in the trigger: values in the payload, a mean of multiple messages values, a count of messages and so on.

.. raw:: latex

    \clearpage

Performers and Protocol Triggers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: latex
    :file: ./latex/performer_protocol_trigger_component_diagram.tex

.. only:: html

  .. figure:: ./latex/performer_protocol_trigger_component_diagram.tex.svg
    :align: center

.. raw:: latex

    \clearpage

Update an Appliance state when a protocol message is received
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: latex
    :file: ./latex/event_from_protocol_sequence_diagram.tex


.. only:: html

  .. figure:: ./latex/event_from_protocol_sequence_diagram.tex.svg
    :align: center

.. raw:: latex

    \clearpage

Lux value changed example
^^^^^^^^^^^^^^^^^^^^^^^^^

A really simple trigger, which is triggered by any knx received message on address 0xAAAA containing a lux value,
can be used to always update the measured value inside an *Appliance* representing a lux sensor::

  - !Performer
    name: "sun lux sensor trigger"
    for appliance: "sun lux sensor"
    commands: []
    triggers:
    - !knx_plugin.trigger.dpt_value_lux.Always {addresses: [0xAAAA]}

The following is a simple, always updating, KNX Trigger::

  >>> knx_plugin.trigger.dpt_value_lux.Always.make([0xAAAA, ])

.. autoclass:: knx_plugin.trigger.dpt_value_lux.Always
   :show-inheritance:
   :undoc-members:

.. raw:: latex
    :file: ./latex/scenario_lux_sensor.tex

.. only:: html

  .. figure:: ./latex/scenario_lux_sensor.tex.svg
    :align: center

.. raw:: latex

    \clearpage

Sun brightness is high example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A slightly more complex trigger that can be used to notify a *sun is bright event*
to some *Appliance* sensible to a *home.event.sun.Bright* event::

  >>> knx_plugin.trigger.dpt_value_lux.Bright.make([0xAAAA, ])

.. autoclass:: knx_plugin.trigger.dpt_value_lux.Bright
   :show-inheritance:
   :undoc-members:

Light is forced on example
^^^^^^^^^^^^^^^^^^^^^^^^^^

When a button is pressed by the user to turn on the light then
the user is saying to the system:

hei, I want the light to stay turned on, do not touch it.

The following is a simple KNX Trigger with a *forcing on* event notified every time
a *on message* on address 0xBBBB through the knx protocol is received::

  >>> knx_plugin.trigger.dpt_switch.On.make([0xBBBB, ], [home.appliance.light.event.forced.Event.On,])

.. autoclass:: knx_plugin.trigger.dpt_switch.On
   :show-inheritance:
   :undoc-members:

.. raw:: latex
    :file: ./latex/scenario_light_trigger.tex

.. only:: html

  .. figure:: ./latex/scenario_light_trigger.tex.svg
    :align: center

.. raw:: latex

    \clearpage


Protocol Commands
-----------------

The *Protocol Commands* are those entities which translate the *Abstract Appliance State* in a protocol message which is able, for example, to turn on or off a device.

A *Performer* asks to its *Protocol Commands* to create, if needed, the protocol messages suited to be sent through the *Protocol Gateways* every time the *Appliance* state is changed by the system.


Performer and Protocol Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: latex
    :file: ./latex/performer_protocol_command_component_diagram.tex

.. only:: html

  .. figure:: ./latex/performer_protocol_command_component_diagram.tex.svg
    :align: center

.. raw:: latex

    \clearpage


Adjust lifx bulb color when knx switch is turned on example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Protocol Commands* inside a *Performer* are always executed when the *Appliance State* is changed by a *Protocol Trigger* in the **same** *Performer*::

    - !Performer
      name: "adjust lifx bulb color when turned on"
      for appliance: "a lifx bulb"
      triggers:
      - !knx_plugin.trigger.dpt_switch.On.make([0xBBBB, ], [home.appliance.light.event.forced.Event.On,])
      commands:
        - !lifx_plugin.command.SetColor {addresses: [["172.31.10.245", 56700]]}


.. raw:: latex
    :file: ./latex/scenario_lifx_command_one_performer.tex

.. only:: html

  .. figure:: ./latex/scenario_lifx_command_one_performer.tex.svg
    :align: center

.. raw:: latex

    \clearpage

Adjust lifx bulb color a few seconds later the knx switch is turned on example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A *Performer Command* will send a message to bus few seconds later a *Protocol Trigger* is triggered if
a *Scheduler Trigger* owning the *Performer Trigger* has been **scheduled** with the *Performer Command* as a target::

    - !Performer
      name: "force on a lifx bulb"
      for appliance: "a lifx bulb"
      triggers:
      - !knx_plugin.trigger.dpt_switch.On.make([0xBBBB, ], [home.appliance.light.event.forced.Event.On,])
      commands: []
    - !Performer
      name: "set color for a lifx bulb"
      for appliance: "a lifx bulb"
      triggers: []
      commands:
      - !lifx_plugin.command.SetColor {addresses: [["172.31.10.245", 56700]]}
   - !protocol.delay.Trigger
     name: "adjust lifx bulb color"
     notify more events: []
     when triggered performers: "force on a lifx bulb"
     and timeout expires: 3
   - !schedule
     trigger: "adjust lifx bulb color"
     for performers: "set color for a lifx bulb"

.. raw:: latex
    :file: ./latex/scenario_lifx_command_multiple_performers.tex

.. only:: html

  .. figure:: ./latex/scenario_lifx_command_multiple_performers.tex.svg
    :align: center

.. raw:: latex

    \clearpage

.. autoclass:: knx_plugin.command.dpt_switch.OnOff
   :show-inheritance:
   :undoc-members:


.. autoclass:: lifx_plugin.command.SetColor
   :show-inheritance:


Appliances and Performers reusability
--------------------------------------

When an *Appliance* model has been defined together with the *Performers* that can change its state then
both the *Appliance* and the *Performers* can be **easily reused simply changing
Protocol Triggers and Protocol Commands** and, if needed, customizing *Appliance* and *Performers* names.

.. raw:: latex

    \clearpage


Performer Class
---------------

.. autoclass:: home.Performer

.. raw:: latex

    \clearpage

protocol.Description Class
--------------------------

.. autoclass:: home.protocol.Description

.. raw:: latex

    \clearpage

protocol.Trigger Class
----------------------

.. autoclass:: home.protocol.Trigger

.. raw:: latex

    \clearpage

protocol.Command Class
----------------------

.. autoclass:: home.protocol.Command

.. raw:: latex

    \clearpage

protocol.Gateway Class
----------------------

.. autoclass:: home.protocol.Gateway

.. raw:: latex

    \clearpage

