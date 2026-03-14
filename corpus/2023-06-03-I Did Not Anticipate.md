# 2023-06-03-I Did Not Anticipate# I Did Not Anticipate

I witness this kind of thing a lot.

"... I did not anticipate ..."

I've been in Software for several decades and that seems to be one of the mantras I hear a lot.

I've been a software consultant for a long time (40-ish years).  I've skunked-worked a lot of projects.

I grew up learning Physics and EE, then backed into software (embedded software, compiler design, language design. RTOSes, etc).

I've always been puzzled as to why I could build electronic devices and feel that they were robust, but, the software that I built was always non-robust.

My current conclusion is that software is permeated with Synchronicity - a single, underlying Pattern.  Everything else, is not permeated with this Pattern.  Just about everything that Humans encounter is Isolated and Decoupled.  Humans think in terms of snapping components together, like LEGO® blocks.  

Software doesn't work like that.  Programmers *think* that they are using LEGO® blocks. but, they're not, due to hidden dependencies, promulgated by the popular programming languages that they use (Haskell, Rust, JS, Python, etc.).

Using languages and thought-patterns that emphasize *synchronicity* causes programmers to solve problems in only a single manner.  Instead of allowing the problem to dictate the solution, programmers allow *synchronicity* to dictate the solution and to couch all problems in terms of *synchronicity* whether that thought-pattern is appropriate to the problem or not.  I call this "notation worship".  If you hear someone say "I'm using a functional approach" before they have considered the ins-and-outs of the problem, then they are suffering from "notation worship".

*Synchronicity* is great for optimizing a solution.  Not all parts of a solution need to be optimized, though.  I'd guess that about 5% of any solution really needs to be optimized.  How do you know which 5% needs to be optimized?  You don't, at first.  You build the solution and make it work.  Then, you measure it and decide where the hot-spots are.

Premature optimization is a curse that slows down development.  Using a programming language - like Haskell, Rust, Python, JS, etc. - that is geared towards optimization, e.g. *synchronicity* - is a good way to slow down development, i.e. to make Development less efficient.

Sticking epicycles, like *thread* and *par* and *rendezvous* into synchronous languages, does not make them non-synchronous.

Text-based programming - we call it *code* - emphasizes the *synchronous* approach.  

Yes, CPUs are *synchronous*, but, higher level languages do not need to be synchronous.

## What's The Fix?

We have been sitting on the fix for several decades.

The fix is simple and obvious, if you are willing to think beyond synchronous programming.

We need to adopt a non-von-Neumann approach to programming.

Early attempts at breaking free from von-Neumann programming include:
- UNIX® pipelines
- FBP - Flow-based-programming
- S/SL - dataless programming language that encourages creation of software pipelines based on an extreme form of type checking (aka Pattern Matching)
- networking 
- internet, peer-to-peer, blockchain

The only remaining question is how to do this "in the small" without needing to resort to hardware assist, such as MMUs, preemption, etc.

Hardware assist is OK.  In the small might be even better.  Maybe, if programmers would be allowed to think in terms of little networks composed of little software units, they might begin to think differently about solving problems.

*Closures* - anonymous functions - have been around a long time.  We have become used to using big, honking closures that we call "processes".  Anonymous functions were introduced in 1956 (Lisp 1.5).  Processes were created as an allergic reaction to Lisp.  It seemed necessary to build closures by hand in C to alleviate the perceived problems of Lisp.  Greenspun's 10th Law all over again.

I call The Fix "0D", meaning zero dependency.  We already know how to do this - every app running in a process is 0D.  The Fix consists of using FIFOs instead of LIFOs for IPC.

0D components Send messages to one another.

The only required innovation is some sort of "Structured Message Passing" protocol, so that messages are not sent in a flat - "strongly connected" manner - but, are sent in some sort of relative, hierarchical manner.

I suggest that 0D Components come in 2 flavours
1. Leaves
2. Containers.

Leaves are what we think of as *code* today.

Containers, are recursive and might invoke leaves.  Containers can contain other Containers or Leaves.  Containers contain children Components and can refer directly, only, to their children Components.  No Component - Leaf or Container - can refer to its peers or ancestors.  Containers route messages between their Children.  Containers cannot route messages to other Components (other than their directly-contained Children).  All routing is determined by a Component's parent.  If a Component wishes to send a message to one of its siblings, it leaves the message(s) in its own output queue and lets its Parent figure out how to route the message(s).   If a Component wishes to send a message to one of its Parent's sibling, it must leave the message(s) in it output queue and allow it Parent to route the message, and its Parent's Parent to route messages that trickle upwards. The Component cannot refer to another Component - it can only leave messages in its own output queue and must rely on its Parent to route the message(s) appropriately.  The protocol makes it possible to rearrange Software Architectures by moving software Components around and by changing the routing.  The Component does not get to decide where its messages will go, only its Parent has that privilege.

This protocol is reminiscent of "dependency injection", but is more structured and less ad-hoc.

- preventions: atoms, syntax skins
- 