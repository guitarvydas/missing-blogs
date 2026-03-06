# 2023-04-22-Hierarchical State Machines# Hierarchical State Machines
HSMs (Hierarchical State Machines) are very similar to StateCharts, minus "orthogonal states" (aka concurrency with hidden coupling (state queries)).

## Diagram Elements

!![Excalidraw/2023-04-22-Hierarchical State Machines 2023-04-22 06.06.36.excalidraw.png](images/2023-04-22-Hierarchical State Machines 2023-04-22 06.06.36.excalidraw_12.png)


### Simplified Example

!![Excalidraw/2023-04-22-Hierarchical State Machines 2023-04-22 06.13.21.excalidraw.png](images/2023-04-22-Hierarchical State Machines 2023-04-22 06.13.21.excalidraw_12.png)



## State
1. name
2. entry code
3. handler code
4. exit code

!![Excalidraw/2023-04-22-Hierarchical State Machines 2023-04-22 06.14.57.excalidraw.png](images/2023-04-22-Hierarchical State Machines 2023-04-22 06.14.57.excalidraw_12.png)


!![Excalidraw/2023-04-22-Hierarchical State Machines 2023-04-22 06.18.00.excalidraw.png](images/2023-04-22-Hierarchical State Machines 2023-04-22 06.18.00.excalidraw_12.png)


