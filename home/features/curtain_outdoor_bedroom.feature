Feature: An outdoor Curtain (in a bedroom).

  It should be closed when the sun (with an high brightness) hits the curtain's window or at sunset or when
  some user is asleep.

  It should be opened when the user is awake (after sunrise) or when the wind is strong.

  It could be forced opened or forced closed.

  Scenario Outline: The Curtain react to wind, sun brightness, sun twilight, sun hit events and user sleepiness.
    Given A curtain.outdoor.bedroom.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | sun_brightness | sun_hit | wind   | from_state                           | event                                  | to_state                             |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |


      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.opened |

      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Strong                | curtain.outdoor.bedroom.state.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.wind.Event.Weak                  | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Awake           | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Asleep          | curtain.outdoor.bedroom.state.closed |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | event.sleepiness.Event.Sleepy          | curtain.outdoor.bedroom.state.closed |

  Scenario Outline: The Curtain react to forced opened/closed events
    Given A curtain.outdoor.bedroom.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | sun_brightness | sun_hit | wind   | from_state                           | event                                       | to_state                                    |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |


      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Asleep     | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Asleep     | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |


  Scenario Outline: The Curtain react to forced opened/closed events from a forced opened state
    Given A curtain.outdoor.bedroom.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Opened
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | sun_brightness | sun_hit | wind   | from_state                                  | event                                       | to_state                                    |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |


  Scenario Outline: The Curtain react to forced opened/closed events from a forced closed state
    Given A curtain.outdoor.bedroom.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Closed
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sleepiness | sun_twilight | sun_brightness | sun_hit | wind   | from_state                                  | event                                       | to_state                                    |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |

      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.opened        |
      | Awake      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.bedroom.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.forced.closed |

      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.bedroom.state.forced.opened |
      | Awake      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.bedroom.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.bedroom.state.closed        |


  Scenario Outline: The Curtain shows its state
    Given A curtain.outdoor.bedroom.Appliance appliance
    And   the appliance has an internal event.sleepiness state at <sleepiness>
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_opened
    Then  the response is <response>

    Examples:
      | sleepiness | sun_twilight | sun_brightness | sun_hit | wind   | forced | state                                       | response |
      | Awake      | Sunrise      | Bright         | Sunleft | Strong | Not    | curtain.outdoor.bedroom.state.opened        | True     |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | Not    | curtain.outdoor.bedroom.state.closed        | False    |
      | Awake      | Sunrise      | Bright         | Sunleft | Weak   | Closed | curtain.outdoor.bedroom.state.forced.closed | False    |
      | Awake      | Sunrise      | Bright         | Sunhit  | Weak   | Opened | curtain.outdoor.bedroom.state.forced.opened | True     |
