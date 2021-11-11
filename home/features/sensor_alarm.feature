Feature: A sensor alarm


  Scenario Outline: The Light react to courtesy and sun brightness events
    Given A sensor.alarm.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.alarm.triggered state at <triggered>
    And   it's calculated state is <from_state>
    When  it receives a new event <event>
    Then  the appliance new state is <to_state>

    Examples:
      | armed | triggered | from_state                   | event                           | to_state                     |
      | Off   | Off       | sensor.alarm.state.unarmed   | event.alarm.armed.Event.On      | sensor.alarm.state.armed     |
      | Off   | Off       | sensor.alarm.state.unarmed   | event.alarm.armed.Event.Off     | sensor.alarm.state.unarmed   |
      | Off   | Off       | sensor.alarm.state.unarmed   | event.alarm.triggered.Event.On  | sensor.alarm.state.unarmed   |
      | Off   | Off       | sensor.alarm.state.unarmed   | event.alarm.triggered.Event.Off | sensor.alarm.state.unarmed   |

      | Off   | On        | sensor.alarm.state.unarmed   | event.alarm.armed.Event.On      | sensor.alarm.state.triggered |
      | Off   | On        | sensor.alarm.state.unarmed   | event.alarm.armed.Event.Off     | sensor.alarm.state.unarmed   |
      | Off   | On        | sensor.alarm.state.unarmed   | event.alarm.triggered.Event.On  | sensor.alarm.state.unarmed   |
      | Off   | On        | sensor.alarm.state.unarmed   | event.alarm.triggered.Event.Off | sensor.alarm.state.unarmed   |

      | On    | Off       | sensor.alarm.state.armed     | event.alarm.armed.Event.On      | sensor.alarm.state.armed     |
      | On    | Off       | sensor.alarm.state.armed     | event.alarm.armed.Event.Off     | sensor.alarm.state.unarmed   |
      | On    | Off       | sensor.alarm.state.armed     | event.alarm.triggered.Event.On  | sensor.alarm.state.triggered |
      | On    | Off       | sensor.alarm.state.armed     | event.alarm.triggered.Event.Off | sensor.alarm.state.armed     |

      | On    | On        | sensor.alarm.state.triggered | event.alarm.armed.Event.On      | sensor.alarm.state.triggered |
      | On    | On        | sensor.alarm.state.triggered | event.alarm.armed.Event.Off     | sensor.alarm.state.unarmed   |
      | On    | On        | sensor.alarm.state.triggered | event.alarm.triggered.Event.On  | sensor.alarm.state.triggered |
      | On    | On        | sensor.alarm.state.triggered | event.alarm.triggered.Event.Off | sensor.alarm.state.armed     |


  Scenario Outline: The alarm sensor shows its state property is_on
    Given A sensor.alarm.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.alarm.triggered state at <triggered>
    And   it's calculated state is <state>
    When  it's asked for its state property is_on
    Then  the response is <response>

    Examples:
      | armed | triggered | state                         | response |
      | Off   | Off       | sensor.alarm.state.unarmed    | False    |
      | On    | Off       | sensor.alarm.state.armed      | True     |
      | Off   | On        | sensor.alarm.state.unarmed    | False    |
      | On    | On        | sensor.alarm.state.triggered  | True     |


  Scenario Outline: The alarm sensor shows its state property is_triggered
    Given A sensor.alarm.Appliance appliance
    And   the appliance has an internal event.alarm.armed state at <armed>
    And   the appliance has an internal event.alarm.triggered state at <triggered>
    And   it's calculated state is <state>
    When  it's asked for its state property is_triggered
    Then  the response is <response>

    Examples:
      | armed | triggered | state                         | response |
      | Off   | Off       | sensor.alarm.state.unarmed    | False    |
      | On    | Off       | sensor.alarm.state.armed      | False    |
      | Off   | On        | sensor.alarm.state.unarmed    | False    |
      | On    | On        | sensor.alarm.state.triggered  | True     |
