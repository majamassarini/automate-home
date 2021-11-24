# Automate home

[![Build Status](https://app.travis-ci.com/majamassarini/automate-home.svg?branch=main)](https://app.travis-ci.com/majamassarini/automate-home)
[![codecov](https://codecov.io/gh/majamassarini/automate-home/branch/main/graph/badge.svg?token=mjBUwkmcML)](https://codecov.io/gh/majamassarini/automate-home)
[![Documentation Status](https://readthedocs.org/projects/automate-home/badge/?version=latest)](https://automate-home.readthedocs.io/en/latest/?badge=latest)

![](icon_128x128.png)


Yet another home automation project because a **smart light is more than just on or off**.

## Overview

When talking about home automation there are at least two goals you could
have in mind:

1. let a user interact with the home devices through many interfaces locally or remotely
2. let devices interact together and let the system change their state

I believe the other home automation projects fits perfectly the first goal,
this project focuses on **automation**, the second one.

What's the difference between this project model and other home automation projects?

The main difference is the design of an *Appliance* where, with the name *Appliance*, I refer to entities like a light, a curtain, a sound player ecc.

One of the simplest *Appliances* I could imagine is a light with two *physical states*: on and off.

A light model could be designed like a deterministic state machine; all the other home automation projects I know do it like that.

Or it could be designed like [a non deterministic state machine](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjE_8OOjeTsAhVR26QKHe9iA4cQmhMwHHoECB8QAg&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FNondeterministic_finite_automaton&usg=AOvVaw27skSr2u7Pk_Ka8zz9O1j0>);
 which is how it is done by this project.

When using a deterministic state machine if you have a light with on/off physical states its model states will be just on/off.
When using a non-deterministic state machine it is quite simple to have more model states for an on/off light, as an example, 
your light could be in an *alarmed* state and it could start blinking.

### Behavior-driven development

I believe logics are the building bricks of a smart home system.
Nevertheless, they are complex to build, debug and share and one of this project goals is to make it easier.

Having an *Appliance* grouping together all its logics **simplifies debug and reuse**.

All *Appliances* inner states can be tested with [BDD](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjqq7PHleTsAhXpA2MBHUVSC2wQFjAAegQIAhAC&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBehavior-driven_development&usg=AOvVaw3zU0d2S_KiO3w9C0gwNWv_) style tests [like this](https://automate-home.readthedocs.io/en/latest/features/features.light_presence.feature-file.html).

BDD style tests make it quite easy to understand the behaviour of every *Appliance* in every possible state and thus make it **shareable**.

**I like to think of this project as a way to share behavioural models for our smart devices more easily.**

## Documentation

For a deep dive into this project see the [documentation](https://automate-home.readthedocs.io/en/latest/?badge=latest).

For a minute guide to this project see the [landing page](https://majamassarini.github.io/automate-home).

### Example projects

Using the docker image:

```shell
docker pull majamassarini/automate-home:latest
```

* [lights models](https://majamassarini.github.io/automate-lights-example/pages/172.31.10.243/index.html) ([configuration](https://github.com/majamassarini/automate-lights-example))
* [curtain models](https://majamassarini.github.io/automate-curtains-example/pages/172.31.10.244/index.html) ([configuration](https://github.com/majamassarini/automate-curtains-example))
* [sound player model](https://majamassarini.github.io/automate-sound-player-example/pages/172.31.10.247/index.html) ([configuration](https://github.com/majamassarini/automate-sound-player-example))
