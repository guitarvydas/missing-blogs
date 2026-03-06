# 2022-07-30-CPUs vs DPUs# Central vs. Distributed
CPU <- Central Processing Unit
DPU <- Distributed Processing Unit

CPU
- mid-1900s idea of computers
- CPUs were expensive and scarce
- Memory was expensive and scarce
- model: 
	- CPU is Central
	- single point of failure
	- all peripherals strongly connected to CPU, star configuration
- synchronous
- lambda
- calculators
	- computers were thought to be useful only for ballistics calculations
- ignore time (t)
	- no history
- expunge control-flow

DPU
- 2020s idea of computers
- IoT, Raspberry Pi, Blockchain, internet
- DPUs are inexpensive and abundant
- Memory is inexpensive and abundant
- model: 2 DPUs connected by 2 one-way wires
- asynchronous
- communicating state machines
- sequencers
	- process control, sequencing of machines
	- parsing -> encoding history
- deal with control-flow
# Stack vs. FIFO
- originally CPUs did not have stacks baked into the architecture (BAL instruction)
- McCarthy's Lisp Lists are stacks (LIFO)
- processes use FIFOs not LIFOs
- unit of concurrency can be made smaller
	- continuations
	- FIFOs
# FP is Stack-Oriented
- basic assumption of FP (Functional Programming) and mathematical notation
	- stacks
	- synchronous operation
	- blocking (caller waits for callee)
# Human Organizational Principles
- asynchronous
	- free will
	- interaction with other humans
- business
	- hierarchical organization
	- ORG charts
- diagrams
	- understood to mean isolated units
	- we don't have ways to draw / think-about synchronous units
- "programming" defies human intuition
	- "programming" is based on synchronous behaviour / analysis
	- epicycles
		- bugs
		- preemption
		- Mars Pathfinder disaster (priorities, priority inversion)
		- gearboxes
		- brittle operation
			- make a change "here" and something "over there" begins to fail
		- libraries 
			- based on synchronous operation
			- *look* like isolated units, but are not (due to hidden dependencies of stack-based control flow)
				- fool programmers into thinking that they are working with isolated units
# Programming is Hard
- "programming"
	- simply control a machine by whatever means necessary
- "multitasking is hard"
	- fundamentally ~10 bytes
	- Loop
		- check if need to continue
		- exec lambda
		- goto Loop
- epicycles
	- "thread safety"
		- not needed in 2 DPU model
		- based on memory sharing 
			- mid-1900s premature optimization of memory usage
			- garbage collection
				- optimize memory usage
	- preemption
		- needed by O/S (Operating Systems) to regain control of blocking
- text
	- programming is about controlling machines
	- textual programming languages are about honing character-based notations 
		- instead of concentrating on simply controlling machines by whatever means possible
	- strict grids of non-overlapping small bitmaps
	- (x,y)
		- ignore (t)
		- actually (line, offset), where (x,y) is based on character cells, not based on pixels
	- based on mid-1900s hardware capabilities
		- early hardware did not deal with pixel-base graphics well
		- hardware designs did not allow overlapping of windows
