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

## Guidelines

1. **Be selective about events** - Not every appliance needs every event
2. **Check state DEFAULTS** - Each state has default events that are always present
3. **Watch for conflicts** - One event enables a state, another disables it
4. **Use state-based triggers when order matters** - Don't send multiple events simultaneously if processing order is critical
5. **Test realistically** - Include all relevant events when testing transitions

## Debugging Checklist

When a transition doesn't work as expected:
- What events are already in the current state?
- What events will the new state process?
- Could any events conflict with the desired transition?
- Are multiple events being sent simultaneously when order matters?
