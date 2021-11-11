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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A Thermostat appliance`
=====================================================================================

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Thermostat react to presence and command events`
---------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A thermostat.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.clima.command state at **\<command\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.thermostat.presence.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "command", "from_state", "event", "to_state"
    :quote: “

    “Off“, “On“, “thermostat.presence.state.keep“, “event.presence.Event.On“, “thermostat.presence.state.on“
    “Off“, “On“, “thermostat.presence.state.keep“, “event.presence.Event.Off“, “thermostat.presence.state.keep“
    “Off“, “On“, “thermostat.presence.state.keep“, “event.clima.command.Event.On“, “thermostat.presence.state.keep“
    “Off“, “On“, “thermostat.presence.state.keep“, “event.clima.command.Event.Off“, “thermostat.presence.state.off“
    “Off“, “On“, “thermostat.presence.state.keep“, “event.clima.command.Event.Keep“, “thermostat.presence.state.keep“
    “Off“, “Off“, “thermostat.presence.state.off“, “event.presence.Event.On“, “thermostat.presence.state.off“
    “Off“, “Off“, “thermostat.presence.state.off“, “event.presence.Event.Off“, “thermostat.presence.state.off“
    “Off“, “Off“, “thermostat.presence.state.off“, “event.clima.command.Event.On“, “thermostat.presence.state.keep“
    “Off“, “Off“, “thermostat.presence.state.off“, “event.clima.command.Event.Off“, “thermostat.presence.state.off“
    “Off“, “Off“, “thermostat.presence.state.off“, “event.clima.command.Event.Keep“, “thermostat.presence.state.keep“
    “Off“, “Keep“, “thermostat.presence.state.keep“, “event.presence.Event.On“, “thermostat.presence.state.keep“
    “Off“, “Keep“, “thermostat.presence.state.keep“, “event.presence.Event.Off“, “thermostat.presence.state.keep“
    “Off“, “Keep“, “thermostat.presence.state.keep“, “event.clima.command.Event.On“, “thermostat.presence.state.keep“
    “Off“, “Keep“, “thermostat.presence.state.keep“, “event.clima.command.Event.Off“, “thermostat.presence.state.off“
    “Off“, “Keep“, “thermostat.presence.state.keep“, “event.clima.command.Event.Keep“, “thermostat.presence.state.keep“
    “On“, “On“, “thermostat.presence.state.on“, “event.presence.Event.On“, “thermostat.presence.state.on“
    “On“, “On“, “thermostat.presence.state.on“, “event.presence.Event.Off“, “thermostat.presence.state.keep“
    “On“, “On“, “thermostat.presence.state.on“, “event.clima.command.Event.On“, “thermostat.presence.state.on“
    “On“, “On“, “thermostat.presence.state.on“, “event.clima.command.Event.Off“, “thermostat.presence.state.off“
    “On“, “On“, “thermostat.presence.state.on“, “event.clima.command.Event.Keep“, “thermostat.presence.state.keep“
    “On“, “Off“, “thermostat.presence.state.off“, “event.presence.Event.On“, “thermostat.presence.state.off“
    “On“, “Off“, “thermostat.presence.state.off“, “event.presence.Event.Off“, “thermostat.presence.state.off“
    “On“, “Off“, “thermostat.presence.state.off“, “event.clima.command.Event.On“, “thermostat.presence.state.on“
    “On“, “Off“, “thermostat.presence.state.off“, “event.clima.command.Event.Off“, “thermostat.presence.state.off“
    “On“, “Off“, “thermostat.presence.state.off“, “event.clima.command.Event.Keep“, “thermostat.presence.state.keep“
    “On“, “Keep“, “thermostat.presence.state.keep“, “event.presence.Event.On“, “thermostat.presence.state.keep“
    “On“, “Keep“, “thermostat.presence.state.keep“, “event.presence.Event.Off“, “thermostat.presence.state.keep“
    “On“, “Keep“, “thermostat.presence.state.keep“, “event.clima.command.Event.On“, “thermostat.presence.state.on“
    “On“, “Keep“, “thermostat.presence.state.keep“, “event.clima.command.Event.Off“, “thermostat.presence.state.off“
    “On“, “Keep“, “thermostat.presence.state.keep“, “event.clima.command.Event.Keep“, “thermostat.presence.state.keep“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Thermostat react to forced on/off/keep events`
-------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A thermostat.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.clima.command state at **\<command\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.thermostat.presence.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "command", "from_state", "event", "to_state"
    :quote: “

    “Off“, “On“, “thermostat.presence.state.keep“, “appliance.thermostat.presence.event.forced.Event.On“, “thermostat.presence.state.forced.on“
    “Off“, “On“, “thermostat.presence.state.keep“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “Off“, “On“, “thermostat.presence.state.keep“, “appliance.thermostat.presence.event.forced.Event.Keep“, “thermostat.presence.state.keep“
    “Off“, “Off“, “thermostat.presence.state.off“, “appliance.thermostat.presence.event.forced.Event.On“, “thermostat.presence.state.forced.on“
    “Off“, “Off“, “thermostat.presence.state.off“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.off“
    “Off“, “Off“, “thermostat.presence.state.off“, “appliance.thermostat.presence.event.forced.Event.Keep“, “thermostat.presence.state.forced.keep“
    “On“, “On“, “thermostat.presence.state.on“, “appliance.thermostat.presence.event.forced.Event.On“, “thermostat.presence.state.on“
    “On“, “On“, “thermostat.presence.state.on“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “On“, “On“, “thermostat.presence.state.on“, “appliance.thermostat.presence.event.forced.Event.Keep“, “thermostat.presence.state.forced.keep“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Thermostat react to forced off/keep events exiting from a forced on state!!!`
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A thermostat.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.clima.command state at **\<command\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.thermostat.presence.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "command", "from_state", "event", "to_state"
    :quote: “

    “On“, “On“, “thermostat.presence.state.on“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “On“, “Off“, “thermostat.presence.state.forced.on“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “On“, “Keep“, “thermostat.presence.state.forced.on“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “On“, “On“, “thermostat.presence.state.on“, “appliance.thermostat.presence.event.forced.Event.Keep“, “thermostat.presence.state.forced.keep“
    “On“, “Off“, “thermostat.presence.state.forced.on“, “appliance.thermostat.presence.event.forced.Event.Keep“, “thermostat.presence.state.forced.keep“
    “On“, “Keep“, “thermostat.presence.state.forced.on“, “appliance.thermostat.presence.event.forced.Event.Keep“, “thermostat.presence.state.forced.keep“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Thermostat react to forced on/off events from a forced keep state`
---------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A thermostat.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.clima.command state at **\<command\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.thermostat.presence.event.forced state at Keep
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "command", "from_state", "event", "to_state"
    :quote: “

    “On“, “On“, “thermostat.presence.state.forced.keep“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “On“, “Off“, “thermostat.presence.state.forced.keep“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “On“, “Keep“, “thermostat.presence.state.keep“, “appliance.thermostat.presence.event.forced.Event.Off“, “thermostat.presence.state.forced.off“
    “On“, “On“, “thermostat.presence.state.forced.keep“, “appliance.thermostat.presence.event.forced.Event.On“, “thermostat.presence.state.forced.on“
    “On“, “Off“, “thermostat.presence.state.forced.keep“, “appliance.thermostat.presence.event.forced.Event.On“, “thermostat.presence.state.forced.on“
    “On“, “Keep“, “thermostat.presence.state.keep“, “appliance.thermostat.presence.event.forced.Event.On“, “thermostat.presence.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Thermostat could be automatically un-forced from a forced on state by clima.command events presence.state events`
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A thermostat.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.clima.command state at **\<command\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.thermostat.presence.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "command", "from_state", "event", "to_state"
    :quote: “

    “Off“, “On“, “thermostat.presence.state.forced.on“, “event.presence.Event.On“, “thermostat.presence.state.on“
    “On“, “Off“, “thermostat.presence.state.forced.on“, “event.clima.command.Event.On“, “thermostat.presence.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Thermostat shows its state`
------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A thermostat.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.clima.command state at **\<command\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.thermostat.presence.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_on
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "command", "forced", "state", "response"
    :quote: “

    “Off“, “Off“, “Not“, “thermostat.presence.state.off“, “False“
    “On“, “On“, “Not“, “thermostat.presence.state.on“, “True“
    “Off“, “On“, “Not“, “thermostat.presence.state.keep“, “True“
    “Off“, “Off“, “On“, “thermostat.presence.state.forced.on“, “True“
    “Off“, “Off“, “Keep“, “thermostat.presence.state.forced.keep“, “True“
    “On“, “On“, “Off“, “thermostat.presence.state.forced.off“, “False“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Thermostat shows its state`
------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A thermostat.presence.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.clima.command state at **\<command\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.thermostat.presence.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_keeping
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "command", "forced", "state", "response"
    :quote: “

    “Off“, “Off“, “Not“, “thermostat.presence.state.off“, “False“
    “On“, “On“, “Not“, “thermostat.presence.state.on“, “False“
    “Off“, “On“, “Not“, “thermostat.presence.state.keep“, “True“
    “Off“, “Off“, “On“, “thermostat.presence.state.forced.on“, “False“
    “Off“, “Off“, “Keep“, “thermostat.presence.state.forced.keep“, “True“
    “On“, “On“, “Off“, “thermostat.presence.state.forced.off“, “False“

