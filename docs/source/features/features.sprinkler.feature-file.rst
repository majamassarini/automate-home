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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A sprinkler appliance`
====================================================================================

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Sprinkler react to not forced events from a not forced state`
----------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A sprinkler.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.rain state at **\<is_raining\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.rain.forecast state at **\<will_rain\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.rain.in_the_past state at **\<has_rained\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.phase state at **\<sun_phase\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.sprinkler.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "sun_phase", "is_raining", "will_rain", "has_rained", "from_state", "event", "to_state"
    :quote: “

    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.enable.Event.On“, “sprinkler.state.on“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.sun.phase.Event.Sunset“, “sprinkler.state.on“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.rain.Event.No“, “sprinkler.state.on“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.rain.forecast.Event.On“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.rain.forecast.Event.Off“, “sprinkler.state.on“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.rain.in_the_past.Event.On“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.on“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.on“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.enable.Event.On“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.sun.phase.Event.Sunset“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.rain.Event.No“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.rain.forecast.Event.Off“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.rain.in_the_past.Event.On“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.partially_on“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.on“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.enable.Event.On“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.sun.phase.Event.Sunset“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.rain.Event.No“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.rain.forecast.Event.On“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.rain.forecast.Event.Off“, “sprinkler.state.on“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.partially_on“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.on“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.partially_on“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.on“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.partially_on“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.partially_on“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.on“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.partially_on“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.partially_on“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunset“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “No“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “Off“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “Off“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.enable.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.Event.No“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “Off“, “Sunrise“, “Gentle“, “On“, “On“, “sprinkler.state.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Sprinkler react to forced events from a not forced state`
------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A sprinkler.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.phase state at Sunset
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.rain.forecast state at **\<will_rain\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.sprinkler.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "will_rain", "from_state", "event", "to_state"
    :quote: “

    “On“, “Off“, “sprinkler.state.on“, “appliance.sprinkler.event.forced.Event.On“, “sprinkler.state.on“
    “On“, “Off“, “sprinkler.state.on“, “appliance.sprinkler.event.forced.Event.PartiallyOn“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.on“, “appliance.sprinkler.event.forced.Event.Off“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.partially_on“, “appliance.sprinkler.event.forced.Event.On“, “sprinkler.state.partially_on“
    “On“, “On“, “sprinkler.state.partially_on“, “appliance.sprinkler.event.forced.Event.PartiallyOn“, “sprinkler.state.partially_on“
    “On“, “On“, “sprinkler.state.partially_on“, “appliance.sprinkler.event.forced.Event.Off“, “sprinkler.state.forced.off“
    “Off“, “Off“, “sprinkler.state.off“, “appliance.sprinkler.event.forced.Event.On“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.off“, “appliance.sprinkler.event.forced.Event.PartiallyOn“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.off“, “appliance.sprinkler.event.forced.Event.Off“, “sprinkler.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Sprinkler react to not forced events from a On forced state, and will be reset by a`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    :gherkin-scenario-description:`sun phase sunrise event`

