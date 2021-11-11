Feature: A indoor dimmerable Light


  Scenario Outline: The Light react to courtesy and sun brightness events
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun_brightness | from_state                        | event                               | to_state                          |
      | On       | Bright         | light.indoor.dimmerable.state.off | event.presence.Event.On             | light.indoor.dimmerable.state.off |
      | On       | Bright         | light.indoor.dimmerable.state.off | event.presence.Event.Off            | light.indoor.dimmerable.state.off |
      | On       | Bright         | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Bright   | light.indoor.dimmerable.state.off |
      | On       | Bright         | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.off |
      | On       | Bright         | light.indoor.dimmerable.state.off | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.off |
      | On       | Dark           | light.indoor.dimmerable.state.off | event.presence.Event.On             | light.indoor.dimmerable.state.off |
      | On       | Dark           | light.indoor.dimmerable.state.off | event.presence.Event.Off            | light.indoor.dimmerable.state.off |
      | On       | Dark           | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Bright   | light.indoor.dimmerable.state.off |
      | On       | Dark           | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.off |
      | On       | Dark           | light.indoor.dimmerable.state.off | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.off |
      | On       | DeepDark       | light.indoor.dimmerable.state.off | event.presence.Event.On             | light.indoor.dimmerable.state.off |
      | On       | DeepDark       | light.indoor.dimmerable.state.off | event.presence.Event.Off            | light.indoor.dimmerable.state.off |
      | On       | DeepDark       | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Bright   | light.indoor.dimmerable.state.off |
      | On       | DeepDark       | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.off |
      | On       | DeepDark       | light.indoor.dimmerable.state.off | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.off |
      | Off      | Bright         | light.indoor.dimmerable.state.off | event.presence.Event.On             | light.indoor.dimmerable.state.off |
      | Off      | Bright         | light.indoor.dimmerable.state.off | event.presence.Event.Off            | light.indoor.dimmerable.state.off |
      | Off      | Bright         | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Bright   | light.indoor.dimmerable.state.off |
      | Off      | Bright         | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.off |
      | Off      | Bright         | light.indoor.dimmerable.state.off | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.off |
      | Off      | Dark           | light.indoor.dimmerable.state.off | event.presence.Event.On             | light.indoor.dimmerable.state.off |
      | Off      | Dark           | light.indoor.dimmerable.state.off | event.presence.Event.Off            | light.indoor.dimmerable.state.off |
      | Off      | Dark           | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Bright   | light.indoor.dimmerable.state.off |
      | Off      | Dark           | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.off |
      | Off      | Dark           | light.indoor.dimmerable.state.off | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.off |
      | Off      | DeepDark       | light.indoor.dimmerable.state.off | event.presence.Event.On             | light.indoor.dimmerable.state.off |
      | Off      | DeepDark       | light.indoor.dimmerable.state.off | event.presence.Event.Off            | light.indoor.dimmerable.state.off |
      | Off      | DeepDark       | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Bright   | light.indoor.dimmerable.state.off |
      | Off      | DeepDark       | light.indoor.dimmerable.state.off | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.off |
      | Off      | DeepDark       | light.indoor.dimmerable.state.off | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.off |


  Scenario Outline: The Light react to forced events
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun_brightness | from_state                        | event                                                                | to_state                                              |
      | On       | Bright         | light.indoor.dimmerable.state.off | appliance.light.indoor.dimmerable.event.forced.Event.Off             | light.indoor.dimmerable.state.off                     |
      | On       | Bright         | light.indoor.dimmerable.state.off | appliance.light.indoor.dimmerable.event.forced.Event.On              | light.indoor.dimmerable.state.forced.on               |
      | On       | Bright         | light.indoor.dimmerable.state.off | appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm | light.indoor.dimmerable.state.forced.circadian_rhythm |
      | On       | Bright         | light.indoor.dimmerable.state.off | appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance      | light.indoor.dimmerable.state.forced.lux_balance      |
      | On       | Bright         | light.indoor.dimmerable.state.off | appliance.light.indoor.dimmerable.event.forced.Event.Show            | light.indoor.dimmerable.state.forced.show             |
      | On       | Bright         | light.indoor.dimmerable.state.off | appliance.light.indoor.dimmerable.event.forced.Event.Not             | light.indoor.dimmerable.state.off                     |


  Scenario Outline: The Light react to forced events from a forced on state
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun_brightness | from_state                              | event                                                                | to_state                                |
      | On       | Bright         | light.indoor.dimmerable.state.forced.on | appliance.light.indoor.dimmerable.event.forced.Event.Off             | light.indoor.dimmerable.state.off       |
      | On       | Bright         | light.indoor.dimmerable.state.forced.on | appliance.light.indoor.dimmerable.event.forced.Event.On              | light.indoor.dimmerable.state.forced.on |
      | On       | Bright         | light.indoor.dimmerable.state.forced.on | appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm | light.indoor.dimmerable.state.forced.on |
      | On       | Bright         | light.indoor.dimmerable.state.forced.on | appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance      | light.indoor.dimmerable.state.forced.on |
      | On       | Bright         | light.indoor.dimmerable.state.forced.on | appliance.light.indoor.dimmerable.event.forced.Event.Show            | light.indoor.dimmerable.state.forced.on |
      | On       | Bright         | light.indoor.dimmerable.state.forced.on | appliance.light.indoor.dimmerable.event.forced.Event.Not             | light.indoor.dimmerable.state.off       |


  Scenario Outline: The Light react to forced events from a forced circadian rhythm state
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at CircadianRhythm
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun_brightness | from_state                                            | event                                                           | to_state                                              |
      | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | appliance.light.indoor.dimmerable.event.forced.Event.Off        | light.indoor.dimmerable.state.off                     |
      | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | appliance.light.indoor.dimmerable.event.forced.Event.Not        | light.indoor.dimmerable.state.off                     |
      | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | appliance.light.indoor.dimmerable.event.forced.Event.On         | light.indoor.dimmerable.state.forced.circadian_rhythm |
      | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance | light.indoor.dimmerable.state.forced.circadian_rhythm |
      | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | appliance.light.indoor.dimmerable.event.forced.Event.Show       | light.indoor.dimmerable.state.forced.circadian_rhythm |


  Scenario Outline: The Light react to forced events from a forced lux balance state
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at LuxBalance
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun_brightness | from_state                                       | event                                                                | to_state                                         |
      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance | appliance.light.indoor.dimmerable.event.forced.Event.Off             | light.indoor.dimmerable.state.off                |
      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance | appliance.light.indoor.dimmerable.event.forced.Event.Not             | light.indoor.dimmerable.state.off                |
      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance | appliance.light.indoor.dimmerable.event.forced.Event.On              | light.indoor.dimmerable.state.forced.lux_balance |
      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance | appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm | light.indoor.dimmerable.state.forced.lux_balance |
      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance | appliance.light.indoor.dimmerable.event.forced.Event.Show            | light.indoor.dimmerable.state.forced.lux_balance |


  Scenario Outline: The Light react to forced events from a forced show state
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at Show
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun_brightness | from_state                                | event                                                                | to_state                                  |
      | On       | Bright         | light.indoor.dimmerable.state.forced.show | appliance.light.indoor.dimmerable.event.forced.Event.Off             | light.indoor.dimmerable.state.off         |
      | On       | Bright         | light.indoor.dimmerable.state.forced.show | appliance.light.indoor.dimmerable.event.forced.Event.Not             | light.indoor.dimmerable.state.off         |
      | On       | Bright         | light.indoor.dimmerable.state.forced.show | appliance.light.indoor.dimmerable.event.forced.Event.On              | light.indoor.dimmerable.state.forced.show |
      | On       | Bright         | light.indoor.dimmerable.state.forced.show | appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm | light.indoor.dimmerable.state.forced.show |
      | On       | Bright         | light.indoor.dimmerable.state.forced.show | appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance      | light.indoor.dimmerable.state.forced.show |


  Scenario Outline: The Light could be automatically un-forced from a forced state by event.presence.Off event and not by sun.brightness events
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at <forced_state>

    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | forced_state    | presence | sun_brightness | from_state                                            | event                               | to_state                                              |
      | On              | On       | Bright         | light.indoor.dimmerable.state.forced.on               | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.forced.on               |
      | On              | Off      | Bright         | light.indoor.dimmerable.state.forced.on               | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.forced.on               |
      | On              | On       | Bright         | light.indoor.dimmerable.state.forced.on               | event.presence.Event.On             | light.indoor.dimmerable.state.forced.on               |
      | On              | Off      | Bright         | light.indoor.dimmerable.state.forced.on               | event.presence.Event.On             | light.indoor.dimmerable.state.forced.on               |
      | On              | On       | Bright         | light.indoor.dimmerable.state.forced.on               | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |
      | On              | Off      | Bright         | light.indoor.dimmerable.state.forced.on               | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |
      | Show            | On       | Bright         | light.indoor.dimmerable.state.forced.show             | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.forced.show             |
      | Show            | Off      | Bright         | light.indoor.dimmerable.state.forced.show             | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.forced.show             |
      | Show            | On       | Bright         | light.indoor.dimmerable.state.forced.show             | event.presence.Event.On             | light.indoor.dimmerable.state.forced.show             |
      | Show            | Off      | Bright         | light.indoor.dimmerable.state.forced.show             | event.presence.Event.On             | light.indoor.dimmerable.state.forced.show             |
      | Show            | On       | Bright         | light.indoor.dimmerable.state.forced.show             | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |
      | Show            | Off      | Bright         | light.indoor.dimmerable.state.forced.show             | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |
      | LuxBalance      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance      | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.forced.lux_balance      |
      | LuxBalance      | Off      | Bright         | light.indoor.dimmerable.state.forced.lux_balance      | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.forced.lux_balance      |
      | LuxBalance      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance      | event.presence.Event.On             | light.indoor.dimmerable.state.forced.lux_balance      |
      | LuxBalance      | Off      | Bright         | light.indoor.dimmerable.state.forced.lux_balance      | event.presence.Event.On             | light.indoor.dimmerable.state.forced.lux_balance      |
      | LuxBalance      | On       | Bright         | light.indoor.dimmerable.state.forced.lux_balance      | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |
      | LuxBalance      | Off      | Bright         | light.indoor.dimmerable.state.forced.lux_balance      | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |
      | CircadianRhythm | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | event.sun.brightness.Event.Dark     | light.indoor.dimmerable.state.forced.circadian_rhythm |
      | CircadianRhythm | Off      | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | event.sun.brightness.Event.DeepDark | light.indoor.dimmerable.state.forced.circadian_rhythm |
      | CircadianRhythm | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | event.presence.Event.On             | light.indoor.dimmerable.state.forced.circadian_rhythm |
      | CircadianRhythm | Off      | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | event.presence.Event.On             | light.indoor.dimmerable.state.forced.circadian_rhythm |
      | CircadianRhythm | On       | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |
      | CircadianRhythm | Off      | Bright         | light.indoor.dimmerable.state.forced.circadian_rhythm | event.presence.Event.Off            | light.indoor.dimmerable.state.off                     |


  Scenario Outline: The Light shows its state: on
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | presence | sun_brightness | forced          | state                                                 | response |
      | On       | Bright         | Not             | light.indoor.dimmerable.state.off                     | False    |
      | On       | Bright         | On              | light.indoor.dimmerable.state.forced.on               | True     |
      | On       | Bright         | CircadianRhythm | light.indoor.dimmerable.state.forced.circadian_rhythm | True     |
      | On       | Bright         | LuxBalance      | light.indoor.dimmerable.state.forced.lux_balance      | True     |
      | On       | Bright         | Show            | light.indoor.dimmerable.state.forced.show             | True     |


  Scenario Outline: The Light shows its state: brightness
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.brightness state at 10
    And   the appliance has an internal appliance.light.event.circadian_rhythm.brightness state at 20
    And   the appliance has an internal appliance.light.event.lux_balancing.brightness state at 30
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property brightness
    Then  the response is <response>

    Examples:
      | presence | sun_brightness | forced          | state                                                 | response |
      | On       | Bright         | Not             | light.indoor.dimmerable.state.off                     | 10       |
      | On       | Bright         | On              | light.indoor.dimmerable.state.forced.on               | 10       |
      | On       | Bright         | CircadianRhythm | light.indoor.dimmerable.state.forced.circadian_rhythm | 20       |
      | On       | Bright         | LuxBalance      | light.indoor.dimmerable.state.forced.lux_balance      | 30       |
      | On       | Bright         | Show            | light.indoor.dimmerable.state.forced.show             | 10       |


  Scenario Outline: The Light shows its state: is_circadian_rhythm
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_circadian_rhythm
    Then  the response is <response>

    Examples:
      | presence | sun_brightness | forced          | state                                                 | response |
      | On       | Bright         | Not             | light.indoor.dimmerable.state.off                     | False    |
      | On       | Bright         | On              | light.indoor.dimmerable.state.forced.on               | False    |
      | On       | Bright         | CircadianRhythm | light.indoor.dimmerable.state.forced.circadian_rhythm | True     |
      | On       | Bright         | LuxBalance      | light.indoor.dimmerable.state.forced.lux_balance      | False    |
      | On       | Bright         | Show            | light.indoor.dimmerable.state.forced.show             | False    |


  Scenario Outline: The Light shows its state: is_lux_balancing
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_lux_balancing
    Then  the response is <response>

    Examples:
      | presence | sun_brightness | forced          | state                                                 | response |
      | On       | Bright         | Not             | light.indoor.dimmerable.state.off                     | False    |
      | On       | Bright         | On              | light.indoor.dimmerable.state.forced.on               | False    |
      | On       | Bright         | CircadianRhythm | light.indoor.dimmerable.state.forced.circadian_rhythm | False    |
      | On       | Bright         | LuxBalance      | light.indoor.dimmerable.state.forced.lux_balance      | True     |
      | On       | Bright         | Show            | light.indoor.dimmerable.state.forced.show             | False    |


  Scenario Outline: The Light shows its state: is_showing
    Given A light.indoor.dimmerable.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_showing
    Then  the response is <response>

    Examples:
      | presence | sun_brightness | forced          | state                                                 | response |
      | On       | Bright         | Not             | light.indoor.dimmerable.state.off                     | False    |
      | On       | Bright         | On              | light.indoor.dimmerable.state.forced.on               | False    |
      | On       | Bright         | CircadianRhythm | light.indoor.dimmerable.state.forced.circadian_rhythm | False    |
      | On       | Bright         | LuxBalance      | light.indoor.dimmerable.state.forced.lux_balance      | False    |
      | On       | Bright         | Show            | light.indoor.dimmerable.state.forced.show             | True     |
