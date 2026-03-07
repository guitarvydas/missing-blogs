# 2022-05-30-Lisp  Smalltalk and the Power of SymmetryResponse to blog post: https://insearchofsecrets.com/2014/08/04/lisp-smalltalk-and-the-power-of-symmetry/

[Meta: A note on style - I write in a style that is different from academic "papers".  I believe in "showing my work" and in brainstorming.  Nothing I write should be construed to be true in the absolute.]


# Quotes
> Lisp has no syntax. You write programs in the parse trees

I agree.  

Lisp has no syntax.

![lisp-parse-tree.png](lisp-parse-tree.png)

Everything in Lisp is a parse tree, in prefix form.


> Are macros the only possible way to make programs that write programs, or might there be others?


Compilers are programs that write programs.  

Text->assember.

/bin/sh (/bin/bash, /bin/zsh) are programs that write programs.

Lisp macros are "more convenient" to use than full-blown compilers.

PEG is a way to write programs that write programs.

LR(k) (YACC, Bison, etc.) is a way to write Language Specs that can then be used to write programs (parsers for the languages).

Writing parsers from specs is different from using DSLs to write parsers.  LR(k) is a language spec.  PEG is a DSL for building parsers.

> It may seem strange to compare object-oriented classes to Lisp macros.

Yep. 

This kind of thing only works if you conflate programs with data.

Programs are one kind of data.  

GUIs (graphics) are another kind of data.

Can you treat Programs the same way you treat GUIs?  I don't think so.

> class inheritance becomes nothing more than a tool for code reuse

Not if you ask true-blue Smalltalkers.

Smalltalkers try to convince you that code reuse should take a back-seat to "semantics".

I think that the above is just a symptom of the fact that Code is different from GUIs.  They need different kinds of data structures and different kinds of treatment.

One size does not fit all.

Smalltalk inheritance is good at describing GUIs.

Other ideas, like OCG and RTL, are better at describing Code.

