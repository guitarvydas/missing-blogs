# 2023-08-08-Two Dimensions of Program Composition
!![Excalidraw/2023-08-08-Two Dimensions of Program Composition 2023-08-08 06.57.56.excalidraw.svg](images/2023-08-08-Two Dimensions of Program Composition 2023-08-08 06.57.56.excalidraw_24.svg)


The notion of ISA is too restrictive in my opinion. https://en.wikipedia.org/wiki/Instruction_set_architecture

I think that there are two (2) main dimensions for building programmable electronic machines, also known as *computers*.

1. Vertical - Composing single-threaded PEMs using ideas like function-based composition. Functions do not treat *time*[^time] as a first-class entity, hence, cannot (easily) describe the full range of capabilities of PEMs (*computers*).  CALL and RETurn instructions in CPUs were *not* invented to support functions.  These instructions were invented for reducing code size by sharing code.  Often, these instructions are implemented using a single, shared, hardware-supported, global variable named the *callstack*.  Extrapolating *function-based composition* to cover multiple-threading is *possible*, but, makes thinking about such multi-CPU architectures more difficult than necessary.
2. Horizontal - I believe that multi-threaded PEMs can be more easily described using the notion of multiple, isolated (single-threaded) computing units, strung together via pipelines, hierarchies, etc. using ideas such as *Structured Message Passing*[^smp].  In 2023, the horizontal composition of PEMs is easily possible using cheap devices such as Arduinos, Raspberry PIs.  Note that the internet is but a network of PEMs sending messages to each other.

[^time]: Often, time manifests itself in program units as *control flow* and *propagation delays* and *ordering*.

[^smp]: Structured Message Passing is simply Message Passing with some sort of structure imposed upon it to make it less flat and less strongly-connected.  I favour an Org-Chart approach (requests flow down, summaries bubble back up, nothing is allowed to flow sideways).

The notions of sharing memory and sharing computing power are anathema to the idea of composing Programmable Electronic Machines using loosely-coupled devices.

The idea of function-based programming languages is deeply ingrained in programmers' minds.  In fact, most programmers find it unnerving to look at and to try to understand PROLOG programs.  PROLOG code *looks* like it is function-based, but contains operations on the left-hand side of the `:=` sign.  This is not a function-based notion, thus, appears foreign and alien to most programmers.

We have become accustomed to using the term "computer" to represent electronic machines that are programmable.  The term "computer" comes from biased thinking about what electronic machines would be used for and arose in the early days of exploration about such machines.  The original idea was that electronic machines could only be used for creating fancy calculators, e.g. ballistics calculators for military ordnance.  Since then, we've discovered that electronic machines can be used for many other interesting purposes, including time-based sequencing of processes, e.g. iMovie, DAWs, process control, robotics.  Yet, the name "computer" has stuck and hasn't been upgraded since its bias-based invention.

I will try to use the term "PEM" instead of "computer" to remind ourselves that we are actually interested in programming electronic machines for many different purposes.

## Multicore

I would characterize the notion of *multicore* computers to be a tortured extrapolation of program composition in the vertical dimension, i.e. single-threaded thinking stretched beyond its comfort zone to cover multi-threaded ideas.

## Thread Libraries

The fact that *thread libraries* even exist is a dead giveaway that multi-threading is an after-thought in function-based thinking.

## Fresher Ideas

