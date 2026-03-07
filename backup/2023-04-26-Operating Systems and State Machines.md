# 2023-04-26-Operating Systems and State Machines# Operating Systems and State Machines

Operating Systems turn function-based code into State Machines, using a clumsy trick (preemption).

Most function-based code relies on CALL/RETURN and recursion and long-running loops.  This kind of code has exactly one State - a big, fat function.  Chopping such code up into smaller bits that can be digested by an operating system at timed intervals, requires the sledge-hammer approach of using *preemption*.  

Preemption interrupts  running code - using a sledge-hammer - and saves the code's State on The Stack.  When the Operating System deems that the code be allowed to consume another morsel of CPU time, the code's State is restored and then picks up where it left off, before it was surreptitiously interrupted.

This kind of trickery works OK when the code in question has only one happy-path.  This trick needs to be emblazoned with epicycles when the code has more than one happy-path.  Today's code usually has more than one happy path.  Internet, robotics, blockchain, etc., are all examples of code with more than one valid happy-path.  Military ballistics calculations are examples of code with single happy-paths.

Epicycles manifest as bloatware.  

Lo and behold, we witness bloated computer applications.  For example, to play a simple game, say Tetris, requires serious investment in a computer and paying tax to one of the operating system corporations (Microsoft, Apple).  Yes, you can play Tetris on a bloated, but, free Operating System - Linux - but, you still need to buy a full-blown computer (and, you pay for the Operating System with your own time).

States in function-based code are called "continuations".  Continuations have an ugly syntax when expressed as pure text.

I had the displeasure of debugging someone else's continuation-based code, when that someone-else used continuations to the max.  Others couldn't understand what was going on and I tried to explain.  I found it easy to understand because I could mentally map continuations onto State Machine diagrams in my head.  Function-based thinkers could not do this and remained confused.  The problem: Continuations are GOTOs with more politically-correct names.  "Structured Progamming" suggests that one convert GOTO-based code into a single happy-path thread.  In reality, there is usually more than one correct path through code, hence, not every problem can use this simplification of being reduced to a single path.  In function-based, "structured" code, all paths except one are considered to be erroneous and given the name *exception*.

## How To Solve This Dilema?

Programmers can solve this problem by removing the need for *preemption* and by chopping up code into smaller, more manageable bits.  This is something programmers already do, when they program with *continuations*.

The control flow between small bits of code can be drawn as ovals with curved arrows between them.  The control flow transitions would be triggered by small messages, called *events*.

A preemption-based operating system can be reduced to a *simple* function that metes out *tick*s to the small bits of code.  I will call that distinguished, *simple* function *The Dispatcher*.  The ticked code must promise to return to the Dispatcher "promptly".  The code must not engage in long-running loops nor endless recursion.  Anything like that would be considered to be a *bug*.

What if you need a long loop or deep recursion?  Simple. Do only a bit of computation, then send a loopback message to youself to signal that the code should be run again.

### Structured Control Flow
As it stands, control flow can be done in an ad-hoc manner that makes the code hard to understand.

The paper "GOTO Considered Harmful" suggested structuring control flow for a single happy-path using a single entry point and a single exit point.  Note that most function-based languages violate this structuring principle by allowing two exit points - `return` and `throw`.

StateCharts suggest a different structuring principle that handles several happy-paths.  StateCharts are based on the concept of State Machines.  StateCharts, also, provide an answer to the "state explosion problem".

At the most basic level, StateCharts provide for a single entry point and a single exit point, while providing transitions to other states based on incoming *event*s.  A State is visited repeatedly, once for each incoming event.  A transition, when fired, causes the underlying state machine to change states and switch to another entry point *on the next invocation*.

StateCharts restrain the state explosion problem by providing for nested states.  Essentially, a state in a state machine is described as a set of layers that represent the state's actions.  Lower layers cannot override the operation of upper layers.  If a transition in an upper layer fires, it causes all lower layers to finalize. A transition in an upper layer supercedes all transitions in lower layers.  This arrangement adds structure and abstraction to state machines.

The problem with Harel's original definition of StateCharts, is that the notation conflates hierarchical state structuring with concurrency.  Harel calls this "orthogonal states".  A state transition is allowed to refer to states in other machines.  This violates the principle of "no name calling".  

The solution to this problem is "simple" - separate hierarchical abstraction from concurrency, using two independent notations.  I use the term *HSM* when discussing hierarchical abstraction and *0D* when discussing decoupling that is a prerequisite for concurrency.  This solution requires that state machines explicitly send out their state information as messages, leaving the onus on the programmer to send state information that might be used elsewhere.  I don't have a solution for this sub-problem at this time, but, expect that it can be solved easily in the future, or, deemed to be not needed.

0D and StateCharts have another interesting property.  One can use drawware to write programs.  Programs can be written in the syntax of hybrid diagrams instead of being written using only textual syntax.

## Video
https://youtu.be/b8I_YTcLaQU
