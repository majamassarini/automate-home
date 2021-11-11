Feature: A zone Light


  Scenario Outline: The Light react to multiple events
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state           | event                               | to_state                    |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | On       | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.courtesy.Event.On             | light.zone.state.on         |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.courtesy.Event.Off            | light.zone.state.on         |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.presence.Event.On             | light.zone.state.on         |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Dark     | light.zone.state.on         |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.On          | light.zone.state.on         |
      | Off   | On       | Off      | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.Off         | light.zone.state.on         |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | On       | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | On       | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.On             | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.Off            | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.presence.Event.On             | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.presence.Event.Off            | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Dark     | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.On          | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.Off         | light.zone.state.on         |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | Off      | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | Off      | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.on         |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.presence.Event.On             | light.zone.state.on         |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.off        |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | Off      | Off      | DeepDark       | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | Off      | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | Off   | Off      | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.On             | light.zone.state.on         |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.Off            | light.zone.state.off        |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.presence.Event.On             | light.zone.state.on         |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.presence.Event.Off            | light.zone.state.on         |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Dark     | light.zone.state.on         |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.On          | light.zone.state.on         |
      | Off   | Off      | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.Off         | light.zone.state.on         |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | On       | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | On       | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.courtesy.Event.Off            | light.zone.state.on         |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.presence.Event.Off            | light.zone.state.off        |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Dark     | light.zone.state.on         |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.On          | light.zone.state.on         |
      | On    | On       | Off      | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.Off         | light.zone.state.on         |
      | On    | On       | On       | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | On       | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | On       | On       | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | On       | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | On       | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | On       | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | On       | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | On       | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | On       | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | On       | On       | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | On       | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | On       | On       | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | On       | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | On       | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | On       | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | On       | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | On       | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | On       | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.Off            | light.zone.state.on         |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.presence.Event.Off            | light.zone.state.on         |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Dark     | light.zone.state.on         |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.On          | light.zone.state.on         |
      | On    | On       | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.Off         | light.zone.state.on         |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.off        |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | Off      | Off      | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.off        |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | Off      | Off      | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.off        |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | Off      | Off      | DeepDark       | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | Off      | On       | Bright         | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.presence.Event.Off            | light.zone.state.off        |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.Dark     | light.zone.state.off        |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.On          | light.zone.state.off        |
      | On    | Off      | On       | Dark           | light.zone.state.off | event.alarm.armed.Event.Off         | light.zone.state.off        |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.courtesy.Event.Off            | light.zone.state.off        |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.presence.Event.On             | light.zone.state.alarmed.on |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.presence.Event.Off            | light.zone.state.on         |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Bright   | light.zone.state.off        |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.Dark     | light.zone.state.on         |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.sun.brightness.Event.DeepDark | light.zone.state.on         |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.On          | light.zone.state.on         |
      | On    | Off      | On       | DeepDark       | light.zone.state.on  | event.alarm.armed.Event.Off         | light.zone.state.on         |


  Scenario Outline: The Light react to multiple events from an alarmed initial state (changed order in events)
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at On
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | courtesy | sun_brightness | from_state                  | event                               | to_state                     |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.off         |
      | On       | Off      | Bright         | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.on          |
      | On       | Off      | Dark           | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.on          |
      | On       | Off      | DeepDark       | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.off         |
      | On       | On       | Bright         | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.on          |
      | On       | On       | Dark           | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.on          |
      | On       | On       | DeepDark       | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.off         |
      | Off      | On       | Bright         | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.on          |
      | Off      | On       | Dark           | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.courtesy.Event.On             | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.courtesy.Event.Off            | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.presence.Event.On             | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.presence.Event.Off            | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.Bright   | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.Dark     | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.sun.brightness.Event.DeepDark | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.alarm.armed.Event.On          | light.zone.state.alarmed.on  |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.alarm.armed.Event.Off         | light.zone.state.on          |
      | Off      | On       | DeepDark       | light.zone.state.alarmed.on | event.toggle.Event.Off              | light.zone.state.alarmed.off |


  Scenario Outline: The Light react to forced on/off events
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state           | event                                  | to_state                    |
      | Off   | On       | Off      | Bright         | light.zone.state.off | appliance.light.event.forced.Event.Off | light.zone.state.off        |
      | Off   | On       | Off      | Bright         | light.zone.state.off | appliance.light.event.forced.Event.On  | light.zone.state.forced.on  |
      | Off   | On       | Off      | Bright         | light.zone.state.off | appliance.light.event.forced.Event.Not | light.zone.state.off        |

      | Off   | On       | On       | DeepDark       | light.zone.state.on  | appliance.light.event.forced.Event.Off | light.zone.state.forced.off |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | appliance.light.event.forced.Event.On  | light.zone.state.on         |
      | Off   | On       | On       | DeepDark       | light.zone.state.on  | appliance.light.event.forced.Event.Not | light.zone.state.on         |


  Scenario Outline: The Light react does not react to forced on/off events from an alarmed state
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state                  | event                                  | to_state                    |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.Off | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.On  | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.Not | light.zone.state.alarmed.on |


  Scenario Outline: The Light react to forced on/off events (from a forced on state)
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal appliance.light.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state                 | event                                  | to_state                   |
      | Off   | On       | Off      | Bright         | light.zone.state.forced.on | appliance.light.event.forced.Event.Off | light.zone.state.off       |
      | Off   | On       | Off      | Bright         | light.zone.state.forced.on | appliance.light.event.forced.Event.On  | light.zone.state.forced.on |
      | Off   | On       | Off      | Bright         | light.zone.state.forced.on | appliance.light.event.forced.Event.Not | light.zone.state.off       |


  Scenario Outline: The Light react to forced on/off events from an alarmed state (and a forced off state)
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state                  | event                                  | to_state                    |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.Off | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.On  | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.Not | light.zone.state.alarmed.on |


  Scenario Outline: The Light react to forced on/off events (from a forced off state)
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal appliance.light.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state                  | event                                  | to_state                    |
      | Off   | On       | Off      | DeepDark       | light.zone.state.forced.off | appliance.light.event.forced.Event.Off | light.zone.state.forced.off |
      | Off   | On       | Off      | DeepDark       | light.zone.state.forced.off | appliance.light.event.forced.Event.On  | light.zone.state.on         |
      | Off   | On       | Off      | DeepDark       | light.zone.state.forced.off | appliance.light.event.forced.Event.Not | light.zone.state.on         |


  Scenario Outline: The Light does not react to forced on/off events from an alarmed state (and a forced off state).
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state                  | event                                  | to_state                    |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.Off | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.On  | light.zone.state.alarmed.on |
      | On    | On       | Off      | Bright         | light.zone.state.alarmed.on | appliance.light.event.forced.Event.Not | light.zone.state.alarmed.on |


  Scenario Outline: The Light could be automatically un-forced from a forced on state by alarm.armed.Event.On and sun.brightness.Event.Bright events and not by other events
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.courtesy state at <courtesy>
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal appliance.light.event.forced state at On

    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | presence | courtesy | sun_brightness | from_state                 | event                               | to_state                   |
      | Off   | On       | On       | Bright         | light.zone.state.forced.on | event.sun.brightness.Event.Dark     | light.zone.state.forced.on |
      | Off   | On       | On       | Bright         | light.zone.state.forced.on | event.sun.brightness.Event.DeepDark | light.zone.state.forced.on |
      | Off   | On       | On       | Bright         | light.zone.state.forced.on | event.sun.brightness.Event.Bright   | light.zone.state.off       |
      | Off   | On       | Off      | Bright         | light.zone.state.forced.on | event.presence.Event.Off            | light.zone.state.forced.on |
      | Off   | Off      | On       | Bright         | light.zone.state.forced.on | event.courtesy.Event.Off            | light.zone.state.forced.on |
      | Off   | Off      | On       | Bright         | light.zone.state.forced.on | event.alarm.armed.Event.Off         | light.zone.state.forced.on |
      | Off   | Off      | On       | Bright         | light.zone.state.forced.on | event.alarm.armed.Event.On          | light.zone.state.off       |


  Scenario Outline: The Light shows its on state
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at DeepDark
    And   the appliance has an internal appliance.light.event.forced state at <forced>
    And   the appliance has an internal event.toggle state at <toggle>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | armed | presence | forced | toggle | state                        | response |
      | Off   | Off      | Not    | On     | light.zone.state.off         | False    |
      | Off   | On       | Not    | On     | light.zone.state.on          | True     |
      | On    | On       | Not    | On     | light.zone.state.alarmed.on  | True     |
      | On    | On       | Not    | Off    | light.zone.state.alarmed.off | False    |
      | Off   | Off      | On     | On     | light.zone.state.forced.on   | True     |
      | Off   | On       | Off    | On     | light.zone.state.forced.off  | False    |


  Scenario Outline: The Light shows its alarmed state
    Given A light.zone.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at DeepDark
    And   the appliance has an internal appliance.light.event.forced state at <forced>
    And   the appliance has an internal event.toggle state at <toggle>
    And   it's calculated state is <state>
    When  it's asked for its state property is_alarmed
    Then  the response is <response>

    Examples:
      | armed | presence | forced | toggle | state                        | response |
      | Off   | Off      | Not    | On     | light.zone.state.off         | False    |
      | Off   | On       | Not    | On     | light.zone.state.on          | False    |
      | On    | On       | Not    | On     | light.zone.state.alarmed.on  | True     |
      | On    | On       | Not    | Off    | light.zone.state.alarmed.off | True     |
      | Off   | Off      | On     | On     | light.zone.state.forced.on   | False    |
      | Off   | On       | Off    | On     | light.zone.state.forced.off  | False    |
