# 2022-06-24-Programming Technique - What To Do Right Now?
Notes:

How to program right now?

Complication results in bugs and gotchas.  Much complication comes from trying to do too much at the same time.  

Don't try to do Creating and Coding and Optimizing at the same time.

Programming is: "controlling a machine" by any means possible.

Coding is only 1/3 of programming.  

Optimizing is only 1/3 of programming.  

Design is only 1/3 of programming.


# Theme
The theme is: 
- [ ] apply Divide-and-Conquer to the act of Programming
	- Divide-and-Conquer need not apply only to Implementation, 
	- and, 
- [ ] apply "reuse" at a higher level 
	- steal organizational ideas from other fields
		- like Structural Engineering
		- like business Org Charts

# Steps For Programming
## Step 1:
Decide which hat you are wearing:
1. Creation / New Project / Design
2. Writing Code
3. Optimizing Existing Code

Many Software Engineers think that they are never (1) Designing.  

If you are doing (2) or (3) and you have to stop to think, then you are, in fact, doing (1) Design.

Often, parts (1), (2) and (3) are combined.  Often, the same person does all three parts.  These tasks could be done more efficiently if segregated.  Even if you cannot afford to split the tasks to different people and you have to do them all yourself, it is beneficial to *know* what you are doing.

Writing code should be a continuous process, limited only by your typing speed.  If you stop to think, then you aren't doing (2) efficiently, and, someone hasn't done (1) sufficiently.  

Stopping while Implementing (Writing Code, (2)) can be caused by:
- trying to do too much work at once
- the need for Design iteration
	- Design cannot be done in a Waterfall manner
		- you can't know everything about the design up-front
		- if you start writing code in an Optimization language (ie. any modern static language) before you know *everything* about the Design, then you are employing the Waterfall method
		- what happens if you learn something new about the Design (AKA Requirements)?
		- what happens if you change your mind?
			- Static Languages force you to make Design decisions up-front (i.e. Waterfall) and make it very "expensive" (unthinkable) to change those decisions
			- designing a new system by designing a Type System needs experimentation and iteration
				- but, most PLs force you to cast the Type System into concrete and tend to make it unimaginable to change your mind later (UX issue, where the user ("U") is a programmer)
				- e.g. early Lisps normalized *all* data structures into a single fiction (Lists), which made it easy to jigger the data structures as new facts about the Design were learned (e.g. changes to Requirements)
					- the problems with this approach were cast into concrete (Optimization, Static Languages) instead of being teased-out and researched further
					- Static Languages are Optimizations of Dynamic Languages
						- Optimization can only be done on *existing* concepts
						- Optimization rarely discovers new, more-expressive concepts
						- One can discover new concepts by *interpolating* using a rigorous model, but, not by *extrapolating* -> if you start with a model that is meant for rigorous analysis, you can only get micro-mangagement-level ideas instead of broad new ideas (Nobel laureate Ilya Prigogene estimates that mathematical modeling set Physics back by 100 years)
- OOP tried to solve this problem, by localizing object behaviour (locality of reference), but, was was turned into a Waterfall Design technique by premature optimization (jumping to Classes instead of Prototypes),
	- JavaScript has a lot of things wrong with it, but the use of Prototype Inheritance supports Design better than any language (incl. Lisp)

Stopping while doing Production Engineering (3) can be caused by:
- [ ] non-existence of "existing code" 
	- -> part (2) is incomplete, which probably means that (1) is incomplete 
	- -> need to allow for iteration and improvement
- [ ] the need to think about optimization and jigger the original Design to make it more optimizable
	- Design changes should be bubbled back to (1), like Change Orders in other fields of Engineering
	- you can't expect the Designer (1) to have thought through all of the implications of code optimization, so, Design iterations are to be expected (driven by pressure from considerations for Optmization)
	- likewise, one shouldn't expect (1) to result in Testable designs, either, so Testability-driven Design iterations are to be expected[^te], and so on for every aspect of the product (e.g. CI/CD, Maintenance, etc.).

[^te]: My first full-time job was at Mitel.  My job was to think about test jigs and to provide feedback to Designers on how to change their designs to make their designs more Testable.  The full gamut of test-engineering considerations is not generalizable, hence, test-re-engineering needs to be done on a per-project basis.  Testability, like everything else, comes in layers.  Some layers can be generalized.  Other layers cannot be generalized.

