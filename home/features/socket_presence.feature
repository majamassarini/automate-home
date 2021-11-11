Feature: A Presence Socket appliance
  A **presence** socket which is by default **off**.
  When *forced on* by the user can be turned *off* by the system if nobody is in the room.

  You could know that nobody is in the room when, as an example, the room alarm sensors are presence.
  Other events could be used for the same purpose.


  Scenario Outline: The Socket does not react to alarm presence events from an unforced state
    Given A socket.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.socket.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                | event                    | to_state                  |
      | Off      | socket.presence.state.off | event.presence.Event.Off  | socket.presence.state.off |
      | Off      | socket.presence.state.off | event.presence.Event.On | socket.presence.state.off |

      | On       | socket.presence.state.off | event.presence.Event.Off  | socket.presence.state.off |
      | On       | socket.presence.state.off | event.presence.Event.On | socket.presence.state.off |

  Scenario Outline: The Socket react to forced on events
    Given A socket.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.socket.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                | event                                   | to_state                        |
      | Off      | socket.presence.state.off | appliance.socket.event.forced.Event.Off | socket.presence.state.off       |
      | Off      | socket.presence.state.off | appliance.socket.event.forced.Event.On  | socket.presence.state.forced.on |


  Scenario Outline: The Socket react to forced on/off events from a forced on state
    Given A socket.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.socket.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                      | event                                   | to_state                        |
      | Off      | socket.presence.state.forced.on | appliance.socket.event.forced.Event.Off | socket.presence.state.off       |
      | Off      | socket.presence.state.forced.on | appliance.socket.event.forced.Event.On  | socket.presence.state.forced.on |

      | On       | socket.presence.state.forced.on | appliance.socket.event.forced.Event.Off | socket.presence.state.off       |
      | On       | socket.presence.state.forced.on | appliance.socket.event.forced.Event.On  | socket.presence.state.forced.on |


  Scenario Outline: The Socket react to alarm presence events from a forced on state
    Given A socket.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.socket.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | from_state                      | event                    | to_state                        |
      | Off      | socket.presence.state.forced.on | event.presence.Event.Off  | socket.presence.state.off       |
      | Off      | socket.presence.state.forced.on | event.presence.Event.On | socket.presence.state.forced.on |

      | On       | socket.presence.state.forced.on | event.presence.Event.Off  | socket.presence.state.off       |
      | On       | socket.presence.state.forced.on | event.presence.Event.On | socket.presence.state.forced.on |


  Scenario Outline: The Socket shows its is_on property
    Given A socket.presence.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.socket.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | presence | forced | state                           | response |
      | On       | Not    | socket.presence.state.off       | False    |
      | On       | On     | socket.presence.state.forced.on | True     |

