# 2022-06-06-Functions Procedures Libraries
---
tags:
- 20220606
---
- The notion of *functions* tangles up several concepts:
- calculators - routines that run sequentially and *always* return a result
- control flow procedures - routines that perform some work, then yield without returning a result
- synchronous library routines - chunks of code that are invoked sequentially, that are meant to be part of calculators or control flow procedures, but, have been abstracted away.  These chunks are included in the code for calculators and control flow procedures.

Further, there are:
- asynchronous components - chunks of code that have been abstracted away from calculators and procedures, but are asynchronous
- input and output APIs consisting of *ports*
- transfer data via message-sending
- messages are sent indirectly by leaving messages on output queues, then routed by the Components' immediate parent Containers (indirection enables flexibility ; indirection can be optimized away later)


## Aside - Functions Are State Machines

The entities that we call *functions* are actually 2-state state machines.

In *state 1*, functions execute code.

When a function calls a library routine or another function, the caller enters *state 2* and blocks awaiting a signal from the callee.

Function *blocking* through CALL usurps responsibility for *blocking* from the parent Operating System. 

The result is destruction of locality-of-reference.

In response to usurpation of responsibilities, Operating Systems must use seldge-hammers, called *preemption*, to regain control of blocking.

## CPS - Continuation Passing Style
CPS is the most obvious manifestation of functions-as-state-machines.

CPS implements GOTO in a supposedly functional manner.

CPS bundles up *the next state* as a first-class piece of code, called a *continuation*, then passes this *next state* to callees.  

Callees explicitly enact state change in the caller, AKA GOTO, by invoking the *continuation* passed to them as parameters.

Such spreading out of state change is another manifestation of the destruction of locality-of-reference.

CALL simply pushes a *bookmark* on the stack and the callee snaps back to the bookmark using RETURN.

With CPS, the whole of the next state is pushed onto the stack (AKA passed as a parameter).  The callee does not simply RETURN, but invokes the caller's next state explicitly.

This complication is the result of 
- using only a textual representation for programs 
- implementing all control flow transfers synchronously
- tangling invocation of library code up with runtime (libraries are typically CALLed synchronously, but, are typically thought of as asynchronous components ; this duality in thinking causes confusion and bugs)