.. home documentation master file, created by
   sphinx-quickstart on Tue Oct  6 21:48:18 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

###########################
automate-home documentation
###########################


.. image:: ../../icon_128x128.png


Why yet another home automation project?

Because I believe that **a smart light could be more than just on or off**.
And I believe that a smart light **should not need your control**, neither local nor remote.

**This project is not yet another interface to access and control your smart devices**,
I'm pretty sure your smart devices already have a great interface to do that.

**This is an automation framework**. It lets you build simple and complex automations, interact with and control them.
But building a system that acts on behalf of you brings some **problems** that
this project strives to solve:

    - :ref:`user should win over the system <win-over-the-system>`
    - :ref:`user should not experience feel of losing control <feel-of-losing-control>`
    - :ref:`debug and reuse of logics should be simple <debug-and-reuse>`

.. _win-over-the-system:
User should win over the system
===============================

When a smart home system connects your devices then there is someone else in
charge of controlling them besides you.

What if you and your smart home system *disagree*?
A really smart home automation system **should let you win**.

Examples
--------

Light
^^^^^

Suppose you have a light which is turned on/off when a motion detector sensor, in the light zone, is triggered/untriggered.
You can turn on/off this same light with a button when you need it because, as an example, you come and go.

Now you need it, you turn on the light and you go away for some time.
In the meanwhile someone else is arriving at home and
the motion sensor went triggered and a few minutes later untriggered.
The motion sensor, in a *smart* home automation system, should not turn off your light **because
the light is not just on but it is forced on by you**; and you should win over the system because you
already knew you would be back in a moment.

.. raw:: latex

    \clearpage

.. raw:: latex
    :file: ./latex/other_projects_garage_light.tex

.. only:: html

  .. figure:: ./latex/other_projects_garage_light.tex.svg
    :align: center


.. raw:: latex
    :file: ./latex/this_project_garage_light.tex

.. only:: html

  .. _light-in-this-project:

  .. figure:: ./latex/this_project_garage_light.tex.svg
    :align: center

.. raw:: latex

    \clearpage

Curtain
^^^^^^^

Suppose you have an automated curtain: it is closed by the system when both the sun is shining
and the sun is hitting the curtain's window. You can open/close the curtain with a button.

Now, for some reason, you need more light and you open the curtain's window with the button.
It is a partly cloudy day and sun comes and goes, nevertheless
your curtain should not be closed again at least until sun goes down.

.. raw:: latex

    \clearpage

.. raw:: latex
    :file: ./latex/other_projects_curtain.tex

.. only:: html

  .. figure:: ./latex/other_projects_curtain.tex.svg
    :align: center


.. raw:: latex
    :file: ./latex/this_project_curtain.tex

.. only:: html

  .. _curtain-in-this-project:

  .. figure:: ./latex/this_project_curtain.tex.svg
    :align: center

.. raw:: latex

    \clearpage


.. _feel-of-losing-control:

User should not experience feel of losing control
=================================================

When the system acts on behalf of you but you don't understand why, you could experience a *feeling of losing control*.

For these reasons a good system should let you know, in every moment, **what** action it has done and **why**.

More logics you have, the more complex they are, more probably it will happen that you think the system went crazy unless you know exactly what happened.

Examples
--------

Light
^^^^^

If, for any reason, *User Bob* was not aware of *User John*
then *User Bob* probably thought the system was wrong: since the garage light did not turn off
(:ref:`an automated light <light-in-this-project>`).

A light model should let *User Bob* know that *User John* **forced the light on**: :ref:`a light description <light widget>`.

Curtain
^^^^^^^

When the curtain is up even if the sun is shining, someone other than you can think the system is broken
unless he knows that the curtain is up because you forced open it
(:ref:`an automated curtain <curtain-in-this-project>`).

A curtain model should let *another user* know that you **forced opened the curtain**: :ref:`a curtain description <curtain widget>`.



.. toctree::
   :maxdepth: 3
   :caption: Contents:

   intro
   appliance
   appliances
   performer
   scheduler
   plugins
   projects
..   example_projects
..   scenes
..   features

.. features/gherkin


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
