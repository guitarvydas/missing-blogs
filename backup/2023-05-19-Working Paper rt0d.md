# 2023-05-19-Working Paper rt0dN.B. This is a working paper.  I have written down a snapshot of my thoughts.  I expect to change my thinking as I discover and discuss more about these issues.

I've included a sample snippet of code only.  The rest of the code is in the github repo https://github.com/guitarvydas/rt0d.

Note that the syntax below is geared for machine-readability, not human-readability.  Human-readability can be achieved by layering syntactic *skins* over the syntax below, e.g. using something like Ohm-JS.

# Generalized Overview
I am trying to rewrite our Odin0D diagram interpreter kernel in some kind of higher-level pseudo-code with the goal of performing compilation in a mostly *find-and-replace* manner using a pipeline of transformers.

The ultimate goal is to enable the use of diagrams as syntax (DaS).  This is but a step in that direction.

I think that the current crop of programming languages, like Rust, Python, etc., expect programmers to supply too much detail which detracts from the task of thinking about problems at a higher level.

I see compiling this stuff to some existing languages, like Python, Rust, etc. as a 2-stage process
1. transpile the pseudo-code into RT ("Recursive Text" base syntax)
2. transpile the RT-for-0D into some existing language like Python, Rust, etc.

"RT" is like assembler with a recursive syntax, instead of a line-oriented syntax.

"RT" contains only a few operations.  "RT" is not meant to be a general-purpose programming language.  The "meaning" of an RT program is decided-upon by a specific transpiler, like that in step 1 above.  "RT" is an attempt at "divide and conquer" - chopping up a compiler into 2 major portions, each, hopefully, simpler to create and grok than a single-piece compiler.

Transpilation in the two steps is done as pipelines of very-small (and, hopefully, very-simple) operations.  For example, my experiments with a Ceptre compiler use something like an 8-stage pipeline for (1) and a 9-stage pipeline for (2).  The Ceptre compiler is, as yet, unfinished.  This compiler (rt0d) is a different experiment, using some of what I learned from progress on the Ceptre compiler.

# Sample Code Snippets
This is but a sample.  For the rest of the code, see the repo  https://github.com/guitarvydas/rt0d.
## Pseudo-code
```
def-proto FIFO
   enqueue : Action
   dequeue : Attribute -> (Message)
   push : Action (Message)
   clear : Action
   empty? : Predicate
```
## Recursive Text
hand-translated from the above pseudo-code
```
(defstruct FIFO
  (enqueue (Action () ()) -)
  (dequeue (Attribute (Message)) -)
  (push (Action (Message) ()) -)
  (clear (Action () ()) -)
  (empty? (Predicate ()) -))
(definit FIFO/new ()())
```
Here, I am using the syntax "-" to mean *external* procedure to be found in supporting code, written in some toolbox language, like Python, CL, Rust, C, etc.

# Struct

A struct is defined by a set of *fields*.  A *field* is defined by these pieces of information:

- name 
- type 
- location

## location
- immediate
- script local
- toolbox
- #undefined

## type
Every field is evaluated using a sequential bit of code.  We have become used to calling this kind of code *functions*.  In fact, evaluation code on a *computer* is not always a true *function*, it is just a sequence of sequential instructions.

```
Action    (in) -> (out)
Filter    (in) -> (out)
Attribute      -> (out)
Predicate (in) ->
```

*Action* and *Filter* are almost the same, except that *Filter* guarantees that it does not contain persistent state.  *Action* might contain persistent state and might use the *heap*

### _destructuring input data_
fn (x:int, y:float, z:String) means that the single block of input data is destructured into 3 sub-types of data: int, float, String

### _destructuring output data_
fn (...) -> (x:int,y:float,z:String)
same as above except that it is with respect to the single block of output data

### *location* 
Then, we need to consider the location of such data, e.g. 
- temporary, e.g. on the callstack
- persistent, e.g. in the heap
- parameter, e.g. in a register or on the callstack
- result, e.g. in a register or on the callstack

### *indirection*
Then, we need to consider the indirection of such data, e.g. 
- "int" is probably immediate
- "float" might be immediate or boxed, where boxed means pointer-to-a-hunk-of-data
- "String" is probably boxed, where boxed means pointer-to-a-hunk-of-data

# "Computer" is a Misnomer
- The original meaning of *computer* is a human(s) using a pencil and paper to calculate the value of some equation
- We should be using a name that implies the true purpose of electronics-based machines, e.g. EM for *electronic machine*.
- *Computer* implies *mathematics notation* whereas full-blown EMs do not necessarily benefit from *mathematics notation*, in fact *mathematics notation* gets in the way and causes development of epicycles (such as thread-safety, preemption, operating systems, etc.)
# "Function" is a Misnomer
- EMs have registers and RAM and instructions that mutate those items.
- EMs can be used for mutation-less FP style programming, but, that is but a subset of what EMs can do.
# "CPU" is a Misnomer
- CPU - Central Processing Unit - made sense in the 1950s when EMs were very expensive and it made sense to timeshare them for reasons of cost.
- Today, though, it makes more sense to use distributed EMs, where nothing is "central".
- Today, though, it is cheap enough to make each EM work in a single-threaded manner.
- In essence, the things we call *CPU*s are really just fancy FPGAs.
- "PU"s not "CPU"s.
# Mathematics Notation
- *Mathematics notation* is based on the use of physically flat technologies, e.g. clay tablets and pointy sticks, paper/graphite/rubber
- *Mathematics notation* is tuned to disallow side-effects, thus, allowing *referential transparency*.
- *Mathematics notation* is essentially a set of rules for effecting *find-and-replace*.
- Note that computer-based tools, such as Microsoft Word, implement *find-and-replace*, but, the syntax for *find* is usually stunted.  Something better than REGEX and straight text is needed for the initial pattern-match, e.g. PDFA-based *parsing* technology, such as PEG and my current favourite Ohm-JS.
- *Mathematics notation* is *synchronous*. Function calling creates ad-hoc blocking, and, thus, argues with the enclosing operating system.  The assumption of *synchronicity* encourages the use of a shared, global callstack and the use of single stack backtraces.  Distributed systems cannot share callstacks nor employ single backtraces at the system level.
- Note that *mathematics* is more than just a notation.  The other part of *mathematics* is deep thinking.
- *Referential Transparency* can be accomplished in other ways than simply using text.  For example, electronics chips can be pulled out of a circuit and replaced by other pin-compatible chips.  Electronics tends to rely on a visual notation - *schematics* - but, achieves the same results in terms of *referential transparency* (IMO, the difference between the two notations is the use of synchrony and asynchrony at very low levels).