Ideas that seem more fruitful in the multi-threaded dimension might be:
- loosely coupled collections of small, Arduino-like machines
- the Green Array https://www.greenarraychips.com [^sharing]
- Dave Ackley's Robust-First Computing and T2 Tiles projects https://www.youtube.com/playlist?list=PLm5k2NUmpIP-4ekppm6JoAqZ1BLXZOztE , https://t2tile.com
- Actor-like technology (admittedly, I know of no implementation of Actors that isn't corrupted by function-based thinking and implementation).

[^sharing]: Do Green Array computing units share memory?  This would be a *vertical*-only approach.  A *horizontal* approach would be to fully isolate each computing unit with its own (hidden) memory.  I haven't looked into this aspect yet.  In fact, what we call *CPU registers* is really the notion of small, isolated, really-fast, local, isolated memory completely owned by CPUs.

## Drawware

My own preference for addressing the notion of programming computers (which is not the same as writing *code*) is to work on ways to draw programs as diagrams and to convert such diagrams into executable scripts (aka "programs") for computing units.

## 0D

I believe that the "breakthrough technology" for addressing the *horizontal dimension* of PEM composition is the notion of 0D - zero dependency.

The goal of 0D is to snip *all* dependencies between program units.  This includes 
- data dependencies
- control flow dependencies.

Programmers are accustomed to thinking about *encapsulating* data dependencies only, using ideas such as Lambdas, OO, etc.

We've already witnessed control flow *isolation* in technologies like operating systems, e.g. UNIX.  This form of encapsulation is heavy-weight, needs extra code and often uses hardware-assist (MMUs, preemption, etc.).  This kind of isolation is usually conflated with the notion of operating systems and the technology has not leaked back into Programming Language design.

0D is a trivial concept.  It implies the use of FIFOs instead of LIFOs for organizing communications between program units.  FIFOs are queues, LIFOs are stacks (lists).  Most modern programming languages make it very easy to write Queue classes, so, there are no fundamental roadblocks to the use of 0D ideas.

Note that CALL and RET on CPUs (ISA) implement stack-based (LIFO) program construction, but, do not provide hardware-assist for queue-based (FIFO) program construction.  Many so-called general purpose programming languages implement functions using CALL and RET instructions.  Functions in such languages are LIFO-only and subtly, but forcefully, encourage programmers to solve all programming problems using only single-threaded thinking.  This kind of thinking leads to work-arounds like the notion of operating systems, preemption, thread libraries, dependency injection, etc., etc. 

Rob Pike seems to be alluding to 0D in his talk https://www.google.com/search?client=safari&rls=en&q=rob+pike+concurrency+is+not+parallelism&ie=UTF-8&oe=UTF-8.

## Programming Languages

Textual programming languages are but cave-man IDEs for programming PEMs.  The notion of PLs[^pl] was invented in the 1950s and hasn't really been improved upon since then.  Interpolations of these ideas have come in the form of CFGs[^cfg].  A break-through technology for dealing with textual PLs was the invention of PEG[^peg].

[^pl]: PL ≡ Programming Language (usually textual)

[^peg]: PEG ≡ Parsing Expression Grammars.  PEG allows parsing matched brackets, while CFG and REGEX do not allow this kind of matching.  This simple change - parsing matched bookends - allows for a completely different style of thinking.  For example, layering and mini-DSLs (SCNs[^scn]) become easy to imagine.

[^cfg]: CFG ≡ Context Free Grammar

[^scn]: SCN ≡ Solution Centric Notation

## DPUs vs CPUs

The term "CPU" mean "Central Processing Unit".

I believe that a real Computer Science should be concerned with DPUs - "Distributed Processing Units" - instead of only being concerned with CPUs (and ISA).

Comput*ing* Science might be concerned with only CPUs.  Our present, commonly accepted use of the word *computer*, though, implies more than just comput*ing*.

## Layers

There is no fundamental need to express programs as flat, synchronous blobs of text.

The concept of *divide and conquer* would be better served by programs that are built in layers.

The language Lisp - loved by some, hated by many - uses a textual representation of layered programs.  Programs are composed of *atoms* or of *lists*.  *Lists* are recursive - they can contain other *lists* or other *atoms*.  *List* are nested and layered, like Russian Dolls.

Lisp programs are *list*s, not text.

0D uses a similar structure
1. Leaf components
2. Container components.

Container components are recursive, like Lisp *lists*.

## Deja Vu All Over Again 
Note that programming based on lambda calculus is headed in the direction of recursive layers, too.

And, the emphasis on *pattern matching* is, well, just *parsing* (see PEG, above).

The ideal would be to program using only text-rewriting.  Many of the "rules" of FP (Functional Programming)[^fp] have been put in place to allow this kind of rewriting.  Syntax-driven translation and compilation preceded this notion as early as the 1970s.

[^fp]: FP rules such as "assign once", "no side effects", "closures", etc.