Feature: A light appliance


  Scenario Outline: The Light react to courtesy and sun brightness events
    Given A light.Appliance appliance
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | courtesy | sun_brightness | from_state      | event                               | to_state        |
      | Off      | Bright         | light.state.off | event.courtesy.Event.On             | light.state.off |
      | Off      | Bright         | light.state.off | event.courtesy.Event.Off            | light.state.off |
      | Off      | Bright         | light.state.off | event.sun.brightness.Event.Bright   | light.state.off |
      | Off      | Bright         | light.state.off | event.sun.brightness.Event.Dark     | light.state.off |
      | Off      | Bright         | light.state.off | event.sun.brightness.Event.DeepDark | light.state.off |

      | Off      | Dark           | light.state.off | event.courtesy.Event.On             | light.state.off |
      | Off      | Dark           | light.state.off | event.courtesy.Event.Off            | light.state.off |
      | Off      | Dark           | light.state.off | event.sun.brightness.Event.Bright   | light.state.off |
      | Off      | Dark           | light.state.off | event.sun.brightness.Event.Dark     | light.state.off |
      | Off      | Dark           | light.state.off | event.sun.brightness.Event.DeepDark | light.state.off |

      | Off      | DeepDark       | light.state.off | event.courtesy.Event.On             | light.state.on  |
      | Off      | DeepDark       | light.state.off | event.courtesy.Event.Off            | light.state.off |
      | Off      | DeepDark       | light.state.off | event.sun.brightness.Event.Bright   | light.state.off |
      | Off      | DeepDark       | light.state.off | event.sun.brightness.Event.Dark     | light.state.off |
      | Off      | DeepDark       | light.state.off | event.sun.brightness.Event.DeepDark | light.state.off |

      | On       | Bright         | light.state.off | event.courtesy.Event.On             | light.state.off |
      | On       | Bright         | light.state.off | event.courtesy.Event.Off            | light.state.off |
      | On       | Bright         | light.state.off | event.sun.brightness.Event.Bright   | light.state.off |
      | On       | Bright         | light.state.off | event.sun.brightness.Event.Dark     | light.state.off |
      | On       | Bright         | light.state.off | event.sun.brightness.Event.DeepDark | light.state.on  |

      | On       | Dark           | light.state.off | event.courtesy.Event.On             | light.state.off |
      | On       | Dark           | light.state.off | event.courtesy.Event.Off            | light.state.off |
      | On       | Dark           | light.state.off | event.sun.brightness.Event.Bright   | light.state.off |
      | On       | Dark           | light.state.off | event.sun.brightness.Event.Dark     | light.state.off |
      | On       | Dark           | light.state.off | event.sun.brightness.Event.DeepDark | light.state.on  |

      | On       | DeepDark       | light.state.on  | event.courtesy.Event.On             | light.state.on  |
      | On       | DeepDark       | light.state.on  | event.courtesy.Event.Off            | light.state.off |
      | On       | DeepDark       | light.state.on  | event.sun.brightness.Event.Bright   | light.state.off |
      | On       | DeepDark       | light.state.on  | event.sun.brightness.Event.Dark     | light.state.on  |
      | On       | DeepDark       | light.state.on  | event.sun.brightness.Event.DeepDark | light.state.on  |


  Scenario Outline: The Light react to forced on/off events
    Given A light.Appliance appliance
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | courtesy | sun_brightness | from_state      | event                                  | to_state               |
      | Off      | Bright         | light.state.off | appliance.light.event.forced.Event.Off | light.state.off        |
      | Off      | Bright         | light.state.off | appliance.light.event.forced.Event.On  | light.state.forced.on  |

      | Off      | Dark           | light.state.off | appliance.light.event.forced.Event.Off | light.state.off        |
      | Off      | Dark           | light.state.off | appliance.light.event.forced.Event.On  | light.state.forced.on  |

      | Off      | DeepDark       | light.state.off | appliance.light.event.forced.Event.Off | light.state.off        |
      | Off      | DeepDark       | light.state.off | appliance.light.event.forced.Event.On  | light.state.forced.on  |

      | On       | Bright         | light.state.off | appliance.light.event.forced.Event.Off | light.state.off        |
      | On       | Bright         | light.state.off | appliance.light.event.forced.Event.On  | light.state.forced.on  |

      | On       | Dark           | light.state.off | appliance.light.event.forced.Event.Off | light.state.off        |
      | On       | Dark           | light.state.off | appliance.light.event.forced.Event.On  | light.state.forced.on  |

      | On       | DeepDark       | light.state.on  | appliance.light.event.forced.Event.Off | light.state.forced.off |
      | On       | DeepDark       | light.state.on  | appliance.light.event.forced.Event.On  | light.state.on         |


  Scenario Outline: The Light react to forced on/off events from a forced on state
    Given A light.Appliance appliance
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | courtesy | sun_brightness | from_state            | event                                  | to_state               |
      | Off      | Bright         | light.state.forced.on | appliance.light.event.forced.Event.Off | light.state.off        |
      | Off      | Dark           | light.state.forced.on | appliance.light.event.forced.Event.Off | light.state.off        |
      | Off      | DeepDark       | light.state.forced.on | appliance.light.event.forced.Event.Off | light.state.off        |
      | On       | Bright         | light.state.forced.on | appliance.light.event.forced.Event.Off | light.state.off        |
      | On       | Dark           | light.state.forced.on | appliance.light.event.forced.Event.Off | light.state.off        |
      | On       | DeepDark       | light.state.on        | appliance.light.event.forced.Event.Off | light.state.forced.off |

      | Off      | Bright         | light.state.forced.on | appliance.light.event.forced.Event.Not | light.state.off        |
      | Off      | Dark           | light.state.forced.on | appliance.light.event.forced.Event.Not | light.state.off        |
      | Off      | DeepDark       | light.state.forced.on | appliance.light.event.forced.Event.Not | light.state.off        |
      | On       | Bright         | light.state.forced.on | appliance.light.event.forced.Event.Not | light.state.off        |
      | On       | Dark           | light.state.forced.on | appliance.light.event.forced.Event.Not | light.state.off        |
      | On       | DeepDark       | light.state.on        | appliance.light.event.forced.Event.Not | light.state.on         |


  Scenario Outline: The Light could be automatically un-forced from a forced on state by sun.brightness events and not by courtesy events
    Given A light.Appliance appliance
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at On

    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | courtesy | sun_brightness | from_state             | event                                  | to_state              |
      | Off      | Dark           | light.state.forced.on  | event.courtesy.Event.On                | light.state.forced.on |
      | Off      | DeepDark       | light.state.forced.on  | event.courtesy.Event.On                | light.state.forced.on |
      | On       | Bright         | light.state.forced.on  | event.sun.brightness.Event.Dark        | light.state.forced.on |
      | On       | Dark           | light.state.forced.on  | event.sun.brightness.Event.DeepDark    | light.state.on        |


  Scenario Outline: The Light could be automatically un-forced from a forced off state by sun.brightness events and not by courtesy events
    Given A light.Appliance appliance
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at Off

    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | courtesy | sun_brightness | from_state             | event                                  | to_state              |
      | On       | DeepDark       | light.state.forced.off | event.courtesy.Event.Off               | light.state.forced.off|
      | On       | DeepDark       | light.state.forced.off | event.courtesy.Event.Off               | light.state.forced.off|
      | On       | DeepDark       | light.state.forced.off | event.sun.brightness.Event.Dark        | light.state.off       |


  Scenario Outline: The Light shows its state
    Given A light.Appliance appliance
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | courtesy | sun_brightness | forced | state                  | response |
      | Off      | Bright         | Not    | light.state.off        | False    |
      | On       | DeepDark       | Not    | light.state.on         | True     |
      | Off      | Bright         | On     | light.state.forced.on  | True     |
      | On       | DeepDark       | Off    | light.state.forced.off | False    |
