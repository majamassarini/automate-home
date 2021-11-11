State
=====

Appliance *States* are the entities which build up the **non deterministic state machine**.

Take a curtain as an example.

A curtain could be **Closed** for many different reasons:
 - it could be *Closed* because someone *forced it to be closed*
 - or it could be *Closed* because *the sun is hitting the window* and the system closes it.

It is up to the *non deterministic state machine design* decide which are the events that allow a *Closed* curtain to become *Opened*:
 - a state called *forced.Closed* receiving the *sun is not hitting the window anymore event* will result in the same *forced.Closed* state.
 - a state called *Closed* receiving the *sun is not hitting the window anymore event* will result in a new *Opened* state.

.. hint::
  You could not say which will be the next *Appliance State*, upon reception of an event,
  unless you know exactly the **internal state** of an *Appliance State*.

.. autoclass:: home.appliance.curtain.outdoor.state.State
  :no-members:

.. raw:: latex

    \clearpage

From *Forced States* to other *States*
--------------------------------------------

When the system changes the *State* of, as an example, a curtain *Appliance* it will put it in a **non forced** State (opened or closed).

When you push the down button you will *force close* the curtain.

When you push the up button you will *force open* the curtain.

When is the curtain unlocked from a forced state?

.. hint::
  Supposing that the system does, most of the time, the things you will do;
  it could be said that the *Appliance State* could be forced only if you disagree with the system rules.

A *forced state* could be **automatically unlocked** when you and the system agree again.


Example
^^^^^^^

The sun is hitting the window and the appliance non deterministic state machine says the curtain should be in a *Closed* state.
But you need it to be opened and pressing a button you open it in a *Forced Opened* state.
Few minutes later the wind starts blowing strong and the system says that the curtain should be in a *Opened* state.
Now you and the system agree and the curtain state can be moved from a *Forced Opened* state to an *Opened* state.

.. hint::
  Every *Event* changing the state could unlock a *forced* state. But sometimes *Events* comes so often,
  and make the state change so often, that is better if they will not unlock a state.
  Is up to the non deterministic state machine
  design decide which are the events which will reset a forced state.

.. raw:: latex

    \clearpage

Event Class
---------------------

.. py:attribute:: home.Event
   :type: TypeVar
   :value: TypeVar('home.Event')

One of:

  - :code:`int`
  - :code:`float`
  - :code:`str`
  - :code:`home.Enum`
  - :code:`home.appliance.light.event.hue.Event`
  - :code:`home.appliance.light.event.brightness.Event`
  - :code:`home.appliance.light.event.saturation.Event`
  - :code:`home.appliance.light.event.temperature.Event`
  - :code:`home.appliance.light.show.cycles.Event`
  - :code:`home.appliance.light.show.ending_brightness.Event`
  - :code:`home.appliance.light.show.ending_hue.Event`
  - :code:`home.appliance.light.show.period.Event`
  - :code:`home.appliance.light.show.starting_brightness.Event`
  - :code:`home.appliance.light.show.starting_hue.Event`
  - :code:`home.appliance.light.event.lux_balancing.brightness.Event`
  - :code:`home.appliance.light.event.circadian_rhythm.brightness.Event`
  - :code:`home.appliance.light.event.circadian_rhythm.hue.Event`
  - :code:`home.appliance.light.event.circadian_rhythm.saturation.Event`
  - :code:`home.appliance.light.event.circadian_rhythm.temperature.Event`
  - :code:`home.appliance.sound.player.event.volume.Event`
  - :code:`home.appliance.sound.player.event.sleepy_volume.Event`
  - :code:`home.appliance.sound.player.event.playlist.Event`
  - :code:`home.appliance.sound.player.event.forced.circadian_rhythm.playlist_a.Event`
  - :code:`home.appliance.sound.player.event.forced.circadian_rhythm.playlist_b.Event`
  - :code:`home.appliance.sound.player.event.forced.circadian_rhythm.playlist_c.Event`
  - :code:`home.appliance.sound.player.event.fade_in.volume.Event`
  - :code:`home.appliance.sound.player.event.fade_in.playlist.Event`
  - :code:`home.appliance.sound.player.event.fade_out.volume.Event`
  - :code:`home.appliance.sound.player.event.fade_out.playlist.Event`

.. raw:: latex

    \clearpage

Callable Class
---------------------

.. autoclass:: home.appliance.Callable

.. raw:: latex

    \clearpage

State Class
---------------------

.. autoclass:: home.appliance.State

.. raw:: latex

    \clearpage

