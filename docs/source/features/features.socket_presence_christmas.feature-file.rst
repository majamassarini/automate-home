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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A Presence Christmas Socket`
==========================================================================================

    :gherkin-feature-description:`A presence Christmas socket which is by default on.`

    :gherkin-feature-description:`It can be turned off by the system if nobody is in the room unless it is Christmas time.`

    :gherkin-feature-description:`You could know that nobody is in the room when, as an example, the room alarm sensors are presence.`

    :gherkin-feature-description:`Other protocol triggers could be used for the same purpose.`

    :gherkin-feature-description:`If it is Christmas time then it is on when outside is deep dark and there is someone in the room.`

    :gherkin-feature-description:`If it is Christmas eve or Christmas day than it is on even if outside is bright or nobody is in the room.`

    :gherkin-feature-description:`If it is San Silvester eve or day than it is on even if outside is bright or nobody is in the room.`

    :gherkin-feature-description:`If it is the Epiphany eve or day than it is on even if outside is bright or nobody is in the room.`

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to alarm presence, sun phase and holiday events (internal alarm presence state is Off)`
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at On
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sun", "christmas", "san_silvester", "epiphany", "from_state", "event", "to_state"
    :quote: “

    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.On“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.off“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.off“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Dark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Dark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Dark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to alarm presence, sun phase and holiday events (internal alarm presence state is On)`
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at Off
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "sun", "christmas", "san_silvester", "epiphany", "from_state", "event", "to_state"
    :quote: “

    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.off“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “DeepDark“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Over“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.presence.Event.On“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.off“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Over“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.off“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Over“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.Off“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.presence.Event.On“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Time“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Over“, “socket.presence.christmas.state.on“
    “Bright“, “Time“, “Day“, “Day“, “socket.presence.christmas.state.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on/off events`
----------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun", "christmas", "san_silvester", "epiphany", "from_state", "event", "to_state"
    :quote: “

    “On“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “appliance.socket.event.forced.Event.Off“, “socket.presence.christmas.state.forced.off“
    “On“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “appliance.socket.event.forced.Event.On“, “socket.presence.christmas.state.on“
    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “appliance.socket.event.forced.Event.Off“, “socket.presence.christmas.state.off“
    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “appliance.socket.event.forced.Event.On“, “socket.presence.christmas.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on/off events from a forced on state`
---------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun", "christmas", "san_silvester", "epiphany", "from_state", "event", "to_state"
    :quote: “

    “On“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “appliance.socket.event.forced.Event.Off“, “socket.presence.christmas.state.forced.off“
    “On“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.on“, “appliance.socket.event.forced.Event.On“, “socket.presence.christmas.state.on“
    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.forced.on“, “appliance.socket.event.forced.Event.Off“, “socket.presence.christmas.state.off“
    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.forced.on“, “appliance.socket.event.forced.Event.On“, “socket.presence.christmas.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket react to forced on/off events from a forced off state`
----------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Off
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun", "christmas", "san_silvester", "epiphany", "from_state", "event", "to_state"
    :quote: “

    “On“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.forced.off“, “appliance.socket.event.forced.Event.Off“, “socket.presence.christmas.state.forced.off“
    “On“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.forced.off“, “appliance.socket.event.forced.Event.On“, “socket.presence.christmas.state.on“
    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “appliance.socket.event.forced.Event.Off“, “socket.presence.christmas.state.off“
    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.off“, “appliance.socket.event.forced.Event.On“, “socket.presence.christmas.state.forced.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket could be automatically un-forced from a forced off state by multiple events`
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at Off
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun", "christmas", "san_silvester", "epiphany", "from_state", "event", "to_state"
    :quote: “

    “On“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.forced.off“, “event.presence.Event.Off“, “socket.presence.christmas.state.off“
    “On“, “DeepDark“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.forced.off“, “event.sun.brightness.Event.Bright“, “socket.presence.christmas.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket could be automatically un-forced from a forced on state by multiple events`
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun", "christmas", "san_silvester", "epiphany", "from_state", "event", "to_state"
    :quote: “

    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “socket.presence.christmas.state.forced.on“, “event.presence.Event.On“, “socket.presence.christmas.state.forced.on“
    “On“, “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.forced.on“, “event.sun.brightness.Event.DeepDark“, “socket.presence.christmas.state.on“
    “On“, “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.forced.on“, “event.holiday.christmas.Event.Day“, “socket.presence.christmas.state.on“
    “On“, “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.forced.on“, “event.holiday.san_silvester.Event.Day“, “socket.presence.christmas.state.on“
    “On“, “Bright“, “Time“, “Over“, “Over“, “socket.presence.christmas.state.forced.on“, “event.holiday.epiphany.Event.Day“, “socket.presence.christmas.state.on“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Socket shows its is_on property`
-----------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A socket.presence.christmas.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.christmas state at **\<christmas\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.san_silvester state at **\<san_silvester\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.holiday.epiphany state at **\<epiphany\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.socket.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_on
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun", "christmas", "san_silvester", "epiphany", "forced", "state", "response"
    :quote: “

    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “Not“, “socket.presence.christmas.state.off“, “False“
    “Off“, “DeepDark“, “Over“, “Over“, “Over“, “On“, “socket.presence.christmas.state.forced.on“, “True“
    “On“, “DeepDark“, “Over“, “Over“, “Over“, “Not“, “socket.presence.christmas.state.on“, “True“
    “On“, “DeepDark“, “Over“, “Over“, “Over“, “Off“, “socket.presence.christmas.state.forced.off“, “False“

