# 2022-06-07-WP Thinking About Orthogonal Programming LanguagesCurrently, I think that *operations* are separate from *operands*.

*Operations* are "syntax".

*Operands* are OO objects.

Note that the assembler statement
```
MOV R0,R1
```
is a *triple*.

relation X subject operand X object operand

Cordy's thesis was about Orthogonal Code Generation.  Based on assembler.

Today, I believe that Ohm-JS makes it possible to split, yet again, *operations* from *operands*.

Ohm-JS gives us easy access to syntax.

We already know about OO objects.

# What Are Operations?
Are *operations* just bigger objects?

Operations are, essentially, *compositions* of *operands*.

Do we *need* to invent artificial objects to hold *compositions* of objects?

If we have access to bowlfuls of syntax, then, no, we can build operations at will.  We can compose objects into larger entities and don't *have* to call them *objects*.  

It may turn out that compositions of objects are just bigger objects, but using Orthogonal Programming Languages might give us a way forward to explore.

Currently, I think of *compositions* of objects as *Components*.  Components, in my mind are async - 0D and simultaneous (concurrency == 0D+simultaneity, IMO).  

If you have 0D, you can make sensible drawings.  [Suprise: I think that hybrid-diagrams are a better syntax for programs than pure-text.]

I wouldn't be surprised if Ackley's stuff relates directly to 0D, but I haven't gone down that path.

# Forcing Only One Paradigm

Currently, I believe that it is folly to use only one paradigm to describe a program.

I might turn out to be wrong, but I would rather let the unifying paradigm emerge than force programs into a box.  

Kinda like anti-premature-optimization.

We saw leaks and whack-a-mole when studying PLFA.  They kept inventing new syntax for operations on lower-level concepts.  Continuing to use pure-text for that kind of thing is like asking for global variable deja vu all over again.  Diagrams express Russian-doll containment better than text does.  Wrapping things in Lambdas only works so far until your eyes start to glaze over.

The Global Variable problem was solved by containment.  The only reason that global variables were a problem is that a pure-text syntax was used.  The syntax allowed leakage.  Text-based programmers had to be very careful.  Later, the idea of "structured programming" was published and showed us how to use pure-text to do containment.  If we had used diagrams, nono-containment would have been obvious.  We couldn't use diagrams because of N0D (synchrony, all programs are highly-connected gearboxes).  Switching to and thinking about 0D makes diagrams (and containment) easy to express.

ATM, I find it easier to *think* about a problem and develop it and express it in draw.io.  After that, I can hand-transpile the diagrams to code in N0D languages.  In fact, I've been drawing diagrams, then hand-transpiling them to fugly text, then using Ohm-JS to crank out JS/Python/Lisp code for me.

This is part of what I learned beeing interested in compilers.  At first, assembler programmers thought that HLLs were inefficient.  Assembler programmers could hand-craft code that blew away most normalized compiler-emitted code (SmallC).  Then, GCC came out and blew away all the old assembler programmers.  Then, the old assembler programmers retired and, now, no one bothers to use assembler to express high-level thinking anymore.

See Also

## 2022-06-06-Toolbox and Orthogonal Programming Languages

I present a *toolbox language* that is an intermediate text form for programming, based on syntax stacks, which allows programming to be *divided and conquered* at the syntactic level.  

I, also, introduce the notion of Orthogonal Programming Languages, which is meant to allow designing programming languages using *divide and conquer* by dividing PLs into two phases 
	- operations
	- operands.
