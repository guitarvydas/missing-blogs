# 2022-10-24-Eh and HSMs AgainHSMs are layered state machines.

A State Machine is composed of States.

A State can be a Leaf node, or, it can be another State Machine (recursively, hierarchically).

A Machine cannot contain code.

A State IS code.

A Machine provides a Send() operation that can be used by any one of its states.

An ė (pronounced "Eh" in ASCII) object is a unit of concurrency.  An ė object is a Machine that catpures all Sends() from it Children and GrandChildren (and so on) and places data on its own output queue.

An HSM is a layered piece of *non*-concurrent code - clockwork code, like what we call *programming* at present- that is used to implement a portion of the insides of an ė object.

## State

A *State* is not just 1 piece of code.

A *State* has
- entry code
- handling code
- exit code

That would be 3 λs, not 1.  

At present, we try to flatten all 3 pieces of code into a single λ.  This can be done using epicycles (AKA *accidental complexity*) and greater confusion (flattening is an optimization which tends to obfuscate the meaning of code).

It is "easy" to conceive of exiting a Machine by hierarchically calling the exit code (deepest first) of the current State and all of it ancestors.

Flattened code *can* do this, but causes hand-wringing, in the form of cleanup code language features like *defer* statements and *finally* and `__del__()` , etc.
## Choosing the Right Weapon
I advocate using multiple notations within a single project.

Currently, we use a single notation - *functions* - to describe every kind of code.

I feel that StateCharts are more convenient than *functions* for describing *sequencing* of actions.  

HSMs are derived from StateCharts.  

I think that StateChart notation subsumes 2 kinds of code:
1. hierarchical Machines and States (synchronous, clockwork code)
2. concurrency (called *Orthogonal States* in StateChart lingo).

I like to separate the concepts into 2 different notations:
- HSMs for hierarchical state machines
- node-and-arrow notation for concurrency (think ė and FBP, etc.).

## Atomic Principles
I like to discover the *atoms* of software construction that can be used to build up UXs for various parts of a problem solution.  

Hence, my extreme interest in Ohm-JS.  I use Ohm-JS to drape syntax skins over *atomic* concepts to create *molecules* and various kinds of programming UXs.

I've developed this attitude, iteratively, over several decades, starting with compilers that create Assembler, Lisp, and, now, Ohm-JS.

## Concurrency
Every concurrent object is a state machine.  

Think Actors.

Currently, ė-like objects are treated very specially, using bloatware in what we call *processes* in operating systems.

Note that operating systems, e.g. UNIX written in C, are simply Greenspun's 10th Rule[^gtr] applied to *closures*.  All of that C code simply implements *closures*.

[^gtr]: "Any sufficiently complicated C or Fortran program contains an ad hoc, informally-specified, bug-ridden, slow implementation of half of Common Lisp." https://en.wikipedia.org/wiki/Greenspun's_tenth_rule

At present, we use *functions* and *functional notation* to describe and implement clockwork code inside of *processes* (ė-like objects).

At present, we write all "code" as functions, then wrap big, honking State Machines around them using processes and operating systems.  

*Functions* have the unfortunate feature of *blocking* (caller waits for callee to execute a *return*), which causes the invention of epicycles called *preemption*.  The *preemption* epicycle, causes further epicycles.  We saw this very clearly in the Mars Pathfinder disaster which necessitated the invention of *priority inheritance* epicycles.

## Flattening
Can you flatten the concept of Machines and States into one Class?  

Yes.  

Is this advisable?  

No.

Flattening is an *optimization* and usually makes things appear to be more complicated, or, dilutes the meaning of things.

I think that it is “simpler” to describe HSMs using 2 classes.

# See Also
[StateCharts](https://guitarvydas.github.io/2020/12/09/StateCharts.html)