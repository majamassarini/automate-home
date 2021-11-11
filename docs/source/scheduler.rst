.. _scheduler-triggers:

Scheduler and Triggers
======================

The system has a **scheduler**.

The system scheduler has just one job: it notifies *Events* gathered from
a triggered *Scheduler Trigger* to the specified *Performers*.
The *Protocol Commands* inside the specified *Performers* will be executed
just after the *Events* are being notified to their *Appliances*.

.. hint::
  **Scheduler Triggers are not Protocol Triggers**.

  But, both *Scheduler Triggers* and *Protocol Triggers* have *Events* to be notified.

  *Scheduler Triggers* can use *Protocol Triggers* to define themselves.

.. raw:: latex

    \clearpage

Scheduler Trigger vs Protocol Triggers
--------------------------------------

Time based triggers
^^^^^^^^^^^^^^^^^^^

You need to use a *Scheduler Trigger* instead of a *Protocol Trigger* when the trigger logic is **time based**.

Suppose you need a mean for a lux value and suppose your device is sending lux data every time the lux is changing.

You can calculate a mean using a protocol trigger: this trigger will be highly sensible to lux changes.

Or you can calculate a **time based** mean using a scheduler trigger: this trigger will be less sensible to lux changes.

Reusable triggers
^^^^^^^^^^^^^^^^^

If you want to define a trigger once and **reuse it with multiple performers** then you need a *Scheduler Trigger*.

A trigger associated with a lux sensor is probably useful for multiple *Appliances*. All the project's
curtains and lights models may need to know the sun brightness level.

Instead of creating one protocol trigger in a performer for every curtain and light,
a single scheduler trigger using a performer with just one protocol trigger can be scheduled.

State triggers
^^^^^^^^^^^^^^

If you need a trigger for the *Appliance* state you need a *Scheduler Trigger*.

If you need to know if the *Appliance* has entered a new state
or exited an old state then you need a schedule trigger.


Scheduler (Class Diagram)
-------------------------

.. raw:: latex
    :file: ./latex/scheduler_class_diagram.tex

.. only:: html

  .. figure:: ./latex/scheduler_class_diagram.tex.svg
    :align: center

.. raw:: latex

    \clearpage

.. raw:: latex

    \clearpage

Scheduler (Sequence Diagram)
----------------------------

.. raw:: latex
    :file: ./latex/scheduler_event_sequence_diagram.tex

.. only:: html

  .. figure:: ./latex/scheduler_event_sequence_diagram.tex.svg
    :align: center

.. raw:: latex

    \clearpage

Trigger Class
-------------

.. autoclass:: home.scheduler.Trigger
   :no-members:

.. raw:: latex

    \clearpage

cron.Trigger
--------------------

.. autoclass:: home.scheduler.trigger.cron.Trigger
   :no-members:

Example
^^^^^^^^^^^^
The following is a *Scheduler Trigger* triggered from Monday to Friday
at 7:15 am.

It has one event: *home.event.sleepiness.Event.Awake*.
If notified to a curtain *Appliance* will probably raise the curtain::

  !cron.Trigger
    name: "wakeup time scheduler trigger"
    notify events:
      - !home.event.sleepiness.Event.Awake
    day_of_week: "mon-fri"
    hour: 7
    minute: 15

The *Scheduler Trigger* is scheduled with the specified *Performers* through this syntax::

  !schedule
    trigger: "wakeup time scheduler trigger"
    for performers: "curtain command performer"

The *Performer* is defined like this::

  !Performer
    name: "curtain command performer"
    for appliance: "a curtain appliance"
    commands:
    - !knx_plugin.command.dpt_updown.UpDown {addresses: [0x1111,]}
    triggers: []

If needed, a list of *Performers* can be created::

  curtain commands:
  - "curtain command performer"
  - "another curtain command performer"

And could be scheduled with the *Scheduler Trigger*::

  !schedule
    trigger: "wakeup time scheduler trigger"
    for performers: "curtain commands"

.. raw:: latex

    \clearpage

interval.Trigger
--------------------

.. autoclass:: home.scheduler.trigger.interval.Trigger
   :no-members:

Example
^^^^^^^^^^^^

This *Scheduler Trigger* can be used, for example, to poll a device state every specified interval of time.

To continuously poll a device, the *Protocol Command* used by the *Performer*, should, probably, ignore the
*Appliance State* and **always build a command Description** for the *Protocol Gateway* to poll the device state.

.. raw:: latex

    \clearpage

date.Trigger
--------------------

.. autoclass:: home.scheduler.trigger.date.Trigger
   :no-members:

.. raw:: latex

    \clearpage

sun.sunrise.Trigger
--------------------

.. autoclass:: home.scheduler.trigger.sun.sunrise.Trigger
   :no-members:

