.. role:: gherkin-step-keyword
.. role:: gherkin-step-content
.. role:: gherkin-feature-description
.. role:: gherkin-scenario-description
.. role:: gherkin-feature-keyword
.. role:: gherkin-feature-content
.. role:: gherkin-background-keyword
.. role:: gherkin-background-content
.. role:: gherkin-scenario-keyword
.. role:: gherkin-scenario-content
.. role:: gherkin-scenario-outline-keyword
.. role:: gherkin-scenario-outline-content
.. role:: gherkin-examples-keyword
.. role:: gherkin-examples-content
.. role:: gherkin-tag-keyword
.. role:: gherkin-tag-content

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A sensor alarm`
=============================================================================

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to courtesy and sun brightness events`
-----------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A sensor.alarm.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.alarm.armed state at **\<armed\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.alarm.triggered state at **\<triggered\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "armed", "triggered", "from_state", "event", "to_state"
    :quote: “

    “Off“, “Off“, “sensor.alarm.state.unarmed“, “event.alarm.armed.Event.On“, “sensor.alarm.state.armed“
    “Off“, “Off“, “sensor.alarm.state.unarmed“, “event.alarm.armed.Event.Off“, “sensor.alarm.state.unarmed“
    “Off“, “Off“, “sensor.alarm.state.unarmed“, “event.alarm.triggered.Event.On“, “sensor.alarm.state.unarmed“
    “Off“, “Off“, “sensor.alarm.state.unarmed“, “event.alarm.triggered.Event.Off“, “sensor.alarm.state.unarmed“
    “Off“, “On“, “sensor.alarm.state.unarmed“, “event.alarm.armed.Event.On“, “sensor.alarm.state.triggered“
    “Off“, “On“, “sensor.alarm.state.unarmed“, “event.alarm.armed.Event.Off“, “sensor.alarm.state.unarmed“
    “Off“, “On“, “sensor.alarm.state.unarmed“, “event.alarm.triggered.Event.On“, “sensor.alarm.state.unarmed“
    “Off“, “On“, “sensor.alarm.state.unarmed“, “event.alarm.triggered.Event.Off“, “sensor.alarm.state.unarmed“
    “On“, “Off“, “sensor.alarm.state.armed“, “event.alarm.armed.Event.On“, “sensor.alarm.state.armed“
    “On“, “Off“, “sensor.alarm.state.armed“, “event.alarm.armed.Event.Off“, “sensor.alarm.state.unarmed“
    “On“, “Off“, “sensor.alarm.state.armed“, “event.alarm.triggered.Event.On“, “sensor.alarm.state.triggered“
    “On“, “Off“, “sensor.alarm.state.armed“, “event.alarm.triggered.Event.Off“, “sensor.alarm.state.armed“
    “On“, “On“, “sensor.alarm.state.triggered“, “event.alarm.armed.Event.On“, “sensor.alarm.state.triggered“
    “On“, “On“, “sensor.alarm.state.triggered“, “event.alarm.armed.Event.Off“, “sensor.alarm.state.unarmed“
    “On“, “On“, “sensor.alarm.state.triggered“, “event.alarm.triggered.Event.On“, “sensor.alarm.state.triggered“
    “On“, “On“, “sensor.alarm.state.triggered“, “event.alarm.triggered.Event.Off“, “sensor.alarm.state.armed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The alarm sensor shows its state property is_on`
-----------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A sensor.alarm.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.alarm.armed state at **\<armed\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.alarm.triggered state at **\<triggered\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_on
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "armed", "triggered", "state", "response"
    :quote: “

    “Off“, “Off“, “sensor.alarm.state.unarmed“, “False“
    “On“, “Off“, “sensor.alarm.state.armed“, “True“
    “Off“, “On“, “sensor.alarm.state.unarmed“, “False“
    “On“, “On“, “sensor.alarm.state.triggered“, “True“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The alarm sensor shows its state property is_triggered`
------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A sensor.alarm.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.alarm.armed state at **\<armed\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.alarm.triggered state at **\<triggered\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_triggered
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "armed", "triggered", "state", "response"
    :quote: “

    “Off“, “Off“, “sensor.alarm.state.unarmed“, “False“
    “On“, “Off“, “sensor.alarm.state.armed“, “False“
    “Off“, “On“, “sensor.alarm.state.unarmed“, “False“
    “On“, “On“, “sensor.alarm.state.triggered“, “True“

