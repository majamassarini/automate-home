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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A light appliance`
================================================================================

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to courtesy and sun brightness events`
-----------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.courtesy state at **\<courtesy\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "courtesy", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “Off“, “Bright“, “light.state.off“, “event.courtesy.Event.On“, “light.state.off“
    “Off“, “Bright“, “light.state.off“, “event.courtesy.Event.Off“, “light.state.off“
    “Off“, “Bright“, “light.state.off“, “event.sun.brightness.Event.Bright“, “light.state.off“
    “Off“, “Bright“, “light.state.off“, “event.sun.brightness.Event.Dark“, “light.state.off“
    “Off“, “Bright“, “light.state.off“, “event.sun.brightness.Event.DeepDark“, “light.state.off“
    “Off“, “Dark“, “light.state.off“, “event.courtesy.Event.On“, “light.state.off“
    “Off“, “Dark“, “light.state.off“, “event.courtesy.Event.Off“, “light.state.off“
    “Off“, “Dark“, “light.state.off“, “event.sun.brightness.Event.Bright“, “light.state.off“
    “Off“, “Dark“, “light.state.off“, “event.sun.brightness.Event.Dark“, “light.state.off“
    “Off“, “Dark“, “light.state.off“, “event.sun.brightness.Event.DeepDark“, “light.state.off“
    “Off“, “DeepDark“, “light.state.off“, “event.courtesy.Event.On“, “light.state.on“
    “Off“, “DeepDark“, “light.state.off“, “event.courtesy.Event.Off“, “light.state.off“
    “Off“, “DeepDark“, “light.state.off“, “event.sun.brightness.Event.Bright“, “light.state.off“
    “Off“, “DeepDark“, “light.state.off“, “event.sun.brightness.Event.Dark“, “light.state.off“
    “Off“, “DeepDark“, “light.state.off“, “event.sun.brightness.Event.DeepDark“, “light.state.off“
    “On“, “Bright“, “light.state.off“, “event.courtesy.Event.On“, “light.state.off“
    “On“, “Bright“, “light.state.off“, “event.courtesy.Event.Off“, “light.state.off“
    “On“, “Bright“, “light.state.off“, “event.sun.brightness.Event.Bright“, “light.state.off“
    “On“, “Bright“, “light.state.off“, “event.sun.brightness.Event.Dark“, “light.state.off“
    “On“, “Bright“, “light.state.off“, “event.sun.brightness.Event.DeepDark“, “light.state.on“
    “On“, “Dark“, “light.state.off“, “event.courtesy.Event.On“, “light.state.off“
    “On“, “Dark“, “light.state.off“, “event.courtesy.Event.Off“, “light.state.off“
    “On“, “Dark“, “light.state.off“, “event.sun.brightness.Event.Bright“, “light.state.off“
    “On“, “Dark“, “light.state.off“, “event.sun.brightness.Event.Dark“, “light.state.off“
    “On“, “Dark“, “light.state.off“, “event.sun.brightness.Event.DeepDark“, “light.state.on“
    “On“, “DeepDark“, “light.state.on“, “event.courtesy.Event.On“, “light.state.on“
    “On“, “DeepDark“, “light.state.on“, “event.courtesy.Event.Off“, “light.state.off“
    “On“, “DeepDark“, “light.state.on“, “event.sun.brightness.Event.Bright“, “light.state.off“
    “On“, “DeepDark“, “light.state.on“, “event.sun.brightness.Event.Dark“, “light.state.on“
    “On“, “DeepDark“, “light.state.on“, “event.sun.brightness.Event.DeepDark“, “light.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to forced on/off events`
---------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.courtesy state at **\<courtesy\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "courtesy", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “Off“, “Bright“, “light.state.off“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “Off“, “Bright“, “light.state.off“, “appliance.light.event.forced.Event.On“, “light.state.forced.on“
    “Off“, “Dark“, “light.state.off“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “Off“, “Dark“, “light.state.off“, “appliance.light.event.forced.Event.On“, “light.state.forced.on“
    “Off“, “DeepDark“, “light.state.off“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “Off“, “DeepDark“, “light.state.off“, “appliance.light.event.forced.Event.On“, “light.state.forced.on“
    “On“, “Bright“, “light.state.off“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “On“, “Bright“, “light.state.off“, “appliance.light.event.forced.Event.On“, “light.state.forced.on“
    “On“, “Dark“, “light.state.off“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “On“, “Dark“, “light.state.off“, “appliance.light.event.forced.Event.On“, “light.state.forced.on“
    “On“, “DeepDark“, “light.state.on“, “appliance.light.event.forced.Event.Off“, “light.state.forced.off“
    “On“, “DeepDark“, “light.state.on“, “appliance.light.event.forced.Event.On“, “light.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to forced on/off events from a forced on state`
--------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.courtesy state at **\<courtesy\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "courtesy", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “Off“, “Bright“, “light.state.forced.on“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “Off“, “Dark“, “light.state.forced.on“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “Off“, “DeepDark“, “light.state.forced.on“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “On“, “Bright“, “light.state.forced.on“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “On“, “Dark“, “light.state.forced.on“, “appliance.light.event.forced.Event.Off“, “light.state.off“
    “On“, “DeepDark“, “light.state.on“, “appliance.light.event.forced.Event.Off“, “light.state.forced.off“
    “Off“, “Bright“, “light.state.forced.on“, “appliance.light.event.forced.Event.Not“, “light.state.off“
    “Off“, “Dark“, “light.state.forced.on“, “appliance.light.event.forced.Event.Not“, “light.state.off“
    “Off“, “DeepDark“, “light.state.forced.on“, “appliance.light.event.forced.Event.Not“, “light.state.off“
    “On“, “Bright“, “light.state.forced.on“, “appliance.light.event.forced.Event.Not“, “light.state.off“
    “On“, “Dark“, “light.state.forced.on“, “appliance.light.event.forced.Event.Not“, “light.state.off“
    “On“, “DeepDark“, “light.state.on“, “appliance.light.event.forced.Event.Not“, “light.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light could be automatically un-forced from a forced on state by sun.brightness events and not by courtesy events`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.courtesy state at **\<courtesy\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "courtesy", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “Off“, “Dark“, “light.state.forced.on“, “event.courtesy.Event.On“, “light.state.forced.on“
    “Off“, “DeepDark“, “light.state.forced.on“, “event.courtesy.Event.On“, “light.state.forced.on“
    “On“, “Bright“, “light.state.forced.on“, “event.sun.brightness.Event.Dark“, “light.state.forced.on“
    “On“, “Dark“, “light.state.forced.on“, “event.sun.brightness.Event.DeepDark“, “light.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light could be automatically un-forced from a forced off state by sun.brightness events and not by courtesy events`
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.courtesy state at **\<courtesy\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.forced state at Off
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "courtesy", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “DeepDark“, “light.state.forced.off“, “event.courtesy.Event.Off“, “light.state.forced.off“
    “On“, “DeepDark“, “light.state.forced.off“, “event.courtesy.Event.Off“, “light.state.forced.off“
    “On“, “DeepDark“, “light.state.forced.off“, “event.sun.brightness.Event.Dark“, “light.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state`
-------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.courtesy state at **\<courtesy\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_on
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "courtesy", "sun_brightness", "forced", "state", "response"
    :quote: “

    “Off“, “Bright“, “Not“, “light.state.off“, “False“
    “On“, “DeepDark“, “Not“, “light.state.on“, “True“
    “Off“, “Bright“, “On“, “light.state.forced.on“, “True“
    “On“, “DeepDark“, “Off“, “light.state.forced.off“, “False“

