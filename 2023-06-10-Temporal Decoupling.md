# 2023-06-10-Temporal Decoupling
## Time in Functional Programming
- implicit
- notation eschews notion of time
- sequencing is hidden / elided
	- statements (lines of code) are ordered top-to-bottom
	- all arguments to a function must be evaluated before the function is invoked
		- order of argument evaluation is not defined, but, the requirement for evaluation of *all* args prior to a function call is strictly defined
		- leads to epicycles like *promises* - *promises* are args that are evaluated, but, result in units of deferred evaluation
- functions involve ad-hoc *blocking*
	- caller blocks until callee returns
	- leads to epicycle: operating systems must use *preemption* to gain control of blocking
	- how deeply nested is the *blocking*? - cannot know
- for other use-cases, you need to "model" time in some manner
- functional notation **fits** building of calculators - 1 input, 1 output
	- e.g. ballistics calculation for military purposes
- functional notation **does not fit** other possible uses of "computers" (Programmable Electronic Machines)
	- `0` inputs 
	- `0` outputs
	- `> 1` inputs
	- `> 1` outputs
- "multiple inputs" is a fiction
	- a function has *exactly one* input
	- the input can be destructured into multiple slots denoted by different types
- "multiple outputs" is a fiction
	- a function has *exactly one* output
	- *see above - multiple inputs*
- assumption - functions take zero (0) time to run
	- propagation delay is ignored
	- this is a convenient *simplifying assumption* for mathematical notation written on paper
	- this is an *unsuitable assumption* for real Programmable Electronic Machines
		- real machines perform *steps* that have non-zero propagation delay (e.g. *opcodes*)
		- functional notation leads to accidental complexities and epicycles when trying to describe machines that have non-zero propagation delays at their core
## Time in Component-Based Programming
- sequencing
	- ordering is explicit
		- e.g. "flows" in FBP drawn as lines
		- e.g. "arrows" in box-and-arrow drawings
		- ordering is defined by the software architect, not the programming language (notation, "SCN")
	- `0` inputs
		- e.g. daemons
	- `0` outputs
		- e.g. printing
			- an input causes an action but no useful return value
		- e.g. buffering operations (an input does not imply an output) (not strictly 0-output, but, not 1:1 in:out)
	- `> 1` inputs
		- e.g. classic Collator problem in FBP
	- `> 1` outputs 
		- more than one *happy path*
		- e.g. internet 
			- inability to deliver data via one route is *not* an exception
			- dealing with multiple routes is but part of the requirements
		- e.g. robotics
			- a single intent may lead to triggering of several asynchronous operations
			- e.g. to grasp a door-knob requires
				- ensure that the robot is near-enough to the doorknob, ask the robot to move closer if necessary
				- move arm towards doorknob
					- move arm at shoulder joint
					- move forearm at elbow joint to compensate for shoulder movement while leaving hand in position for grasping
					- move fingers in grasping motion
					- move joints in each finger,
						- say 3 joints in each finger 
				- summary: "put hand on doorknob" involves several simultaneous commands
					- move robot, if necessary
					- move arm
					- grasp fingers
						- nested operation (grasping one finger results in 3 commands (one for each knuckle))
					- etc.
		- e.g. human physiology
			- autonomous system controls some 500 sub-components, all asynchronous and non-conscious
		- exceptions are not exceptional
			- so-called *exceptions* are simply data, nothing special
			- we see the concept of *exceptions* leaking out of functional notation...
				- in the form of *return codes*
				- in the form of *multiple return values* 
					- a multiple return value is actually a structure containing more than one piece of information, then destructured into multiple pieces of information with distinct sub-types

## Temporal Decoupling
Because PEMs (Programmable Electronic Machines, colloquially called "computers") have non-zero propagation delays, the program units must be evaluated in some sort of order.

If the *order* (*sequencing*) is tied to other program units, the units are *temporally coupled*.

To maximize the ability for Software Architects to shuffle program units around in a design, e.g. Christopher Alexander-like *patterns*, the units must be fully isolated - decoupled from one another.  Corollary: you can't move program units around if they are coupled, they can only be moved around in larger wholes.

To fully decouple units of code, one must break all connections between units of code, textual and temporal.  

Temporal decoupling means that units of code can be arranged in any order for evaluation.  Currently popular programming languages, like Haskell, Rust, Python, etc. define a single, strict order of evaluation (sequential, synchronous) and must rely on certain coding restrictions, for example lack of side-effects.  These restrictions encourage a certain style of programming while discouraging other styles of programming.

