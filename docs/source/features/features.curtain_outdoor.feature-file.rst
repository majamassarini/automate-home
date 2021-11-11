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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`An outdoor Curtain.`
==================================================================================

    :gherkin-feature-description:`It should be closed when the sun (with an high brightness) hits the curtain's window or at sunset.`

    :gherkin-feature-description:`It should be opened at sunrise or when the wind is strong.`

    :gherkin-feature-description:`It could be forced opened or forced closed.`

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to wind, sun brightness, sun twilight and sun hit events`
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.outdoor.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.wind state at **\<wind\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.hit state at **\<sun_hit\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sun_twilight", "sun_brightness", "sun_hit", "wind", "from_state", "event", "to_state"
    :quote: “

    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunrise“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.twilight.civil.Event.Sunset“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Bright“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.Dark“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.brightness.Event.DeepDark“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunhit“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.sun.hit.Event.Sunleft“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Strong“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “event.wind.Event.Weak“, “curtain.outdoor.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to forced opened/closed events`
------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.outdoor.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.wind state at **\<wind\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.hit state at **\<sun_hit\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sun_twilight", "sun_brightness", "sun_hit", "wind", "from_state", "event", "to_state"
    :quote: “

    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to forced opened/closed events from a forced opened state`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.outdoor.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.wind state at **\<wind\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.hit state at **\<sun_hit\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Opened
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sun_twilight", "sun_brightness", "sun_hit", "wind", "from_state", "event", "to_state"
    :quote: “

    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.opened“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain react to forced opened/closed events from a forced closed state`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.outdoor.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.wind state at **\<wind\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.hit state at **\<sun_hit\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at Closed
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sun_twilight", "sun_brightness", "sun_hit", "wind", "from_state", "event", "to_state"
    :quote: “

    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “DeepDark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “DeepDark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Dark“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Dark“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Dark“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunleft“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Bright“, “Sunleft“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.opened“
    “Sunset“, “Bright“, “Sunhit“, “Strong“, “curtain.outdoor.state.forced.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.forced.closed“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Opened“, “curtain.outdoor.state.forced.opened“
    “Sunset“, “Bright“, “Sunhit“, “Weak“, “curtain.outdoor.state.closed“, “appliance.curtain.event.forced.Event.Closed“, “curtain.outdoor.state.closed“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Curtain shows its state`
---------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A curtain.outdoor.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.wind state at **\<wind\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.twilight.civil state at **\<sun_twilight\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.hit state at **\<sun_hit\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.curtain.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_opened
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sun_twilight", "sun_brightness", "sun_hit", "wind", "forced", "state", "response"
    :quote: “

    “Sunrise“, “Bright“, “Sunleft“, “Strong“, “Not“, “curtain.outdoor.state.opened“, “True“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “Not“, “curtain.outdoor.state.closed“, “False“
    “Sunrise“, “Bright“, “Sunleft“, “Weak“, “Closed“, “curtain.outdoor.state.forced.closed“, “False“
    “Sunrise“, “Bright“, “Sunhit“, “Weak“, “Opened“, “curtain.outdoor.state.forced.opened“, “True“