A state can contain another full state machine (it's child)[^vis].

[^vis]: Should a state that contains another machine be represented differently?  For example, maybe a compound state is drawn as an ellipse with a drop-shadow or with a thicker line or with a dotted line or with a different colour?

Upon *exit*, children state machines (if any) are exited.  This happens in reverse order - deepest child first.  The parent's *exit code* is executed last.

Upon *entry*, children state machines (if any) are entered.  This happens in a top-down manner.  The parent's *entry code* is executed, then, its child machine (if any) is entered.  This happens recursively downward and stops when a state contains no children.

*Entry* is a *proc*.
*Handler* is a *proc*.
*Exit* is a *proc*.


## Transition
1. guard
2. code

!![Excalidraw/2023-04-22-Hierarchical State Machines 2023-04-22 06.37.42.excalidraw.png](images/2023-04-22-Hierarchical State Machines 2023-04-22 06.37.42.excalidraw_12.png)


A *guard* is a boolean function (aka *predicate*) that fires the transition when given conditions are met.

When the transition fires, it executes its *transition code*.

Only one transition fires.  Or no transitions fire, if no guards are true.

A more-than-type checker can check the guards for complete coverage of all input possibilities[^pm].

[^pm]: Note the similiarity to *pattern matching* in functional programming.

Only the set of transitions attached to a state are valid.  

When a state is active and revisited, the state's transition guards are checked for firing.  

At most one transition is fired.  

What happens if more than one guard is true?  Undefined.  Probably an error at runtime, or compile-time.

If no guards are *true* and the state has no child machine, nothing happens and the state machine remains in the same state.

If no guards are *true* and the state has a child machine, the guard-checking-and-firing process occurs in the child.

Note that a parent gets "first dibs" on any incoming event.  If a parent fires a transition, then its child's (if any) transitions are not checked. In other words - a *child* cannot affect the behaviour of its parent.

If a state fires a transition, the machine typically steps to a new state, causing the state to perform its exit sequence and causing the new state to perform its entry sequence.

N.B. If a transition loops back onto the same state, the state performs its exit sequence and then performs its entry sequence.  This behaviour follows from the above transition-firing rule.  

Note that a programmer can control code execution by choosing to place code on transitions or entries/exits of a state.  For example, if you want to run code only once when entering a state that has a loopback transition, leave the *entry* code empty and place the run-once code on the transition into the state.

!![Excalidraw/2023-04-22-Hierarchical State Machines 2023-04-22 06.54.11.excalidraw.png](images/2023-04-22-Hierarchical State Machines 2023-04-22 06.54.11.excalidraw_12.png)


*Guard* is a *boolean function (predicate)*.
*Transition* is a *proc*.

## Start Ball

A circle pointing to the default state of a state machine.

The arrow from the start ball to the default state can be annotated with transition code that is fired exactly once when the state machine is first entered.  This is *almost* like *entry code* on the parent state, but, provides locality of reference, e.g. to set up data that is local only to a machine (and, therefore, should not be handled by the parent machine).

## State Machine

A state machine is a collection of states and transitions between states and one start ball.

A state machine is repeatedly activated by some other routine (e.g. an *event loop* dispatcher[^psm]) that "sends events" into the state machine.

[^psm]: Or, a parent state.

An *event* is some kind of *tag* plus a lump of data (a union of all types).

When a state machine is activated, it executes the handler code in its current state (only the current state) and the machine attempts to fire a transition.

As described above, if the current state contains a child machine and no transitions are fired in the parent state, the machine attempts to (recursively) fire transitions in the child state.  This recursive process continues downward until a descendant state contains no children.

Note that, upon an input event, a parent machine might remain in its current state while some child might change its state.  The programming "power" of this paradigm is provided by this simple, subtle, nesting ability.  The classic "state explosion problem" is contained and controlled by this paradigm.

### Switch/Case Code Instead of State Machine Drawings - Commentary

It is possible to express state machines in a textual manner.

I find that drawings are easier to read and to "reason about" than linear textual code.

Function-based code can easily express 1-in, 1-out functions, but, is less suitable for expressing control-flow sequencing.

Diagrams, augmented with functional, textual code, capture the best of both worlds.  Diagrams express control flow, whereas textual functions express equations.

## Parental Authority Instead of Inheritance
Note the subtle difference between HSMs and OO.

HSMs do not allow method overriding.

This means that every diagram is stand-alone and can be understood without checking to see if ancestors change the diagram's behaviour.

This, then, allows more-understandable layering of code.

Details are elided, but not removed.  The (human) reader gets an overview of the design and can choose to dig deeper for more details, but, isn't forced to look at details all at once.

## Example - Desk Lamp
A desk lamp is controlled by two momentary switches:
1. power ON/OFF
2. intensity (LOW/MEDIUM/HIGH)

When the lamp is turned ON using the first switch, the lamp intensity can be set using the second switch.

When the lamp is first turned ON, it always lights at LOW intensity.  Subsequent pushes of the second switch cause the intensity to cycle through its three levels, looping back from HIGH to LOW on a third press.

When the lamp is turned OFF - using a second push of the first switch - the lamp turns off, regardless of which intensity it was set at.

!![Excalidraw/2023-04-22-Hierarchical State Machines 2023-04-22 07.32.26.excalidraw.png](images/2023-04-22-Hierarchical State Machines 2023-04-22 07.32.26.excalidraw_12.png)


Due to the limitations of this drawing tool...
- I've drawn the ON submachine on the same diagram. I would think that double-clicking on the ON state should open an editor containing the submachine.  This would allow both diagrams to be simpler - we wouldn't need to combine both drawings into a single diagram[^ftr].  
- I've chosen not to show code of any kind (transition, entry, handler, exit).

[^ftr]: For the record, yes, I prefer nesting instead of an infinite canvas combined with zooming in and out.  An infinite canvas evokes notions of absolute-ness, while nesting evokes notions of relative-ness.

## Concurrency vs. Synchronocity
HSMs support the construction of *synchronous* code, only.

HSMs do not support concurrency directly.  See 0D for that.

Harel's StateCharts conflate both concepts - async and sync code - into the same notation.

HSMs + 0D form a fruitful programming environment which enables creating code using async and sync paradigms and visualizing of code in both paradigms.

## Implementation
The drawings in this document were done with Excalidraw.

Excalidraw saves drawings on disk as JSON files.  Draw.io, yEd, etc. save drawings on disk as XML files.

It should be straight-forward to compile a visual language, based on the above concepts, into code using tools such as JSON, XML and SVG libraries, Ohm-JS (and PEG parsing), etc.

I've compiled draw.io diagrams to code for other purposes, using Common Lisp, e.g. as experimental 0D-ish code in https://github.com/guitarvydas/eh and https://github.com/bmfbp/bmfbp.  I've compiled yEd diagrams into code for an experimental Visual Shell in https://github.com/guitarvydas/vsh.  An example of a diagram compiler for 0D is in https://handmade.network/p/374/odin0d/.  Snap.love looks interesting, but I haven't investigated it https://git.sr.ht/~akkartik/snap.love.  None of these examples directly compile HSM diagrams, but they act as proofs of concept for doing so.

The repo https://github.com/guitarvydas/py0d/tree/feedback contains text code for HSMs and States, in Python.  This code is tangled up with experiments in 0D.

I would guess that XState contains working textual code for StateCharts (incl. orthogonal states, which can be ignored for HSMs), but, I haven't investigated.

A silent video of drawware done in LispWorks, more than a decade ago https://www.youtube.com/watch?v=8vZ8Pi32oMo shows, both, HSMs (0:19) and async components...

## See Also
XState.  Ignore orthogonal states. https://xstate.js.org

Drakon.  Rocket science. A way to draw control flow similar in intent to HSMs, but with a different visual syntax. https://drakon-editor.sourceforge.net.

Harel's StateCharts paper https://guitarvydas.github.io/2020/12/09/StateCharts.html.  Ignore orthogonal states.

Flow Based Programming (making concurrency a first-class concept) https://jpaulm.github.io/fbp/.  Coming from an EE background, I prefer to think in terms of *events* instead of *streams*.  I, also, believe that a decent UX *must* support fan-out[^fanout].

[^fanout]: Fan-out allows ellision. The complexity of a diagram can be reduced by eliding / compressing details, e.g. by collapsing multiple ports into a single port.  Fan-in is the other end of fan-out.  Fan-in is allowed by FBP and 0D.  AFAICT, FBP does not allow fan-out, while 0D does allow fan-out.  Fan-out raises the issue of data copying (which, then, leads to the need for garbage collection or other automated storage management).