Example
^^^^^^^^^^^^
::

  !sun.sunrise.Trigger
    name: "sunrise scheduler trigger"
    notify more events: []
    latitude: 44.00
    longitude: 12.00
    elevation: 280

.. raw:: latex

    \clearpage

sun.twilight.civil.sunrise.Trigger
----------------------------------

.. autoclass:: home.scheduler.trigger.sun.twilight.civil.sunrise.Trigger
   :no-members:

Example
^^^^^^^^^^^^
::

  !sun.twilight.civil.Trigger
    name: "start of morning twilight scheduler trigger"
    notify more events: []
    latitude: 44.00
    longitude: 12.00
    elevation: 280

.. raw:: latex

    \clearpage

sun.sunset.Trigger
--------------------

.. autoclass:: home.scheduler.trigger.sun.sunset.Trigger
   :no-members:

Example
^^^^^^^^^^^^
::

  !sun.sunset.Trigger
    name: "sunset scheduler trigger"
    notify more events: []
    latitude: 44.00
    longitude: 12.00
    elevation: 280


.. raw:: latex

    \clearpage

sun.twilight.civil.sunset.Trigger
---------------------------------

.. autoclass:: home.scheduler.trigger.sun.twilight.civil.sunset.Trigger
   :no-members:

Example
^^^^^^^^^^^^
::

  !sun.twilight.civil.sunset.Trigger
    name: "end of civil twilight scheduler trigger"
    notify more events: []
    latitude: 44.00
    longitude: 12.00
    elevation: 280

.. raw:: latex

    \clearpage

sun.sunhit.Trigger
--------------------

.. autoclass:: home.scheduler.trigger.sun.sunhit.Trigger
   :no-members:

Example
^^^^^^^^^^^^

This trigger could be used, when you do not have an internal lux sensor,
to approximate the time of day when the sun is entering from a window::

  !sun.sunhit.Trigger
    name: "sun hit east exposed window"
    notify more events: []
    latitude: 45
    longitude: 12
    elevation: 800
    position: !Position {bottom_altitude: 10, upper_altitude: 90, min_azimuth: 45, max_azimuth: 135}

  !sun.sunhit.Trigger
    name: "sun hit sud exposed window"
    notify more events: []
    latitude: 45
    longitude: 12
    elevation: 800
    position: !Position {bottom_altitude: 10, upper_altitude: 90, min_azimuth: 135, max_azimuth: 225}

  !sun.sunhit.Trigger
    name: "sun hit west exposed window"
    notify more events: []
    latitude: 45
    longitude: 12
    elevation: 800
    position: !Position {bottom_altitude: 10, upper_altitude: 90, min_azimuth: 225, max_azimuth: 315}

.. raw:: latex

    \clearpage

sun.sunleft.Trigger
--------------------

.. autoclass:: home.scheduler.trigger.sun.sunleft.Trigger
   :no-members:

Example
^^^^^^^^^^^^

This trigger should probably be used every time you use a sun.sunhit.Trigger.

Its definition is like the following::

  !sun.sunleft.Trigger
    name: "sun left east exposed window"
    notify more events: []
    latitude: 45
    longitude: 12
    elevation: 800
    position: !Position {bottom_altitude: 10, upper_altitude: 90, min_azimuth: 20, max_azimuth: 145}

.. raw:: latex

    \clearpage

protocol.Trigger
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.Trigger
   :no-members:

Example
^^^^^^^^^^^^

An example showing how *curtain Appliances* can be notified of a *strong wind Event* through a KNX message.

The *Protocol Trigger* is bound with the *anemometer Appliance* through the following Performer::

  !Performer
    name: "strong wind performer"
    for appliance: "anemometer"
    commands: []
    triggers:
    - !knx_plugin.trigger.dpt_value_wsp.Strong {addresses: [0xAAAA,], events: [home.event.wind.Event.Strong,]}

A *Protocol Scheduler Trigger* is built for the *Protocol Trigger* found in the above *Performer*::

  !protocol.Trigger
    name: "strong wind scheduler trigger"
    notify more events: []
    when triggered performers: "strong wind performer"


The *Scheduler Trigger* is scheduled to notify events to the curtains::

  !schedule
    trigger: "strong wind performer"
    for performers: "curtain commands"

.. raw:: latex

    \clearpage

protocol.delay.Trigger
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.delay.Trigger
   :no-members:

Example
^^^^^^^^^^^^

An example showing how a Light can be potentially turned Off
seconds after a movement sensor is no more triggered

The *Protocol Trigger* is bound with the *movement sensor Appliance* through the following Performer::

  !Performer
    name: "courtesy off performer"
    for appliance: "movement sensor"
    commands: []
    triggers:
    - !knx_plugin.trigger.dpt_switch.Off {addresses: [0xBBBB,], events: [home.event.courtesy.Event.Off,]}

