Feature: A sound player appliance


  Scenario Outline: The Sound Player react to not forced events from a not forced state
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.elapsed state at <elapsed>
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sleepiness | elapsed | from_state                 | event                         | to_state                   |
      | On       | Awake      | On      | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | On       | Awake      | On      | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | On       | Awake      | On      | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.off     |
      | On       | Awake      | On      | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | On       | Awake      | On      | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | On       | Awake      | On      | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | On       | Awake      | On      | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | On       | Awake      | Off     | sound.player.state.fade_in | event.presence.Event.On       | sound.player.state.fade_in |
      | On       | Awake      | Off     | sound.player.state.fade_in | event.presence.Event.Off      | sound.player.state.off     |
      | On       | Awake      | Off     | sound.player.state.fade_in | event.sleepiness.Event.Awake  | sound.player.state.fade_in |
      | On       | Awake      | Off     | sound.player.state.fade_in | event.sleepiness.Event.Sleepy | sound.player.state.fade_in |
      | On       | Awake      | Off     | sound.player.state.fade_in | event.sleepiness.Event.Asleep | sound.player.state.fade_in |
      | On       | Awake      | Off     | sound.player.state.fade_in | event.elapsed.Event.On        | sound.player.state.off     |
      | On       | Awake      | Off     | sound.player.state.fade_in | event.elapsed.Event.Off       | sound.player.state.fade_in |
      | On       | Asleep     | On      | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | On       | Asleep     | On      | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | On       | Asleep     | On      | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.off |
      | On       | Asleep     | On      | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | On       | Asleep     | On      | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | On       | Asleep     | On      | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | On       | Asleep     | On      | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | On       | Asleep     | Off     | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | On       | Asleep     | Off     | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | On       | Asleep     | Off     | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.fade_in |
      | On       | Asleep     | Off     | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | On       | Asleep     | Off     | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | On       | Asleep     | Off     | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | On       | Asleep     | Off     | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | On       | Sleepy     | On      | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | On       | Sleepy     | On      | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | On       | Sleepy     | On      | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.off |
      | On       | Sleepy     | On      | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | On       | Sleepy     | On      | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | On       | Sleepy     | On      | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | On       | Sleepy     | On      | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | On       | Sleepy     | Off     | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | On       | Sleepy     | Off     | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | On       | Sleepy     | Off     | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.fade_in |
      | On       | Sleepy     | Off     | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | On       | Sleepy     | Off     | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | On       | Sleepy     | Off     | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | On       | Sleepy     | Off     | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | Off      | Awake      | On      | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | Off      | Awake      | On      | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | Off      | Awake      | On      | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.off     |
      | Off      | Awake      | On      | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | Off      | Awake      | On      | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | Off      | Awake      | On      | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | Off      | Awake      | On      | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | event.presence.Event.On       | sound.player.state.fade_in     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | event.presence.Event.Off      | sound.player.state.off     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | event.sleepiness.Event.Awake  | sound.player.state.fade_in     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | event.sleepiness.Event.Sleepy | sound.player.state.fade_in     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | event.sleepiness.Event.Asleep | sound.player.state.fade_in     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | event.elapsed.Event.On        | sound.player.state.off     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | event.elapsed.Event.Off       | sound.player.state.fade_in     |
      | Off      | Asleep     | On      | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | Off      | Asleep     | On      | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | Off      | Asleep     | On      | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.off     |
      | Off      | Asleep     | On      | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | Off      | Asleep     | On      | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | Off      | Asleep     | On      | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | Off      | Asleep     | On      | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | Off      | Asleep     | Off     | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | Off      | Asleep     | Off     | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | Off      | Asleep     | Off     | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.fade_in     |
      | Off      | Asleep     | Off     | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | Off      | Asleep     | Off     | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | Off      | Asleep     | Off     | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | Off      | Asleep     | Off     | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | Off      | Sleepy     | On      | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | Off      | Sleepy     | On      | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | Off      | Sleepy     | On      | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.off     |
      | Off      | Sleepy     | On      | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | Off      | Sleepy     | On      | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | Off      | Sleepy     | On      | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | Off      | Sleepy     | On      | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | event.presence.Event.On       | sound.player.state.off     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | event.presence.Event.Off      | sound.player.state.off     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | event.sleepiness.Event.Awake  | sound.player.state.fade_in     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | event.sleepiness.Event.Sleepy | sound.player.state.off     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | event.sleepiness.Event.Asleep | sound.player.state.off     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | event.elapsed.Event.On        | sound.player.state.off     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | event.elapsed.Event.Off       | sound.player.state.off     |

  Scenario Outline: The Sound Player react to forced events from a not forced state
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.elapsed state at <elapsed>
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sleepiness | elapsed | from_state                 | event                                                     | to_state                                   |
      | On       | Awake      | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | On       | Awake      | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | On       | Awake      | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | On       | Awake      | Off     | sound.player.state.fade_in | appliance.sound.player.event.forced.Event.On              | sound.player.state.fade_in                 |
      | On       | Awake      | Off     | sound.player.state.fade_in | appliance.sound.player.event.forced.Event.Off             | sound.player.state.forced.off              |
      | On       | Awake      | Off     | sound.player.state.fade_in | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.fade_in                 |
      | On       | Asleep     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | On       | Asleep     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | On       | Asleep     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | On       | Asleep     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | On       | Asleep     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | On       | Asleep     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | On       | Sleepy     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | On       | Sleepy     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | On       | Sleepy     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | On       | Sleepy     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | On       | Sleepy     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | On       | Sleepy     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | Off      | Awake      | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | Off      | Awake      | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | Off      | Awake      | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | appliance.sound.player.event.forced.Event.On              | sound.player.state.fade_in               |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.forced.off                     |
      | Off      | Awake      | Off     | sound.player.state.fade_in     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.fade_in|
      | Off      | Asleep     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | Off      | Asleep     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | Off      | Asleep     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | Off      | Asleep     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | Off      | Asleep     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | Off      | Asleep     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | Off      | Sleepy     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | Off      | Sleepy     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | Off      | Sleepy     | On      | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | Off      | Sleepy     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |
      | Off      | Sleepy     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off                     |
      | Off      | Sleepy     | Off     | sound.player.state.off     | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |

  Scenario Outline: The Sound Player react to not forced events from a On forced state, and will be reset by a
  Presence Off event
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.sound.player.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                   | event                         | to_state                     |
      | On       | sound.player.state.forced.on | event.presence.Event.On       | sound.player.state.forced.on |
      | On       | sound.player.state.forced.on | event.presence.Event.Off      | sound.player.state.off       |
      | On       | sound.player.state.forced.on | event.sleepiness.Event.Awake  | sound.player.state.forced.on |
      | On       | sound.player.state.forced.on | event.sleepiness.Event.Sleepy | sound.player.state.forced.on |
      | On       | sound.player.state.forced.on | event.sleepiness.Event.Asleep | sound.player.state.fade_out  |
      | On       | sound.player.state.forced.on | event.elapsed.Event.On        | sound.player.state.forced.on |
      | On       | sound.player.state.forced.on | event.elapsed.Event.Off       | sound.player.state.forced.on |
      | Off      | sound.player.state.forced.on | event.presence.Event.On       | sound.player.state.forced.on |
      | Off      | sound.player.state.forced.on | event.presence.Event.Off      | sound.player.state.off       |
      | Off      | sound.player.state.forced.on | event.sleepiness.Event.Awake  | sound.player.state.forced.on |
      | Off      | sound.player.state.forced.on | event.sleepiness.Event.Sleepy | sound.player.state.forced.on |
      | Off      | sound.player.state.forced.on | event.sleepiness.Event.Asleep | sound.player.state.forced.on |
      | Off      | sound.player.state.forced.on | event.elapsed.Event.On        | sound.player.state.forced.on |
      | Off      | sound.player.state.forced.on | event.elapsed.Event.Off       | sound.player.state.forced.on |

  Scenario Outline: The Sound Player react to forced events from a On forced state
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal appliance.sound.player.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | from_state                   | event                                                     | to_state                     |
      | sound.player.state.forced.on | appliance.sound.player.event.forced.Event.Off             | sound.player.state.off       |
      | sound.player.state.forced.on | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.on |


  Scenario Outline: The Sound Player react to not forced events from a circadian rhythm forced state, and will be reset by a
  Presence Off event
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.sound.player.event.forced state at CircadianRhythm
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                                 | event                         | to_state                                   |
      | On       | sound.player.state.forced.circadian_rhythm | event.presence.Event.On       | sound.player.state.forced.circadian_rhythm |
      | On       | sound.player.state.forced.circadian_rhythm | event.presence.Event.Off      | sound.player.state.off                     |
      | On       | sound.player.state.forced.circadian_rhythm | event.sleepiness.Event.Awake  | sound.player.state.forced.circadian_rhythm |
      | On       | sound.player.state.forced.circadian_rhythm | event.sleepiness.Event.Sleepy | sound.player.state.forced.circadian_rhythm |
      | On       | sound.player.state.forced.circadian_rhythm | event.sleepiness.Event.Asleep | sound.player.state.fade_out                |
      | On       | sound.player.state.forced.circadian_rhythm | event.elapsed.Event.On        | sound.player.state.forced.circadian_rhythm |
      | On       | sound.player.state.forced.circadian_rhythm | event.elapsed.Event.Off       | sound.player.state.forced.circadian_rhythm |
      | Off      | sound.player.state.forced.circadian_rhythm | event.presence.Event.On       | sound.player.state.forced.circadian_rhythm |
      | Off      | sound.player.state.forced.circadian_rhythm | event.presence.Event.Off      | sound.player.state.off                     |
      | Off      | sound.player.state.forced.circadian_rhythm | event.sleepiness.Event.Awake  | sound.player.state.forced.circadian_rhythm |
      | Off      | sound.player.state.forced.circadian_rhythm | event.sleepiness.Event.Sleepy | sound.player.state.forced.circadian_rhythm |
      | Off      | sound.player.state.forced.circadian_rhythm | event.sleepiness.Event.Asleep | sound.player.state.forced.circadian_rhythm |
      | Off      | sound.player.state.forced.circadian_rhythm | event.elapsed.Event.On        | sound.player.state.forced.circadian_rhythm |
      | Off      | sound.player.state.forced.circadian_rhythm | event.elapsed.Event.Off       | sound.player.state.forced.circadian_rhythm |

  Scenario Outline: The Sound Player react to forced events from a Circadian Rhythm forced state
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal appliance.sound.player.event.forced state at CircadianRhythm
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | from_state                                 | event                                         | to_state                                   |
      | sound.player.state.forced.circadian_rhythm | appliance.sound.player.event.forced.Event.Off | sound.player.state.off                     |
      | sound.player.state.forced.circadian_rhythm | appliance.sound.player.event.forced.Event.On  | sound.player.state.forced.circadian_rhythm |


  Scenario Outline: The Sound Player react to not forced events from an off forced state, and will be reset by a
  Presence Off event
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.sleepiness state at Awake
    And   the appliance has an internal appliance.sound.player.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | from_state                    | event                         | to_state                      |
      | sound.player.state.forced.off | event.presence.Event.On       | sound.player.state.forced.off |
      | sound.player.state.forced.off | event.presence.Event.Off      | sound.player.state.off        |
      | sound.player.state.forced.off | event.sleepiness.Event.Awake  | sound.player.state.forced.off |
      | sound.player.state.forced.off | event.sleepiness.Event.Sleepy | sound.player.state.forced.off |
      | sound.player.state.forced.off | event.sleepiness.Event.Asleep | sound.player.state.forced.off |
      | sound.player.state.forced.off | event.elapsed.Event.On        | sound.player.state.forced.off |
      | sound.player.state.forced.off | event.elapsed.Event.Off       | sound.player.state.forced.off |

  Scenario Outline: The Sound Player react to forced events from a Circadian Rhythm forced state
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.elapsed state at Off
    And   the appliance has an internal event.sleepiness state at Awake
    And   the appliance has an internal appliance.sound.player.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | from_state                    | event                                                     | to_state                                   |
      | sound.player.state.forced.off | appliance.sound.player.event.forced.Event.CircadianRhythm | sound.player.state.forced.circadian_rhythm |
      | sound.player.state.forced.off | appliance.sound.player.event.forced.Event.On              | sound.player.state.forced.on               |


  Scenario Outline: The Sound Player shows its property: is_on
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.sleepiness state at <sleepiness1>
    And   the appliance has an internal appliance.sound.player.event.forced state at <forced>
    And   the appliance has an internal event.sleepiness state at <sleepiness2>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | sleepiness1 | forced          | sleepiness2 | state                                      | response |
      | Sleepy      | Not             | Asleep      | sound.player.state.off                     | False    |
      | Sleepy      | Not             | Awake       | sound.player.state.fade_in                 | True     |
      | Sleepy      | On              | Asleep      | sound.player.state.fade_out                | True     |
      | Sleepy      | On              | Sleepy      | sound.player.state.forced.on               | True     |
      | Sleepy      | CircadianRhythm | Sleepy      | sound.player.state.forced.circadian_rhythm | True     |
      | Awake       | Off             | Sleepy      | sound.player.state.forced.off              | False    |

  Scenario Outline: The Sound Player shows its property: is_circadian_rhythm
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.sleepiness state at <sleepiness1>
    And   the appliance has an internal appliance.sound.player.event.forced state at <forced>
    And   the appliance has an internal event.sleepiness state at <sleepiness2>
    And   it's calculated state is <state>
    When  it's asked for its state property is_circadian_rhythm
    Then  the response is <response>

    Examples:
      | sleepiness1 | forced          | sleepiness2 | state                                      | response |
      | Sleepy      | Not             | Asleep      | sound.player.state.off                     | False    |
      | Sleepy      | Not             | Awake       | sound.player.state.fade_in                 | False    |
      | Sleepy      | On              | Asleep      | sound.player.state.fade_out                | False    |
      | Sleepy      | On              | Sleepy      | sound.player.state.forced.on               | False    |
      | Sleepy      | CircadianRhythm | Sleepy      | sound.player.state.forced.circadian_rhythm | True     |
      | Awake       | Off             | Sleepy      | sound.player.state.forced.off              | False    |

  Scenario Outline: The Sound Player shows its property: is_fading
    Given A sound.player.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.sleepiness state at <sleepiness1>
    And   the appliance has an internal appliance.sound.player.event.forced state at <forced>
    And   the appliance has an internal event.sleepiness state at <sleepiness2>
    And   it's calculated state is <state>
    When  it's asked for its state property is_fading
    Then  the response is <response>

    Examples:
      | sleepiness1 | forced          | sleepiness2 | state                                      | response |
      | Sleepy      | Not             | Asleep      | sound.player.state.off                     | False    |
      | Sleepy      | Not             | Awake       | sound.player.state.fade_in                 | True     |
      | Sleepy      | On              | Asleep      | sound.player.state.fade_out                | True     |
      | Sleepy      | On              | Sleepy      | sound.player.state.forced.on               | False    |
      | Sleepy      | CircadianRhythm | Sleepy      | sound.player.state.forced.circadian_rhythm | False    |
      | Awake       | Off             | Sleepy      | sound.player.state.forced.off              | False    |


  Scenario Outline: The Sound Player shows its property: volume
    Given A sound.player.Appliance appliance
    And   the appliance has an internal appliance.sound.player.event.volume state at 70
    And   the appliance has an internal appliance.sound.player.event.sleepy_volume state at 60
    And   the appliance has an internal appliance.sound.player.event.fade_in.volume state at 50
    And   the appliance has an internal appliance.sound.player.event.fade_out.volume state at 80
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.sleepiness state at <sleepiness1>
    And   the appliance has an internal appliance.sound.player.event.forced state at <forced>
    And   the appliance has an internal event.sleepiness state at <sleepiness2>
    And   it's calculated state is <state>
    When  it's asked for its state property volume
    Then  the response is <response>

    Examples:
      | sleepiness1 | forced          | sleepiness2 | state                                      | response |
      | Asleep      | Not             | Asleep      | sound.player.state.off                     | 70       |
      | Sleepy      | Not             | Awake       | sound.player.state.fade_in                 | 50       |
      | Sleepy      | On              | Asleep      | sound.player.state.fade_out                | 80       |
      | Sleepy      | On              | Sleepy      | sound.player.state.forced.on               | 60       |
      | Asleep      | CircadianRhythm | Sleepy      | sound.player.state.forced.circadian_rhythm | 60       |
      | Awake       | Off             | Sleepy      | sound.player.state.forced.off              | 70       |

  Scenario Outline: The Sound Player shows its property: playlist
    Given A sound.player.Appliance appliance
    And   the appliance has an internal appliance.sound.player.event.playlist state at Playlist
    And   the appliance has an internal appliance.sound.player.event.forced.circadian_rhythm.playlist_a state at PlaylistA
    And   the appliance has an internal appliance.sound.player.event.forced.circadian_rhythm.playlist_b state at PlaylistB
    And   the appliance has an internal appliance.sound.player.event.forced.circadian_rhythm.playlist_c state at PlaylistC
    And   the appliance has an internal appliance.sound.player.event.fade_in.playlist state at PlaylistFadeIn
    And   the appliance has an internal appliance.sound.player.event.fade_out.playlist state at PlaylistFadeOut
    And   the appliance has an internal event.user state at B
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.sleepiness state at <sleepiness1>
    And   the appliance has an internal appliance.sound.player.event.forced state at <forced>
    And   the appliance has an internal event.sleepiness state at <sleepiness2>
    And   it's calculated state is <state>
    When  it's asked for its state property playlist
    Then  the response is <response>

    Examples:
      | sleepiness1 | forced          | sleepiness2 | state                                      | response        |
      | Asleep      | Not             | Asleep      | sound.player.state.off                     | Playlist        |
      | Sleepy      | Not             | Awake       | sound.player.state.fade_in                 | PlaylistFadeIn  |
      | Sleepy      | On              | Asleep      | sound.player.state.fade_out                | PlaylistFadeOut |
      | Sleepy      | On              | Sleepy      | sound.player.state.forced.on               | Playlist        |
      | Asleep      | CircadianRhythm | Sleepy      | sound.player.state.forced.circadian_rhythm | PlaylistB       |
      | Awake       | Off             | Sleepy      | sound.player.state.forced.off              | Playlist        |
