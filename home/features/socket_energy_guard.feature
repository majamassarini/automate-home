Feature: A Energy Guard Socket
  A energy guard socket which is by default always on.

  A energy guard socket enters a detachable state when its detach logic is enabled and power consuming levels are too high.

  A energy guard socket enters an off state when its detach logic is enabled and power consuming levels are too high for too much time.

  When power consuming levels lower down it will be on again.

  You could have more energy guard sockets. A socket can enable the detach logic of another socket when turning itself off.

  This will design a priority level between sockets.

    1) When a socket is turned off then it will enable the detach logic of another socket A -> enables -> B -> enables -> C -> enables -> D.

    2) When a socket is turned on then it will disable its detach logic by itself.

    3) When power consuming levels are high again than will be enabled the detach logic for the lowest priority socket.


  Scenario Outline: The Socket react to power and enable events
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | consumption | duration | from_state                           | event                                        | to_state                             |
      | Off    | No          | Short    | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | Off    | No          | Short    | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | Off    | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | Off    | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | Off    | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.on         |
      | Off    | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | Off    | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | Off    | Low         | Short    | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | Off    | Low         | Short    | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | Off    | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | Off    | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | Off    | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.on         |
      | Off    | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | Off    | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | Off    | High        | Short    | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.detachable |
      | Off    | High        | Short    | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | Off    | High        | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | Off    | High        | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | Off    | High        | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.on         |
      | Off    | High        | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | Off    | High        | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | On     | No          | Short    | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | On     | No          | Short    | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | On     | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | On     | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | On     | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.detachable |
      | On     | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | On     | No          | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | On     | Low         | Short    | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | On     | Low         | Short    | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | On     | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | On     | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | On     | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.detachable |
      | On     | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | On     | Low         | Short    | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | On     | High        | Short    | socket.energy_guard.state.detachable | event.enable.Event.On                        | socket.energy_guard.state.detachable |
      | On     | High        | Short    | socket.energy_guard.state.detachable | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | On     | High        | Short    | socket.energy_guard.state.detachable | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | On     | High        | Short    | socket.energy_guard.state.detachable | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | On     | High        | Short    | socket.energy_guard.state.detachable | event.power.consumption.Event.High           | socket.energy_guard.state.detachable |
      | On     | High        | Short    | socket.energy_guard.state.detachable | event.power.consumption.duration.Event.Short | socket.energy_guard.state.detachable |
      | On     | High        | Short    | socket.energy_guard.state.detachable | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.off        |


      | Off    | No          | Long     | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | Off    | No          | Long     | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | Off    | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | Off    | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | Off    | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.on         |
      | Off    | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | Off    | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | Off    | Low         | Long     | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | Off    | Low         | Long     | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | Off    | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | Off    | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | Off    | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.on         |
      | Off    | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | Off    | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | Off    | High        | Long     | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.detachable |
      | Off    | High        | Long     | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | Off    | High        | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | Off    | High        | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | Off    | High        | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.on         |
      | Off    | High        | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | Off    | High        | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | On     | No          | Long     | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | On     | No          | Long     | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | On     | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | On     | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | On     | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.detachable |
      | On     | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | On     | No          | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | On     | Low         | Long     | socket.energy_guard.state.on         | event.enable.Event.On                        | socket.energy_guard.state.on         |
      | On     | Low         | Long     | socket.energy_guard.state.on         | event.enable.Event.Off                       | socket.energy_guard.state.on         |
      | On     | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | On     | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | On     | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.Event.High           | socket.energy_guard.state.detachable |
      | On     | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Short | socket.energy_guard.state.on         |
      | On     | Low         | Long     | socket.energy_guard.state.on         | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.on         |

      | On     | High        | Long     | socket.energy_guard.state.off        | event.enable.Event.On                        | socket.energy_guard.state.off        |
      | On     | High        | Long     | socket.energy_guard.state.off        | event.enable.Event.Off                       | socket.energy_guard.state.off        |
      | On     | High        | Long     | socket.energy_guard.state.off        | event.power.consumption.Event.No             | socket.energy_guard.state.on         |
      | On     | High        | Long     | socket.energy_guard.state.off        | event.power.consumption.Event.Low            | socket.energy_guard.state.on         |
      | On     | High        | Long     | socket.energy_guard.state.off        | event.power.consumption.Event.High           | socket.energy_guard.state.off        |
      | On     | High        | Long     | socket.energy_guard.state.off        | event.power.consumption.duration.Event.Short | socket.energy_guard.state.off        |
      | On     | High        | Long     | socket.energy_guard.state.off        | event.power.consumption.duration.Event.Long  | socket.energy_guard.state.off        |

  Scenario Outline: The Socket react to forced on/off events
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at Not
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | consumption | duration | from_state                           | event                                   | to_state                             |
      | Off    | No          | Short    | socket.energy_guard.state.on         | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.forced.off |
      | Off    | No          | Short    | socket.energy_guard.state.on         | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.on         |

      | On     | High        | Short    | socket.energy_guard.state.detachable | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.forced.off |
      | On     | High        | Short    | socket.energy_guard.state.detachable | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.forced.on  |

      | On     | High        | Long     | socket.energy_guard.state.off        | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.off        |
      | On     | High        | Long     | socket.energy_guard.state.off        | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.forced.on  |


  Scenario Outline: The Socket react to forced on/off events from a forced on state
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at On
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | consumption | duration | from_state                          | event                                   | to_state                             |
      | Off    | No          | Short    | socket.energy_guard.state.on        | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.forced.off |
      | Off    | No          | Short    | socket.energy_guard.state.on        | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.on         |

      | On     | High        | Short    | socket.energy_guard.state.forced.on | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.detachable |
      | On     | High        | Short    | socket.energy_guard.state.forced.on | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.forced.on  |

      | On     | High        | Long     | socket.energy_guard.state.forced.on | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.off        |
      | On     | High        | Long     | socket.energy_guard.state.forced.on | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.forced.on  |


  Scenario Outline: The Socket react to forced on/off events from a forced off state
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at Off
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | consumption | duration | from_state                           | event                                   | to_state                             |
      | Off    | No          | Short    | socket.energy_guard.state.forced.off | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.forced.off |
      | Off    | No          | Short    | socket.energy_guard.state.forced.off | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.on         |

      | On     | High        | Short    | socket.energy_guard.state.forced.off | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.forced.off |
      | On     | High        | Short    | socket.energy_guard.state.forced.off | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.detachable |

      | On     | High        | Long     | socket.energy_guard.state.off        | appliance.socket.event.forced.Event.Off | socket.energy_guard.state.off        |
      | On     | High        | Long     | socket.energy_guard.state.off        | appliance.socket.event.forced.Event.On  | socket.energy_guard.state.forced.on  |


  Scenario Outline: The Socket could be automatically un-forced from a forced off state by enable events and not by power.consumption events
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at Off

    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | consumption | duration | from_state                           | event                                       | to_state                             |
      | Off    | High        | Long     | socket.energy_guard.state.forced.off | event.enable.Event.On                       | socket.energy_guard.state.off        |
      | On     | Low         | Long     | socket.energy_guard.state.forced.off | event.power.consumption.Event.High          | socket.energy_guard.state.forced.off |
      | On     | High        | Short    | socket.energy_guard.state.forced.off | event.power.consumption.duration.Event.Long | socket.energy_guard.state.forced.off |


  Scenario Outline: The Socket could be automatically un-forced from a forced on state by enable events and not by power.consumption events
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at On

    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | enable | consumption | duration | from_state                          | event                                       | to_state                            |
      | On     | High        | Long     | socket.energy_guard.state.forced.on | event.enable.Event.Off                      | socket.energy_guard.state.on        |
      | On     | High        | Long     | socket.energy_guard.state.forced.on | event.power.consumption.Event.High          | socket.energy_guard.state.forced.on |
      | On     | High        | Long     | socket.energy_guard.state.forced.on | event.power.consumption.duration.Event.Long | socket.energy_guard.state.forced.on |


  Scenario Outline: The Socket shows its is_on property
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | enable | consumption | duration | forced | state                                | response |
      | Off    | No          | Short    | Not    | socket.energy_guard.state.on         | True     |
      | Off    | No          | Short    | Off    | socket.energy_guard.state.forced.off | False    |
      | On     | High        | Short    | Not    | socket.energy_guard.state.detachable | True     |
      | On     | High        | Long     | Not    | socket.energy_guard.state.off        | False    |
      | On     | High        | Long     | On     | socket.energy_guard.state.forced.on  | True     |

  Scenario Outline: The Socket shows its is_detachable property
    Given A socket.energy_guard.Appliance appliance
    And   the appliance has an internal event.enable state at <enable>
    And   the appliance has an internal event.power.consumption state at <consumption>
    And   the appliance has an internal event.power.consumption.duration state at <duration>
    And   the appliance has an internal appliance.socket.event.forced state at <forced>
    And   it's calculated state is <state>
    When  it's asked for its state property is_detachable
    Then  the response is <response>

    Examples:
      | enable | consumption | duration | forced | state                                | response |
      | Off    | No          | Short    | Not    | socket.energy_guard.state.on         | False    |
      | Off    | No          | Short    | Off    | socket.energy_guard.state.forced.off | False    |
      | On     | High        | Short    | Not    | socket.energy_guard.state.detachable | True     |
      | On     | High        | Long     | Not    | socket.energy_guard.state.off        | False    |
      | On     | High        | Long     | On     | socket.energy_guard.state.forced.on  | False    |