- [ ] if you are using a modern programming language while working on a new project, you are doing Design, Implementation and Optimization at the same time (not recommended)

## Step 2a- Design
- [ ] aspire to Flexibility
- [ ] RAD - Rapid Application Development
	- used to be a buzzword in the mid-1900's
	- overtaken by considerations for Optimization
		- "RAD" has fallen out of use
		- "RAD" is essentially ignored, now, in lieu of using languages designed for Optimization
- [ ] use Dynamic Languages 
	- freedom of thought
	- more expressive than Static Languages
		- Static Languages are programming languages jiggered to allow easier Optimization (only 1/3 of the problem)
## Step 2b - Coding
- 10 fingers
	- QWERTY keyboard better than piano keyboard better than stylus / mouse
	- piano keyboard requires moving hand / arm
	- mouse reduces fine motor movement of 5 fingers down to one not-so-fine motor movement of one hand / arm
		- mouse requires removing hand from QWERTY keyboard
		- emacs' "every operation bound to a keystroke" is the right idea, but, emacs tends to be presented as a wall of details, instead of being presented in a layered manner, making it hard to learn emacs.  I first learned emacs 30 years ago, but, continue to bump into new features every day.
## Step 2c - Optimization
- sweat the little details
- suggest sweeping changes to the Designer(s), e.g. as Change Orders, or, at least as conscious decisions
- transliterate Code to static languages
	- manually
	- or, automatically using something like Ohm-JS
	- currently, I believe that writing code twice is faster than trying to develop a project with only a static language 
		- actually, I favour:
			1. develop Design as a diagram (draw.io, for now)
			2. transliterate (manually) the diagram to "structured" pseudo-code
			3. write an Ohm-JS program to transpile the pseudo-code to a language-of-your-choice
				- I use my own *prep* tool to help me do this (Ohm-JS progam to help write Ohm-JS programs)
		- note to self: what are my rules for creating technical diagrams? 
			- not many new rules
			- containment
			- ports
- provenance - trail of breadcrumbs back to original Design
	- ability to recover original design by removing (switching off) optimizations
	- current PL designs inhibit "switching off" of big issues
		- [ ] big issue - synchronization
			- multi-tasking is considered to be difficult because you have to work-around unwanted synchronization first
			- multi-tasking should be O(10bytes), but has ballooned into K/M/G-bytes, because of unwanted synchronization
		- [ ] big issue - lexical scoping
			- JavaScript's "objects" are an attempt at circumventing lexical scoping (dynamic lookup instead of static lookup)
		- [ ] big issue - classes
			- instead of prototype-based inheritance
				- Prototype-base inheritance = Dynamic, Class-based inheritance = Static
			- "classes" are an Optimization of prototype-based inheritance (classes are optimized for Compile-Time)
			- Prototype-based inheritance is good for Design, whereas Class-based inheritance is good for Production Engineering
- remove indirection (for Production Engineering)
- profile, optimize only what is necessary, ignore the rest
	- leave the Design alone, except where needed, leave Dynamic code be Dynamic, except where necessary
	- -> do we need a hybrid Dynamic+Static language?  Embedded languages?  Sector Lisp? APE?
# Code Flexibility
- [ ] use "threads"
	- use closures instead of threads
- [ ] deferred output, routing done by parent not by child
	- very important
	- no hard-coded assumptions in child code
	- eschew calling functions by name
		- hard-coded names -> dependencies
		- dependencies -> epicycles, tight-coupling
- [ ] unrestrained output destination
	- no restriction re. the idea of returning a value *only* to the caller
	- simple example: server code that includes logging calls - results go to requestor, and, logging goes to dev
		-  a function can produce only one result, but, logging produces 2 results 
		- one of the results is, derisively, called a "side-effect" 
			- it's only a "side effect" if you want to optimize it away, otherwise it is a valid effect
- [ ] do not hard-wire names into code 
	- C has `(*f)(...)`, 
	- ports are better
	- /bin/sh creates "everything-is-a-file" fiction, e.g. stdin+stdout+stderr+FDs 
		- -> normalized access
		- normalization -> less code
	- DLLs attempt to break hard-wiring using load-time indirection, but DLLs solve only 50% of the problem by assuming hard-wired CALL/RETURN protocol instead of one-way SEND protocol
- [ ] output parameter-list (AKA output ports)
- [ ] normalize
	-  try to make "everything the same"
	- normalization -> less code
	- normalization -> easier code generation
