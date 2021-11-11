Feature: An outdoor Curtain.
  It should be closed when the sun (with an high brightness) hits the curtain's window or at sunset.
  It should be opened at sunrise or when the wind is strong.
  It could be forced opened or forced closed.

  Scenario Outline: The Curtain react to wind, sun brightness, sun twilight and sun hit events
    Given A curtain.outdoor.Appliance appliance
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sun_twilight | sun_brightness | sun_hit | wind   | from_state                   | event                                  | to_state                     |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.opened |

      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.closed |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.closed |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.closed |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Bright      | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.Dark        | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunrise | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.twilight.civil.Event.Sunset  | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Bright      | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.Dark        | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.brightness.Event.DeepDark    | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunhit             | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.sun.hit.Event.Sunleft            | curtain.outdoor.state.closed |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Strong                | curtain.outdoor.state.opened |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | event.wind.Event.Weak                  | curtain.outdoor.state.closed |

  Scenario Outline: The Curtain react to forced opened/closed events
    Given A curtain.outdoor.Appliance appliance
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sun_twilight | sun_brightness | sun_hit | wind   | from_state                   | event                                       | to_state                            |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |


  Scenario Outline: The Curtain react to forced opened/closed events from a forced opened state
    Given A curtain.outdoor.Appliance appliance
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Opened
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sun_twilight | sun_brightness | sun_hit | wind   | from_state                          | event                                       | to_state                            |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.opened        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.forced.opened | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |


  Scenario Outline: The Curtain react to forced opened/closed events from a forced closed state
    Given A curtain.outdoor.Appliance appliance
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at Closed
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sun_twilight | sun_brightness | sun_hit | wind   | from_state                          | event                                       | to_state                            |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunleft | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Dark           | Sunhit  | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunleft | Weak   | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunrise      | Bright         | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunrise      | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | DeepDark       | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | DeepDark       | Sunleft | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | DeepDark       | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | DeepDark       | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Dark           | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Dark           | Sunleft | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Dark           | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Dark           | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Bright         | Sunleft | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Bright         | Sunleft | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |

      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.opened        |
      | Sunset       | Bright         | Sunhit  | Strong | curtain.outdoor.state.forced.closed | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.forced.closed |

      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Opened | curtain.outdoor.state.forced.opened |
      | Sunset       | Bright         | Sunhit  | Weak   | curtain.outdoor.state.closed        | appliance.curtain.event.forced.Event.Closed | curtain.outdoor.state.closed        |


  Scenario Outline: The Curtain shows its state
    Given A curtain.outdoor.Appliance appliance
    And   the appliance has an internal event.wind state at <wind>
    And   the appliance has an internal event.sun.brightness state at <sun_brightness>
    And   the appliance has an internal event.sun.twilight.civil state at <sun_twilight>
    And   the appliance has an internal event.sun.hit state at <sun_hit>
    And   the appliance has an internal appliance.curtain.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_opened
    Then  the response is <response>

    Examples:
      | sun_twilight | sun_brightness | sun_hit | wind   | forced | state                               | response |
      | Sunrise      | Bright         | Sunleft | Strong | Not    | curtain.outdoor.state.opened        | True     |
      | Sunrise      | Bright         | Sunhit  | Weak   | Not    | curtain.outdoor.state.closed        | False    |
      | Sunrise      | Bright         | Sunleft | Weak   | Closed | curtain.outdoor.state.forced.closed | False    |
      | Sunrise      | Bright         | Sunhit  | Weak   | Opened | curtain.outdoor.state.forced.opened | True     |
