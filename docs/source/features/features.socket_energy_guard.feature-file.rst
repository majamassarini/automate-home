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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A Energy Guard Socket`
====================================================================================

    :gherkin-feature-description:`A energy guard socket which is by default always on.`

    :gherkin-feature-description:`A energy guard socket enters a detachable state when its detach logic is enabled and power consuming levels are too high.`

    :gherkin-feature-description:`A energy guard socket enters an off state when its detach logic is enabled and power consuming levels are too high for too much time.`

    :gherkin-feature-description:`When power consuming levels lower down it will be on again.`

    :gherkin-feature-description:`You could have more energy guard sockets. A socket can enable the detach logic of another socket when turning itself off.`

    :gherkin-feature-description:`This will design a priority level between sockets.`

    :gherkin-feature-description:`1) When a socket is turned off then it will enable the detach logic of another socket A -\> enables -\> B -\> enables -\> C -\> enables -\> D.`

    :gherkin-feature-description:`2) When a socket is turned on then it will disable its detach logic by itself.`

    :gherkin-feature-description:`3) When power consuming levels are high again than will be enabled the detach logic for the lowest priority socket.`

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to power and enable events`
-------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "from_state", "event", "to_state"
    :quote: “

    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.on“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “Off“, “High“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.detachable“
    “Off“, “High“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “Off“, “High“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “Off“, “High“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “Off“, “High“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.on“
    “Off“, “High“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “Off“, “High“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “On“, “No“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “On“, “No“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “On“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “On“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “On“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.detachable“
    “On“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “On“, “No“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “On“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “On“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “On“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “On“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “On“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.detachable“
    “On“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “On“, “Low“, “Short“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “event.enable.Event.On“, “socket.energy_guard.state.detachable“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “event.power.consumption.Event.High“, “socket.energy_guard.state.detachable“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.detachable“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.off“
    “Off“, “No“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “Off“, “No“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “Off“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “Off“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “Off“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.on“
    “Off“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “Off“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “Off“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “Off“, “High“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.detachable“
    “Off“, “High“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “Off“, “High“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “Off“, “High“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “Off“, “High“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.on“
    “Off“, “High“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “Off“, “High“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “On“, “No“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “On“, “No“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “On“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “On“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “On“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.detachable“
    “On“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “On“, “No“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “On“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.On“, “socket.energy_guard.state.on“
    “On“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “On“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “On“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “On“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.detachable“
    “On“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.on“
    “On“, “Low“, “Long“, “socket.energy_guard.state.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.on“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “event.enable.Event.On“, “socket.energy_guard.state.off“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “event.enable.Event.Off“, “socket.energy_guard.state.off“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “event.power.consumption.Event.No“, “socket.energy_guard.state.on“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “event.power.consumption.Event.Low“, “socket.energy_guard.state.on“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “event.power.consumption.Event.High“, “socket.energy_guard.state.off“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “event.power.consumption.duration.Event.Short“, “socket.energy_guard.state.off“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on/off events`
----------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "from_state", "event", "to_state"
    :quote: “

    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.forced.off“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.on“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.forced.off“
    “On“, “High“, “Short“, “socket.energy_guard.state.detachable“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.forced.on“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.off“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on/off events from a forced on state`
---------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "from_state", "event", "to_state"
    :quote: “

    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.forced.off“
    “Off“, “No“, “Short“, “socket.energy_guard.state.on“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.on“
    “On“, “High“, “Short“, “socket.energy_guard.state.forced.on“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.detachable“
    “On“, “High“, “Short“, “socket.energy_guard.state.forced.on“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.forced.on“
    “On“, “High“, “Long“, “socket.energy_guard.state.forced.on“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.off“
    “On“, “High“, “Long“, “socket.energy_guard.state.forced.on“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on/off events from a forced off state`
----------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Off
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "from_state", "event", "to_state"
    :quote: “

    “Off“, “No“, “Short“, “socket.energy_guard.state.forced.off“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.forced.off“
    “Off“, “No“, “Short“, “socket.energy_guard.state.forced.off“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.on“
    “On“, “High“, “Short“, “socket.energy_guard.state.forced.off“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.forced.off“
    “On“, “High“, “Short“, “socket.energy_guard.state.forced.off“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.detachable“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “appliance.socket.event.forced.Event.Off“, “socket.energy_guard.state.off“
    “On“, “High“, “Long“, “socket.energy_guard.state.off“, “appliance.socket.event.forced.Event.On“, “socket.energy_guard.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket could be automatically un-forced from a forced off state by enable events and not by power.consumption events`
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Off
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "from_state", "event", "to_state"
    :quote: “

    “Off“, “High“, “Long“, “socket.energy_guard.state.forced.off“, “event.enable.Event.On“, “socket.energy_guard.state.off“
    “On“, “Low“, “Long“, “socket.energy_guard.state.forced.off“, “event.power.consumption.Event.High“, “socket.energy_guard.state.forced.off“
    “On“, “High“, “Short“, “socket.energy_guard.state.forced.off“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.forced.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket could be automatically un-forced from a forced on state by enable events and not by power.consumption events`
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "from_state", "event", "to_state"
    :quote: “

    “On“, “High“, “Long“, “socket.energy_guard.state.forced.on“, “event.enable.Event.Off“, “socket.energy_guard.state.on“
    “On“, “High“, “Long“, “socket.energy_guard.state.forced.on“, “event.power.consumption.Event.High“, “socket.energy_guard.state.forced.on“
    “On“, “High“, “Long“, “socket.energy_guard.state.forced.on“, “event.power.consumption.duration.Event.Long“, “socket.energy_guard.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket shows its is_on property`
-----------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_on
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "forced", "state", "response"
    :quote: “

    “Off“, “No“, “Short“, “Not“, “socket.energy_guard.state.on“, “True“
    “Off“, “No“, “Short“, “Off“, “socket.energy_guard.state.forced.off“, “False“
    “On“, “High“, “Short“, “Not“, “socket.energy_guard.state.detachable“, “True“
    “On“, “High“, “Long“, “Not“, “socket.energy_guard.state.off“, “False“
    “On“, “High“, “Long“, “On“, “socket.energy_guard.state.forced.on“, “True“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket shows its is_detachable property`
-------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.energy_guard.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption state at **\<consumption\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.power.consumption.duration state at **\<duration\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_detachable
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "consumption", "duration", "forced", "state", "response"
    :quote: “

    “Off“, “No“, “Short“, “Not“, “socket.energy_guard.state.on“, “False“
    “Off“, “No“, “Short“, “Off“, “socket.energy_guard.state.forced.off“, “False“
    “On“, “High“, “Short“, “Not“, “socket.energy_guard.state.detachable“, “True“
    “On“, “High“, “Long“, “Not“, “socket.energy_guard.state.off“, “False“
    “On“, “High“, “Long“, “On“, “socket.energy_guard.state.forced.on“, “False“

