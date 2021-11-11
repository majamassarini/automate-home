Feature: An indoor blackout Curtain.

  It should be closed at sunset or when some user is asleep.

  It should be opened when the user is awake after sunrise.

  It could be forced opened or forced closed.

  Scenario Outline: The Curtain react to sun twilight and user sleepiness events.
    Given A curtain.indoor.blackout.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal appliance.curtain.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | from_state                           | event                                  | to_state                             |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.indoor.blackout.state.opened |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.indoor.blackout.state.closed |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened | event.sleepiness.Event.Awake           | curtain.indoor.blackout.state.opened |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened | event.sleepiness.Event.Asleep          | curtain.indoor.blackout.state.closed |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened | event.sleepiness.Event.Sleepy          | curtain.indoor.blackout.state.opened |

      | Awake      | Sunset       | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.indoor.blackout.state.opened |
      | Awake      | Sunset       | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.indoor.blackout.state.closed |
      | Awake      | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Awake           | curtain.indoor.blackout.state.closed |
      | Awake      | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Asleep          | curtain.indoor.blackout.state.closed |
      | Awake      | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Sleepy          | curtain.indoor.blackout.state.closed |

      | Asleep     | Sunrise      | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.indoor.blackout.state.closed |
      | Asleep     | Sunrise      | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.indoor.blackout.state.closed |
      | Asleep     | Sunrise      | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Awake           | curtain.indoor.blackout.state.opened |
      | Asleep     | Sunrise      | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Asleep          | curtain.indoor.blackout.state.closed |
      | Asleep     | Sunrise      | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Sleepy          | curtain.indoor.blackout.state.opened |

      | Asleep     | Sunset       | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.indoor.blackout.state.closed |
      | Asleep     | Sunset       | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.indoor.blackout.state.closed |
      | Asleep     | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Awake           | curtain.indoor.blackout.state.closed |
      | Asleep     | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Asleep          | curtain.indoor.blackout.state.closed |
      | Asleep     | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Sleepy          | curtain.indoor.blackout.state.closed |

      | Sleepy     | Sunrise      | curtain.indoor.blackout.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.indoor.blackout.state.opened |
      | Sleepy     | Sunrise      | curtain.indoor.blackout.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.indoor.blackout.state.closed |
      | Sleepy     | Sunrise      | curtain.indoor.blackout.state.opened | event.sleepiness.Event.Awake           | curtain.indoor.blackout.state.opened |
      | Sleepy     | Sunrise      | curtain.indoor.blackout.state.opened | event.sleepiness.Event.Asleep          | curtain.indoor.blackout.state.closed |
      | Sleepy     | Sunrise      | curtain.indoor.blackout.state.opened | event.sleepiness.Event.Sleepy          | curtain.indoor.blackout.state.opened |

      | Sleepy     | Sunset       | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.indoor.blackout.state.opened |
      | Sleepy     | Sunset       | curtain.indoor.blackout.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.indoor.blackout.state.closed |
      | Sleepy     | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Awake           | curtain.indoor.blackout.state.closed |
      | Sleepy     | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Asleep          | curtain.indoor.blackout.state.closed |
      | Sleepy     | Sunset       | curtain.indoor.blackout.state.closed | event.sleepiness.Event.Sleepy          | curtain.indoor.blackout.state.closed |

  Scenario Outline: The Curtain react to forced opened/closed events
    Given A curtain.indoor.blackout.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal appliance.curtain.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | from_state                           | event                                       | to_state                                    |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.indoor.blackout.state.opened        |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.indoor.blackout.state.forced.closed |

      | Awake      | Sunset       | curtain.indoor.blackout.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.indoor.blackout.state.forced.opened |
      | Awake      | Sunset       | curtain.indoor.blackout.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.indoor.blackout.state.closed        |


  Scenario Outline: The Curtain react to forced opened/closed events from a forced opened state
    Given A curtain.indoor.blackout.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal appliance.curtain.event.forced state at Opened
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | from_state                                  | event                                       | to_state                                    |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.indoor.blackout.state.opened        |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.indoor.blackout.state.forced.closed |

      | Awake      | Sunset       | curtain.indoor.blackout.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.indoor.blackout.state.forced.opened |
      | Awake      | Sunset       | curtain.indoor.blackout.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.indoor.blackout.state.closed        |


  Scenario Outline: The Curtain react to forced opened/closed events from a forced closed state
    Given A curtain.indoor.blackout.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal appliance.curtain.event.forced state at Closed
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | from_state                                  | event                                       | to_state                                    |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.indoor.blackout.state.opened        |
      | Awake      | Sunrise      | curtain.indoor.blackout.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.indoor.blackout.state.forced.closed |

      | Awake      | Sunset       | curtain.indoor.blackout.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.indoor.blackout.state.forced.opened |
      | Awake      | Sunset       | curtain.indoor.blackout.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.indoor.blackout.state.closed        |


  Scenario Outline: The Curtain shows its state
    Given A curtain.indoor.blackout.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal appliance.curtain.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_opened
    Then  the response is <response>

    Examples:
      | sleepiness | sun_twilight | forced | state                                       | response |
      | Awake      | Sunrise      | Not    | curtain.indoor.blackout.state.opened        | True     |
      | Awake      | Sunset       | Not    | curtain.indoor.blackout.state.closed        | False    |
      | Awake      | Sunrise      | Closed | curtain.indoor.blackout.state.forced.closed | False    |
      | Awake      | Sunset       | Opened | curtain.indoor.blackout.state.forced.opened | True     |
