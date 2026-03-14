# 2023-07-17-What are the Steps in Creating a Compiler?## What do we need to know to compile a piece of code?

- phrasing (parsing, syntax)
- type system information gathering
- type system consistency checking
- data allocation
- mapping control flow to the most efficient use of specific CPU opcodes

---

## Further Discussion

### Data Allocation
Try to answer the question: for each piece of data, can the data be most efficiently located in a register, stack, heap, file system, cache, etc.?

Note that there are, also, low-level allocation issues - is the data int8, or int16, or int32 or int64 or float or double, or ...? Divide and conquer: don't worry about the low-level details until the high-level details have been covered off.
  
### Mapping Actions to the Most Efficient Use of Specific CPU Opcodes

This is also known as *code emission*.

This deals with *control flow*, not *data structure*.
  
Code emission can be done in two phases, as per Fraser/Davidson's RTL or Cordy's OCG
	1. generate dumb code for a virtual target
	2. optimize dumb code for a specific target 

N.B. this is "divide and conquer" in action.

Optimizing dumb code for a specific target, (2), is a purely textual transformation

Control flow and data structure are *orthogonal* concepts.  This is quite obvious when you look at assembler.  Assembler has *opcodes* and *operands*.  The "best" architectures keep a strict separation between the two concepts (e.g. PDP-11, NS32016, etc, etc.).  We already know how to construct *operands* - i.e. OO.  And we already know how to deal with *control flow* - syntax.  Ohm-JS and PEG make syntax even easier to deal with. 

FYI, RTL is used by GCC, Cordy's OCG is a generalization of the concept.

The OCG thesis does not specifically speak about RTL.

- OCG ≡ Orthogonal Code Generation
- RTL ≡ Register Transfer Language

The RTL paper says to use a simple "peephole optimizer" in phase (2).

I built a peephole optimizer in AWK and got it working.  This is a very simple technique, even simple enough for me to understand.

GCC goes beyond using just RTL to, also, using Dragon-Book concepts for globally optimizing code.

Many dyed-in-the-wool assembler bigots retired soon after seeing that GCC could produce code as good as, or better, than they could produce manually.  

I would not be at all surprised if a similar thing happened to FP and CPS bigots in the next few years.

### Denotational Semantics

Denotational Semantics is a functional way of specifying control-flow mappings.

My favourite book on Denotational Semantics is Peter Lee's "Realistic Compiler Generation" https://www.amazon.ca/Realistic-Compiler-Generation-Peter-Lee/dp/0262121417 

- ---

## Why Should I Care?

What are the benefits of building compilers better and faster?

### Hours, Instead of Weeks / Months / Years

A goal of making compiler-building cheaper is that DSLs, and what I call SCNs[^scn], make it easier to *imagine* and trivial to build.  Current programming languages encourage Waterfall Design methods.  *Imagining* new ideas and starting afresh (deleting all existing work) is the antithesis of Waterfall thinking.

Using better - more suitable - notations means that problems can be solved differently.  Instead of force-fitting a single notation, e.g. Rust, Python, C++, etc. - onto a problem, the problem could drive the notations that are used.  The problem should drive the notations used to solve it, instead of allowing a notation to drive the solution.  

Multiple notations could be used within the same solution.  For example, if part of the problem includes a *search*, then PROLOG-y syntax is useful, and, if part of the problem includes formatting output then Python `"{...}"` (and JS and /bin/sh) syntax is more appropriate.

The tooling problem becomes one of designing IDEs that accommodate multiple notations and plumb the multiple notations together into whole solutions, instead of force-fitting a problem into a *single* language style.

After all, textual programming languages are simply 1950s IDEs for programming computers, invented before computers supported windowing and distribution.  

Continuing to use sequential, textual programming languages in 2023 is like Groundhog Day all over again.

[^scn]: SCN == Solution Centric Notation.  Syntax is cheap.  Physicists create unique notations to think about specific aspects of problems. Software developers could do the same, i.e. programmers could invent new notations in an afternoon, and use multiple notations to divide-and-conquer parts of any problem, instead of force-fitting a single notation (Rust, Python, C++, etc.) onto a whole problem and solution.
## How To Cheat?
Obviously, building a full-blown compiler for every SCN involves a lot of work and time.

How can we drastically reduce the turn-around time for this process?

One way is to do what Alan Kay said:
31:50 "In a 'real' Computer Science, the best languages of an era should serve as 'assembly code" for the next generation of expression.
[https://www.youtube.com/watch?v=fhOHn9TClXY&t=859s](https://www.youtube.com/watch?v=fhOHn9TClXY&t=859s)

Allocation and code emission have been already handled in a plethora of languages.  It seems to me that Common Lisp provides the most generic toolkit for compiler-building.

At first, the act of type checking can be punted to the runtime.  There is little need to do full-blown, static type checking in early stages of software product development.  Static type checking can be viewed as an optimization that is needed only during Production Engineering, the final step in creating a software product.  Static type checking is essentially a transpilation process that converts high level code into unchecked assembler. 

The act of creating new syntaxes can be handled using advanced parsing technologies, like Ohm-JS, PEG, etc.  It appears that ChatGPT can perform transpilation from one language into another, as long as both, source and target languages are well understood by ChatGPT.  

I'm experimenting with both approaches - Ohm-JS based transpilation and ChatGPT based transpilation.

# See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity (see blogs that begin with a date 202x-xx-xx-)
- https://github.com/guitarvydas
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
WIP - leanpub'ed (leanpub encourages publishing books before they are finalized, inviting feedback)
https://leanpub.com/u/paul-tarvydas
### Discord
https://discord.gg/Jjx62ypR
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice sought)