- [ ] message passing instead of recursion
- [ ] eschew Loops (and recursion) 
	- these don't make sense in a distributed environment anyway
- [ ] switch notations
	- example: basic multitasking is O(10 bytes), yet, WIndows/MacOS/Linux bloats this concept into O(100,000 bytes)
	- example: Sector Lisp is O(512 bytes), yet, Python is O(100,000 bytes)
		- original FP is simple, but, if you force it to do something that it is not designed for (e.g. mutation), you get bloatware
- [ ] Orthogonal Code - operations vs. operands 
	- *operands* are OO objects
	- *operations* are "the rest" of control flow
		- some camps profess that *all* control flow should be wrapped as objects
		- but we're not there yet, we only know how to wrap a limited set of control flow, e.g. how to wrap conditional evaluation, but not how to wrap sequencing (my gut says "Harel Statecharts" for sequencing)
		- operands are encapsulated, e.g. by OO, but operations (control-flow) tend to be less-encapsulated (needing blunder-buss, bloatware approaches like *processes* and *multi-tasking*)
	- Cordy's thesis - Orthogonal Code Generator [thesis](https://books.google.ca/books/about/An_Orthogonal_Model_for_Code_Generation.html?id=X0OaMQEACAAJ&redir_esc=y)
		- Fraser/Davidson paper [researchgate](https://www.researchgate.net/publication/220404697_The_Design_and_Application_of_a_Retargetable_Peephole_Optimizer) used in GCC is a subset of OCG ideas
		- OCG was originally intended for Assembler, but is applicable to programming languages when used with Ohm-JS
# Code Inflexibility
- [ ] most modern programming languages produce inflexible code
- [ ] function-based code results in inflexible code
	- names of called functions are hard-wired into the code, requiring epicycles like DLLs
	- DLLs solve only 50% of the problem 
		- CALL in DLLs is indirect, but, 
		- RETURN in DLLs still uses a global variable, and, 
			- is constrained to providing a result to only one place defined by the caller not the callee
	- CALL/RETURN is a state machine 
		- includes a "blocked, waiting for return" state
		- thwarts belief that operating systems control blocked-ness
		- -> epicycles to work around (implicit) blocked state -> bloatware 
- [ ] aspire to 0D (zero dependency)
	- eschew use of tools that paper-over dependency issues
	- eschew use of packages
	- eschew use of package managers
	- eschew use of *make*

# Efficiency
"Efficiency" is in the eye of the beholder.

## Design-Phase Efficiency
Emphasize turn-around time during Design phase.

REPLs.
- iterative development of Design.

OK to burn CPU cycles on souped-up dev machine.

Big-O consideration doesn't matter during Design phase.

What matters is if the turn-around time is "fast enough" on a dev machine.

### Bret Victor
I think that Bret Victor's message breaks down to:
1. programs are technical scripts that don't need to be expressed using only text
2. use REPLs

Graphics, technical graphics, are programming scripts.   Text-based programming languages can be supplanted by hybrid languages that employ graphics, overlapping cells, and text[^text].

[^text]: Whereas text-based code consists of grids of non-overlapping cells of small bitmaps (AKA characters).

Sliders are REPLs for non-textual programs.

## Production Engineering - Efficiency
Production Engineering emphasizes low-cost to end-user.

Smallness, or speed, or combination of both.

Production Engineering -> cheapest machine that can be used, e.g. rPI, xbox, instead of expensive laptop.

Smallness, speed on rPI - it is ludicrous to use Linux for a small app on a small machine.  Removing Linux will result in smaller size and faster operation, but, will need extra Production Engineering time.

Big-O matters.

But, using modern programming languages, e.g. Python, Rust, you cannot calculate through-put of a software function because of dependencies.  
- Gedanken examples of conundrum: 
	- Q: What are the through-put specs for your favourite O/S - Linux, Windows, MacOS?  
	- Q: If you write an app, how fast will it run, what is its through-put?
# Step 0 - Simplify Using 0D
Use `Send()` instead of calling functions.

Easy to implement.

Create a list of deferred messages, let parent component route the messages

`self.send (sender, port, data, trail)`

- sender: object ref to sender of message (usually *self* (but might be different for tester code))
- port: string, name of message tag (AKA pin-name on hardware ICs)
- data: anything
- trail: list of previous messages (for debugging, tracing (tracer bullets), one list for every message, instead of one list for all messages, provenance)