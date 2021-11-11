Feature: A presence Light
  A presence Light which is by default off.
  When forced on by the user can be turned off by the system if nobody is in the room.

  You could know that nobody is in the room when, as an example, the room alarm sensors are presence.
  Other events could be used for the same purpose.


  Scenario Outline: The Light does not react to alarm presence events from an unforced state
    Given A light.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                      | event                    | to_state                        |
      | Off      | light.presence.state.off | event.presence.Event.Off  | light.presence.state.off |
      | Off      | light.presence.state.off | event.presence.Event.On | light.presence.state.off |

      | On       | light.presence.state.off | event.presence.Event.Off  | light.presence.state.off |
      | On       | light.presence.state.off | event.presence.Event.On | light.presence.state.off |

  Scenario Outline: The Light react to forced on events
    Given A light.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                      | event                                  | to_state                              |
      | Off      | light.presence.state.off | appliance.light.event.forced.Event.Off | light.presence.state.off       |
      | Off      | light.presence.state.off | appliance.light.event.forced.Event.On  | light.presence.state.forced.on |


  Scenario Outline: The Light react to forced on/off events from a forced on state
    Given A light.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.light.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                            | event                                  | to_state                              |
      | Off      | light.presence.state.forced.on | appliance.light.event.forced.Event.Off | light.presence.state.off       |
      | Off      | light.presence.state.forced.on | appliance.light.event.forced.Event.On  | light.presence.state.forced.on |

      | On       | light.presence.state.forced.on | appliance.light.event.forced.Event.Off | light.presence.state.off       |
      | On       | light.presence.state.forced.on | appliance.light.event.forced.Event.On  | light.presence.state.forced.on |


  Scenario Outline: The Light react to alarm presence events from a forced on state
    Given A light.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.light.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                            | event                    | to_state                              |
      | Off      | light.presence.state.forced.on | event.presence.Event.Off  | light.presence.state.off       |
      | Off      | light.presence.state.forced.on | event.presence.Event.On | light.presence.state.forced.on |

      | On       | light.presence.state.forced.on | event.presence.Event.Off  | light.presence.state.off       |
      | On       | light.presence.state.forced.on | event.presence.Event.On | light.presence.state.forced.on |


  Scenario Outline: The Light shows its is_on property
    Given A light.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.light.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | presence | forced | state                                 | response |
      | On       | Not    | light.presence.state.off       | False    |
      | On       | On     | light.presence.state.forced.on | True     |

