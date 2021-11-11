Feature: A Presence Christmas Socket
  A presence Christmas socket which is by default on.
  It can be turned off by the system if nobody is in the room unless it is Christmas time.

  You could know that nobody is in the room when, as an example, the room alarm sensors are presence.
  Other protocol triggers could be used for the same purpose.

  If it is Christmas time then it is on when outside is deep dark and there is someone in the room.

  If it is Christmas eve or Christmas day than it is on even if outside is bright or nobody is in the room.

  If it is San Silvester eve or day than it is on even if outside is bright or nobody is in the room.

  If it is the Epiphany eve or day than it is on even if outside is bright or nobody is in the room.


  Scenario Outline: The Socket react to alarm presence, sun phase and holiday events (internal alarm presence state is Off)
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at On
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sun      | christmas | san_silvester | epiphany | from_state                          | event                                  | to_state                            |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.off |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.On               | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.off |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Dark     | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.off |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.off |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Dark     | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Dark     | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Dark     | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |


  Scenario Outline: The Socket react to alarm presence, sun phase and holiday events (internal alarm presence state is On)
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at Off
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | sun      | christmas | san_silvester | epiphany | from_state                          | event                                  | to_state                            |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | DeepDark | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.off |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.off |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | DeepDark | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Bright   | Over      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Over      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.Off                | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.presence.Event.On               | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.off | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.off |
      | Bright   | Time      | Over          | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.off |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Over     | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.Off                | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.presence.Event.On               | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.DeepDark    | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.sun.brightness.Event.Bright      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Over     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Time     | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.christmas.Event.Day      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Over | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.san_silvester.Event.Day  | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Over      | socket.presence.christmas.state.on  |
      | Bright   | Time      | Day           | Day      | socket.presence.christmas.state.on  | event.holiday.epiphany.Event.Day       | socket.presence.christmas.state.on  |

  Scenario Outline: The Socket react to forced on/off events
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun      | christmas | san_silvester | epiphany | from_state                          | event                                   | to_state                                   |
      | On       | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | appliance.socket.event.forced.Event.Off | socket.presence.christmas.state.forced.off |
      | On       | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on  | appliance.socket.event.forced.Event.On  | socket.presence.christmas.state.on         |

      | Off      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | appliance.socket.event.forced.Event.Off | socket.presence.christmas.state.off        |
      | Off      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off | appliance.socket.event.forced.Event.On  | socket.presence.christmas.state.forced.on  |


  Scenario Outline: The Socket react to forced on/off events from a forced on state
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun      | christmas | san_silvester | epiphany | from_state                                | event                                   | to_state                                   |
      | On       | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on        | appliance.socket.event.forced.Event.Off | socket.presence.christmas.state.forced.off |
      | On       | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.on        | appliance.socket.event.forced.Event.On  | socket.presence.christmas.state.on         |

      | Off      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.forced.on | appliance.socket.event.forced.Event.Off | socket.presence.christmas.state.off        |
      | Off      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.forced.on | appliance.socket.event.forced.Event.On  | socket.presence.christmas.state.forced.on  |


  Scenario Outline: The Socket react to forced on/off events from a forced off state
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun      | christmas | san_silvester | epiphany | from_state                                 | event                                   | to_state                                   |
      | On       | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.forced.off | appliance.socket.event.forced.Event.Off | socket.presence.christmas.state.forced.off |
      | On       | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.forced.off | appliance.socket.event.forced.Event.On  | socket.presence.christmas.state.on         |

      | Off      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off        | appliance.socket.event.forced.Event.Off | socket.presence.christmas.state.off        |
      | Off      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.off        | appliance.socket.event.forced.Event.On  | socket.presence.christmas.state.forced.on  |


  Scenario Outline: The Socket could be automatically un-forced from a forced off state by multiple events
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun      | christmas | san_silvester | epiphany | from_state                                 | event                             | to_state                            |
      | On       | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.forced.off | event.presence.Event.Off           | socket.presence.christmas.state.off |
      | On       | DeepDark | Time      | Over          | Over     | socket.presence.christmas.state.forced.off | event.sun.brightness.Event.Bright | socket.presence.christmas.state.off |

  Scenario Outline: The Socket could be automatically un-forced from a forced on state by multiple events
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | presence | sun      | christmas | san_silvester | epiphany | from_state                                | event                                 | to_state                                  |
      | Off      | DeepDark | Over      | Over          | Over     | socket.presence.christmas.state.forced.on | event.presence.Event.On              | socket.presence.christmas.state.forced.on |
      | On       | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.forced.on | event.sun.brightness.Event.DeepDark   | socket.presence.christmas.state.on        |
      | On       | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.forced.on | event.holiday.christmas.Event.Day     | socket.presence.christmas.state.on        |
      | On       | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.forced.on | event.holiday.san_silvester.Event.Day | socket.presence.christmas.state.on        |
      | On       | Bright   | Time      | Over          | Over     | socket.presence.christmas.state.forced.on | event.holiday.epiphany.Event.Day      | socket.presence.christmas.state.on        |


  Scenario Outline: The Socket shows its is_on property
    Given A socket.presence.christmas.Appliance appliance
    And   the appliance has an internal event.presence state at <presence>
    And   the appliance has an internal event.sun.brightness state at <sun>
    And   the appliance has an internal event.holiday.christmas state at <christmas>
    And   the appliance has an internal event.holiday.san_silvester state at <san_silvester>
    And   the appliance has an internal event.holiday.epiphany state at <epiphany>
    And   the appliance has an internal appliance.socket.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | presence | sun      | christmas | san_silvester | epiphany | forced | state                                      | response |
      | Off      | DeepDark | Over      | Over          | Over     | Not    | socket.presence.christmas.state.off        | False    |
      | Off      | DeepDark | Over      | Over          | Over     | On     | socket.presence.christmas.state.forced.on  | True     |
      | On       | DeepDark | Over      | Over          | Over     | Not    | socket.presence.christmas.state.on         | True     |
      | On       | DeepDark | Over      | Over          | Over     | Off    | socket.presence.christmas.state.forced.off | False    |

