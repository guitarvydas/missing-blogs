# 2022-12-13-4D Computing
Computers can be bicycles for the mind, but, this is currently discouraged by programming notation.

Notation and language affects the way you allow yourself to think.

I would say that computers are a new medium for expression in 4 dimensions x/y/z/t.

IMO, this medium has yet to be explored in depth.

Text-based functional notation, e.g. `f(x)` or `f(x,y,z)` addresses only one use-case for computers - computers as sophisticated calculators - but cannot easily express other uses of computers, e.g. sequencers (time, history), IoT, robotics, internet, blockchain, gaming, animation, etc.

Obviously, we CAN express these concepts in the current notation, but, programmers are encouraged - by exclusive use of this single notation - to think in 2D and to create calculators.

When all you've got is a single notation for describing calculators, everything looks like a calculator.

A calculator takes one input (which might look like several inputs, thanks to the miracle of destructuring) and produces one output.  The calculator model is so insufficient for expressing programs, that a bag has been added onto the side of the model, called 'exceptions'.

If you want to build YAC (Yet Another Calculator), the current notation is appropriate.  If you want to build a sequencer, switch to another notation(s).  When starting a new project, it is unneccessary to jump to the premature conclusion that the project is YAC until you've savoured all of the project's details.


Sub-question: how?  1st step - explain, break down what we have, recognize what we don't have

We have been under-utilizing computers by force-fitting a 2D notation onto the development of programs for computers.  The 2D notation was originally designed for use on clay tablets and only recently has been incrementally improved to employ the use of graphite and rubber.  In collapsing 4D down to 2D to fit the notation, it seems customary to explictly "model" the 3rd dimension and to simply discard the 4th dimension.  Although the 2D notation CAN be used to "model" all 4 dimensions, it encourages programmers to think in 2D and to ignore the pesky other dimensions.

The first 100 or so pages of Nobel Laureate Ilya Polyani's book "Order Out Of Chaos" alludes to this problem and, iirc, blames the 2D notation for setting Physics back by some 100 years.

If you examine the field of sports psychology, such as work by Dr. Gabriele Wulf, you learn that attention to detail breaks "flow" (aka "the zone") and interrupts otherwise smooth operation of brain function.  I would posit that concentrating on details, such as modeling in a force-fitted notation, qualifies as unwanted attention to detail.  Physicist Richard Feyman found it necessary to invent a notation suited to his purposes ("Feynman diagrams") when thinking about a specific problem in Physics.

As a result of using an ill-fitting notation, our use of computers is mostly limited to expressing what is easy to express in the notation, i.e. the creation of more-and-more complicated calculators, instead of fully utilizing the other dimensions of computer capabilities.  For example, when creating applications for sequencing machines (such as OBS, robotics, internet, IoT, blockchain, etc.), we are told to ignore the 4th dimension or to use assembler-level, ad-hoc libraries and epicycles, like preemption.  We CAN design sequencers using the 2D notation, but, designing calculators is much easier.

Behavior Trees (used in robotics and gaming (NPCs)) work around (aka "creates epicycles" for) the problems caused by 2D notation by creating State Machines and inserting *time* as an event called "tick".  As far as I can tell, "ticks" are artificially made to behave like synchronous clocks not by need but by habit.

Observation: `f(x)` has several flaws as a notation for programming:
- hard-wired function name `f` creates implicit dependency
- single parameters and single return values - this notation does not support multiple parameters, but, gives the impression that it does by expunging time
- ad-hoc blocking
- hard-wired routing decision.

Observation: In the notation, parameters are actually single blocks of non-homogenous data that arrive/leave at the same time, i.e. "multiple parameters" are entirely synchronous.  Blocks of data can be destructured to *appear* to contain more than one datum of different types,  but the dimension of time (t) has been silently removed from parameters, in this notation.  We all know that servers accept parameters at different times, but our notation does not allow us to express this fact easily.

Observation: In the notation, functions block in an ad-hoc manner. The caller suspends operation until the the callee produces a result.  This behaviour fights against operating systems which must, then, resort to using preemption to pull the rug out from under functions.  This effect is not seen in paper versions of the 2D notation, wherein operations take 0 time, but, is noticable in electronic versions of the notation, where every operation - including CALL/RETURN - takes a finite and measurable amount of time.

Observation: In the notation, RETURNing a value to the caller is a routing decision.  This decision is hard-wired into the hardware.  This didn't use to be the case.  Hardware used to support co-routines as being of the same importance as calls.  Early computer hardware did not have built-in support for a shared call-stack.
