# 2023-07-23-Control Flow and Data are Not the Same
# Control Flow and Data are *Not* the Same
Data is a static lump of memory.

Control flow, though, is two things:
1. a static lump of memory
2. an interpreter of that static lump of memory.

The static lump of memory contained in a *control flow* object can be thought of as a *script*.

## Concrete Example: McCarthy's Lisp
In Lisp 1.5, Data is very simplistic:
1. Atoms
2. Lists.

In Lisp 1.5, Control Flow is defined by the *eval()* function operating on a *script* consisting of the above form of very simplistic data (Lists and Atoms).

In Lisp 1.5 a *script* is a list and the *interpreter* of the script is the *eval ()* function.  The *script* is a static lump of memory and the *interpreter* is a function

# Operations
## Operations on Data
Data contains one operation (aka *method*): *mutation*.

## Operations on Control Flow
Control flow contains two operations:
1. *moving* data
2. *interpretation* of the data.

Note that *compilers* interpret Data.  The only difference between *compilers* and what-is-called *interpreters* is the timing of the interpretation - *when* is the data interpreted?  In a *compiler*, the data is interpreted once and converted to a simpler Control Flow object (aka *assembler* - the CPU is an interpreter of bytes in RAM).  In an *interpreter* that data is interpreted at runtime as it is encountered, possibly over and over again without regard to whether the same script has been interpreted earlier.

Note that what is called *binding* in functional languages is actually *mutation*.  When a function is called, a value on the callstack is mutated and automatically cleaned up upon return from the function.


### JIT
Aside: a JIT is an interpreter which interprets its *script* data once, then caches the result and reuses the cached result when it sees the same script again.  Furthermore, a JIT might interpret its script differently depending on what it considers the input data to be.  A JIT caches these different, type-dependent interpretations and reuses them (the results) as appropriate. In each case, the higher-level control-flow interpreter produces a lower-level control-flow interpreter which contains simpler *script* elements that can be interpreted more quickly and efficiently.  
The point of a JIT is to simplify pre-execution *compilation*.  JITs amortize *interpretation* of *script*s across *pre-execution* and *execution* times.  

The traditional work-flow is to create two categories of *interpretation*
1. compile-time
2. runtime.

JITs redefine this model by creating three categories of *interpretation*:
1. compile-time
2. runtime once
3. runtime repeatedly.

## Memory Allocation
All data is stored in some kind of RAM, i.e. Random Access Memory.

Some kinds of RAM can be accessed and mutated more quickly / efficiently than other kinds of RAM.

For example, the RAM that we call *registers* is the fastest RAM available.  It is typically very small and located very close to the CPU (providing faster electron travel times).

The stuff that we traditionally call RAM is slower than registers, but faster - and more expensive - than other kinds of memory, like disks and caches and other distant machines.

## Garbage Collection

If memory is expensive-enough for us to want to reuse it, we must clean up the memory and recycle it.

This operation is usually called *memory allocation*.

There are many schemes for cleaning up and recycling memory:
- the biblical flood method
	- employed by UNIX process - when a process dies, UNIX recycles the memory that was used by the process
- callstack
	- this scheme is convenient for programmers, but,
		- uses special registers, e.g. the SP (Stack Pointer)
		- must follow a stack-based (nested) protocol
		- mutates a global variable, the SP
		- is limited by the number of registers used (usually one global register, the SP)
		- is limited
	- mutation occurs upon CALL
	- freeing occurs upon RETURN
	- further mutation of variables "on the stack" may or may not occur during the operation (interpretation) of the function
	- is recursive *only* in a restrictive sense
		- usually, recursion is limited by a single stack approach
- heap
	- Random Access
	- Random Mutation
	- ad-hoc allocation and freeing needed in languages like assembler, C, Odin
	- various schemes for GC
		- replace ad-hoc allocation and freeing with more general schemes
		- cost is lack of low-level control and "efficiency"

