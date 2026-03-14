# 2023-07-31-Race Conditions
# Race Conditions

There is actually only one (1) Race Condition.

Race Conditions are caused by limitations in our hardware's ability to detect timing of events.

## Obvious Non-Race
![](images/2023-07-31-Race%20Conditions%202023-08-01%2019.16.51.excalidraw.svg)


Clearly, we can tell that B arrived before A.

Because 1 second is a looong time and our hardware can differentiate events that happen at that time scale.

## Not-So Obvious

!
![](images/2023-07-31-Race%20Conditions%202023-08-01%2019.27.39.excalidraw.svg)

Did A come before B or did B come before A???  

We can't tell.  Our hardware is not good enough to tell the difference at this tiny time-scale.

## The Solution - A Simple State Machine

- If our hardware says that A arrived before B, we expect to see a B next, then we hold A in a buffer and for a B.

- If our hardware says that B arrived before A, we expect to see a A next, then we hold B in a buffer and wait for an A.

- In case *waiting-for-B*, if we see what we expect - an A - then, we save it and produce output using the saved A and B.
- In case *waiting-for-A*, if we see what we expect - a B - then, we save it and produce output using the saved A and B
- In all other cases, we error out.


### Error

- if we see an A, then we expect a B.  If we get another A, then *error*.
- if we see a B, then we expect an A.  If we get another B, then *error*.

