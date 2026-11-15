Performer and Protocols
=======================

A **Performer** is the entity that binds together an *Appliance*, its **protocol commands** and its **protocol triggers**.

**Protocol commands** create protocol messages for one or more physical devices realizing the *Appliance*.
**Protocol triggers** map protocol messages from one or more physical devices to *events* for the realized *Appliance*.

*Performers* translate received protocol messages to **events** for an *Appliance* through *protocol triggers*.
When an *Appliance* changes its *State*, *Performers* translate the **transition** from the
*old Appliance State* to the *new Appliance State* into a list of protocol messages via *protocol commands*.

How the commands run
--------------------

**Triggers change the appliance state; the state change drives the commands.**

Every state change of an *Appliance*, whatever caused it (a protocol trigger, a
:ref:`scheduler trigger<scheduler-triggers>`, a change from the web UI received through Redis), runs the
commands of **every** *Performer* of that *Appliance*. Each command decides what to send from the
*old* and the *new* state alone: it sends only when the property it controls (``is_on``, ``volume``,
``playlist``, ``play_mode``, ``group``, ``setpoint`` …) has changed, or, for an idempotent
command that applies the current state (e.g. a color), whenever the appliance is in a state that needs it.

When the change comes from a device reporting its own state (a Sonos play or volume echo, a KNX status on the
address the commands write to), the commands for that same device are left out: the device already has the
change, and sending it back would be an echo. See :py:meth:`home.protocol.Description.reaches_a_device_of`.

Designing performers
--------------------

Keep the two roles in separate *Performers*:

- a **trigger performer** has protocol triggers that send named events, and no commands;
- a **command performer** has protocol commands, and no triggers. Usually there is one per *Appliance*,
  listing its commands in the order the device needs them.

::

    - !Performer
      name: "sonos triggers"
      for appliance: "a sound player"
      triggers:
      - !knx_plugin.trigger.dpt_switch.On
        addresses: [0x0C08]
        events:
        - !home.appliance.sound.player.event.forced.Event.On
      - !knx_plugin.trigger.dpt_control_dimming.VolumeStep {addresses: [0x0C09]}
      commands: []

    - !Performer
      name: "sonos commands"
      for appliance: "a sound player"
      triggers: []
      commands:
      - !soco_plugin.command.mode.Command {addresses: ["Bath"]}
      - !soco_plugin.command.playlist.Command {addresses: ["Bath"]}
      - !soco_plugin.command.volume.absolute.Command {addresses: ["Bath"]}
      - !soco_plugin.command.play.Command {addresses: ["Bath"]}
      - !soco_plugin.command.pause.Command {addresses: ["Bath"]}

When a KNX push button with address 0x0C08 is pressed, the sound player is forced on and the
*sonos commands* send its play mode, playlist, volume and play. When the dimming button 0x0C09 is
pressed, the volume of the current state goes up or down and *volume.absolute* sends it.

To send something only in particular circumstances, make those circumstances part of the
*Appliance* state: a trigger or a scheduler trigger sends an event that sets a property, and the
command reacts to that property. If the *Appliance* has no property for it, add one to the
*Appliance* type; don't add a "when" field to a protocol command and don't send an event that
doesn't change the state only to make a *Performer* run.

What goes wrong otherwise
^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------+
| Design mistake                                | What happens                                                  |
+===============================================+===============================================================+
| A command that sends every time it runs       | It fires on every state change of the appliance: a volume     |
|                                               | change regroups the speakers or restarts the playlist.        |
+-----------------------------------------------+---------------------------------------------------------------+
| A relative command (e.g. a volume delta)      | The appliance never knows the device value: the next absolute |
|                                               | command, or the web UI, jumps back to the old value.          |
+-----------------------------------------------+---------------------------------------------------------------+
| An event sent only to make a performer run    | It doesn't change the state, so no command runs because of it,|
|                                               | and nothing records it.                                       |
+-----------------------------------------------+---------------------------------------------------------------+
| A "when" field in a protocol command          | The protocol plugin depends on one home's use cases and the   |
| (e.g. the name of a state)                    | command breaks in any other situation.                        |
+-----------------------------------------------+---------------------------------------------------------------+
| A property event of another state             | The value changes in a state that isn't in use: the device    |
|                                               | never changes, and nothing logs an error.                     |
+-----------------------------------------------+---------------------------------------------------------------+

.. note::
  The **home** package has only an **abstract definition for every entity in the home.protocol package**.

Implementations are found in external packages, one per protocol.

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

Every time the system receives a message through one of its *Protocol Gateways*, the message is checked against compatible *Protocol Triggers*.

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

Returned *Events* can be obtained by applying functions to data collected in the trigger: values from the payload, a mean of multiple message values, a count of messages, and so on.

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

hey, I want the light to stay on — don't touch it.

The following is a simple KNX Trigger with a *forcing on* event notified every time
an *on message* on address 0xBBBB is received through the KNX protocol::

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

A *Performer Command* will send a message to the bus a few seconds after a *Protocol Trigger* is activated,
if a *Scheduler Trigger* that references the *Protocol Trigger* has been **scheduled** with the *Performer Command* as a target::

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
both the *Appliance* and the *Performers* can be **easily reused by simply changing the
Protocol Triggers and Protocol Commands** and, if needed, customizing the *Appliance* and *Performer* names.

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

