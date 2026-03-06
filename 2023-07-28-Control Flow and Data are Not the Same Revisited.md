# 2023-07-28-Control Flow and Data are Not the Same Revisited*[unfinished]*

# Control Flow and Data are *Not* the Same
This note is an extension of a previous article https://publish.obsidian.md/programmingsimplicity/2023-07-23-Control+Flow+and+Data+are+*Not*+the+Same.

I try to clarify the purpose of the previous article.

The article describes two things, 
1. the problem, and, 
2. one possible solution to the problem.

The problem is that control flow and data are not the same kinds of things.  

Data is piece of one-dimensional memory
1. a Cell in memory,

Control flow has two dimensions:
1. A set of Cells in memory
2. What do with those Cells.  How to treat the Cell contents as coded operations and how to step through the Cells sequentially.

Current function-based thinking is trying to force us into treating control flow as data.  This idea treats only one aspect of control flow, leaving the other aspect to be handled in an ad-hoc manner.  Functions deal with Cells in memory - what their type is, how to bind them to human-readable names or stack-based offsets[^debruijn], how to mutate their contents. Control flow does not contain only one Cell.  Control flow contains an ordered sequence of Cells - a *list* of Cells. Control flow is concerned with how to interpret the contents of the cells as operation codes, sequentially.  Interpretation of a cell needs a finite amount of time, before the next cell can be interpreted.  This is called "propagation delay".

Functional notation tends to ignore propagation delay.  In functional notation, propagation delay is not a first class entity, and must be modelled explicitly as a second-class entity.  Ignoring propagation delay is a valid way to treat a certain class of problems but it's not a valid way to treat *all* problems and it's certainly not a way to treat the science of how electronic machines work.

For example 
```
function g (a) : a + 2
function f (b) : b + 7
f (g (x))
```

in functional notation, the third line can be replaced by
```
(a + 2) + 7
```

whereas in a more sequential notation that takes propagation delay into account, the third line is:
```
block (block alloc(temp1) temp1:=calculate(a+2) unblock) alloc(temp0) temp0=(temp1+7) free(temp1) unblock
```
My eyes say that the functional notation is less verbose when we want to calculate the value of a function, whereas the second sequential notation is more accurate with regards as to what's really going on inside an electronic machine.

[^debruijn]: Debruijn indexing assigns numeric names to Cells.  The names change depending on the position of Cells in the callstack.

A solution is to use entirely isolated components.  Isolation is *more* than encapsulation. *Encapsulation* encapsulates only data, but, *isolation* encapsulates both data and control flow. For example, *isolation* is embodied as *processes* in operating systems.  *Encapsulation* is employed by Smalltalk, and, applies only to data.  Control flow in Smalltalk is done using ad-hoc parsing, resulting in a minimalistic Smalltalk syntax

Full-blown *isolation* allows for the use of many specialized languages.  I call them SCNs.

It is vital to describe solutions to problems using many SCNs.  This is Divide-and-Conquer.  Divide the problem up into many sub-problems, then, solve each sub-problem in the best way possible using a specialized SCN for each sub-problem.

---

##  The Fallacy of Conflating Control Flow and Data
Attempts to treat control flow as data leads to ad-hoc interpretation of data.

For example, we see variations on skimpy parsers in early languages like BASIC and Smalltalk and Forth.  More modern languages simply hide their ad-hoc control flow underneath layers of complication.  

These skimpy kinds of parsers use operations that should be reserved for data manipulation to encode search and sequencing and state machines.  *COND* was meant to be a conditional filter/evaluator for functions, but, it has been extended to *IF...THEN...ELSE* and is used in conjunction with data to implement state machines (parsers are state machines).  State machines should be implemented using specialized DSLs (like BNF and PEG) instead of being hacked together in ad-hoc ways.  This practice has led to edicts such as "state is bad" and "assign-once" and "imperative code is bad" as band-aids instead of developing solutions to the deeper problem of misusing conditional evaluation and stateful variables.

Note that all of the above forbidden strategies are simply facts of Reality.  They are neither good nor bad, but, making edicts against their use ignores Reality and avoids creating a true Science of Electronic Machines:
- computers have State
- computers execute code in an imperative manner (step-wise, sequential, ordered, time-based)
- computers can mutate the same memory location more than once.

Note that *functional notation* can be used to express some of these ideas, i.e. Denotational Semantics succeeds in doing this, but, FP (functional programming) attempts to avoid these issues by banning their use.  I believe that it is less expensive and more expressive to create different mini-DSLs (I call them SCNs) for each of these ideas and to plumb such disparate SCNs  together to form a whole solution, instead of trying to express the whole solution using only one language / DSL.

---
## Bloatware
I observe that present-day software technique generate bloated applications.
## Fallacy of Complexity
- Complexity is not a problem, it's a challenge
- Everything is complicated
	- The challenge is 
		- to figure out how something works, and, then, 
		- to explain how it works, in a *simple* way
	- the choice of what to figure out what is essentially ad hoc - you pick some thing to figure out based on your own preferences
## Divide and Conquer
*[TBD]*
## Atomicity
In general, fan-out must be handled atomically.  The same message must be inserted into all destination queues "at the same time" without allowing interleaving of other messages.

A cheap way to do this is to describe each connection in a single-sender and single-receiver manner, BUT, *all* connections must be tried - atomically - for this to work.

## Passing Control Flow Objects in Messages
*[TBD]*
- I hadn't actually thought about this in this way.
- I think of "control flow" objects as isolated Arduinos that contain private, non-shareable memory.  Lifting that model up into software, instead of hardware, makes it possible to think about passing these things around in a first-class manner.  I haven't thought of what the implications of that might be...

# See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity (see blogs that begin with a date 202x-xx-xx-)
- https://guitarvydas.github.io/ (up to about mid-2022)
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
WIP - leanpub'ed (leanpub encourages publishing books before they are finalized)
https://leanpub.com/u/paul-tarvydas
### Discord
https://discord.gg/Jjx62ypR
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice needed)