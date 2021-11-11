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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A Presence Socket appliance`
==========================================================================================

    :gherkin-feature-description:`A \*\*presence\*\* socket which is by default \*\*off\*\*.`

    :gherkin-feature-description:`When \*forced on\* by the user can be turned \*off\* by the system if nobody is in the room.`

    :gherkin-feature-description:`You could know that nobody is in the room when, as an example, the room alarm sensors are presence.`

    :gherkin-feature-description:`Other events could be used for the same purpose.`

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket does not react to alarm presence events from an unforced state`
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "from_state", "event", "to_state"
    :quote: “

    “Off“, “socket.presence.state.off“, “event.presence.Event.Off“, “socket.presence.state.off“
    “Off“, “socket.presence.state.off“, “event.presence.Event.On“, “socket.presence.state.off“
    “On“, “socket.presence.state.off“, “event.presence.Event.Off“, “socket.presence.state.off“
    “On“, “socket.presence.state.off“, “event.presence.Event.On“, “socket.presence.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on events`
------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "from_state", "event", "to_state"
    :quote: “

    “Off“, “socket.presence.state.off“, “appliance.socket.event.forced.Event.Off“, “socket.presence.state.off“
    “Off“, “socket.presence.state.off“, “appliance.socket.event.forced.Event.On“, “socket.presence.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on/off events from a forced on state`
---------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "from_state", "event", "to_state"
    :quote: “

    “Off“, “socket.presence.state.forced.on“, “appliance.socket.event.forced.Event.Off“, “socket.presence.state.off“
    “Off“, “socket.presence.state.forced.on“, “appliance.socket.event.forced.Event.On“, “socket.presence.state.forced.on“
    “On“, “socket.presence.state.forced.on“, “appliance.socket.event.forced.Event.Off“, “socket.presence.state.off“
    “On“, “socket.presence.state.forced.on“, “appliance.socket.event.forced.Event.On“, “socket.presence.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to alarm presence events from a forced on state`
----------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "from_state", "event", "to_state"
    :quote: “

    “Off“, “socket.presence.state.forced.on“, “event.presence.Event.Off“, “socket.presence.state.off“
    “Off“, “socket.presence.state.forced.on“, “event.presence.Event.On“, “socket.presence.state.forced.on“
    “On“, “socket.presence.state.forced.on“, “event.presence.Event.Off“, “socket.presence.state.off“
    “On“, “socket.presence.state.forced.on“, “event.presence.Event.On“, “socket.presence.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket shows its is_on property`
-----------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_on
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "forced", "state", "response"
    :quote: “

    “On“, “Not“, “socket.presence.state.off“, “False“
    “On“, “On“, “socket.presence.state.forced.on“, “True“