A *Protocol Scheduler Trigger* is built for the *Protocol Trigger* found in the above *Performer*::

  !protocol.delay.Trigger
    name: "courtesy off scheduler trigger"
    notify more events: []
    when triggered performers: "courtesy off performer"
    and timeout expires: 180

The *Scheduler Trigger* is scheduled to notify events to the lights::

  !schedule
    trigger: "courtesy off scheduler trigger"
    for performers: "lights commands"

.. raw:: latex

    \clearpage

protocol.enum.Trigger
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.enum.Trigger
   :no-members:

Example
^^^^^^^

Choose a user (A/B/C), using a knx up/down button, to select a playlist for a sound player.

Define *Performers* and  *Protocol Triggers*::

  - !Performer
    name: "next user button"
    for appliance: "a sound player"
    triggers:
      - !knx_plugin.trigger.dpt_updown.Up { addresses: [ 0x0C0A ] }
    commands: [ ]

  - !Performer
    name: "previous user button"
    for appliance: "a sound player"
    triggers:
      - !knx_plugin.trigger.dpt_updown.Down { addresses: [ 0x0C0A ] }
    commands: [ ]

Define *Scheduler Triggers*::

  - !protocol.enum.Trigger
    name: "choose next user bagno"
    notify more events: []
    plus selected event: !home.event.user.Event.A
    or: "next"
    when triggered performers: "next user button"

  - !protocol.enum.Trigger
    name: "choose previous user"
    notify more events: []
    plus selected event: !home.event.user.Event.A
    or: "previous"
    when triggered performers: "previous user button"

Schedule the *Scheduler Triggers*::

  - !schedule
    trigger: "choose next user bagno"
    for performers: "comandi sonos bagno"

  - !schedule
    trigger: "choose previous user bagno"
    for performers: "comandi sonos bagno"

.. raw:: latex

    \clearpage

protocol.mean.Trigger
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.mean.Trigger
   :no-members:

.. raw:: latex

    \clearpage

protocol.mean.LesserThan
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.mean.LesserThan
   :no-members:

Example
^^^^^^^

Calculate mean value for wind speed in a time base of 60 seconds. Notify when speed is weak.

Define the trigger *Performer*, using an home assistant sensor::

  - !Performer
    name: "wind performer"
    for appliance: "anemometer"
    commands: []
    triggers:
      - !home_assistant_plugin.service.sensor.float.trigger.Always {entity_id: "sensor.wind_speed"}

Define the *Scheduler Trigger*::

  - !protocol.mean.LesserThan
    name: "weak wind trigger"
    notify more events:
      - !home.event.wind.Event.Weak
    when triggered performers: "wind performer"
    num of samples: 5
    hit value: 1
    timeout seconds: 60

Schedule the *Scheduler Trigger*::

  - !schedule
    trigger: "weak wind trigger"
    for performers: "a curtain command performer"

.. raw:: latex

    \clearpage

protocol.mean.GreaterThan
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.mean.GreaterThan
   :no-members:

Example
^^^^^^^

Calculate mean value for sun brightness in a time base of 60 seconds. Notify when brightness is high.

Define the trigger *Performer*, using a knx sensor::

  - !Performer
    name: "luxmeter"
    for appliance: "luxmeter"
    commands: []
    triggers:
    - !knx_plugin.trigger.dpt_value_lux.Always {addresses: [0x0A04]}

Define the *Scheduler Trigger*::

  - !protocol.mean.GreaterThan
    name: "sun is bright (slowly changing)"
    notify more events:
      - !home.event.sun.brightness.Event.Bright
    when triggered performers: "luxmeter"
    num of samples: 250
    hit value: 40000
    timeout seconds: 60

Schedule the *Scheduler Trigger*::

  - !schedule
    trigger: "sun is bright (slowly changing)"
    for performers: "a curtain command performer"

.. raw:: latex

    \clearpage

protocol.mean.InBetween
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.mean.InBetween
   :no-members:

.. raw:: latex

    \clearpage

protocol.multi.Trigger
--------------------------

.. autoclass:: home.scheduler.trigger.protocol.multi.Trigger
   :no-members:

.. raw:: latex

    \clearpage

circadian_rhythm.Trigger
--------------------------

.. autoclass:: home.scheduler.trigger.circadian_rhythm.Trigger
   :no-members:

Example
^^^^^^^^^^^^