# CALL / RETURN Spaghetti
- CALL / RETURN based on Stacks, not FIFOs
- synchronous operation baked-in by hardware
- [Call Return Spaghetti](https://guitarvydas.github.io/2020/12/09/CALL-RETURN-Spaghetti.html)

# Routing Asynchronously
Components come in 2 kinds:
1. Leaf Components
2. Container Components

Components contain components, Leaf or Containers (recursive definition).

Containers contain
- collection of components
	- composition
- routing information
	- routing can only be done for direct children
		- Child to Child(ren)
	- routing from input of Container to Child(ren)
	- routing from Child output to Container output
	- edge-case - routing from input of Container to output of same Container
		- straight-through
- Components cannot Send messages to peers or other components
- Containers can Send "commands" "down" to Child(ren)
- Child(ren) can Send summary data "up" to Container
- nothing else
	- cross-talk prohibited
	- structured message-passing (down, up only)
# 0D
- zero dependency
- easy to do in existing languages with FIFOs
- `f(x)`
	- 3 kinds of dependency baked in
		1. hard-wired name of callee
		2. blocking protocol (caller waits for callee)
		3. routing is hard-wired - callee->caller only
- allows diagrams
	- diagrams are "free"
	- diagrams fit human intuition about isolation
- concurrency
	- concurrency is "free"
	- current multitasking breaks down into 2 parts:
		1. 0D - zero dependencies
			- Components are fully isolated from one another
				- data isolation (AKA "encapsulation")
				- control-flow isolation (AKA "asynchronous")
		1. sequencing
			- option: perform steps sequentially
			- option: begin steps simultaneously (optimization)
# Escaping Stack-Based Thinking
- eschew call/return
	- eschew functions (due to hardware implementation of functions)
- eschew RETURN statement
	- place outputs into FIFO output queue
		- let Parent (Container) do the routing
- deferred Send
	- Send simply places output into FIFO
	- Send does not invoke other Components (only the Parent Container can do that, via Routing)
	- Parent Container deals with Routing only when Child Component finishes a *step*
- *step*
	- do only one part of computation at a time
	- don't do complete computation at once
		- edge-case: computation is so simple that it does not need to be broken down into steps
- Eschew Loop, Recursion
- Get in, get out promptly
- equivalent to looping
	- Send feedback messages to oneself if computation needs to loop
- be explicit
	- stacks are separate components
		- not hidden / elided
- optimization
	- optimization is specific to an app
		- generalizing optimization leads to mediocrity
		- who knows how better to optimize an app?
			- General Purpose Language designer, or,
			- app-builder
	- if an app doesn't need optimization
		- why optimize at all?
	- optimize only the hot spots
		- leave everything else alone
	- GPLs are tuned for optimization
		- hide Architectural details behind a wall of detail
- static vs dynamic languages
	- static languages are optimizations of dynamic languages
	- static languages are tuned for optimizing operational details at the expense of obfuscating Architecture
- iteration on Design and Production Engineering
	- iterate
		- develop app using dynamic language
		- easy to "change your mind" - discard work and quickly replace it with imrpoved Design
			- example of bad: develop code in C for 2 years -> reluctant to adopt changes
		- Production Engineering = Optimization = Static Language
			- optimize only after-the-fact (get it working first)
			- optimize only the hot spots (profile first)
		- type checking
			- lint
			- not languge redesign
- Abstraction
	- need to lasso groups and replace with simple components
		- reduce number of ports (in and out)
	- NC - No Connection
		- need to be able to ignore features (ports in and out) that don't apply to current app
- perspective
	- program computers
	- not notation worship, notation honing
		- there is no "one language to rule them all"
		- realize limitations of any notation
			- e.g. FP is good for stack-based, no mutation calculators
				- but, FP, is less good for multitasking, distributed (non-stack-based) applications, mutation-based (RAM) applications
				- dragging FP out of its "sweet spot" has resulted in bloatware, e.g. operating systems, languages larger the SL (512 bytes)
	- user-defined data structures
		- DSLs for designing data shapes
		- not for designing control flow
		- OOP
	- syntax
		- DSLs for designing control flow
	- Orthogonal Programming Languages
		- control-flow description is orthogonal to data description
		- concept used in GCC (Fraser-Davidson peephole tech -> "everything is a Register" (until later pass))
		- concept generalized by Cordy [An Orthogonal Model For Code Generation](https://books.google.ca/books?id=X0OaMQEACAAJ&dq=bibliogroup:%22University+of+Toronto+Computer+Systems+Research+Institute+Technical+Report+CSRI%22&hl=en&sa=X&ved=2ahUKEwig1Legm8bqAhWvlHIEHYzzBYEQ6AEwBHoECAEQAQs)
		- enabled by Ohm-JS and PEG and easy-to-build syntaxes (as opposed to Language Theory approach)

# Discussion - Actors
Actors (Hewitt) are most often implemented using CALL/RETURN, hence, most implementations do not implement Actors faithfully.

Actors should be isolated, but, CALL/RETURN implementation introduces dependencies in the form of synchronous control-flow.

# Discussion - OOP, Smalltalk, Objects
OOP is most often implemented using CALL/RETURN, hence, most implementations do not implement OOP faithfully.

OOP Objects should be isolated, but, CALL/RETURN implementation introduces dependencies in the form of synchronous control-flow.

I conclude that the implementations of Smalltalk that I have seen do not implement message-passing nor encapsulation.  Or, splitting hairs, "encapsulation" must mean containment-of-data but does not include containment-of-control-flow.
