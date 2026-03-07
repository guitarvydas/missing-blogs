# 2023-07-10-Gradual Optimization## Gradual Optimization

Below, are my current thoughts on a workflow for gradually optimizing a piece of code.

## GC
Garbage Collection is a generalization that makes it easer to Design a program, since you can elide all concerns about allocation and think only about the details of the Design.

But, generalization produces code that is "less efficient" than a finely-tuned solution for the specific problem.

## Round Trip
It is easier to throw information away than it is to infer and insert information,
  - "round trip" is a difficult goal - unnecessary 
  - "one way transpilation" is much easier than full-blown "round-trip"
  - if you start with code that handles allocation, you can throw away the type information to make a GC'ed version that is easier to think about
  
To design an app, one wants freedom from having to worry about allocation, i.e. one wants a GCed language.

But, to optimize the design, one needs to iterate the designed code to allow it to solve issues of allocation efficiency.

## Suggested Solution
Begin with a loosey-goosey Design and iterate it until it satisfies the needs of the user(s).

Then, iterate the code to tweak it to allow better efficiency.  Keep track of provenance with respect to the original Design.

Gradually add more type information and iterate, making the type information more precise.

To keep track of provenance against the original design and to regression-test, use a tool that maps the optimized code back to GCed code and compare it with the original design.

## What Do You Need to Know About a Variable?
- its name (if any)
- its semantic type
- its machine type
- how to allocate it
- how to clone it
- how to discard it (free it without memory leaks)

### Semantic Type
A *semantic* type is dependent on the *problem*.  A starting point might be:
- number
- string
- boolean
- pure function (lambda)
- procedure (impure function)
- user-defined type, defined only in terms of the above, but, not excrutiatingly specified at the machine level
- etc.

### Machine Type
A *machine* type is dependent on the *target hardware*.  A starting point might be:
- int32
- int64
- float
- double
- mutable array of ASCII bytes
- mutable array of Unicode bytes
- immutable array of ASCII bytes
- immutable array of Unicode bytes
- machine type signature for every field
- etc.

Note that most current hardware supports a machine type called "byte".  Yet, the lowest-level machine type is actually a "bit".

The "bit" type was more deeply explored in early hardware architectures in the form of
- 12-bit words (PDP-??, I think)
- Huffman-encoded opcodes (Burroughs, I think)

## Programming Languages for Optimization
- assembler
- C
- Odin
- Rust
- Haskell
- Scheme
- etc.

## Programming Languages for Design
- Python
- Smalltalk
- Common Lisp
- Tcl
- JavaScript
- etc.

Unfortunately, these languages are based on a single hard-wired pattern - the synchronous pattern[^fn] - and, therefore, are unsuitable for Designing distributed applications (thread libraries are the "assembler" of distributed apps, i.e. something to be abstracted, structured and avoided).

[^fn]: Any language that is based on the notion of *functions* is hard-wired to be synchronous-first.  It is possible to break the hard-wired synchronous pattern, but requires epicycles (e.g. preemption, thread libraries, etc.)

### Programming Languages for Design, Free of a Hard-Wired Synchronous Paradigm

- PROLOG, miniKanren, other relational languages

## Programming Languages Containing Gradual Typing
- Common Lisp

## Programming Languages That Can Infer Some Type Information
- ML
- Odin

Using machines to infer type information can free Designers, Engineers and Production-Engineers of some manual work.
