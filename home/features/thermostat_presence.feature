Feature: A Thermostat appliance


  Scenario Outline: The Thermostat react to presence and command events
    Given A thermostat.presence.Appliance appliance
    And   the appliance has an internal event.clima.command state at <command>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.thermostat.presence.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | command | from_state                     | event                          | to_state                       |
      | Off      | On      | thermostat.presence.state.keep | event.presence.Event.On        | thermostat.presence.state.on   |
      | Off      | On      | thermostat.presence.state.keep | event.presence.Event.Off       | thermostat.presence.state.keep |
      | Off      | On      | thermostat.presence.state.keep | event.clima.command.Event.On   | thermostat.presence.state.keep |
      | Off      | On      | thermostat.presence.state.keep | event.clima.command.Event.Off  | thermostat.presence.state.off  |
      | Off      | On      | thermostat.presence.state.keep | event.clima.command.Event.Keep | thermostat.presence.state.keep |

      | Off      | Off     | thermostat.presence.state.off  | event.presence.Event.On        | thermostat.presence.state.off  |
      | Off      | Off     | thermostat.presence.state.off  | event.presence.Event.Off       | thermostat.presence.state.off  |
      | Off      | Off     | thermostat.presence.state.off  | event.clima.command.Event.On   | thermostat.presence.state.keep |
      | Off      | Off     | thermostat.presence.state.off  | event.clima.command.Event.Off  | thermostat.presence.state.off  |
      | Off      | Off     | thermostat.presence.state.off  | event.clima.command.Event.Keep | thermostat.presence.state.keep |

      | Off      | Keep    | thermostat.presence.state.keep | event.presence.Event.On        | thermostat.presence.state.keep |
      | Off      | Keep    | thermostat.presence.state.keep | event.presence.Event.Off       | thermostat.presence.state.keep |
      | Off      | Keep    | thermostat.presence.state.keep | event.clima.command.Event.On   | thermostat.presence.state.keep |
      | Off      | Keep    | thermostat.presence.state.keep | event.clima.command.Event.Off  | thermostat.presence.state.off  |
      | Off      | Keep    | thermostat.presence.state.keep | event.clima.command.Event.Keep | thermostat.presence.state.keep |

      | On       | On      | thermostat.presence.state.on   | event.presence.Event.On        | thermostat.presence.state.on   |
      | On       | On      | thermostat.presence.state.on   | event.presence.Event.Off       | thermostat.presence.state.keep |
      | On       | On      | thermostat.presence.state.on   | event.clima.command.Event.On   | thermostat.presence.state.on   |
      | On       | On      | thermostat.presence.state.on   | event.clima.command.Event.Off  | thermostat.presence.state.off  |
      | On       | On      | thermostat.presence.state.on   | event.clima.command.Event.Keep | thermostat.presence.state.keep |

      | On       | Off     | thermostat.presence.state.off  | event.presence.Event.On        | thermostat.presence.state.off  |
      | On       | Off     | thermostat.presence.state.off  | event.presence.Event.Off       | thermostat.presence.state.off  |
      | On       | Off     | thermostat.presence.state.off  | event.clima.command.Event.On   | thermostat.presence.state.on   |
      | On       | Off     | thermostat.presence.state.off  | event.clima.command.Event.Off  | thermostat.presence.state.off  |
      | On       | Off     | thermostat.presence.state.off  | event.clima.command.Event.Keep | thermostat.presence.state.keep |

      | On       | Keep    | thermostat.presence.state.keep | event.presence.Event.On        | thermostat.presence.state.keep |
      | On       | Keep    | thermostat.presence.state.keep | event.presence.Event.Off       | thermostat.presence.state.keep |
      | On       | Keep    | thermostat.presence.state.keep | event.clima.command.Event.On   | thermostat.presence.state.on   |
      | On       | Keep    | thermostat.presence.state.keep | event.clima.command.Event.Off  | thermostat.presence.state.off  |
      | On       | Keep    | thermostat.presence.state.keep | event.clima.command.Event.Keep | thermostat.presence.state.keep |


  Scenario Outline: The Thermostat react to forced on/off/keep events
    Given A thermostat.presence.Appliance appliance
    And   the appliance has an internal event.clima.command state at <command>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.thermostat.presence.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | command | from_state                     | event                                                 | to_state                              |
      | Off      | On      | thermostat.presence.state.keep | appliance.thermostat.presence.event.forced.Event.On   | thermostat.presence.state.forced.on   |
      | Off      | On      | thermostat.presence.state.keep | appliance.thermostat.presence.event.forced.Event.Off  | thermostat.presence.state.forced.off  |
      | Off      | On      | thermostat.presence.state.keep | appliance.thermostat.presence.event.forced.Event.Keep | thermostat.presence.state.keep        |

      | Off      | Off     | thermostat.presence.state.off  | appliance.thermostat.presence.event.forced.Event.On   | thermostat.presence.state.forced.on   |
      | Off      | Off     | thermostat.presence.state.off  | appliance.thermostat.presence.event.forced.Event.Off  | thermostat.presence.state.off         |
      | Off      | Off     | thermostat.presence.state.off  | appliance.thermostat.presence.event.forced.Event.Keep | thermostat.presence.state.forced.keep |

      | On       | On      | thermostat.presence.state.on   | appliance.thermostat.presence.event.forced.Event.On   | thermostat.presence.state.on          |
      | On       | On      | thermostat.presence.state.on   | appliance.thermostat.presence.event.forced.Event.Off  | thermostat.presence.state.forced.off  |
      | On       | On      | thermostat.presence.state.on   | appliance.thermostat.presence.event.forced.Event.Keep | thermostat.presence.state.forced.keep |


  Scenario Outline: The Thermostat react to forced off/keep events exiting from a forced on state!!!
    Given A thermostat.presence.Appliance appliance
    And   the appliance has an internal event.clima.command state at <command>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.thermostat.presence.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | command | from_state                          | event                                                 | to_state                              |
      | On       | On      | thermostat.presence.state.on        | appliance.thermostat.presence.event.forced.Event.Off  | thermostat.presence.state.forced.off  |
      | On       | Off     | thermostat.presence.state.forced.on | appliance.thermostat.presence.event.forced.Event.Off  | thermostat.presence.state.forced.off  |
      | On       | Keep    | thermostat.presence.state.forced.on | appliance.thermostat.presence.event.forced.Event.Off  | thermostat.presence.state.forced.off  |

      | On       | On      | thermostat.presence.state.on        | appliance.thermostat.presence.event.forced.Event.Keep | thermostat.presence.state.forced.keep |
      | On       | Off     | thermostat.presence.state.forced.on | appliance.thermostat.presence.event.forced.Event.Keep | thermostat.presence.state.forced.keep |
      | On       | Keep    | thermostat.presence.state.forced.on | appliance.thermostat.presence.event.forced.Event.Keep | thermostat.presence.state.forced.keep |


  Scenario Outline: The Thermostat react to forced on/off events from a forced keep state
    Given A thermostat.presence.Appliance appliance
    And   the appliance has an internal event.clima.command state at <command>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.thermostat.presence.event.forced state at Keep
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | command | from_state                            | event                                                | to_state                             |
      | On       | On      | thermostat.presence.state.forced.keep | appliance.thermostat.presence.event.forced.Event.Off | thermostat.presence.state.forced.off |
      | On       | Off     | thermostat.presence.state.forced.keep | appliance.thermostat.presence.event.forced.Event.Off | thermostat.presence.state.forced.off |
      | On       | Keep    | thermostat.presence.state.keep        | appliance.thermostat.presence.event.forced.Event.Off | thermostat.presence.state.forced.off |

      | On       | On      | thermostat.presence.state.forced.keep | appliance.thermostat.presence.event.forced.Event.On  | thermostat.presence.state.forced.on  |
      | On       | Off     | thermostat.presence.state.forced.keep | appliance.thermostat.presence.event.forced.Event.On  | thermostat.presence.state.forced.on  |
      | On       | Keep    | thermostat.presence.state.keep        | appliance.thermostat.presence.event.forced.Event.On  | thermostat.presence.state.forced.on  |


  Scenario Outline: The Thermostat could be automatically un-forced from a forced on state by clima.command events presence.state events
    Given A thermostat.presence.Appliance appliance
    And   the appliance has an internal event.clima.command state at <command>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.thermostat.presence.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | command | from_state                          | event                        | to_state                     |
      | Off      | On      | thermostat.presence.state.forced.on | event.presence.Event.On      | thermostat.presence.state.on |
      | On       | Off     | thermostat.presence.state.forced.on | event.clima.command.Event.On | thermostat.presence.state.on |


  Scenario Outline: The Thermostat shows its state
    Given A thermostat.presence.Appliance appliance
    And   the appliance has an internal event.clima.command state at <command>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.thermostat.presence.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | presence | command | forced | state                                 | response |
      | Off      | Off     | Not    | thermostat.presence.state.off         | False    |
      | On       | On      | Not    | thermostat.presence.state.on          | True     |
      | Off      | On      | Not    | thermostat.presence.state.keep        | True     |
      | Off      | Off     | On     | thermostat.presence.state.forced.on   | True     |
      | Off      | Off     | Keep   | thermostat.presence.state.forced.keep | True     |
      | On       | On      | Off    | thermostat.presence.state.forced.off  | False    |


  Scenario Outline: The Thermostat shows its state
    Given A thermostat.presence.Appliance appliance
    And   the appliance has an internal event.clima.command state at <command>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal appliance.thermostat.presence.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_keeping
    Then  the response is <response>

    Examples:
      | presence | command | forced | state                                 | response |
      | Off      | Off     | Not    | thermostat.presence.state.off         | False    |
      | On       | On      | Not    | thermostat.presence.state.on          | False    |
      | Off      | On      | Not    | thermostat.presence.state.keep        | True     |
      | Off      | Off     | On     | thermostat.presence.state.forced.on   | False    |
      | Off      | Off     | Keep   | thermostat.presence.state.forced.keep | True     |
      | On       | On      | Off    | thermostat.presence.state.forced.off  | False    |
