# 2022-07-17-Notation SuitabilityA simple test for the suitability (readability) of a notation is to imagine "off-shoring" a specification written in the notation and having a suitable implementation returned.

Consider notations from other more mature disciplines, e.g.
1. electronics schematics
2. construction blueprints
3. music scores.

1 is non-textual, and, node-and-wire.  

2 is non-textual, and, diagrammatic 

3 is non-textual, and, time-varying, and, hard real-time, and, teachable to 5-year olds.

A technical diagram is a strict subset of more general visual art, like programming languages are a strict subset of more general prose.

# Programming Languages
Programming languages are IDEs for the task of programming machines.

Due to historical reasons, we have insisted on building such IDEs using only (x,y) notations based on grids of strictly non-overlapping, fixed-sized bitmaps (actually, we further restrict (x,y) to only be (line,column)) .

This kind of inside-the-box thinking has led to 
1. the Mars Pathfinder disaster, and epicycles (aka "workarounds" and "fixes") that address the symptom, but do not cure the cause
2. unstructured, GOTO-based programming (rebranded as CPS due to political correctness)
3. state machines that block (i.e. *functions* and *function-calling*)
4. stupid pet tricks that lather epicycles onto notations to address fundamental problems, like GC and "thread safety" needed due to a notation being stretched beyond its sweet spot by the requirement for mutation.

# Node-Red
Node-red falls short of the ideal of being off-shorable.

Maybe another question to ask is: do robotics hobbyists use node-red or do they use ROS or do they use something else?  

Why?

## Single-Input API
What jumps out at me as node-red's first-order deficiency is the concept that all components have exactly one input.

You cannot understand the input API of a node-red component by simply looking at the diagram.  You have to look at the underlying Javascript code (or at the wall of documentation).  The point of a notation is to give the reader a way to understand what is going on without presenting an overwhelming amount of detail.  

Using the above "test for notation suitability", one could not ship a node-red flow diagram off-shore and get it implemented.  One would have to augment the diagram/requirements with more detail.  This isn't, for example, the case with a circuit diagram containing 7404 ICs.  The circuit builder could substitute any 7404 from any manufacturer, based on the accepted pin-out of a generic 7404.  This line of reasoning becomes more tenuous as we move to VLSI chips, but, an 8086 is an 8086 regardless of which factory it comes from.

A single input also implies synchronous behaviour.  It does not prohibit asynchronousity, but it does cause one to think synchronously[^nail].

[^nail]: If all you have is a hammer, then everything looks like a nail.

The last time I looked, the idea of a single-input was hard-wired into and sprayed throughout the editor code for node-red.

# 0D vs. Synchrony
I currently believe that the most problematic aspect of our current crop of programming languages is the use of pervasive, under-the-hood synchrony.

Distributed computers - e.g. internet, blockchain, IoT, rPIs - are independent, and, asynchronous, and, their behaviour varies over time. 

I would argue that programming notation for distributed computers needs to use (x,y,t) notations instead of clay-tablet/paper-based notations such as (x,y).

*Modeling* (x,y,t) using only (x,y) notation is not good enough.

(x,y)-based notation can be used to model an *aspect* of a computer program, but, not *all aspects* of a computer program.

In analogy, electronics schematics tend to leave off the + and ground connections from drawings.  The schematic notation does not get rid of power and ground connections, the notation simply elides these details from a particular view of the circuit design.

0D means "zero dependencies".  Programming IDEs (languages) should aspire to reaching the goal of 0D[^fx].

[^fx]: Aside: `f(x)` hard-wires the dependency on `f` into the caller's code.  Referring to other components by name should be forbidden.

# Layers
I believe that software should be arranged in layers with 2 kinds of components:
1. Leaves
2. Containers.

Containers contain compositions of other components (Leaves or Containers).

Containers route messages between children[^direct] components.

[^direct]: Direct children only.  A Container can only refer to its own direct children, not grandchildren nor peers.

# Sector Lisp
The GC[^gc] invented by Tunney for Sector Lisp is 40 bytes in size [sic, bytes, not K, not M, not G].

[^gc]: GC means "Garbage Collector".

Is this smallness due only to stupid assembler pet-tricks, or, is there something else at play here?

# Bloatware
Why do we insist on crushing Raspberry PIs with bloatware such as Linux, Windows, MacOS, ROS, etc., etc. when Sector Lisp fits in less than 512 bytes?

Where is the big-O notation for comparing Sector Lisp against Linux, etc.?  

In fact, where is the big-O analysis of Linux?

Big-O is just a (another) notation.  Maybe it is simply unsuitable for analyzing Linux?

# Statecharts
Harel's Statecharts demonstrate that programming IDEs (languages) do not need to rely only on text.

Statecharts cannot be used to express every nuance in a program, but, statecharts diagrammatically express certain nuances of programs.

# Text
Text cannot be used to express every nuance in a program.

Some things make sense when expressed in textual form, e.g. mathematical equations.

Some things do not make sense when expressed in textual form, e.g. networks of distributed computers (and, libraries of software components, etc.)

# Tells

Rhetorical question: what is considered to be *difficult* in programming these days?  

Is this difficulty due to the fact that the problem is fundamentally difficult or because the notation makes it difficult to express?

Feynman invented Feynman diagrams.  The notation makes a difficult concept easier-to-express.  The notation does not express *all* of Physics, just one aspect of Physics.

I argue that one can always invent new notations to re-express any difficult concept in simpler-to-understand terms.

# Simplicity

Simplicity is "the lack of nuance".  

A good notation elides certain nuances, but, does not expunge those nuances.

Any interesting problem needs to be expressed using multiple notations. 

There can be no "one language to rule them all" for any sufficiently-interesting problem.