| :gherkin-step-keyword:`Given` A sprinkler.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.phase state at Sunset
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.rain.forecast state at **\<will_rain\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.sprinkler.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "will_rain", "from_state", "event", "to_state"
    :quote: “

    “On“, “On“, “sprinkler.state.partially_on“, “event.enable.Event.On“, “sprinkler.state.partially_on“
    “On“, “On“, “sprinkler.state.partially_on“, “event.enable.Event.Off“, “sprinkler.state.off“
    “On“, “On“, “sprinkler.state.partially_on“, “event.sun.phase.Event.Sunset“, “sprinkler.state.partially_on“
    “On“, “On“, “sprinkler.state.partially_on“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “On“, “sprinkler.state.partially_on“, “event.rain.Event.Gentle“, “sprinkler.state.off“
    “On“, “On“, “sprinkler.state.partially_on“, “event.rain.Event.No“, “sprinkler.state.partially_on“
    “On“, “On“, “sprinkler.state.partially_on“, “event.rain.forecast.Event.On“, “sprinkler.state.partially_on“
    “On“, “On“, “sprinkler.state.partially_on“, “event.rain.forecast.Event.Off“, “sprinkler.state.on“
    “On“, “On“, “sprinkler.state.partially_on“, “event.rain.in_the_past.Event.On“, “sprinkler.state.off“
    “On“, “On“, “sprinkler.state.partially_on“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.enable.Event.On“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.enable.Event.Off“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.sun.phase.Event.Sunset“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.rain.Event.Gentle“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.rain.Event.No“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.rain.forecast.Event.On“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.rain.forecast.Event.Off“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.rain.in_the_past.Event.On“, “sprinkler.state.forced.on“
    “Off“, “Off“, “sprinkler.state.forced.on“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Sprinkler react to not forced events from a PartiallyOn forced state, and will be reset by a`
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    :gherkin-scenario-description:`sun phase sunrise event`

| :gherkin-step-keyword:`Given` A sprinkler.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.phase state at Sunset
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.rain.forecast state at **\<will_rain\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.sprinkler.event.forced state at PartiallyOn
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "will_rain", "from_state", "event", "to_state"
    :quote: “

    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.enable.Event.On“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.enable.Event.Off“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.sun.phase.Event.Sunset“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.Event.Gentle“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.Event.No“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.forecast.Event.On“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.forecast.Event.Off“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.in_the_past.Event.On“, “sprinkler.state.forced.partially_on“
    “On“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.enable.Event.On“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.enable.Event.Off“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.sun.phase.Event.Sunset“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.Event.Gentle“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.Event.No“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.forecast.Event.On“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.forecast.Event.Off“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.in_the_past.Event.On“, “sprinkler.state.forced.partially_on“
    “Off“, “Off“, “sprinkler.state.forced.partially_on“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.forced.partially_on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Sprinkler react to not forced events from a Off forced state, and will be reset by a`
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    :gherkin-scenario-description:`sun phase sunrise event`

| :gherkin-step-keyword:`Given` A sprinkler.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.phase state at Sunset
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.rain.forecast state at **\<will_rain\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.sprinkler.event.forced state at Off
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "will_rain", "from_state", "event", "to_state"
    :quote: “

    “On“, “Off“, “sprinkler.state.forced.off“, “event.enable.Event.On“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.enable.Event.Off“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.rain.Event.Gentle“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.rain.Event.No“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.rain.forecast.Event.On“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.forced.off“
    “On“, “Off“, “sprinkler.state.forced.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.enable.Event.On“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.enable.Event.Off“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.sun.phase.Event.Sunset“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.sun.phase.Event.Sunrise“, “sprinkler.state.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.rain.Event.Gentle“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.rain.Event.No“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.rain.forecast.Event.On“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.rain.forecast.Event.Off“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.rain.in_the_past.Event.On“, “sprinkler.state.forced.off“
    “On“, “On“, “sprinkler.state.forced.off“, “event.rain.in_the_past.Event.Off“, “sprinkler.state.forced.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Sprinkler shows its property\: duration`
-------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A sprinkler.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.phase state at Sunset
| :gherkin-step-keyword:`And` the appliance has an internal event.enable state at **\<enable\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.rain.forecast state at **\<will_rain\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.sprinkler.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property duration
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "enable", "forced", "will_rain", "state", "response"
    :quote: “

    “Off“, “Not“, “Off“, “sprinkler.state.off“, “1200“
    “On“, “Not“, “Off“, “sprinkler.state.on“, “1200“
    “On“, “Not“, “On“, “sprinkler.state.partially_on“, “350“
    “Off“, “On“, “Off“, “sprinkler.state.forced.on“, “1200“
    “Off“, “PartiallyOn“, “Off“, “sprinkler.state.forced.partially_on“, “350“
    “On“, “Off“, “Off“, “sprinkler.state.forced.off“, “1200“