> The real power of Smalltalk’s [object system,](http://www.smalltalk.org/articles/article_20100320_a3_Getting_The_Message.html)including its classes, is not inheritance–it’s _reflection._

I think that this is, yet another kind of data structure.  

An IDE for exploring Design...

What is the "best" data structure for iterating Design thoughts?  REPLs and Reflection.

> Smalltalk is powerful because _all Smalltalk data are programs_

Sigh.

> Class programming in Smalltalk

Classes are just optimized versions of *prototype inheritance*.

If you want to pre-compile *inheritance*, you use classes.

If you want to explore the design space of a problem, you don't bother with pre-compilation...

> Class programming in Smalltalk is simply data manipulating programs that are themselves data–it’s the inverse of the Lisp philosophy, but the end result is the same.

You can write programs that write programs without using Classes nor Macros.

I believe in FDD (Failure-Driven Development).  Writing programs that write programs is a fundamental of FDD.

> because Lisp source code is expressed in the same form as running Lisp code, which is expressed in the same form as Lisp data, the three are interchangeable

Not quite.  

Expressing Code as some kind of data structure, then building a Language/Library to manipulate that data structure makes writing programs that write programs easier.

Macros and Classes are not vital to the idea of writing code that writes code.

Macros and Classes are ways that you organize programs.  If your programs are meant to write other programs, you are building complicated programs.  You want to pull out all of the stops and use whatever organizing tricks that you have up your sleeve.

> So Lisp macros aren’t the only way that programs can write programs

Right.  

Currently, I'm using JavaScript to write programs that write programs.

Actually, currently, I think that Ohm-JS is a wonderful way to write programs that write programs.

I've written myself a tool, that I call *prep* that hangs off of Ohm-JS to help me.

> If a language allows programs and data to be treated as the same thing

IMO, there is no "one language to rule them all" and it is silly to think that you can collapse ALL possible programming desires into one language. 

Programming cashflows, balance sheets, etc., is (currently) best done with Spreadsheets.

Programming spreadsheets is best done in some programming language, like Rust, C, Python, etc.

Analyzing programming is best done with theorem-provers and AGDA, and ...

Analyzing a problem space is best done with a REPL.

You can't do ALL of the above using only one programming language.

Lisp and Smalltalk are good at certain kinds of programming.

Trying to force ALL of programming into just one of the above languages is just silly and leads to epicycles and bloatware.

Programmers mouth the phrase "divide and conquer" but don't really apply the principles.  If they really believed in "divide and conquer" they wouldn't waste their time on the quest for "one language to rule  them all" and would concentrate on how to build solutions using many programming languages (incl. many syntaxes, not just text).

# Lisp and Smalltalk Commonality
- lack of syntax
	- due to mid-1950s fear of parsing
- based on 1 CPU model
- synchronous-under-the-hood
	- they got away with pervasive-synchrony because of the 1 CPU model
	- why pay for synchronization when you don't need it?
	- synchrony is counter-intuitive to humans, which is (at least) one reason why "programming" is considered to be "difficult".

# Good
- dynamic languages
- REPL
- reflection
- lisp is assembler, but, makes it easy to create anonymous functions

# Bad
- lisp is assembler
- Objects are not a good way to organize control-flow (but, Objects are a good way to organize data)
	- inheritance, et al
	- programmers break locality of reference to force-fit classes onto control-flow
	- programmers faced with the conundrum of using inheritance for code-sharing vs. using inheritance for semantics reasons (lots of early literature about this issue - should have been a *tell* that something was fishy)
- classes are prematurely-optimized prototype-inheritance 

# Lisp "Syntax"
Lisp "syntax" is prefix-based.

Some people really hate this, others love it.

Assembler programmers used to love assembler and hated high-level languages like C and Pascal.  (Thankfully, they retired and, now, just about no-one uses assembler to create interesting programs).

# Smalltalk "Syntax"
No-parenthesis syntax for function args.

Function name is a normal ID.

Parameters are named with ":" IDs.

Smalltalk syntax allowed building of cheesy parsers for Smalltalk "syntax".

# Smalltalk Lie About Message-Passing
- Smalltalk does not "send" messages.
	- Sending requires the sender and the receiver to be in separate CPUs (separate processes, if you have to fake separate CPUs on 1 CPU)
	-  Smalltalk uses CALL/RETURN
	- CALL/RETURN is synchronous
	- CALL/RETURN usurps responsibility for *blocking* from Operating System (Operating Systems need to resort to using a sledge-hammer (preemption) to get back control of *blocking*)

# Lisp Macros Came From FEXPRs
Early Lisps had FEXPRs.  

This works for dynamic languages and allowed imaginations to soar and resulted in the invention of macros.

The premature-optimization clique expunged FEXPRs with a vengeance.

They tinkered with Lisp until it became compilable. 

They won.

Now, almost all languages employ premature optimization.  Programming language syntaxes are warped to support premature optimization instead of design exploration.

Downside: Pre-Cambrian Explosion style of free thinking was drastically restricted and diminished.  "New" languages were all basically the same - synchronous-under-the-hood, no REPLs [^vscode], and, confused about the distinction between data-flow and control-flow, bloatware, notation-worship instead of faithful modelling of CPU operations.

[^vscode]: VSCode still sucks as a debugger, compared to better Lisp debuggers (I don't mean SBCL/Slime).

# First-Class Functions
In Lisp, (lambda (x) ...)

In Smalltalk, [x | ...] (called "blocks").

"Closures" were invented, later, as a way to create first-class functions at compile-time.

McCarthy used something called ALISTs that were simple to understand and implement and, didn't need compilable closures.  

If you want to see how beautiful the FP paradigm can be, study Sector Lisp.  (GC in 40 bytes, no mutation) [I made a silent video of the GC in attempting to understand it.  I will gladly share...   I, also, made a lot of notes as I was having AHA moments and I implemented (hacked together) Sector Lisp in Python to better understand its workings and its smallness.]

Note that "processes" in Operating Systems are simply ad-hoc implementations of first-class, nested functions (closures, if you wish).  See Greenspun's 10th Rule.

# CONS vs. List Objects
CONS is simpler and "more efficient" than any other implementation of Lists that I have seen.

CONS assumes no mutation.

List Objects tend to use mutation.

CONS tacks new items onto the front of the List.  Structure sharing is implicit.  

![CONS-structure-sharing.png](CONS-structure-sharing.png)

In *pure* FP, everything happens in a stack-like manner. 

Mutation - heaps and GC and assigment and ... - inhibits stack-like behaviour and implicit structure-sharing.

# The Kitchen Sink Environment
The Soup.

Both, (early) Lisp and Smalltalk work on an environment-based basis.

All functionality is available at all times.

No declaration-before-use.  If it's in the environment, you can use it, even if you put it in the environment later.

"Environment"-based languages are "dynamic".  These kinds of languages support Design and inhibit Production Engineering (AKA compilation, optimization).

"Static" languages promote Production Engineering and inhibit Design.

The ideas of REPLs and Reflection were invented in "dynamic languages".  Later, attempts were made to bring these concepts into the world of premature optimization.

# Bret Victor
I think that Bret Victor is simply pointing out that Design matters. 

And, that Design-oriented languages matter.

This, to me, comes back to some of the ideas of Lisp and Smalltalk.

I sum up Bret Victor's Worry-Dream ideas as:
1. stop using grids of sequential, non-overlapping small bitmaps (characters)
2. use REPLs

# Schizophrenia
Lisp and Smalltalk are schizophrenic.

It was/is believed that there must be "one language to rule them all", and, Lisp and Smalltalk tried to cover all of the bases in the continuum from Design to Production Engineering.

Along these lines, we see extremes like JavaScript (Design, I guess) vs Rust (The Trains Run On Time).  And little in between.

And, then, we are faced with the problem that the 1950s 1-CPU model doesn't work so well on the internet.

# Encapsulation
Lisp: LAMBDA

Smalltalk: Objects

Lambda Calculus: LAMBDA

Schizoprenia: control-flow vs. data-flow.  "Encapsulation" applies to data.  "Processes" apply to control-flow.

[aside: I think that Cordy's thesis about Orthogonal Code Generation is on the right track.  Control flow is "syntax" and data-descriptors are OO objects.]

# Atoms
Lisp: everything is a CONS cell.

Smalltalk: everything is an Object.

Lambda Calculus: Everything is a callable function (or a set of them).  UX doesn't matter, rigor trumps UX.

# Fads - Data in Lieu of Control-Flow
> there is no distinction in Smalltalk between data and programs

If this were such a great idea, everyone would be using Smalltalk.

Q: Why isn't everyone using Smalltalk and data-only-ness?  

IMO: Obviously, something is wrong with this idea, and programmers "feel it in their gut", even if they can't put their finger(s) on the reasons.

IMO: Part of the problem is that programmers are indoctrinated to believe that optimization trumps UX.  Part of the problem is that programmers are indoctrinated to believe that "programming is just a hard problem" and cannot see the brain-damage that pervasive synchrony has caused.  Big Pharma, step aside.  Big CSC needs elbow room in the Ivory Tower.

# Do You Need Macros if you have Objects?

IMO: Yes.

I think that it is a mistake to conflate conrol-flow and data-flow into a single notation.

Cordy and GCC got it right.  It is much easier to build big programs if you treat control flow and data flow as two completely distinct things ("orgthogonal").

Cordy wrote his thesis on Orthogonal Code Generation.  GCC used the idea of RTL from Fraser-Davidson, in essence a subset of OCG.  [Fraser-Davidson called it "peephole optimization".]

Lambda Calculus is an over-reaction to the attempt to force everything into a single paradigm.  The flavour of the month is "everything is a function" (a λ).  Another name for this phenoma of extremes is "whack-a-mole".  Lambda calculus is great if you ignore the inconvenient detail of UX[^hedberg].

[^hedberg]:https://www.youtube.com/watch?v=UH9tOfwg06I

# Conclusion
I think that the article points out the need for "dynamic languages" in addition to "static languages".

There are thoughts-you-can-think in "dynamic languages" that you can't think in "static languages".

## Practicality

I suggest that one be aware of what "goal" one has:
1. Are you trying to figure out what the requirements are, what the problem is, how to attack it?  Iteration. Design.
2. Are you trying to Production Engineer a deliverable?  Already-working code, making it lower-cost in some dimension.  Compilation.

(1) and (2) use completely different skill sets.  (1) usually uses whiteboards because there ain't no decent languages for Design[^sync].  Other disciplines have figured this out, e.g. Structural Engineering (Architecting, Engineering, Construction).

[^sync]: Currently, I conclude that pervasive synchrony is evil.  Theorists use pervasive synchrony to fulfill their goals (analysis).  They have - somehow - convinced programmers that *all* programming languages should employ pervasive synchrony, to the detriment of Design.

Can you use two completely different languages/technologies for the same project?  AI does it - Python for the coordination layer and then drop down to souped-up hardware for the nitty-gritty, speed-uber-alles stuff.

Lisp and Smalltalk have been around for a while.  I know that Lisp can break out to C/Assembler (FFI) when it needs speed and non-Lisp libraries.  I imagine that Smalltalks can do that, too.

A not-yet-existing IDE would be able to plumb various languages together.  UNIX pipes were heading in that direction (but then were bloatified).  I haven't dug into Tunney's APE stuff, but, I wonder if that is heading in the right direction (by "right" I mean multi-lingual).

For now, UNIX pipes are the way to go (for multi-lingual solutions).  Messages and recursion ain't the same thing.  Messages are queued up in a FIFO manner whereas recursion passes data (arguments, bindings) in a LIFO manner.  Recursion means synchrony, messages mean asynchrony.