## The Meme of Control Flow *Is* the Same as Data
Attempts to treat control flow as data results in ad-hoc interpretation of data.

For example, we see variations on skimpy parsers in early languages like BASIC and Smalltalk and Forth.  More modern languages simply hide their ad-hoc control flow underneath layers of complication.  

## Parsing

Less ad-hoc seeming parsers, like CFGs, are *pattern matchers*.  They *interpret* data in very narrow manners, e.g. treating bytes as *characters* and sequences of *characters* as words and phrases to be pattern matched.

## More Operations
### Data Mutation
- Getters
	- Lookup a value in the immediate object.
	- If the named value does not exist in the immediate object, lookup the value in the object's ancestor (parent).
	- If the object has no parent, the value is *nil*.
- Setters
	- Copy on write.
### Data Allocation
- Allocate / Instantiate
- Free
- Clone
### Data Inheritance and Prototypes
Data can *inherit* the data layout of protoytpes.

*Prototypal inheritance* operations can *add* fields to the prototype.

*Prototypal inheritance* operations can *remove* fields from itself that appear in the prototype.

### Data Operators
Code within data objects can 
- change the data
- perform built-in operations on the data, such as `+`, given arguments that are other data objects

### Control Flow Dynamic Ancestry and Static Ancestry
In the most general cases, *ancestry* is determined at runtime. *[Research question: can ancestry be determined solely at compile/build time?  In all likelihood such static ancestry will turn out to be a subset of more general dynamic ancestry.]*

### Control Flow Ancestry: Ancestral Authority
Control flow Parental Authority is like inheritance, with the exception that a derivative cannot change the behaviour of its ancestor.  The behaviour of a control flow object is defined from the top down. Control flow is defined by the highest-up ancestor and cannot be overridden by a derivative (aka child).

### Control Flow Punting (Delegation)
A control flow object may punt work to a descendant.

A control flow object always gets "first dibs" on performing work before punting the work further down the family tree.

### Control Flow Phrases
Code within control flow objects can contain phrases made up of a sequence of *words* and *operands*.

### Word
A *word* is any sequence of characters enclosed in brackets `❲...❳`.  The characters may contain spaces and newlines.  If *word*s contain the brackets `❲...❳`, they must be matched in pairs.

For example
- `❲abc❳` is valid
- `❲a b c❳` is valid
- `❲abc`❲def❳ghi❳` is valid
- `❲abc❲defghi❳` is invalid
- `❲abcdef❳ghi❳` is invalid, in fact, it is parsed as a valid word `❲abcdef❳` followed by an invalid word `ghi❳`

*[Research question: can words contain escaped characters?]*

### Operand

### Control Flow Operands
Code within control flow objects can refer to data objects as *operands*, but, can only
- instantiate *operands*
- move *operands* from one operand to another
- invoke *method*s on operands

### Control Flow Independence
Control flow objects are completely independent from other control flow objects, hence, are concurrent.

Concurrency can be used to implement *parallelism*.

*Operands* instantiated by a control flow object are completely contained within the control flow object and cannot implicitly leak out to other control flow objects.  Two instantiations of control flow objects, from the same base, contain completely independent instances of *operands*.

### Message Passing
Control flow objects can communicate with other control objects purely through message passing.

Data within messages is cloned and is not shared between objects.

- Structure Message Passing
	- requests / commands flow downwards
	- responses / summaries flow upwards
	- inter-object message passing is performed *only* by a common parent
	- objects can receive input messages
	- objects can create output messages, but cannot specify their destination, ie. output messages are queued up on the sending object's *output queue* and distributed *only* by an object's direct parent
	- a parent determines all message routing for its direct children 
- Connections
	- a connection is defined by 3 attributes:
		1. direction
			- down
			- up
			- across
			- through
			- ignore
		2. sender: {object X port}
		3. receiver: {object X port}
	- all connections within a object must be atomically visited for each message *routing* operation
		- during routing, an output message is copied and converted into an input message with the appropriate input port for the receiver's object
		- 
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