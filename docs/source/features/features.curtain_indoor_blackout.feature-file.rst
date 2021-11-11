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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`An indoor blackout Curtain.`
==========================================================================================

    :gherkin-feature-description:`It should be closed at sunset or when some user is asleep.`

    :gherkin-feature-description:`It should be opened when the user is awake after sunrise.`

    :gherkin-feature-description:`It could be forced opened or forced closed.`

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to sun twilight and user sleepiness events.`
-------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.indoor.blackout.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sleepiness state at **\<sleepiness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sleepiness", "sun_twilight", "from_state", "event", "to_state"
    :quote: “

    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.indoor.blackout.state.opened“
    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.indoor.blackout.state.closed“
    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sleepiness.Event.Awake“, “curtain.indoor.blackout.state.opened“
    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sleepiness.Event.Asleep“, “curtain.indoor.blackout.state.closed“
    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sleepiness.Event.Sleepy“, “curtain.indoor.blackout.state.opened“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.indoor.blackout.state.opened“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.indoor.blackout.state.closed“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Awake“, “curtain.indoor.blackout.state.closed“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Asleep“, “curtain.indoor.blackout.state.closed“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Sleepy“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunrise“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunrise“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunrise“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Awake“, “curtain.indoor.blackout.state.opened“
    “Asleep“, “Sunrise“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Asleep“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunrise“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Sleepy“, “curtain.indoor.blackout.state.opened“
    “Asleep“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Awake“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Asleep“, “curtain.indoor.blackout.state.closed“
    “Asleep“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Sleepy“, “curtain.indoor.blackout.state.closed“
    “Sleepy“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.indoor.blackout.state.opened“
    “Sleepy“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.indoor.blackout.state.closed“
    “Sleepy“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sleepiness.Event.Awake“, “curtain.indoor.blackout.state.opened“
    “Sleepy“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sleepiness.Event.Asleep“, “curtain.indoor.blackout.state.closed“
    “Sleepy“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “event.sleepiness.Event.Sleepy“, “curtain.indoor.blackout.state.opened“
    “Sleepy“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.indoor.blackout.state.opened“
    “Sleepy“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.indoor.blackout.state.closed“
    “Sleepy“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Awake“, “curtain.indoor.blackout.state.closed“
    “Sleepy“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Asleep“, “curtain.indoor.blackout.state.closed“
    “Sleepy“, “Sunset“, “curtain.indoor.blackout.state.closed“, “event.sleepiness.Event.Sleepy“, “curtain.indoor.blackout.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to forced opened/closed events`
------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.indoor.blackout.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sleepiness state at **\<sleepiness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sleepiness", "sun_twilight", "from_state", "event", "to_state"
    :quote: “

    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.indoor.blackout.state.opened“
    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.indoor.blackout.state.forced.closed“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.indoor.blackout.state.forced.opened“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.indoor.blackout.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to forced opened/closed events from a forced opened state`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.indoor.blackout.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sleepiness state at **\<sleepiness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Opened
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sleepiness", "sun_twilight", "from_state", "event", "to_state"
    :quote: “

    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.indoor.blackout.state.opened“
    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.indoor.blackout.state.forced.closed“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.indoor.blackout.state.forced.opened“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.indoor.blackout.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to forced opened/closed events from a forced closed state`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.indoor.blackout.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sleepiness state at **\<sleepiness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Closed
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sleepiness", "sun_twilight", "from_state", "event", "to_state"
    :quote: “

    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.indoor.blackout.state.opened“
    “Awake“, “Sunrise“, “curtain.indoor.blackout.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.indoor.blackout.state.forced.closed“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.indoor.blackout.state.forced.opened“
    “Awake“, “Sunset“, “curtain.indoor.blackout.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.indoor.blackout.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain shows its state`
---------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.indoor.blackout.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.sleepiness state at **\<sleepiness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_opened
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sleepiness", "sun_twilight", "forced", "state", "response"
    :quote: “

    “Awake“, “Sunrise“, “Not“, “curtain.indoor.blackout.state.opened“, “True“
    “Awake“, “Sunset“, “Not“, “curtain.indoor.blackout.state.closed“, “False“
    “Awake“, “Sunrise“, “Closed“, “curtain.indoor.blackout.state.forced.closed“, “False“
    “Awake“, “Sunset“, “Opened“, “curtain.indoor.blackout.state.forced.opened“, “True“