An example showing how the temperature's Light could be adjusted during the day::

  !circadian_rhythm.Trigger
  name: "adjust light temperature during the day"
  events: []
  events_in_a_day:
    - !light.event.circadian_rhythm.temperature.Event { value: 2700 }
    - !light.event.circadian_rhythm.temperature.Event { value: 2700 }
    - !light.event.circadian_rhythm.temperature.Event { value: 3600 }
    - !light.event.circadian_rhythm.temperature.Event { value: 4600 }
    - !light.event.circadian_rhythm.temperature.Event { value: 5600 }
    - !light.event.circadian_rhythm.temperature.Event { value: 6500 }
    - !light.event.circadian_rhythm.temperature.Event { value: 6500 }
    - !light.event.circadian_rhythm.temperature.Event { value: 5600 }
    - !light.event.circadian_rhythm.temperature.Event { value: 4600 }
    - !light.event.circadian_rhythm.temperature.Event { value: 3600 }
    - !light.event.circadian_rhythm.temperature.Event { value: 2700 }
    - !light.event.circadian_rhythm.temperature.Event { value: 2700 }

A *Protocol Command* is linked with the *lifx bulb Appliance* through the following Performer::

  !Performer
    name: "lifx bulb command"
    for appliance: "lifx bulb"
    commands:
      - !lifx_plugin.command.SetColor {addresses: [["172.31.10.245", 56700]]}
    triggers: []

The *Scheduler Trigger* is scheduled to notify events to the light::

  !schedule
    trigger: "adjust light temperature during the day"
    for performers: "lifx bulb command"


.. raw:: latex

    \clearpage

state.entering.Trigger
----------------------

.. autoclass:: home.scheduler.trigger.state.entering.Trigger
   :no-members:

Example
^^^^^^^

Set the lowest possible volume when entering *Fade In* state in a sound player.

Define the *Scheduler Trigger*::

  - !state.entering.delay.Trigger
    name: "fade in vol 1"
    notify events:
      - !sound.player.event.fade_in.volume.Event { value: 1 }
    when appliance state became: "Fade In"

Schedule the *Scheduler Trigger*::

  - !schedule
    trigger: "fade in vol 1"
    for performers: "fade sonos"

Define the *Performer* used by the scheduler::

  - !Performer
    name: "fade sonos"
    for appliance: "sonos bagno"
    commands:
      - !soco_plugin.command.volume.ramp.Command { addresses: [ "Bagno" ], fields: { "ramp_type": 'SLEEP_TIMER_RAMP_TYPE' } }
    triggers: [ ]

.. raw:: latex

    \clearpage

state.entering.delay.Trigger
----------------------------

.. autoclass:: home.scheduler.trigger.state.entering.delay.Trigger
   :no-members:

Example
^^^^^^^

Ramp up the volume when entering *Fade In* state in a sound player.

Define the *Scheduler Trigger*::

  - !state.entering.delay.Trigger
    name: "fade in vol 5"
    notify events:
      - !sound.player.event.fade_in.volume.Event { value: 5 }
    when appliance state became: "Fade In"
    and timeout expires: 10

Schedule the *Scheduler Trigger*::

  - !schedule
    trigger: "fade in vol 5"
    for performers: "fade sonos"

Define the *Performer* used by the scheduler::

  - !Performer
    name: "fade sonos"
    for appliance: "sonos bagno"
    commands:
      - !soco_plugin.command.volume.ramp.Command { addresses: [ "Bagno" ], fields: { "ramp_type": 'SLEEP_TIMER_RAMP_TYPE' } }
    triggers: [ ]


.. raw:: latex

    \clearpage

state.entering.delay.duration.Trigger
-------------------------------------

.. autoclass:: home.scheduler.trigger.state.entering.delay.duration.Trigger
   :no-members:

Example
^^^^^^^

Turn off a sprinkler, through a knx switch, after a *variable time*, timeout starts when the *Sprinkler Appliance state became "On"*.
The time is expressed by the *Appliance state through its duration property*.

Define the *Scheduler Trigger*::

  - !state.entering.delay.duration.Trigger
    name: "disable sprinkler"
    notify events:
      - !home.event.enable.Event.Off
    when appliance state became (and appliance state duration elapsed): "On"

Schedule the *Scheduler Trigger*::

  - !schedule
    trigger: "disable sprinkler"
    for performers: "sprinkler command performer"

Define the *Performer* used by the scheduler::

  - !Performer
    name: "sprinkler command performer"
    for appliance: "a sprinkler"
    commands:
      - !knx_plugin.command.dpt_switch.OnOff { addresses: [ 0x0C1C ] }
    triggers: [ ]


.. raw:: latex

    \clearpage


state.exiting.Trigger
---------------------

.. autoclass:: home.scheduler.trigger.state.exiting.Trigger
   :no-members:

.. raw:: latex

    \clearpage

state.exiting.delay.Trigger
---------------------------

.. autoclass:: home.scheduler.trigger.state.exiting.delay.Trigger
   :no-members:

.. raw:: latex

    \clearpage

