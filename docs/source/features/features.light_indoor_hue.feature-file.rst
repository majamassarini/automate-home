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

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`A indoor hue Light`
=================================================================================

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to courtesy and sun brightness events`
-----------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “Bright“, “light.indoor.hue.state.off“, “event.presence.Event.On“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.off“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Bright“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.off“
    “On“, “Dark“, “light.indoor.hue.state.off“, “event.presence.Event.On“, “light.indoor.hue.state.off“
    “On“, “Dark“, “light.indoor.hue.state.off“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Dark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Bright“, “light.indoor.hue.state.off“
    “On“, “Dark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.off“
    “On“, “Dark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.off“
    “On“, “DeepDark“, “light.indoor.hue.state.off“, “event.presence.Event.On“, “light.indoor.hue.state.off“
    “On“, “DeepDark“, “light.indoor.hue.state.off“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “On“, “DeepDark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Bright“, “light.indoor.hue.state.off“
    “On“, “DeepDark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.off“
    “On“, “DeepDark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.off“
    “Off“, “Bright“, “light.indoor.hue.state.off“, “event.presence.Event.On“, “light.indoor.hue.state.off“
    “Off“, “Bright“, “light.indoor.hue.state.off“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “Off“, “Bright“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Bright“, “light.indoor.hue.state.off“
    “Off“, “Bright“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.off“
    “Off“, “Bright“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.off“
    “Off“, “Dark“, “light.indoor.hue.state.off“, “event.presence.Event.On“, “light.indoor.hue.state.off“
    “Off“, “Dark“, “light.indoor.hue.state.off“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “Off“, “Dark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Bright“, “light.indoor.hue.state.off“
    “Off“, “Dark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.off“
    “Off“, “Dark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.off“
    “Off“, “DeepDark“, “light.indoor.hue.state.off“, “event.presence.Event.On“, “light.indoor.hue.state.off“
    “Off“, “DeepDark“, “light.indoor.hue.state.off“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “Off“, “DeepDark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Bright“, “light.indoor.hue.state.off“
    “Off“, “DeepDark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.off“
    “Off“, “DeepDark“, “light.indoor.hue.state.off“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to forced events`
--------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at Not
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “Bright“, “light.indoor.hue.state.off“, “appliance.light.indoor.dimmerable.event.forced.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.off“, “appliance.light.indoor.dimmerable.event.forced.Event.On“, “light.indoor.hue.state.forced.on“
    “On“, “Bright“, “light.indoor.hue.state.off“, “appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“
    “On“, “Bright“, “light.indoor.hue.state.off“, “appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance“, “light.indoor.hue.state.forced.lux_balance“
    “On“, “Bright“, “light.indoor.hue.state.off“, “appliance.light.indoor.dimmerable.event.forced.Event.Show“, “light.indoor.hue.state.forced.show“
    “On“, “Bright“, “light.indoor.hue.state.off“, “appliance.light.indoor.dimmerable.event.forced.Event.Not“, “light.indoor.hue.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to forced events from a forced on state`
-------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at On
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “Bright“, “light.indoor.hue.state.forced.on“, “appliance.light.indoor.dimmerable.event.forced.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.forced.on“, “appliance.light.indoor.dimmerable.event.forced.Event.On“, “light.indoor.hue.state.forced.on“
    “On“, “Bright“, “light.indoor.hue.state.forced.on“, “appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm“, “light.indoor.hue.state.forced.on“
    “On“, “Bright“, “light.indoor.hue.state.forced.on“, “appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance“, “light.indoor.hue.state.forced.on“
    “On“, “Bright“, “light.indoor.hue.state.forced.on“, “appliance.light.indoor.dimmerable.event.forced.Event.Show“, “light.indoor.hue.state.forced.on“
    “On“, “Bright“, “light.indoor.hue.state.forced.on“, “appliance.light.indoor.dimmerable.event.forced.Event.Not“, “light.indoor.hue.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to forced events from a forced circadian rhythm state`
---------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at CircadianRhythm
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “appliance.light.indoor.dimmerable.event.forced.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “appliance.light.indoor.dimmerable.event.forced.Event.Not“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “appliance.light.indoor.dimmerable.event.forced.Event.On“, “light.indoor.hue.state.forced.circadian_rhythm“
    “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance“, “light.indoor.hue.state.forced.circadian_rhythm“
    “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “appliance.light.indoor.dimmerable.event.forced.Event.Show“, “light.indoor.hue.state.forced.circadian_rhythm“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to forced events from a forced lux balance state`
----------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at LuxBalance
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “appliance.light.indoor.dimmerable.event.forced.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “appliance.light.indoor.dimmerable.event.forced.Event.Not“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “appliance.light.indoor.dimmerable.event.forced.Event.On“, “light.indoor.hue.state.forced.lux_balance“
    “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm“, “light.indoor.hue.state.forced.lux_balance“
    “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “appliance.light.indoor.dimmerable.event.forced.Event.Show“, “light.indoor.hue.state.forced.lux_balance“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light react to forced events from a forced show state`
