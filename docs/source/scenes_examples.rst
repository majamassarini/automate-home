Example
^^^^^^^

An example showing how a button can be used to recall the "sleepy" snapshot.

The "sleepy" snapshot:

 1. starts the Sonos player with the specified playlist
 2. stops the Sonos player after an hour (this is more than a snapshot)
 3. turns off a KNX light
 4. set a calming color to the Lifx light
 5. turns off the Lifx light after an hour (this is more than a snapshot)

.. note::
  The button used to recall the snapshot is a KNX device.

  The KNX light will recall its snapshot state by itself when the KNX button is pressed.

  The Sonos player and the Lifx bulb need something more (like the following system configuration) to become part of the same scene.

A *Protocol Trigger* is bound with the *scene button Appliance* through the following Performer::

  !Performer
    name: "scene button trigger"
    for appliance: "scene button"
    commands: []
    triggers:
    - !knx_plugin.trigger.custom_scene.Equal {addresses: [0xAAAA], number: 3}

The following *Protocol Scheduler Triggers* are built using the above *Performer*::

  !protocol.Trigger
    name: "turn on Sonos player"
    notify more events: [!home.appliance.sound.player.event.forced.Event.On]
    when triggered performers: "scene button trigger"

  !protocol.delay.Trigger
    name: "turn off Sonos player in one hour"
    notify more events: [!home.appliance.sound.player.event.forced.Event.Off]
    when triggered performers: "scene button trigger"
    and timeout expires: 3600

  !protocol.Trigger
    name: "set a calming color to Lifx bulb"
    notify more events: [!home.appliance.light.event.forced.Event.On,
                         !home.appliance.light.event.hue.Event(270)]
    when triggered performers: "scene button trigger"

  !protocol.delay.Trigger
    name: "turn off the Lifx bulb in one hour"
    notify more events: [!home.appliance.light.event.forced.Event.Off]
    when triggered performers: "scene button trigger"
    and timeout expires: 3600

The *Scheduler Triggers* are scheduled to notify events to the Sonos Player and the Lifx Bulb::

  !schedule
    trigger: "turn on Sonos player"
    for performers: "sonos player command"

  !schedule
    trigger: "turn off Sonos player in one hour"
    for performers: "sonos player command"

  !schedule
    trigger: "set a calming color to Lifx bulb"
    for performers: "lifx color command"

  !schedule
    trigger: "turn off the Lifx bulb in one hour"
    for performers: "lifx command"

The Sonos player *Protocol Commands* are *Home Assistant* protocol commands:
The *Performer* is defined like this::

  - !Performer
    name: "sonos player command"
    for appliance: "sonos player"
    commands:
      - !home_assistant_plugin.service.media_player.command.Play {entity_id: "media_player.my_bedroom"}
      - !home_assistant_plugin.service.media_player.command.Pause {entity_id: "media_player.my_bedroom"}
    triggers: []

The *lifx color command* *Performer* is defined like this::

  - !Performer
    name: "lifx color command"
    for appliance: "lifx bulb"
    commands:
      - !lifx_plugin.command.SetColor {addresses: [["172.31.10.245", 56700]]}
    triggers: []

