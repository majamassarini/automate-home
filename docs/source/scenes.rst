Scenes and Appliances
=====================

A scene is a snapshot of your smart devices states.
In every moment you can recall the snapshot.

Using a scene is just a quick way to put every device, belonging to the scene,
in the state you want. You are saying to the system, hey do not
touch the state of this devices, I'm using them.
This is the reason why *a scene should usually use forced events*.

.. hint::
    But it is not a good choice to use *forced events* if you are not interacting with devices.
    **It is a good choice just when you are interacting directly with them.**

Suppose that you want to turn off all your not needed *smart*
sockets when you go to bed.
You have a button which sends a *forced off* event to all of them.

Now, one of your socket, only when comes Christmas time, is used to turn
on and off your Christmas tree at sunset and sunrise.

What if you will send a *forced off* to that *socket*?
When you wake up in the morning you will find the Christmas tree off.

**You do not really need to force off your sockets. You are not using them!**
You need to say them you are going to bed.
All the sockets but the special one a :ref:`socket.presence.christmas.Appliance Appliance <socket.presence.christmas.Appliance>`,
will change their state from a *forced on state* (if someone let them on) to an *off state*
(if nobody is using them, because all of you are in bed, can be
ok to ignore a forced state).
The special socket will do the same until Christmas time will come.

Why an *all of us in bed event* is better than a *forced off event*?

 1. Because every non deterministic state machine can dynamically adjust its behaviour to the new event.

 2. And moreover, **you can understand why an appliance behaves differently from what you expect.**

Suppose you configured the system to send a *Christmas time event* starting
from December 8th. But, this year, you have not yet made your Christmas tree.
Nevertheless your socket is not turning off anymore at night and you are wondering why.
Since you can see the *socket Appliance* internal state you can see that it
received a *Christmas time event*. You now have an explanation of its
changed behaviour.


