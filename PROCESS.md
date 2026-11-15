# The Process Module

`home/process.py` is the central runtime orchestrator.  It owns the single
asyncio event loop and routes every event — whether it comes from a protocol
bus, a scheduled timer, or a Redis broadcast from another node — through the
appliance state machines.

## Architecture overview

```
Protocol gateways ──► _on_protocol_event()
                            │
                            ├─► _schedule_by_protocol_trigger()   (scheduler triggers)
                            └─► _update_performers_by_protocol_trigger()
                                        │
                                        ├─ performer.update_by(trigger)   (state update)
                                        ├─ _schedule_by_appliance_state() (state triggers)
                                        ├─ _make_msgs_except_echo()       (every performer's
                                        │                                  commands, not to the
                                        │                                  reporting device)
                                        ├─ redis_gateway.on_appliance_updated_by_process()
                                        └─ _write()                        (bus messages)

APScheduler ────────► schedule()  ──► _queue.put()
                                            │
                                    _run() drains queue
                                            │
                                    _notify(appliance, events)  (state update +
                                                                 every performer's commands)
                                    _schedule_by_appliance_state()
                                    redis_gateway.on_performer_updated_by_process()
                                    _write()   (bus messages)

Redis (remote node) ─► _on_appliance_updated_by_redis()
                            │
                            ├─ old_appliance.update(new_appliance)
                            ├─ _schedule_by_appliance_state()   (once per update)
                            └─ _make_msgs() + _write()          (every performer's commands)
```

## One pipeline for every state change

Whatever causes a state change (a bus message, a scheduler trigger, a Redis
update from the web UI), the brain does the same three things:

1. evaluates the appliance's state-based scheduler triggers once;
2. asks the commands of **every** performer of the appliance which messages
   the change needs (`Performer.execute(old_state, new_state)`): a command
   sends only when the property it controls changed, so running all of them is
   safe, and it doesn't matter which performer handled the event;
3. sends the messages, in performer order and then command order.

When the change comes from a bus message, the commands for the device that
sent it are left out (`Performer.execute_except_to`, through
`Description.reaches_a_device_of`): a device reporting its own state already
has it, and sending it back would be an echo. KNX compares the ASAPs of the
group addresses, the other protocols their addresses.

The commands also run when an event doesn't change the state: commands that
compare the states send nothing, and idempotent commands that apply the
current state (a LIFX color after the bulb has booted) send it again.

See the performer design rules in `docs/source/performer.rst`.

## Event sources

### 1. Protocol bus events (KNX, Lifx, Sonos …)

Each registered protocol gateway runs in its own asyncio task
(`gateway.run([callback])`).  When a bus message arrives the gateway decodes it
into a protocol trigger and calls the callback, which invokes
`_on_protocol_event`.

`_on_protocol_event` does two things **synchronously** (no queue):

1. **`_schedule_by_protocol_trigger`** — walks every registered scheduler
   trigger and enqueues those that match the incoming protocol trigger (protocol
   scheduler triggers, e.g. `!protocol.Trigger` in YAML).  The matching
   performers are notified *asynchronously* later by `_run`.

2. **`_update_performers_by_protocol_trigger`** — finds every performer whose
   own protocol trigger matches the bus message, calls `performer.update_by()`,
   evaluates state-based scheduler triggers, tells Redis about the state change
   and sends the bus messages of every performer of the appliance, except
   those for the device that sent the message.  This path is **synchronous** in the sense that the
   state update and Redis save happen before the coroutine returns.

### 2. Scheduler / timer events (APScheduler)

APScheduler calls `schedule(performer, trigger)` when a job fires.  This puts a
`(performer, trigger, trigger.events)` tuple onto the unbounded async queue
`_queue`.

The `_run` coroutine drains the queue one item at a time:

```
performer, trigger, events = await _queue.get()
```

Dispatch rules inside `_run`:

| Trigger type | Action |
|---|---|
| `state.entering.disable_events.Trigger` | Calls `appliance.disable(event)` for each event — prevents those events from being processed by the state machine |
| `date.enable_events.Trigger` | Calls `appliance.enable(event)` for each event — reverses a previous disable |
| Everything else | `_notify(appliance, events)` → state update and the messages of every performer of the appliance → `_schedule_by_appliance_state` → Redis save → bus messages |

After processing (whether successful or not), `_schedule_by_trigger_fork` is
called if the trigger is still enabled.  This re-arms recurring triggers
(e.g. `date.resettable.Trigger`) by registering their next fire time with
APScheduler.

### 3. Redis broadcasts from remote nodes

When another node (e.g. the `ws` web server) publishes a state change via Redis,
`_on_appliance_updated_by_redis` is called.  It:

1. Updates the local appliance to match the received state.
2. Calls `_schedule_by_appliance_state` so state-based scheduler triggers fire.
3. Runs the commands of every performer of that appliance and sends the
   resulting bus messages.

Each protocol writer call is wrapped in `asyncio.wait_for(..., timeout=1.0)` so
a slow or stalled gateway (e.g. Home Assistant websocket) cannot block the
remaining writers.

## State-trigger evaluation

`_schedule_by_appliance_state(scheduler, appliance, old_state, new_state)` is
called after **every** state change, regardless of the event source.  It scans
every state-type scheduler trigger registered for the appliance's performers
and fires those whose `is_triggered(old_state, new_state)` returns `True`.
All matching triggers are pushed onto `_queue` for `_run` to process.
Delayed variants (e.g. `state.entering.delay.duration.Trigger`) also call
`_schedule_by_trigger_fork` to register a one-shot timer with APScheduler.

## Lifecycle

```python
process = Process(my_home, redis_gateway)
process.add(knx_gateway)   # repeat for each protocol
process.run(scheduler)     # blocks until KeyboardInterrupt
```

`run()` obtains the event loop, calls `create_tasks()` (which creates the `_run`
task and one task per protocol gateway), starts the scheduler via
`loop.call_soon(scheduler.start)`, then connects the Redis gateway and enters
`loop.run_forever()`.  On `KeyboardInterrupt` it disconnects all gateways and
closes the loop.

## Key invariants

* **One queue, one consumer.** All APScheduler-generated events flow through
  `_queue` and are processed sequentially by `_run`.  This eliminates data
  races between timed events.

* **Protocol events are processed outside the queue.** `_on_protocol_event` runs
  directly in the gateway callback, so a KNX telegram is reflected in the state
  and sent to Redis before any pending queue items are processed.

* **Redis is the source of truth for remote nodes.** When `_run` calls
  `redis_gateway.on_performer_updated_by_process`, the gateway serialises the
  appliance state and publishes it so every other node can synchronise.

* **All events come from outside the dispatch loop.** Every state machine
  transition happens through events that arrive from the protocol bus,
  APScheduler, or Redis.  State-based scheduler triggers (including
  `state.entering.disable_events.Trigger`) are always queued for `_run` to
  process after the current dispatch completes.  This ensures every transition
  is visible to `_schedule_by_appliance_state`, saved to Redis, and observable
  by `_on_appliance_updated_by_redis`.

* **1-second writer timeout on every bus send.** All three dispatch paths
  (`_run`, `_update_performers_by_protocol_trigger`, `_on_appliance_updated_by_redis`,
  `_on_performer_updated_by_redis`) wrap each protocol writer call in
  `asyncio.wait_for(..., timeout=1.0)` and catch the resulting exception
  per-writer.  A stalled gateway therefore blocks its own writer for at most
  one second and never prevents other gateways from sending.