Temporally decoupled units of code *can* have *side-effects* and *state* and *control flow*, as long as the *side-effects* and *state* and *control flow* do not leak out beyond the boundaries of the code units.  

Component-based technologies, like FBP, encourage decoupling through the simple addition of input *and* output ports on the code units.

Full decoupling - textual and temporal - is accomplished by guaranteeing that *all* inter-component communication and data flow are done *only* through ports.

When code units are fully decoupled - textually and temporally - they can be treated as *black boxes*.  It no longer matters what happens on the inside of code units, as long as nothing leaks out beyond the boundaries of the code units.

## State Is Not Bad
State, in itself, is not bad.  It is a fact of life.  CPUs inherently have state (registers, RAM).

Ad-hoc use of state is bad.

State that leaks information into other components is bad.

Use of state can be elided through the use of isolation and nesting.  Encapsulation, as espoused by OO, is a weaker form of isolation.

The use of input and output ports and the restriction that all data must flow through ports is a way to accomplish isolation and nesting.

State is often used to implement ad-hoc control flows.  It is bad to allow such ad-hoc implementations to cross-couple with other code units.  If such state is fully isolated, we don't care how it is used.

## Control Flow Is Not Bad
Control flow, in itself, is not bad.  It is a fact of life.  

CPUs inherently have control flow.  CPUs are designed to execute instructions (aka *opcodes*) in a sequential manner, with propagation delays.

Note that this does not mean that all higher level programming languages must be sequential in nature, only that they must produce scripts of sequential operations.

## Side-Effects Are Not Bad
Side-effects, in themselves, are not bad. They are a fact of life.  

CPUs inherently have side-effects, in the form of mutation of registers and mutation of RAM.

## Sequencing, Control Flow
Sequencers are ordered steps of programming, e.g.
1. do this step first
2. then, do this step second
3. then, do this step third
4. etc.

Functional notation does involve sequencing of steps, *but*, elides the concept and *restricts* the ways in which architects can control sequencing.  For example, a function may contain a sequence of lines of code ordered in a top-to-bottom manner.  Any call to any other function immediately pauses the sequence and waits for the other function to return a value, before resuming the sequence.  This is *blocking* - implicit and ad-hoc.

Note that *relational programming* languages do not imply sequencing.  The program is expressed as a set of *relations* which must be satisfied, but, the actual sequencing of the evaluation of such operations is determined by the relational engine, not by the software architect nor by the notation.

## Nesting
Further to simplifying temporal decoupling, one wants a way to *nest* and *elide* sequencing in a *relative* manner.  Nesting - without any information leakage - allows treating program units as *black boxes*.  Currently-popular programming languages, based on *functions* and on the *CALL* and *RETURN* opcodes of PEMs - e.g. Haskell, Python, Rust, etc. - tend to leak information / knowledge-of-details, and, thus, discourage the creation of program units as *black boxes*.  Programmers *believe* in a fiction, i.e. that code libraries are *black boxes*, but, libraries leak details, e.g. calling a function by name is a detail leak. The name of a called function is itself is an absolute - as opposed to relative - piece of information.  Attempts at addressing this kind of leakage have been done through the use of epicycles such as *packages*.

The general concept of *nesting* is apparent with Russian Dolls and peeling successive skins from onions.
!![300](Russian_Dolls_12.jpg)

!![300](Open_onion_(303892944)_12.jpg)

## Reality
CPU designs are based on sequencing of steps - sequencing of scripts of opcodes.  

It is necessary to acknowledge and deal with this reality.  

It is *not* necessary to build languages that follow this pattern of deep, low-level sequencing.  

Examples of languages that eschew implicit sequencing include:
		- e.g. Relational Languages
		- e.g. FBP
		- e.g. UNIX pipelines

Examples of problems that require non-sequential ordering of operations:
	- windowing systems
	- mouse (computer mouse) movement and clicking
	- GUIs.

## Appendix - Attributions
### Russian Dolls
https://commons.wikimedia.org/wiki/File:Russian_Dolls.jpg
https://upload.wikimedia.org/wikipedia/commons/0/0a/Russian_Dolls.jpg
Lachlan Fearnley, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons
### Onion Layers
https://commons.wikimedia.org/wiki/File:Open_onion_(303892944).jpg
https://upload.wikimedia.org/wikipedia/commons/d/d0/Open_onion_%28303892944%29.jpg
darwin Bell from San Francisco, USA, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons