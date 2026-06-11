# Automate home

[![Build Status](https://app.travis-ci.com/majamassarini/automate-home.svg?branch=main)](https://app.travis-ci.com/majamassarini/automate-home)
[![codecov](https://codecov.io/gh/majamassarini/automate-home/branch/main/graph/badge.svg?token=mjBUwkmcML)](https://codecov.io/gh/majamassarini/automate-home)
[![Documentation Status](https://readthedocs.org/projects/automate-home/badge/?version=latest)](https://automate-home.readthedocs.io/en/latest/?badge=latest)

![](icon_128x128.png)


Yet another home automation (iot) project because a **smart light is more than just on or off**.

## Overview

Home automation projects generally aim at one (or both) of two goals:

1. let a user interact with their home devices through many interfaces, locally or remotely;
2. let devices interact with each other and let the system change their state on its own.

Most home automation projects nail the first goal. This project focuses on the second one: **automation**.

The key difference is in how an *Appliance* — a light, a curtain, a sound player, anything with a state — is modelled.

Other projects model a device as a deterministic state machine: a light with on/off physical states has just two model states, on and off.

This project models it as a [non-deterministic state machine](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton): the same on/off light can have **more model states than physical states** — for example an *alarmed* state in which it blinks, layered on top of its physical on/off.

### Behaviour-driven development

Automations are the building blocks of a smart home system, but they are notoriously hard to build, debug and share. Grouping all of an *Appliance*'s logic into one state machine **simplifies both debugging and reuse**.

Every *Appliance* state and transition is covered by [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) style tests — see [an example](https://automate-home.readthedocs.io/en/latest/features/features.light_presence.feature-file.html) — which make it easy to understand exactly how an *Appliance* behaves in every state, and **shareable** as a behavioural model rather than just a pile of YAML.

## automate-home vs Home Assistant

A natural question is: *why not just do all of this in Home Assistant?*

Home Assistant is unmatched as a **device gateway** — discovering and talking to an
enormous range of hardware, with a polished UI, mobile app, dashboards and voice
integration that this project would never match. That's exactly why an
[automate-home-assistant-plugin](https://github.com/majamassarini/automate-home-assistant-plugin)
exists: let Home Assistant be the gateway to the device world, and let *Appliances* be
the **behaviour** on top of it. This project ships its own native plugins for
[KNX](https://github.com/majamassarini/automate-knx-plugin),
[Lifx](https://github.com/majamassarini/automate-lifx-plugin) and
[Sonos](https://github.com/majamassarini/automate-sonos-plugin) — the protocols it talks
to most directly — and relies on the Home Assistant plugin for everything else.

Where automate-home shines is modelling **genuinely stateful appliance behaviour** —
reacting to several independent event sources (presence, sleepiness, timers, user-forced
commands, device echoes) and combining them into a small number of explicit, named
states. A few things make that tractable here:

- **Reuse through real class hierarchies.** An *Appliance* type is written **once** —
  its states, transitions and guards — and every physical instance reuses that same,
  already-debugged logic; only the wiring to the physical device changes. In plain Home
  Assistant that behaviour ends up copy-pasted per device in YAML, or hand-rolled into a
  templated blueprint, mixing behaviour and wiring back together.

- **BDD tests as a regression net.** Every *Appliance* state and transition is covered
  by BDD style tests — hundreds of scenarios that pin down exactly how it reacts to every
  event in every state, the kind of timing- and ordering-sensitive coverage that's nearly
  impossible to get from poking a real device and watching what happens.

- **A richer vocabulary for reacting to raw bus data.** *Protocol Triggers* are a
  first-class, YAML-wireable concept here: you react not just to a single message on the
  bus, but to *patterns* in a stream of them. For example:

    - `protocol.mean.GreaterThan` / `LesserThan` / `InBetween` — average a sensor's
      readings over a rolling window and fire only once the *mean* crosses a threshold
      (e.g. wind speed or outdoor light level as "strong"/"weak"/"in between"), so a
      single noisy reading doesn't flip an appliance back and forth;
    - `protocol.multi.Trigger` — combine several independent triggers with
      positive/negative logic, e.g. turning separate zone sensors into a single "this
      zone just became occupied/empty" event;
    - `protocol.enum.Trigger` — step through a small enum of events each time a message
      arrives, e.g. a wall button cycling through "next/previous user";
    - `protocol.timer.Trigger` — fire a follow-up event some seconds after the original
      one, e.g. a scene that, once triggered, schedules itself to be undone later.

  In a pure Home Assistant setup this kind of stream-level reasoning is
  integration-internal Python that users don't get to wire themselves; here it's an open,
  composable layer you can build new appliance behaviour on without writing a plugin.

- **One Appliance, several cooperating protocols, one coherent state.** An *Appliance*
  only knows *what* it should be (e.g. "the light should be on"); the *Performer* layer
  maps that to actual protocol commands and reads protocol feedback back. So a single
  *Appliance* can be wired to devices speaking entirely different protocols — say a bulb
  on one wireless protocol switched by a wall unit on a wired bus — and the end user still
  sees and interacts with **one** light, with one well-defined state. In a pure Home
  Assistant setup the unit of modelling is the *entity*, normally one per
  device/integration; presenting such a pair as a single coherent thing means
  hand-building a group or templated entity (with its own scripts to reconcile both
  devices' states) plus an automation to keep them in sync — the same
  assemble-it-yourself-and-hope-it-stays-in-sync pattern, now applied to *cross-protocol*
  composition, and just as exercised by the BDD suite as everything else.

- **A UI generated from the same wiring that drives the automation.**
  [automate-ws](https://github.com/majamassarini/automate-ws) renders, for every
  *Appliance*, a details page built directly from its live state plus the very same
  Performer/Trigger configuration that drives it: an **Inputs** section listing every
  trigger and the protocol address it listens on, an **Outputs** section listing every
  command and the protocol address it writes to, and a filterable history of the events
  that led to the current state. There's no separate dashboard to design or keep in sync
  — the UI **is** the wiring, always up to date, and it answers "why is this appliance in
  this state?" directly. In Home Assistant, dashboards are a separate artifact from
  automations: a Lovelace card shows an entity's current state and history, but to see
  *which automation is watching it and what it would do next* means going to read the
  automation configuration separately.

In short: reach for Home Assistant (or its plugin here) for **connectivity** — discovering
and commanding devices, dashboards, notifications, voice. Reach for an *Appliance* when
the **behaviour** itself is the hard part.

## Documentation

For a deep dive into this project see the [documentation](https://automate-home.readthedocs.io/en/latest/?badge=latest).

For a minute guide to this project see the [landing page](https://majamassarini.github.io/automate-home).

For understanding how state machines process events and why some transitions may not work as expected, see [State Machine Event Processing](STATE_MACHINE_EVENT_PROCESSING.md).

For a detailed description of the runtime event loop and how protocol events, scheduler timers, and Redis broadcasts are routed through the appliance state machines, see [The Process Module](PROCESS.md).

## Installation

Install the Python packages with pip:

```shell
pip install automate-ws automate-graphite-feeder  # graphite_feeder is optional, for event graphs in the UI

python -m home --configuration-file configuration.ini             # the automation engine
python -m ws --configuration-file configuration.ini               # the web UI
python -m graphite_feeder --configuration-file configuration.ini  # optional: feeds event graphs to the UI
```

Each process reads the same `configuration.ini`; its `[project] project_dir` points at
the directory holding your YAML *Appliances*, *Performers* and *Scheduler Triggers*.
[`home/example.ini`](home/example.ini) is a good starting template — see the
[documentation](https://automate-home.readthedocs.io/en/latest/?badge=latest) for the
full configuration file layout.

## Contributing

Pull requests are welcome!

## License

The automate-home project is licensed under GPL3.
