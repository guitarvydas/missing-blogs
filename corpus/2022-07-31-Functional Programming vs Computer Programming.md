# 2022-07-31-Functional Programming vs Computer Programming
[Below, I use the shorthand "FP" in place of the phrase "functional programming"].

# Pure FP
- works with stacks - LIFOs not FIFOs
- uses a blocking protocol - caller blocks and waits for callee to produce a result
- hard-wires routing : the callee *must* return a result *only* to the caller

# Distributed Programming
- model: 2 rPIs connected by 2 one-way wires
- cannot work (well) with only stacks
	- it is inefficient to send whole stacks on one-way wires
- needs FIFOs for IPC (inter-process communication)
- cannot work (well) with components that take blocking into their own hands
	- DP needs a scheduler
	- DP needs to arbitrarily decide on the order of execution of components
	- the Scheduler needs to control blocking - which components to run and when
		- individual Components cannot make the decision of when to run
		- individual Components cannot make the decision of when to invoke other blocking Components (e.g. libraries)
- DP components are Communicating-State-Machines / Actors / Objects-with-state
- DP components are 0D
- DP components isolate data *and* control flow
- data isolation is called "encapsulation", but,
	- "encapsulation" (of data) is not enough
- "control flow" isolation is called "processes"
	- but, could be implemented more efficiently and more expressively, e.g. continuations
# Gearboxes Instead of Objects
Synchronous thinking leads to designs of systems where components are strongly interconnected.

Changing any component or adding new components can cause unexepected consequences elsewhere in the system.

This feature is given the name "dependency".

A system composed of truly-independent objects - 0D - would not behave this way.  Changing or adding components to a system does not change its fundamental behaviour.

# Libraries
Programmers are under the illusion that *code libraries* and *functions* provide isolation.

Clearly, this is not the case, witnessed by the number of "dependency"-handling tools that have been developed, e.g. *make*, *package managers*, etc.

*Libraries* and *functions* that use the callstack protocol, i.e. by using CALL/RETURN, are implictly synchronized and have implicit dependencies.
# Unit Testing
It is difficult to test software components because of the baggage they carry along with them, due to implicit synchronization and N0D coding practices, like hard-wiring names of callees into calling code.

# FP Models Only A Slice Of Programming
Computers have RAM (Random Access Memory).  

FP inhibits mutation, AKA RAM.
# FP Is Hard-Wired Into CPU Hardware
CALL/RETURN and the call stack (a global, mutable data structure) is hard-wired into most CPU hardware architectures.

This was not always the case.

Early CPUs did not support call stacks in hardware. (The IBM 360 BAL instruction was used instead)

# FP Is Intrinsically Synchronous
Since FP is intrinsicly stack-based, FP is synchronous.
# FP Is Designed For Single-CPU Systems
Synchronous design favours single-cpu systems, not distributed systems.

Asynchronous design *can* be done in FP, but requires jumping-through-hoops, e.g. using preemption.

The synchronous model of computing made sense in the mid-1900s, when CPUs were scarce and memory was scarce.

Today, 
- CPUs are abundant and cheap.
- Memory is abundant and cheap.

The ground-rules have changed.

Programmers should no longer be basing programming on the biases of the mid-1900s.

In fact CPUs should be named something else, e.g. DPUs, to emphasize the distributed nature of computing and to de-emphasize the mid-1900s bias towards Central computing.

Programming languages based on the synchronous model make it more-difficult-than-necessary to create distributed systems.

# Memory Recycling
Because memory was scarce in the mid-1900s, programmers evolved techniques (AKA "epicycles") for re-using and sharing memory, e.g. "garbage collection", "thread safety", etc.

Programmers continue to use those techniques today, even though CPUs and Memory are no longer scarce.
# Notation Worship
Programming languages, even in the 2020s are based on the function model.

To continue using functions, programmers have invented workarounds (AKA "epicycles"), such as "callbacks", "CPS" (re-branded "GOTO"), etc.

