# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

from behave import given, when, then, use_step_matcher
import home

use_step_matcher("re")


@given(r"A ([\w.]+) appliance")
def build_an_appliance(context, app):
    namespace = home.appliance
    for attr in app.split("."):
        namespace = getattr(namespace, attr)

    context.appliance = namespace(("A %s" % app), [])
    context.internal_state = []


@given(r"the appliance has an internal ([\w.]+) state at (\w+)")
def appliance_internal_state(context, path, state):
    namespace = home
    for attr in path.split("."):
        namespace = getattr(namespace, attr)
    try:
        event = getattr(namespace, "Event")
        value = getattr(event, state)
    except AttributeError:
        try:
            value = event(int(state))
        except ValueError:
            value = event(str(state))

    context.internal_state.append(value)


@given(r"the brightness ([\w.]+) state at (\w+)")
def brightness_state(context, path, value):
    namespace = home
    for attr in path.split("."):
        namespace = getattr(namespace, attr)
    event = getattr(namespace, "Event")

    context.internal_state.append(event(int(value)))


@given(r"it\'s calculated state is ([\w.]+)")
def appliance_initial_state(context, state):
    namespace = home.appliance
    for attr in state.split("."):
        namespace = getattr(namespace, attr)
    klass = getattr(namespace, "State")

    for event in context.internal_state:
        try:
            context.appliance.notify(event)
        except KeyError as e:
            raise e

    initial_state_class = type(context.appliance.state)
    if not (initial_state_class == klass):
        raise Exception(
            "The initial state is %s instead of %s" % (initial_state_class, klass)
        )


@when(r"it receives a new event ([\w.]+)")
def appliance_received_new_event(context, event):
    namespace = home
    for attr in event.split("."):
        namespace = getattr(namespace, attr)

    context.appliance.notify(namespace)


@then(r"the appliance new state is ([\w.]+)")
def appliance_final_state(context, state):
    namespace = home.appliance
    for attr in state.split("."):
        namespace = getattr(namespace, attr)
    klass = getattr(namespace, "State")

    final_state_class = type(context.appliance.state)
    if not (final_state_class == klass):
        raise Exception(
            "The new state is %s instead of %s" % (final_state_class, klass)
        )


@when(r"it\'s asked for its state property ([\w_]+)")
def appliance_property(context, prop):
    context.property = getattr(context.appliance.state, prop)


@then(r"the response is ([<>°{}:%,. \w]+)")
def appliance_response(context, prop):
    if not (str(context.property) == prop):
        raise Exception(
            "The appliance state property is %s instead of %s"
            % (context.property, prop)
        )
