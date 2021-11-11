*********
Appliance
*********

**Appliances are entities which group together behavioural rules**.

**Appliances are abstract non deterministic state machines**, they do not know how to turn on your light,
they just know that your light should be turned on.

**Events** are notified to *Appliances* and can make transit the state machine.

.. tip::
  The *Appliance* state machine can be modified by a user at any time.

  **Event** processing, inside an *Appliance* instance, can be **disabled/enabled** (:ref:`example <event disable widget>`).

  If, as an example, you have a curtain model automated to be opened by the system when it receives the event
  *home.event.sleepiness.Event.Awake*, meaning the user has to be wake up, then the user can inhibit the
  processing of such an event every time he does not want to be wake up.

Appliances states are designed to be **easily reusable**.

When writing the state machine one of the most difficult things is to be sure that every transition is correct.
For this reason the behaviour of an Appliance is tested and described by a :ref:`BDD test <Features>`.


.. raw:: latex

    \clearpage

.. toctree::

    appliance/state

.. raw:: latex

    \clearpage


Appliance Class
===============


.. autoclass:: home.Appliance

.. raw:: latex

    \clearpage