# F(x)
Even a simple function call, like `f(x)`, creates several hidden dependencies:
1. The callee's name is hard-wired into the caller's code.
2. The function call implies blocking behaviour - the caller must block and wait for the callee to return a result.
3. The function call hard-wires the routing protocol into the code - the callee *must* return a result to the caller.  Allowing the callee to send results elsewhere is frowned upon and given the derisive name "side effect", even if the effect is not meant to be performed on the side.  Furthermore, the routing protocol is such that exactly one result is allowed - multiple results, or zero results, are not allowed.  Programmers have worked around this problem by structuring and destructuring result data.  Likewise, with input parameters - the routing protocol allows exactly one synchronous parameter block.
4. The parameter list represents *one* datum, which might be destructured into several types of sub-data.  Even if the call syntax involves multiple parameters, e.g. `f(x,y,z)`, the effect is the same - one block of data is transferred synchronously and, maybe, destructured by the callee into several sub-types of data.  The functional routing protocol implies that the input datum must be sent in a synchronous block and that the functional component must be brought to life only at that point.  This protocol does not model the behaviour of daemons or servers or web crawlers.  Servers can accept multiple parameters at different times, i.e. asynchronous.  Daemons and web crawlers often have zero (0) parameters and run in the background, collecting data without having it sent to them.

# Conclusion FP Inhibits Distributed Programming
- FP emobodies "synchronous programming", whereas distributed programming need "asynchronous programming" and 0D
- we need a notation (AKA programming language) that uses FIFOs at the substrate levels
- we need a notation (AKA programming language) that enables 0D components
- we need a notation that fully isolates components