# Make All Aspects of EMs Syntactic
Making *all* aspects of EMs syntactic without side effects makes it possible to use *find-and-replace* to build *compilers* incrementally.  

You don't need to garner semantic information about programs and store that information in persistent tables, you form a pipeline of operators and simply chip away at the source code as it passes by, passing modified source on down the line.  The modified source contains more and more detailed information, e.g. a local variable `x` belongs to (is in the scope of) a function `f`.

# Verbatim
At some point, an operator in the pipeline will need to make a final decision and make it stick, e.g. specifying exactly what code to emit.

This kind of thing - I call it a *verbatim* - can be inserted into the code stream bracketed by special brackets, for example `«...»`.  *Verbatims* can be simply ignored by downstream operators and passed down the line.

A program is considered to be "fully compiled" when it contains only *verbatims*.

# How?
- Ohm-JS
- PEG
	- PEG can - subtly - parse something that CFGs cannot parse - matching pairs of brackets.
	- This makes it easy to imagine and implement *verbatim* constructs.
	- PEG makes it possible to create *phrases* that contain whitespace.
- CFGs discourage this kind of thinking by trying to force-fit *all* aspects of general purpose programming languages into one notation (e.g. Functional Programming).

# Self (`$`)
All functions implicitly receive *self* (syntax `$`) as a parameter.

# Parameter Names
All parameters must be prefixed by the character `%`.

Yes, this is a pain to write, for humans.  But, the goal is to create a machine-readable syntax that can be manipulated by *find-and-replace*.  Creating a syntactic *skin* that is more human-readable should be easy to do, using something like Ohm-JS.

# Temporary Variable Names
All temporary variables must be prefixed by the character `_`.

# Defstruct
`Defstruct` declares the *fields* of a struct, defining 3 pieces of info for each *field*, e.g. *name*, *type*, *location*.

# Definit
`Definit` declares an initializing function for an instance of the associated struct.  Note that this is similar to `__init__()` in Python.

# Defm
Define a general-purpose *method* / *Action*.

# Defscope
Define the scope for a temporary variable.  An RT operation.
```
(defscope _m
  ...)
```
# Defsynonym
```
def-synonym Port-Kind ~ String
```
Define a synonym that is in effect for the complete compilation unit.

Declaration-before-use is not necessary.  Declaration-anywhere is required, but, is more convenient to use and to emit automatically.

N.B. all characters, except white-space, are valid id characters.  In this case "`-`" appears as part of the symbol `Port-Kind` where the "`-`" is just another character, like any alphanumeric character, and has no other syntactic meaning ("`-`" is not a separator and does not mean subtraction in this syntax).

`Defsynonym` is a pseudo-code-only construct and is screened out in RT translations of the code.  `Defsynonym` does not appear in RT.

---

# May 20, 2023

revelation? Each field of a *struct* contains a *function*.  In the case of Attributes, the function references / destructures a privately captured lump of mutable data.  A bit of local, persistent RAM.
```
(defstruct Message
  (port (Attribute (String)) (lambda () (slot $ 'port)))
  (datum (Attribute (*)) (lambda () (slot $ 'datum))))
(definit Message/new (%p %d) 
  (mutate (slot port $) %p) 
  (mutate (slot datum $) %d))
```
So, *slot* is a reference to the captured data.

So, `(mutate (slot port $) %p)` gets the effective address of the "port" variable in the captured data while `mutate` changes the location at that effective address.

Q: should `mutate` be allowed to be used only in `definit`s, or, does it need to be generalized to be available elsewhere?  Are there 2 kinds of `mutate`, one for use only in `definit` and one for more general use?  Does this difference make it easier for the optimizer?

So, to the outside world, access to a field is *always* a function call.  Some functions are allowed to use special operations to dig deeper, but those operations are encased inside a function as far as the outside world can tell.

Normalization.  One way to do anything --> simplicity, ease-of-automation.

Context-dependent operations.  The outside world sees only one thing - a callable function, the function, though, has access to operations that cannot be accessed by the outside world.

---

# Appendix - Abridged Version

# Working Paper rt0D
..."Computer" is a Misnomer, "Function" is a Misnomer, "CPU" is a Misnomer, Mathematics Notation, Verbatim, How?...

The ultimate goal is to enable the use of diagrams as syntax (DaS).  This is but a step in that direction.

... "RT" is like assembler with a recursive syntax, instead of a line-oriented syntax ...

The rest of the note is at https://github.com/guitarvydas/rt0d/blob/main/doc/2023-05-19-Working%20Paper%20rt0d.md