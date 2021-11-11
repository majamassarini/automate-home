Feature: A sprinkler appliance


  Scenario Outline: The Sprinkler react to not forced events from a not forced state
    Given A sprinkler.Appliance appliance
    And   the appliance has an internal event.rain state at <is_raining>
    And   the appliance has an internal event.rain.forecast state at <will_rain>
    And   the appliance has an internal event.rain.in_the_past state at <has_rained>
    And   the appliance has an internal event.sun.phase state at <sun_phase>
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal appliance.sprinkler.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | sun_phase | is_raining | will_rain | has_rained | from_state                   | event                            | to_state                     |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.enable.Event.On            | sprinkler.state.on           |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.sun.phase.Event.Sunset     | sprinkler.state.on           |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.rain.Event.No              | sprinkler.state.on           |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.rain.forecast.Event.On     | sprinkler.state.partially_on |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.rain.forecast.Event.Off    | sprinkler.state.on           |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.rain.in_the_past.Event.On  | sprinkler.state.partially_on |
      | On     | Sunset    | No         | Off       | Off        | sprinkler.state.on           | event.rain.in_the_past.Event.Off | sprinkler.state.on           |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.enable.Event.On            | sprinkler.state.partially_on |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.sun.phase.Event.Sunset     | sprinkler.state.partially_on |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.rain.Event.No              | sprinkler.state.partially_on |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.rain.forecast.Event.Off    | sprinkler.state.partially_on |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.rain.in_the_past.Event.On  | sprinkler.state.partially_on |
      | On     | Sunset    | No         | Off       | On         | sprinkler.state.partially_on | event.rain.in_the_past.Event.Off | sprinkler.state.on           |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.enable.Event.On            | sprinkler.state.partially_on |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.sun.phase.Event.Sunset     | sprinkler.state.partially_on |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.rain.Event.No              | sprinkler.state.partially_on |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.rain.forecast.Event.On     | sprinkler.state.partially_on |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.rain.forecast.Event.Off    | sprinkler.state.on           |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | Off        | sprinkler.state.partially_on | event.rain.in_the_past.Event.Off | sprinkler.state.partially_on |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.partially_on |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.partially_on |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.on           |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.partially_on |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.partially_on |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.on           |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.partially_on |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.partially_on |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |

      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.on           |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.partially_on |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | No         | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.partially_on |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunset    | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | No         | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | No         | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | Off       | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | Off        | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.On            | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.enable.Event.Off           | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunset     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.Gentle          | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.Event.No              | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.On     | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.forecast.Event.Off    | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | Off    | Sunrise   | Gentle     | On        | On         | sprinkler.state.off          | event.rain.in_the_past.Event.Off | sprinkler.state.off          |

  Scenario Outline: The Sprinkler react to forced events from a not forced state
    Given A sprinkler.Appliance appliance
    And   the appliance has an internal event.sun.phase state at Sunset
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.rain.forecast state at <will_rain>
    And   the appliance has an internal appliance.sprinkler.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | will_rain | from_state                   | event                                              | to_state                            |
      | On     | Off       | sprinkler.state.on           | appliance.sprinkler.event.forced.Event.On          | sprinkler.state.on                  |
      | On     | Off       | sprinkler.state.on           | appliance.sprinkler.event.forced.Event.PartiallyOn | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.on           | appliance.sprinkler.event.forced.Event.Off         | sprinkler.state.forced.off          |
      | On     | On        | sprinkler.state.partially_on | appliance.sprinkler.event.forced.Event.On          | sprinkler.state.partially_on        |
      | On     | On        | sprinkler.state.partially_on | appliance.sprinkler.event.forced.Event.PartiallyOn | sprinkler.state.partially_on        |
      | On     | On        | sprinkler.state.partially_on | appliance.sprinkler.event.forced.Event.Off         | sprinkler.state.forced.off          |
      | Off    | Off       | sprinkler.state.off          | appliance.sprinkler.event.forced.Event.On          | sprinkler.state.forced.on           |
      | Off    | Off       | sprinkler.state.off          | appliance.sprinkler.event.forced.Event.PartiallyOn | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.off          | appliance.sprinkler.event.forced.Event.Off         | sprinkler.state.off                 |

  Scenario Outline: The Sprinkler react to not forced events from a On forced state, and will be reset by a
  sun phase sunrise event
    Given A sprinkler.Appliance appliance
    And   the appliance has an internal event.sun.phase state at Sunset
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.rain.forecast state at <will_rain>
    And   the appliance has an internal appliance.sprinkler.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | will_rain | from_state                   | event                            | to_state                     |
      | On     | On        | sprinkler.state.partially_on | event.enable.Event.On            | sprinkler.state.partially_on |
      | On     | On        | sprinkler.state.partially_on | event.enable.Event.Off           | sprinkler.state.off          |
      | On     | On        | sprinkler.state.partially_on | event.sun.phase.Event.Sunset     | sprinkler.state.partially_on |
      | On     | On        | sprinkler.state.partially_on | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | On     | On        | sprinkler.state.partially_on | event.rain.Event.Gentle          | sprinkler.state.off          |
      | On     | On        | sprinkler.state.partially_on | event.rain.Event.No              | sprinkler.state.partially_on |
      | On     | On        | sprinkler.state.partially_on | event.rain.forecast.Event.On     | sprinkler.state.partially_on |
      | On     | On        | sprinkler.state.partially_on | event.rain.forecast.Event.Off    | sprinkler.state.on           |
      | On     | On        | sprinkler.state.partially_on | event.rain.in_the_past.Event.On  | sprinkler.state.off          |
      | On     | On        | sprinkler.state.partially_on | event.rain.in_the_past.Event.Off | sprinkler.state.partially_on |
      | Off    | Off       | sprinkler.state.forced.on    | event.enable.Event.On            | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.enable.Event.Off           | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.sun.phase.Event.Sunset     | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.sun.phase.Event.Sunrise    | sprinkler.state.off          |
      | Off    | Off       | sprinkler.state.forced.on    | event.rain.Event.Gentle          | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.rain.Event.No              | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.rain.forecast.Event.On     | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.rain.forecast.Event.Off    | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.rain.in_the_past.Event.On  | sprinkler.state.forced.on    |
      | Off    | Off       | sprinkler.state.forced.on    | event.rain.in_the_past.Event.Off | sprinkler.state.forced.on    |


  Scenario Outline: The Sprinkler react to not forced events from a PartiallyOn forced state, and will be reset by a
  sun phase sunrise event
    Given A sprinkler.Appliance appliance
    And   the appliance has an internal event.sun.phase state at Sunset
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.rain.forecast state at <will_rain>
    And   the appliance has an internal appliance.sprinkler.event.forced state at PartiallyOn
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | will_rain | from_state                          | event                            | to_state                            |
      | On     | Off       | sprinkler.state.forced.partially_on | event.enable.Event.On            | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.enable.Event.Off           | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.sun.phase.Event.Sunset     | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.sun.phase.Event.Sunrise    | sprinkler.state.off                 |
      | On     | Off       | sprinkler.state.forced.partially_on | event.rain.Event.Gentle          | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.rain.Event.No              | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.rain.forecast.Event.On     | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.rain.forecast.Event.Off    | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.rain.in_the_past.Event.On  | sprinkler.state.forced.partially_on |
      | On     | Off       | sprinkler.state.forced.partially_on | event.rain.in_the_past.Event.Off | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.enable.Event.On            | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.enable.Event.Off           | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.sun.phase.Event.Sunset     | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.sun.phase.Event.Sunrise    | sprinkler.state.off                 |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.rain.Event.Gentle          | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.rain.Event.No              | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.rain.forecast.Event.On     | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.rain.forecast.Event.Off    | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.rain.in_the_past.Event.On  | sprinkler.state.forced.partially_on |
      | Off    | Off       | sprinkler.state.forced.partially_on | event.rain.in_the_past.Event.Off | sprinkler.state.forced.partially_on |

  Scenario Outline: The Sprinkler react to not forced events from a Off forced state, and will be reset by a
  sun phase sunrise event
    Given A sprinkler.Appliance appliance
    And   the appliance has an internal event.sun.phase state at Sunset
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.rain.forecast state at <will_rain>
    And   the appliance has an internal appliance.sprinkler.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | will_rain | from_state                 | event                            | to_state                   |
      | On     | Off       | sprinkler.state.forced.off | event.enable.Event.On            | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.enable.Event.Off           | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.sun.phase.Event.Sunset     | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.sun.phase.Event.Sunrise    | sprinkler.state.off        |
      | On     | Off       | sprinkler.state.forced.off | event.rain.Event.Gentle          | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.rain.Event.No              | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.rain.forecast.Event.On     | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.rain.forecast.Event.Off    | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.rain.in_the_past.Event.On  | sprinkler.state.forced.off |
      | On     | Off       | sprinkler.state.forced.off | event.rain.in_the_past.Event.Off | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.enable.Event.On            | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.enable.Event.Off           | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.sun.phase.Event.Sunset     | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.sun.phase.Event.Sunrise    | sprinkler.state.off        |
      | On     | On        | sprinkler.state.forced.off | event.rain.Event.Gentle          | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.rain.Event.No              | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.rain.forecast.Event.On     | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.rain.forecast.Event.Off    | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.rain.in_the_past.Event.On  | sprinkler.state.forced.off |
      | On     | On        | sprinkler.state.forced.off | event.rain.in_the_past.Event.Off | sprinkler.state.forced.off |

  Scenario Outline: The Sprinkler shows its property: duration
    Given A sprinkler.Appliance appliance
    And   the appliance has an internal event.sun.phase state at Sunset
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.rain.forecast state at <will_rain>
    And   the appliance has an internal appliance.sprinkler.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property duration
    Then  the response is <response>

    Examples:
      | enable | forced      | will_rain | state                               | response |
      | Off    | Not         | Off       | sprinkler.state.off                 | 1200     |
      | On     | Not         | Off       | sprinkler.state.on                  | 1200     |
      | On     | Not         | On        | sprinkler.state.partially_on        | 350      |
      | Off    | On          | Off       | sprinkler.state.forced.on           | 1200     |
      | Off    | PartiallyOn | Off       | sprinkler.state.forced.partially_on | 350      |
      | On     | Off         | Off       | sprinkler.state.forced.off          | 1200     |
