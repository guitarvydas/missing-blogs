# 2022-08-21-Eh Pluggable Software Components
# ė - Goal and Overview

The goal of this project is to program computers using pluggable units of software.

To do this we need:
- micro-concurrency
- 0D
- layers, relative sofware units
- multiple languages.

## Hello World 
Very simple example
## Leaf
![hello world eh-Leaf.png](images/hello world eh-Leaf.png)

## Container
![400](images/hello world eh-helloworld.png) 

## Re-Architecting
![400](images/hello world eh-helloworldworld.png)

# Benefits
- technical drawings come "for free"
- concurrency comes "for free"
- "build and forget" development
- distributed programming comes "for free"
- multiple-CPU paradigm
- ability to plug together software components to create mimimal set of functionality, instead of using an all-in-one behemoth operating system

further discussion...
## Eh - Benefits

# Benfits of ė
- anti-bloatware
	- a major source of bloat is special-case code needed to handle out-of-sweet-spot use-cases
		- for example, FP works well if mutation is prohibited
			- mutation added to any programming language that uses functions results in epicycles
				- "epicycle" ≣ "workaround"
				- e.g. "thread safety"
				- e.g. heaps and "garbage collection" for heaps
				- e.g. Mars Pathfinder disaster ("priority inversion")
- technical drawings come "for free"
- concurrency comes "for free"
- "build and forget" development
	- adding new software cannot change existing software
		- not true with state-of-the-art libraries
			- changing something "here" might cause something "over there" to operate differently