# Pure FP - Sector Lisp
Pure FP (Functional Programming) is embodied beautifully in [Sector Lisp](https://justine.lol/sectorlisp/).

Sector Lisp is essentially McCarthy's Lisp, with a better/smaller GC (Garbage Collector).  The Sector Lisp GC is about 40 bytes long [sic - bytes, not K, not M, not G].

Ostensibly, Sector Lisp looks like a bag of assembler tricks, but, I believe that Sector Lisp's smallness is not due only to assembler-level optimizations, but, that Sector Lisp's smallness is due to adherence to design principles at a very basic level.

For example, Sector Lisp deals *only* with FP expression and does not attempt to extend the FP paradigm beyond its "sweet spot", it is not possible to perform mutation in Sector Lisp.

# Multiple Notations
I contend that multiple notations can be used to solve a programming problem.  The FP notation is a good approximation of programming when used within its inherent constraints.  If one wishes to use mutation, one should use another notation instead of attempting to bend the FP paradigm to incorporate mutation. Mutation is, of course, inherent to computing, since computers are constructed using RAM memory (Random Access Memory can be altered and overwritten in a "random", non-sequential, manner).

There is no "one language to rule them all".

Languages, notations, elide various aspects of problem domains, making it impossible to express the problem in its entirety in a single notation.

---


## 2022-07-31-SLIDES Functional Programming vs Computer Programming

# Pure FP
- LIFOs not FIFOs
- uses a blocking protocol
- hard-wires routing
- inherently synchronous
---

# Distributed Programming
- model: 2 rPIs connected by 2 one-way wires
- it is inefficient to send whole stacks on one-way wires
- needs FIFOs for IPC (inter-process communication)
- DP components are Communicating-State-Machines / Actors / Objects-with-state
- DP components are 0D
- DP components isolate data *and* control flow

# DP Scheduler
- DP needs a scheduler
- DP needs to arbitrarily decide on the order of execution of components
- the Scheduler needs to control blocking - which components to run and when
	- individual Components cannot make the decision of when to run
	- individual Components cannot make the decision of when to invoke other blocking Components (e.g. libraries)

# 0D Is More Than Encapsulation
- data isolation is called "encapsulation", but,
	- "encapsulation" (of data) is not enough
- "control flow" isolation is called "processes"
	- but, could be implemented more efficiently and more expressively, e.g. continuations

---
# Gearboxes Instead of Objects
Synchronous thinking leads to designs of systems where components are strongly interconnected.

Changing any component or adding new components can cause unexepected consequences elsewhere in the system.

This feature is given the name "dependency".

A system composed of truly-independent objects - 0D - would not behave this way.  Changing or adding components to a system does not change its fundamental behaviour.

---

# Libraries
Programmers are under the illusion that *code libraries* and *functions* provide isolation.

Clearly, this is not the case, witnessed by the number of "dependency"-handling tools that have been developed, e.g. *make*, *package managers*, etc.

*Libraries* and *functions* that use the callstack protocol, i.e. by using CALL/RETURN, are implictly synchronized and have implicit dependencies.

---
# Unit Testing
It is difficult to test software components because of the baggage they carry along with them, due to implicit synchronization and N0D coding practices, like hard-wiring names of callees into calling code.


---
# FP Models Only A Slice Of Programming
Computers have RAM (Random Access Memory).  

FP inhibits mutation, AKA RAM.

---
# FP Is Hard-Wired Into CPU Hardware
CALL/RETURN and the call stack (a global, mutable data structure) is hard-wired into most CPU hardware architectures.

This was not always the case.

Early CPUs did not support call stacks in hardware. (The IBM 360 BAL instruction was used instead)


---
# FP Is Intrinsically Synchronous
Since FP is intrinsicly stack-based, FP is synchronous.

---
# FP Is Designed For Single-CPU Systems
Synchronous design favours single-cpu systems, not distributed systems.

Asynchronous design *can* be done in FP, but requires jumping-through-hoops, e.g. using preemption.

The synchronous model of computing made sense in the mid-1900s, when CPUs were scarce and memory was scarce.

Today, 
- CPUs are abundant and cheap.
- Memory is abundant and cheap.

The ground-rules have changed.

Programmers should no longer be basing programming on the biases of the mid-1900s.

In fact CPUs should be named something else, e.g. DPUs, to emphasize the distributed nature of computing and to de-emphasize the mid-1900s bias towards Central computing.

Programming languages based on the synchronous model make it more-difficult-than-necessary to create distributed systems.

---
# Memory Recycling
Because memory was scarce in the mid-1900s, programmers evolved techniques (AKA "epicycles") for re-using and sharing memory, e.g. "garbage collection", "thread safety", etc.

Programmers continue to use those techniques today, even though CPUs and Memory are no longer scarce.

---
# Notation Worship
Programming languages, even in the 2020s are based on the function model.

To continue using functions, programmers have invented workarounds (AKA "epicycles"), such as "callbacks", "CPS" (re-branded "GOTO"), etc.

---
# F(x)
Even a simple function call, like `f(x)`, creates several hidden dependencies:
1. The callee's name is hard-wired into the caller's code.
2. The function call implies blocking behaviour - the caller must block and wait for the callee to return a result.
3. The function call hard-wires the routing protocol into the code - the callee *must* return a result to the caller.  Allowing the callee to send results elsewhere is frowned upon and given the derisive name "side effect", even if the effect is not meant to be performed on the side.  Furthermore, the routing protocol is such that exactly one result is allowed - multiple results, or zero results, are not allowed.  Programmers have worked around this problem by structuring and destructuring result data.  Likewise, with input parameters - the routing protocol allows exactly one synchronous parameter block.
4. The parameter list represents *one* datum, which might be destructured into several types of sub-data.  Even if the call syntax involves multiple parameters, e.g. `f(x,y,z)`, the effect is the same - one block of data is transferred synchronously and, maybe, destructured by the callee into several sub-types of data.  The functional routing protocol implies that the input datum must be sent in a synchronous block and that the functional component must be brought to life only at that point.  This protocol does not model the behaviour of daemons or servers or web crawlers.  Servers can accept multiple parameters at different times, i.e. asynchronous.  Daemons and web crawlers often have zero (0) parameters and run in the background, collecting data without having it sent to them.

---

# Conclusion FP Inhibits Distributed Programming
- FP emobodies "synchronous programming", whereas distributed programming need "asynchronous programming" and 0D
- we need a notation (AKA programming language) that uses FIFOs at the substrate levels
- we need a notation (AKA programming language) that enables 0D components
- we need a notation that fully isolates components

---
# Pure FP - Sector Lisp
- Pure FP is embodied beautifully in [Sector Lisp](https://justine.lol/sectorlisp/).

- GC is about 40 bytes long.

- Sector Lisp
	- What makes it so small?
	- Is SL just a bag of assembler tricks, or, something deeper?

---
# IMO - Sector Lisp's Smallness
- Smallness due to adherence to design principles at a very basic level.

- Sector Lisp deals *only* with FP expression
	- no attempt to extend the FP paradigm beyond its "sweet spot", 
	- it is not possible to perform mutation in Sector Lisp.

---
# Multiple Notations
I contend that multiple notations can be used to solve a programming problem.  The FP notation is a good approximation of programming when used within its inherent constraints.  If one wishes to use mutation, one should use another notation instead of attempting to bend the FP paradigm to incorporate mutation. Mutation is, of course, inherent to computing, since computers are constructed using RAM memory (Random Access Memory can be altered and overwritten in a "random", non-sequential, manner).

There is no "one language to rule them all".

Languages, notations, elide various aspects of problem domains, making it impossible to express the problem in its entirety in a single notation.