---------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at Show
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “Bright“, “light.indoor.hue.state.forced.show“, “appliance.light.indoor.dimmerable.event.forced.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.forced.show“, “appliance.light.indoor.dimmerable.event.forced.Event.Not“, “light.indoor.hue.state.off“
    “On“, “Bright“, “light.indoor.hue.state.forced.show“, “appliance.light.indoor.dimmerable.event.forced.Event.On“, “light.indoor.hue.state.forced.show“
    “On“, “Bright“, “light.indoor.hue.state.forced.show“, “appliance.light.indoor.dimmerable.event.forced.Event.CircadianRhythm“, “light.indoor.hue.state.forced.show“
    “On“, “Bright“, “light.indoor.hue.state.forced.show“, “appliance.light.indoor.dimmerable.event.forced.Event.LuxBalance“, “light.indoor.hue.state.forced.show“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light could be automatically un-forced from a forced state by event.presence.Off event and not by sun.brightness events`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced_state\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<from_state\>**
| :gherkin-step-keyword:`When` it receives a new event **\<event\>**
| :gherkin-step-keyword:`Then` the appliance new state is **\<to_state\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "forced_state", "presence", "sun_brightness", "from_state", "event", "to_state"
    :quote: “

    “On“, “On“, “Bright“, “light.indoor.hue.state.forced.on“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.forced.on“
    “On“, “Off“, “Bright“, “light.indoor.hue.state.forced.on“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.forced.on“
    “On“, “On“, “Bright“, “light.indoor.hue.state.forced.on“, “event.presence.Event.On“, “light.indoor.hue.state.forced.on“
    “On“, “Off“, “Bright“, “light.indoor.hue.state.forced.on“, “event.presence.Event.On“, “light.indoor.hue.state.forced.on“
    “On“, “On“, “Bright“, “light.indoor.hue.state.forced.on“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “On“, “Off“, “Bright“, “light.indoor.hue.state.forced.on“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “Show“, “On“, “Bright“, “light.indoor.hue.state.forced.show“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.forced.show“
    “Show“, “Off“, “Bright“, “light.indoor.hue.state.forced.show“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.forced.show“
    “Show“, “On“, “Bright“, “light.indoor.hue.state.forced.show“, “event.presence.Event.On“, “light.indoor.hue.state.forced.show“
    “Show“, “Off“, “Bright“, “light.indoor.hue.state.forced.show“, “event.presence.Event.On“, “light.indoor.hue.state.forced.show“
    “Show“, “On“, “Bright“, “light.indoor.hue.state.forced.show“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “Show“, “Off“, “Bright“, “light.indoor.hue.state.forced.show“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “LuxBalance“, “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.forced.lux_balance“
    “LuxBalance“, “Off“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.forced.lux_balance“
    “LuxBalance“, “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “event.presence.Event.On“, “light.indoor.hue.state.forced.lux_balance“
    “LuxBalance“, “Off“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “event.presence.Event.On“, “light.indoor.hue.state.forced.lux_balance“
    “LuxBalance“, “On“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “LuxBalance“, “Off“, “Bright“, “light.indoor.hue.state.forced.lux_balance“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “CircadianRhythm“, “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “event.sun.brightness.Event.Dark“, “light.indoor.hue.state.forced.circadian_rhythm“
    “CircadianRhythm“, “Off“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “event.sun.brightness.Event.DeepDark“, “light.indoor.hue.state.forced.circadian_rhythm“
    “CircadianRhythm“, “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “event.presence.Event.On“, “light.indoor.hue.state.forced.circadian_rhythm“
    “CircadianRhythm“, “Off“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “event.presence.Event.On“, “light.indoor.hue.state.forced.circadian_rhythm“
    “CircadianRhythm“, “On“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “event.presence.Event.Off“, “light.indoor.hue.state.off“
    “CircadianRhythm“, “Off“, “Bright“, “light.indoor.hue.state.forced.circadian_rhythm“, “event.presence.Event.Off“, “light.indoor.hue.state.off“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: on`
------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_on
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “False“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “True“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “True“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “True“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “True“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: brightness`
--------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.brightness state at 10
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.circadian_rhythm.brightness state at 20
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.lux_balancing.brightness state at 30
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property brightness
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “10“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “10“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “20“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “30“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “10“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: hue`
-------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.hue state at 10
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.circadian_rhythm.hue state at 20
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.show.starting_hue state at 30
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property hue
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “10“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “10“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “20“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “10“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “10“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: saturation`
--------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.saturation state at 10
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.circadian_rhythm.saturation state at 20
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property saturation
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “10“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “10“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “20“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “10“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “10“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: temperature`
---------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.temperature state at 10
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.event.circadian_rhythm.temperature state at 20
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property temperature
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “10“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “10“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “20“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “10“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “10“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: is_circadian_rhythm`
-----------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_circadian_rhythm
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “False“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “False“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “True“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “False“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “False“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: is_lux_balancing`
--------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_lux_balancing
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “False“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “False“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “False“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “True“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “False“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`The Light shows its state\: is_showing`
--------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` A light.indoor.hue.Appliance appliance
| :gherkin-step-keyword:`And` the appliance has an internal event.presence state at **\<presence\>**
| :gherkin-step-keyword:`And` the appliance has an internal event.sun.brightness state at **\<sun_brightness\>**
| :gherkin-step-keyword:`And` the appliance has an internal appliance.light.indoor.dimmerable.event.forced state at **\<forced\>**
| :gherkin-step-keyword:`And` it's calculated state is **\<state\>**
| :gherkin-step-keyword:`When` it's asked for its state property is_showing
| :gherkin-step-keyword:`Then` the response is **\<response\>**

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "presence", "sun_brightness", "forced", "state", "response"
    :quote: “

    “On“, “Bright“, “Not“, “light.indoor.hue.state.off“, “False“
    “On“, “Bright“, “On“, “light.indoor.hue.state.forced.on“, “False“
    “On“, “Bright“, “CircadianRhythm“, “light.indoor.hue.state.forced.circadian_rhythm“, “False“
    “On“, “Bright“, “LuxBalance“, “light.indoor.hue.state.forced.lux_balance“, “False“
    “On“, “Bright“, “Show“, “light.indoor.hue.state.forced.show“, “True“