- distributed programming comes "for free"
	- blockchain
	- internet
	- robotics
	- games using [NPCs](https://en.wikipedia.org/wiki/Non-player_character)
- multiple-CPU paradigm
	- existing techniques are based on a single-CPU paradigm, prevalent in 1950's thinking
- ability to plug together software components to create mimimal set of functionality
	- no need for all-in-one operating systems
# Usage
*make*

This runs *run.bash* which runs a single 0D Leaf component *echo.py* and prints its output queue at the command-line.

*Test.py* invokes *hello.py* and feeds it a trigger message (True).

Then *test.py* invokes *world.py* and feeds it the above output.

*World.py* is almost like *hello.py* except that *hello.py* does not echo its input whereas *world.py* does echo its input.  *World.py* emits 2 outputs for each input it receives.

Both components - *hello.py* and *world.py* send outputs to their respective output queues.

The final result is:
1. *hello.py* outputs ['hello'] on output port 'stdout'
2. *world.py* inputs 'hello' on its input port, then outputs ['hello', 'world'] on its output port 'stdout'. 

*Test.py* invokes the two components and sends them messages in sequence.  This process can be generalized to what I call a *Container* component, but, I didn't get there before the jam ended.

Note that the .outputs () method returns a dictionary of stacks (LIFO) of values for each port.  This was a conscious decision. LIFOs, Alists are what original McCarthy FP-style code used. Sector Lisp continues the tradition of using LIFOs.  I think that this is one of the secret ingredients for the anti-bloatwareness of Sector Lisp.  No RAM, therefore, no heaps, therefore, no mutation, therefore, simplified data access via push/pop/lambda-binding.  Lambda-binding and LIFO call-stacks fit together to make small code and no-fuss structure-sharing.

Sequencing in this paradigm is explicit and caused by the order of the *send*s.  Sequencing in most textual programming languages is implicit and is controlled by the syntax of the language (lines of code are ordered sequences).

## End of Jam
The jam ended before test.py worked correctly, but, today - 1 day after the jam - test.py is working.

## Post Jam
Next, would be to make a Container (Composite) component - *helloworld.py* that contained two components that can be chained together.  Chaining is not necessary in this paradigm and I keep it only to make the examples look more familiar.

After that would come a rearrangement of *helloworld.py* that would contain one *hello.py* and two *world.py*s, resulting in "['world', 'hello', 'world', 'hello']"
# Key Insights
- 0D - No Dependencies 
- FIFOs and LIFOs
- Pipelines
- Structured Message Passing
- "First Principles Thinking"
- Closures
- "Parallelism" is composed of more than one concept

## FIFOs vs LIFOs
- LIFOs are implemented in most modern programming languages (i.e. function call and call-stack)
- LIFOs make implementing Operating Systems and pluggable components more difficult than necessary
- both LIFOs and FIFOs are useful, but only LIFOs are inherently supported by modern programming languages 
	- e.g. function calling employs a LIFO, and does not employ a FIFO
	- FIFOs *can* be modeled as classes, but that is not the same as being inherently supported by the notation / programming language
## Pipelines
Pipelines are useful for plumbing software units together, but, functions calling functions do not implement pipelines (due to the LIFO issue).
## Structured Message Passing
![structured message passing.png](images/structured message passing.png)
## First Principles Thinking

## First Principles Thinking

#link
First Principles Thinking
https://fs.blog/first-principles/

https://jamesclear.com/first-principles

## Various Random Issues
My notes about Operating Systems, in screencast form: [https://beta-share.descript.com/view/gdfwt4MfKjF](https://beta-share.descript.com/view/gdfwt4MfKjF)
- divide-and-conquer - developers vs. end-users  
- divide-and-conquer - 2 main technical aspects of operating systems  
- bloatware  
- processes  

## Divide and Conquer
- divide and conquer is understood by most programmers
- but, most programmers do not employ *enough* divide-and-conquer
	- e.g. what is commonly call "parallelism" can be broken into 2 categories
		1. 0D
		2. Simultaneity
## Closures
- Operating Systems are Greenspun's 10th Rule applied to Closures

## Scalability
Pluggability is necessary for scalability, but, more elaborate (complicated) examples would be needed.

## Parallelism: Redux
1. 0D
2. Simultaneity
## Further Discussion

## Eh - Key Insights

# FIFOs vs LIFOs
- LIFOs are implemented in most modern programming languages (i.e. function call and call-stack)
- LIFOs make implementing Operating Systems and pluggable components more difficult than necessary
- both LIFOs and FIFOs are useful, but only LIFOs are inherently supported by modern programming languages 
	- e.g. function calling employs a LIFO, and does not employ a FIFO
	- FIFOs *can* be modeled as classes, but that is not the same as being inherently supported by the notation

# Pipelines
- pipelines are useful for plumbing software units together
	- but, functions calling functions do not implement pipelines (due to LIFO issue)
	- pipelines use FIFOs for communication

# Structured Message Passing
![wip-original/attic/structured message passing.png](images/structured message passing.png)
# First Principles Thinking
[First Principles Thinking](#first-principles-thinking)
# Various Random Issues
My notes about Operating Systems, in screencast form: [https://beta-share.descript.com/view/gdfwt4MfKjF](https://beta-share.descript.com/view/gdfwt4MfKjF)
- divide-and-conquer - developers vs. end-users  
- divide-and-conquer - 2 main technical aspects of operating systems  
- bloatware  
- processes  
- (disclaimer: I'm toying with Descript beta to produce tech video. This is my first attempt and might be unduly klunky)  
- (disclaimer: I'm still mulling on what to do for the jam. There is a strong chance that I won't be able to decide before the jam ends.)  
- (ps. I would be happy to discuss this stuff with anyone who is interested...)
# Divide and Conquer
- divide and conquer is understood by most programmers
- but, most programmers do not employ *enough* divide-and-conquer
	- e.g. what is commonly call "parallelism" can be broken into 2 categories
		1. 0D
		2. Simultaneity
# Closures
- Operating Systems are Greenspun's 10th Rule applied to Closures


# How Is This Different From What We Already Have?
State-of-the-art operating systems, like Linux, Windows, MacOS, have two (2) main functions:
1. control multitasking and blocking
2. provide a rich set of device drivers.

Wrapper operating systems cannot control blocking when the programming units perform ad-hoc, unstructured blocking on their own.  "Functions" *block* when calling other functions.  State-of-the-art Operating Systems need to resort to brute-force methods to pry blocking away from programming units, e.g. preemption.

This project does not *directly* address the issue of providing a rich set of device drivers (2), since, each device driver represents "hard work" - specific knowledge about the internal workings of each device, where each device might have wildly different operations.  Programming such devices is made harder by the over-use of synchronization, etc.  As such, writing device drivers in a stand-alone style should be "easier".  Incorporating already-existing device drivers is discussed below.
# Status
This project is essentially about joining the pieces of the project into a coherent whole.
- Most of the pieces are on the floor (see sub-projects) and getting simpler with each iteration.
- Currently working on Python version of Leaf components using HSMs (hierarchical state machines), trying to simplify [HSM P.O.C.](https://github.com/guitarvydas/hsm)
## Github
[eh](https://github.com/guitarvydas/eh)
# Future
- Containers
- Examples
- DaS
	- draw.io, SVG
- using existing O/Ss
- using existing Software
- emerging technologies
	- Robotics 
	- Games - NGPs, Actors
- anti-bloatware using Lambda wrappers
	- Lambdas, λs, are stack-oriented (LIFO), trying to use λs for non-stack-oriented programs causes bloat
	- functions that call other functions perform ad-hoc blocking, which O/Ss must fight to maintain control of blocking (e.g. using preemption)
# Sub-Projects
## 0D - No Dependencies
- use FIFOs, don't use function calls for component-to-component messaging
- deferred message sending
	- don't deliver message immediately, just stick it in an output queue
	- parent wrapper component ("Container") walks output queue of Child and routes messages to other children (or to its own output queue)
## FIFOs and LIFOs
- building FIFOs is a no-brainer in most modern languages
## Pipelines
- UNIX is an example of pipelining put to good use
	- UNIX uses "lines" (terminated with newline) as the substrate for communication
	- this is too complicated 
		- restricts UNIX tools to processing text
	- use bytes instead of lines
		- include "tag" string/byte in message
- Communicating HSMs will be much smaller units of software than full-blown UNIX commands
## Structured Message Passing
0D makes it possible to choose how to structure a system composed of Components.

Structured Message Passing is like Structured Programming.  Nothing new added to the toolbox.

Good design principles based on what we already know, e.g. ORG Charts in business.  

Don't colour outside of the lines.

Contain, contain, contain.

## "First Principles Thinking"
Survey of current problems.

Survey summarized in screencast (above).

### Conclusions
- over-synchronization
	- it's difficult to do some simple things (like multitasking), because of presence of pervasive synchronization
- FIFOs not LIFOs
- O/S processes are just clumsy, big closures with FIFOs for input (often called "mailboxes")
- FIFOs for output are often implemented under-the-hood by Operating Systems
	- could be easily implemented using Classes (don't need Operating Systems to handle output FIFOs for apps)
## Closures
No-brainer using most modern programming languages.
## Diagrams - DaS (Diagrams as Syntax)
- done at least once with Prolog+Lisp+Haskell
	- theory: could be much simpler using Ohm-JS
	- previous version used backtracking to figure out (inference) containment relationships
	- theory: SVG grouping can embed containment relationships directly in the data without further inferencing
	- containment relationships are:
		- nested boxes
		- ports belonging to boxes
	- connection relationships are:
		- line begins at element
		- line ends at element
- i.e. containment and connection represent slightly more information than what is alreadycontained in program text files now
	- i.e. easy to implement, once you know that you want these relationships
	- ASCII Art for "box" is `{...}`
	- the "global variable problem" exists because containment is not strictly adhered-to
		- ASCII-Art for box doesn't make it "as obvious" that a variable is not contained in a box, or crosses the edges of a box
- draw.io creates compressed .drawio files which contain enough info for parsing
- SVG contains almost enough info
	- rectangles
	- ellipses
	- lines
	- text
	- grouping
	- missing: source and target elements for lines 
		- draw.io outputs source and target information
- Ohm-JS can parse .drawio files
	- Ohm-JS is based on PEG, includes backtracking and easy parsing
- currently blocked on creating a JS program to uncompress .drawio format
	- just a technicality, done more than once in the past
	- needs to be made stand-alone or into a library function (probably 1-line in JS)

## Hierarchical State Machines
Use hierarchy to conquer the "state explosion problem".

First suggested by Harel in original StateChart paper [Harel StateCharts](https://guitarvydas.github.io/2020/12/09/StateCharts.html)

Parent overrides Child, which is opposite to what is considered to be *class inheritance* in programming.

If a Parent changes state, it exits all Child states (recursively, to any depth).

A Child cannot change the behaviour of a Parent, hence, each unit of code (a diagram or text) "make sense" in a stand-alone manner, hence, no hidden dependencies.

Operating System *processes* are State Machines.  HSM results in State Machines that are smaller than Operating System state machines.

# Approach

## Formulate questions
Questions such as...
- Why do hardware designs tend to work while software designs fail and become more complicated?
- Pipelines are different from functions.  How are pipelines different? 
- Message passing.  Is message-passing possible in the synchronous paradigm?
- Message passing - asynchronous - has a bad rep because it is often ad-hoc.  Is there an equivalent to "structured programming" for async message-passing?
- Closures - are closures the same as "processes" in operating systems? 
- DaS - Diagrams as Syntax.  Why are most programming languages textual?
- Tells - what is currently considered difficult?  Multitasking, async, callbacks, mutation, sequencing, history, state ... Can these be improved?  Are they difficult because they're difficult or because our notation makes them difficult?
- Is "something" the same across all programming languages?
- What is parallelism?
- Operating Systems and Programming Languages were invented in the 1950's under the single-cpu assumption.  Is the single-cpu assumption still valid?
- Are end-users forced to use the "same" operating systems / computer environments as developers?

- Can the goal (pluggable components) be sub-divided into smaller sub-goals?
	- Which properties must components have to be pluggable?
	- Which properties inhibit pluggability?


## Synthesize
- upon answering the above questions, it is possible to synthesize a new programming environment?
# Discussion

## micro-concurrency

- concurrency *inside* the components not *outside* the components
- state-of-the-art operating systems, e.g. Linux, Windows, MacOS, are big state machines that run internally-synchronous units of software ("apps")
- can we shrink the scale of behemoth operating systems?


## 0D

# 0D
Zero-dependencies.

- no dependencies whatsoever
- insidious dependencies include:
	- name-calling, hard-wired names of target functions (e.g. libraries)
	- over-use of synchronization
		- call-return uses the call-stack as a global variable
		- call-return mutates the call-stack
		- call-return blocks the caller while it waits for the callee to *return* (a hidden dependency)
	- hard-wired routing


## 2022-07-11-0D

# 0D Is Important
I continue to struggle with finding ways to say "0D is important".

0D means "zero dependency".

---

# Problem of Perception
People don't "see" that there is a difference between functions and 0D

---
# Analogy - Perspective in Art

The perception problem is akin to pre- and post-perspective Art.

People didn't "see the need" for perspective in 2D artwork until "steam engine time" 

[Paul Morrison used the phrase "Steam Engine Time"].

---

# Faster Horses
The perception problem is akin to:

> If I had asked people what they wanted, they would have said faster horses” 

attributed to Henry Ford

---
# First Use-Case For Electric Motors
The perception problem is is akin to the first use-case for electric motors.

First use-case: pump water uphill to create artificial streams that could turn paddlewheels that ran factories [Digital Darwinism](https://www.amazon.ca/Digital-Darwinism-Survival-Business-Disruption/dp/0749482281)

https://www.amazon.ca/Digital-Darwinism-Survival-Business-Disruption/dp/0749482281

---

# Epicycles
We have developed epicycles due to dependencies and workarounds that manage dependences 

Like *make*, *package managers*, *nixos*, etc.

Instead of simply removing all dependencies.

---

# Programming Should be Easy
Programming should be easy

But, modern programming using state-of-the-art languages is not easy.

---

# Tells
- Prevalent notion that "multitasking is difficult".

- Prevalent notion that "distributed programming is difficult".

- Prevalent notion that "systems programming is difficult" 
	- and, can only be expressed using low-level languages

---
# If It's Difficult, Invent a New Notation
If something looks difficult, invent a new notation to describe it.  

Create another layer to abstract-away the constructs in the current layer.

---
# Functional Programming
Functional programming is a notation for designing calculators.

# Sequencers
Multitasking, IoT, internet, music and video sequencers, robotics programs, etc. are not calculators.

The dimension of time (*t*) cannot be ignored in a notation for building sequencers.

*Modeling* a fundamental concept (like *t*) is not as good as building a notation around the concept.

---
# Example: Evolution of Software Notations
- Electronics looked difficult, so opcodes and instruction sets were invented 
	- instruction sets are, but, a notation that abstracts-away the underlying rats' nests of complicated details of electrons flowing within oxides

- Opcodes and instructions sets using binary codes looked difficult, so Assembler was invented

- Assembler looked difficult, so C was invented

- C looked difficult, so higher-level languages were invented.

- Now, programming in higher-level languages looks difficult ...

# The Difference Between *Electronics* Design and *Software* Design...
Electronics components are 0D, completely isolated from one another

Software components are rife with dependencies and built-in synchronization, N0D (non-0D)

---

# Analogy: LEGO®
Single type - round peg
	- just one type, not many types

A single type begets simplicity
	- simplicity is "the lack of nuance"

0D - no interdependencies
	- cutting one LEGO® block in half does not affect any other LEGO® block

- LEGO® blocks can be snapped together to form larger systems
- Larger systems built out of LEGO® blocks can be broken down by removing blocks
- Blocks from one system can be reused to build other systems
- Complete sub-systems can be broken away from existing systems and can be used to build other systems
---
# Software Libraries and Functions
Libraries of functions cannot be easily reused due to inter-dependencies.

Libraries of functions cannot be easily tested in a stand-alone manner, due to inter-dependencies.

---

# OOP Does Not Implement "Message Passing"
Message passing in OOP languages is implemented using N0D Call/Return

Rhetorical question: Is OOP an abstract notation, or, is OOP a technique for programming CPUs?
- methods imply the use of blocking functions (see "functional notation")

---

# Functional Notation
Functional notation is based on blocking state machines
- e.g. `f(x)` blocks the caller until the callee returns a value
	- this is a state machine, the state is recorded as bookmarks on The Call Stack

 "Blocking" thwarts the efforts of Operating Systems to control applications, and, makes Operating Systems more dificult to implement, needing more nuance and workarounds, often resulting in latent gotchas.

---

# Sector Lisp
[Sector Lisp](https://justine.lol/sectorlisp/) is an example of how small and beautiful FP notation can be if it is left alone and not overloaded with concepts that are outside of its "sweet spot".

Jart's GC is only 40 bytes [sic, not K, not M, not G, but, bytes].

Sector Lisp: https://justine.lol/sectorlisp/

---
# Functional Notation and Hardwiring Names

`f(x)` hardwires the name `f` into the callers code

Making it difficult to use the code in other situations.

---
# OOP "Encapsulation" Is Not Enough
"Encapsulation" encapsulates data

"Encapsulation" does not encapsulate control flow

---

# Control Flow And Data Flow
Control flow and data are not the same concepts

A single notation for both cannot be used without compromising one or the other.

"Data" is layout of information *in storage*

"Control flow" is layout of behaviour *in time*

---

# Schizophrenia
Previous attempts to subsume both, data and control flow, into the same notation have resulted in schizophrenic programming languages that sacrifice one or the other notion.

Popular fad today: sacrifice control flow layout, while emphasizing data layout.

---
# Structured Programming
Attempt to apply structuring concepts to control flow layout

Recommendation for structuring -> single input, single output 
	- layering
	- abstraction of control flow layout

---
# Analogy: Human Interaction, "Free Will"
Humans understand how to deal with independent units (e.g. other humans).

Hard-wiring synchronization into an underlying notation defies human intuition, giving rise to the notion that "programming is difficult" and requiring many years of schooling to learn to think in terms of over-synchronized units

---
# Diagrams
Humans understand blocks on diagrams to represent independent units

Mapping diagrams to Synchronous Programming Languages[^spl] defeats the purpose of creating diagrams

SPLs do not faithfully represent 0D diagrams.

---
# Solutions: No Name Calling


### 2022-07-11-No Name Calling

# Solutions: No Name Calling
- Prohibit naming of callees.

Suggestion: Use message-passing FIFOs and let a Container wrapper route the messages.

Python: instead of `f(x)`, use

```
self.send (..., outputPort, data, ...)
```

suggestion: 
- outputPort is a string
- data is any Python datum
- just Send the message, let the Receiver check the validity of the input (type, design rules, etc.)


#### 2022-07-11-Type Stacks

# Type Stacks
- progressive type checking
- pipeline of type checkers
- input to pipeline is general and loosey-goosey
- output of pipeline is specific and checked
- each stage in the pipeline checks 1 kind of detail and passes the data on, or, sends an Error message
- compose type checker chain using smaller blocks
- no need to *abort*, just don't send data on to the next stage in case of error



![type stacks.png](images/type stacks.png)

# Solutions: Extending Flow-Based Programming

### 2022-07-11-Extending Flow-Based Programming

# Attention to UX Instead of Mathematical Niceties
- need for abstraction
	- lasso a group of components with a total of N ports
	- replace group of components by a single component with fewer than N ports 
		- implies fan-out for implementation
		- implies single-entry & single-exit points, abstracting FIFOs (bounded queues) down to single input and single output

![diagrammatic abstraction.png](images/diagrammatic abstraction.png)

# Secret Sauce of FBP
0D

No dependencies.

Often mis-named "parallelism".

Parallel software components imply 0D.

0D components do not imply parallelism.


# Programming Languages are IDEs for programming
- PLs (IDEs) invented in mid-1900s
	- to appease hardware capabilities of the day
- based on cells of bitmaps ("characters")
- cells may not overlap
- cells are fixed-sized
	- font sizing affects many cells at the same time
- windows are not fixed-size
- rectangles on a diagram are not fixed-size
	- it is convenient to use a diagram editor to change the size of a rectangle
	- it is not convenient to use a diagram editor to change the size of a piece of text (by dragging a corner, say)


# Fan-Out
- one output feeds many inputs
- requires copying, or, copy-on-write, or, ...
- copying
	- implies memory management (GC (Garbage Collection)
- copy-on-write
	- JavaScript assignment semantics, creating *own* variables

[^spl]: "Synchronous Programming Languages" means just about every popular programming language in use today, e.g. Python, Rust, Haskel, Lisp, JavaScript, C, etc.  Relational Programming Languages are not SPLs.

## 2022-08-21-Layers

- layers
	- steppable
	- recursive/fractal 
		- no limits to depth and # of layers
	- relativity, hierarchy
		- software units must not refer to other units using absolute references
		- moving feast
		- UNIX hierarchical file system
			- originally, most operating systems were flat, not hierarchical
			- hierarchy made managing data easier - in layers
				- we want programs to be arranged in hierarchies
				- possible in existing programming languages, but neutral - not encouraged



# References
[Harel StateCharts](https://guitarvydas.github.io/2020/12/09/StateCharts.html)
[call/return spaghetti](https://guitarvydas.github.io/2020/12/09/CALL-RETURN-Spaghetti.html)
name
	- no Greek
	- no ASCII
Dependency essay
Functions vs. dependencies article
[Movable Feast Machine](https://guitarvydas.github.io/2020/12/09/CALL-RETURN-Spaghetti.html) not related, but, indication of "steam engine time" - similar issues being addressed differently

## 2022-07-10-Layered Programming - New-Breed Structured Programming

One thing I haven't mentioned in essay form is the notion of chopping programs into 2 kinds: 

- Leaf programs 
- Container programs.

Leaf components are where code (the traditional notion of code) goes, while the only job of Containers is to route messages between FIFO queues.  

Containers are recursive and layered.  Containers contain Leaves and/or other Containers.

Components, whether Leaf or Container, contain a FIFO output queue and can only communicate with other components by leaving messages in their output queue, to be routed by their parent Container.  Output messages are deferred and are not routed until all children have given control back to the Container.  No Component can refer directly to any other component, except that a parent Container can see its own direct children and can route messages between them.

I think of routing as being a programming language - beyond what is traditionally considered to be part of programming languages.  

I see FBP in this light.  I see internet in this light.  I see IoT in this light.  I see robotics in this light.  

Routing is sometimes called "coordination language", but I think that it is important to think of it as a programming language.  

In the same vein, I think of "compiling" diagrams instead of merely "modelling" programs using diagrams.  A subtle difference, but, one which leads to vastly different ways of approaching the problem(s).  Maybe akin to the shift in art, when drawing-with-perspective was introduced.

With "modelling", you try to express the diagrams using data structures in standard general-purpose programming languages.

With "compiling", you treat diagrams as *syntax*.  Boxes and ellipses are like *characters* to be parsed as part of the ecosystem of a programming language.

*Text characters* are not usually overlapped and are displayed in grid form.  Boxes and ellipses (and lines and text-elements) are not restricted to grid layouts and can be overlapped and resized in the editor.

The idea of programming languages using overlappable/resizable cells opens up new avenues of thought beyond that of using only programming languages that disallow overlapping of cells.  

I think that this results in distributed-thinking instead of synchronous-thinking.

Layers are to modern programming as "Structured Programming" was to assembler programming.


## 2022-05-30-Fire and Forget

---
tags:
- graphicessay
- concurrency
- fireandforget
- multitasking
- 0D
- closures

---

# Fire And Forget
![fireandforget-fire-and-forget.png](fireandforget-fire-and-forget.png)

### 2022-06-04-Fire and Forget

Fire-and-forget - most often called "concurrency" and "paralellism" entails two aspects:
- snipping dependencies
- the element of *time*, non-synchronization.

Humans understand *synchronization* at a visceral level.

For example, humans deal with other humans ("Hi, how are you?", "Can you do this for me...?", "I need this by Tuesday") on a daily basis.  

Synchronization is done on an as-needed basis ("give it to me when you're done.")

There is no need to install synchronization into *every* program[^ps].

[^ps]: I call this "pervasive synchronization".

Too much synchronization slows everything down.  

When there is too much synchronization, the slowest player determines the final speed of the result.

[aside: I found Harel's Statecharts to be a brilliantly wonderful idea.  I found Harel's synchronous analysis of Statecharts to be entirely unpractical, because it required all orthogonal states to be fully synchronized and micro-managed.]

The lazy way to analyze the behaviour of a system is to imagine micro-management - every action is synchronized at a very low-level.  Every action, even "concurrent" actions, are imagined to consist of small micro-steps that are fully synchronized with the operation of other actions.  
A less-lazy way to analyze the behaviour of a system is to imagine that it is composed of asynchronous levels (layers).

Example: A Swiss clock contains many interlocking gears, the micro-actions of the clock are completely synchronized with other actions of the clock.  The clock proceeds to tell time based on interlocking micro-actions.  

In the micro-managed model, two clocks are just like one bigger clock - all actions of each clock are completely synchronized and are dependent on each other's micro-steps.

In an async model, the two clocks are completely independent.  The actions of one clock's gears do not affect, do not slow down, the action of the other clock's gears.

# Simultaneity
![fireandforget-simultaneity.png](fireandforget-simultaneity.png)

# Faking Multitasking on 1 CPU
![fireandforget-faking-on-1-cpu.png](fireandforget-faking-on-1-cpu.png)
# Anti 0D
Tools that appease the use of dependencies instead of addressing the fundamental problem (getting rid of dependencies).
![fireandforget-anti-0D.png](fireandforget-anti-0D.png)
# Execution
![fireandforget-execution.png](fireandforget-execution.png)
# Operating System Processes
![fireandforget-operating-system-processes.png](fireandforget-operating-system-processes.png)
# Multiple Single CPUs
![fireandforget-multiple-single-cpus.png](fireandforget-multiple-single-cpus.png)iple Single CPUs

# Closures
![fireandforget-closures.png](fireandforget-closures.png)

[2022-06-04-Fire and Forget](#2022-06-04-fire-and-forget)

# Tools / POCs
Tools and Proofs of Concept that are related to this project but not part of the 1-week Jam
- https://github.com/guitarvydas/das2json
	- transpiles diagram testbench.drawio to JSON
	- transpiles diagram helloworld.drawio to JSON
	- uses hybrid diagram elements containing Python code
		- boxes, connections, ports written as a diagram
		- "Leaf" code written as Python (embedded in the diagrams)
		- the diagrams are hybrids - boxes + ports + lines + Python code
			- i.e. micro-concurrency written in diagram form, the rest written as regular Python code
			- do the minimum necessary, and let Python do the rest of the heavy lifting
	- uses PROLOG inferencing to create a factbase, including containment and connection relationships
	- could be simplified, probably with Ohm-JS
- https://github.com/guitarvydas/das
	- similar to above, except slightly more ambitious
	- transpiles helloworld.drawio to Python, then runs the Python
	- transpiles d2py.drawio to Python, then runs the Python
		- d2py.drawio is a "script" for self-compiling the das-to-python transpiler to Python
		- the resulting Python script calls "make" for building the transpiler
		- the diagram shows one way to trap errors and quit
		- the UX (the diagram language syntax) could be more humane - at the moment, it consists of boxes and lines which might look "too complicated" to non-programmers (thought: maybe rely on box containment to "inherit" messages, eliding some of the ports and lines)
- https://github.com/guitarvydas/vsh
	- checkout afa53b8
	- contains very old (pre-2013) Visual Shell experiment
	- diagram compiler written in itself (using yEd editor)
	- generates .gsh files
	- .gsh is *grash* a minimal (approx 8 instruction) assembler for invoking UNIX C system functions (e.g. dup2(), exec(), etc.)
	- (I ran out of time during this Jam to make this work again)
- pipelines
	- see UNIX shells
	- see Aho's paper on using pipeline syntax as a replacement for Denotational Semantics syntax
	- (I ran out of time to dig up this reference during this Jam)
- micro-concurrency
	- partially based on implementing [Harel StateCharts](https://guitarvydas.github.io/2020/12/09/StateCharts.html)
	- partially based on Holt's book [Concurrent Euclid, UNIX, Tunis](https://www.amazon.ca/Concurrent-Euclid-Unix-System-Tunis/dp/0201106949)
	- partially based on designing hardware using state machine diagrams
	- "sequencing" and "concurrency" is "easy" with state diagrams, less easy with functional notation
- conclusions about 0D and "parallelism"
	- [0D](https://publish.obsidian.md/programmingsimplicity/2022-07-11-0D)
- HSM - Hierarchical State Machines
	- [HSM P.O.C.](https://github.com/guitarvydas/hsm)
## Notes to Self

## 2022-08-21-Notes on Eh

Programming is the act of controlling a computer.

Programming is done by connecting a series of stand-alone units together.

Software units send Messages to one another using Structured Message Passing.

"Operating systems" and "programming languages" as we know them today, are not needed when all programming is done by composition of stand-alone units of software.

# How Is This Different From What We Already Have?
## Current Operating Systems

State-of-the-art operating systems, like Linux, Windows, MacOS, have two (2) main functions:
1. control multitasking and blocking
2. provide a rich set of device drivers.

Wrapper operating systems cannot control blocking when the progamming units perform ad-hoc, unstructured blocking on their own.  "Functions" *block* when calling other functions.  State-of-the-art O/Ss  need to resort to brute-force methods to pry blocking away from programming units, e.g. preemption.

This proposal does not *directly* address the issue of providing a rich set of device drivers (2), since, each device driver represents "hard work" - specific knowledge about the internal workings of each device, where each device might have wildly different operations.  Programming such devices is made harder by the over-use of synchronization, etc., outlined in this proposal.  As such, writing device drivers in a stand-alone style should be "easier".  Incorporating already-existing device drivers is discussed below.
## Current Programming Languages
- over-use of synchronization
- over-use of blocking (AKA "functions" ; functions *block* when calling other functions)
- over-use of dependencies
- programmers are under the illusion that Code Libraries provide stand-alone units of software
	- this is not the case, for example "changing something here" might cause "something over there" to function differently (due to over-use of dependencies).
- ASCII Art instead of diagrams
	- use of textual programming languages led to the "global variable problem"
		- Textual programming languages attempt to fake-out drawing of nested containers, leaving too much room for crossing the boundaries of containers
		- The "problem" would have been instantly visible if diagrams had been used, and, I assert that we would never have had to have dealt with "global variables"
		- Global variables are possible to express only with textual languages, or, with diagrams that omit container boundaries

## Programming
- Programming consists of two (2) main activities
1. Design, "creativity"
2. Production Engineering, "optimization".

State-of-the-art programming languages, like Rust, C++, Haskell, Python, etc. address the issues of Production Engineering (2), but tend to ignore Design (1).

Methodologies like Agile, Pair Programming, etc., are attempts at adding structure to the process of Design.

Previous attempts at structuring the Design process tend to be ignored:
- Dynamic Languages
- REPLs
- Rapid Prototyping


### Design in Other Disciplines
More-established disciplines, like song-writing, teach methods for "creation", such as
- brainstorming
- mind-mapping
- iteration

Brainstorming tends not to be discussed with respect to modern programming, although Agile and Pair Programming hint at this process.  

The idea of a REPL is iteration - experiment and modify and repeat. Agile is simply a very-slow-REPL.

Requirements-gathering hasn't been formalized and pinned down.

Most non-programmers don't want to deal with (specify) all of the details.  The amount of detail that non-programmers provide is variable, making it hard to formalize the process.  Additionally, non-programmers will try to describe what they want by, instead, describing how they think it should be done - this makes it even harder to piece together what it is they want.  Non-programmers are often wrong about how something should be programmed.  (A sign at my auto-mechanic says something like "shop rate: $70/hour or $90/hour if you watch").

Likewise, theorists are usually wrong about what tools would help the software-creation process.  A glaring example of this is the invention of language-theory and tools like YACC.  In 2004, the PEG process was (re-)invented and is markedly more flexible than YACC.  PEG is not based on language-theory.  PEG is essentially a DSL for specifying parsers directly, instead of using Language-Theory to for specifying parsers.  A very flexible manifestation of PEG is the Ohm-JS language.  Another example is the attempt to insert macros into programming languages.  Macros make more sense as part of editors, not programming languages.

## FDD vs Waterfall Design Method
[Failure Driven Design](https://guitarvydas.github.io/2021/04/23/Failure-Driven-Design.html)

If you don't iterate a Design or the understanding of the Requirements, you are designing using the Waterfall Method.

Agile is an attempt to iterate a Design and Requirements (i.e. a very-slow REPL).

TDD is an attempt to iterate the understanding of a Design.

## Epicycles
We have been adding epicycles to the programming workflow to fake out programming via stand-alone units of software, e.g.
- packages
- package managers
- make

- text-only

# How Do We Incorporate Already-Existing Software Into This Scheme?
- run Comopnent-based software "under" existing operating systems with "FLI" interfaces to existing operating systems

- commonality between all programming languages
	- functions -> sync, blocking
	- 

# Notes
- all languages and OSs were invented in the 1950's mindset of "single CPU"
- now, we have multiple CPUs and the ground rules have changed, but, techniques are still stuck on the single-cpu/everything-is-a-calculator model
- steaming pile of bloatware (Linux, Windows, MacOS, Rust, C++, Python, JavaScript, node.js, etc.)
- over-use of synchronization (due to 1950's single-cpu model)
- ad-hoc blocking - O/S must fight with functions for control
- epicycles due to using "calculator model" for "distributed programming" -> extra code to work around forcing distributed programming into the "calculator model" domain
- eh inner concurrency instead of O/S-supplied concurrency

# Principles
- FIFOs (queues) for inter-component communication
	- LIFOs (stack) for inner communication (function calls)
- child cannot override parent - every layer makes stand-alone sense and cannot depend-on (be altered by) adding children
	- parent gets "first dibs" on all incoming messages
	- parent punts messages to child if message unwanted by parent
	- parent recursively exits children if parent state changes
- little communicating operating systems instead of 1 huge one
- SVG is a super-set of Text (SVG contains rectangles, ellipses, lines, text, grouping)
- pure functions are pure functions - i.e. no mutatation, hence, do not express RAM, Concurrency, etc. (they can model these concepts, but modeling is not as good as expressing)