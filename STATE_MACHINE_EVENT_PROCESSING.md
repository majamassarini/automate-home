# State Machine Event Processing

## Why Events May Have No Effect

**Sending an event to a state machine can have no effect even when it appears it should work.**

When a state transitions to a new state, **all events from the previous state are carried forward**. If a conflicting event exists in the state, it may immediately reverse the transition.

## Example: Sound Player Won't Fade In

A sound player receives `sleepiness.Event.Awake` to fade in at 7:00 AM:

```python
# Off state transitions to Fade In
class Sleepiness(Callable):
    def run(self, event, state):
        if event == home.event.sleepiness.Event.Awake:
            if home.event.elapsed.Event.On not in state:
                state = self.get_new_state(state, "fade_in")  # ← Transition
        return state
```

But Fade In immediately reverts to Off:

```python
# Fade In processes presence.Event.Off (from previous state)
class Presence(Callable):
    def run(self, event, state):
        if event == home.event.presence.Event.Off:
            state = self.get_new_state(state, "off")  # ← Reverts!
        return state
```

**Processing sequence:**
1. Off state receives `sleepiness.Event.Awake`
2. Transition to Fade In (new state inherits **all events from Off**, including `presence.Event.Off`)
3. Fade In state processes `presence.Event.Off`
4. Fade In immediately transitions back to Off
5. **Net result: Sound player stays Off**

## Event Processing Order is Unpredictable

**You cannot send multiple events at the same time when processing order matters.**

When multiple events are sent simultaneously (in the same update cycle), you cannot control which one is processed first. If the order matters for correct behavior, use state-based triggers instead.

### Example: Resetting elapsed.Off on Fade In

When a sound player transitions to Fade In, we need to reset `elapsed.Off` so the system can listen for fade completion.

**Wrong approach - sending events together:**

```yaml
# Trigger sends both events at the same time
- !protocol.Trigger
  name: "wakeup time"
  notify events:
    - !home.event.sleepiness.Event.Awake  # Triggers Fade In transition
    - !home.event.elapsed.Event.Off       # Should reset elapsed
```

**Problem:** We don't know which event is processed first. If `elapsed.Off` is processed before the state transition, it gets carried to the Fade In state but we lose the guarantee it was set *after* entering Fade In.

**Correct approach - state-based trigger:**

```yaml
# Trigger fires when entering Fade In state
- !state.entering.Trigger
  name: "fade in reset elapsed"
  notify events:
    - !home.event.elapsed.Event.Off
  when appliance state became: "Fade In"
```

This guarantees `elapsed.Off` is sent **after** the state transition completes.

## Events Always Come From Outside

All state machine transitions happen through events that arrive from **outside
the dispatch loop**: the protocol bus, APScheduler, or Redis.  State-based
scheduler triggers (e.g. `state.entering.disable_events.Trigger`) are always
**queued** for `_run` to process after the current dispatch completes.

This design preserves two properties that the system depends on:

1. **`_schedule_by_appliance_state` sees every transition.**  If a trigger were
   applied synchronously inside a callback, the resulting sub-transition would
   be invisible to `_schedule_by_appliance_state`.

2. **Redis reflects every transition.**  Every state change is saved to Redis.
   The `_on_appliance_updated_by_redis` path — which runs trigger-less
   performers such as the Sonos play/pause/volume commands — relies on
   comparing `old_state` and `new_state`.  It detects an off→on transition
   only when the local appliance was genuinely off before the Redis update
   arrived.

### Protocol echoes and how to suppress them

When a play command is sent to Sonos, the device echoes back a stop/pause
event.  That echo arrives as `forced.Event.Off`, which the Fade In state
machine processes as a transition to Forced Off.  `_on_appliance_updated_by_redis`
then fires with `(Fade In, Forced Off)` and sends a **pause** command — silencing
Sonos just after it started playing.

The play command itself is sent directly by the performer in `_run` (or
`_update_performers_by_protocol_trigger`) when the off→on state transition
happens, not via the echo path.  The echo is purely a side-effect to suppress.

To suppress the echo, configure a `state.entering.disable_events.Trigger` for
`forced.Event.Off` in the YAML.  This trigger is queued and fires very quickly
(the event loop processes the next queue item almost immediately after the state
transition), well before the echo travels over the network and arrives at the
gateway.  Any further echoes are silently ignored until the paired
`state.entering.delay.enable_events.Trigger` re-enables `forced.Event.Off` after
a few seconds.

## Guidelines

1. **Be selective about events** - Not every appliance needs every event
2. **Check state DEFAULTS** - Each state has default events that are always present
3. **Watch for conflicts** - One event enables a state, another disables it
4. **Use state-based triggers when order matters** - Don't send multiple events simultaneously if processing order is critical
5. **Test realistically** - Include all relevant events when testing transitions
6. **All events come from outside** - See the section above

## Debugging Checklist

When a transition doesn't work as expected:
- What events are already in the current state?
- What events will the new state process?
- Could any events conflict with the desired transition?
- Are multiple events being sent simultaneously when order matters?
