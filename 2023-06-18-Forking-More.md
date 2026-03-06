# 2023-06-18-Forking-More# Previous Essay

https://publish.obsidian.md/programmingsimplicity/2023-06-11-Fork

# Forking - More Thoughts

Forking is what GitHub supports.  I was trying to use a word that might already mean something to someone.

JS does forking.  

Forking is “prototypal inheritance”.  

The language “Self” explored the issue of prototypal inheritance.  

Self “invented" JIT compilation.

The precursor to JIT-like compilation was *fastcalls* in some Lisps.

Most languages jumped right over prototypal inheritance to class-based inheritance.  Prototypal inheritance is the dynamic version of inheritance.  Class-based inheritance is an optimization of prototypal inheritance which allows inheritance to be calculated at compile-time. Class-based inheritance requires describing solutions in a way that appeases compilers and makes the solutions fall in line with what is convenient for the class-based language compilers.

Note the significance of the above.  JIT compilation might not have been invented if only class-based inheritance was available.  I include other inventions like REPLs in this invented-using-dynamic languages.  I believe that Haskell was first envisioned using Lisp.

In my opinion, class-based inheritance encourages premature optimization and discourages coming up with fresh ideas for solving problems.  

It is - obviously - possible to take dynamic inventions and to re-express them in optimized form.  Often, with enough thought, it is possible to take the dynamic-ness out of designs and to make them compile-able.  

Compilation is the idea of pre-processing programs to move some of the code - usually things like type checks - out of the runtime code and into the pre-processor code that runs at "compile time".  Pre-processing uses up more CPU cycles than dynamic checking, and, it uses up more human brain cycles in trying to figure out how to do the preprocessing.  It is hoped that this extra work can be amortized over the runs of the final program with the net result being more economical.  Hard work done up front can be removed from the 1,000,000 times that the resulting final app is run, making the final app "faster" and "cheaper".

Yet, compilation is but an optimization.  We all know that premature optimization is bad.  In this case, premature optimization cuts off design ideas at the knees and forces designs to take a certain shape.  Things like JIT compilation and REPLs are easier to *imagine* without premature optimization.  Once a first-cut is made, it can be optimized.  If you optimize too soon, the first-cut becomes so laborious that you end up avoiding ideas that should be otherwise obvious.

## How Drawware, ė, Diagramming Are Related to Forking

Diagrams are nice, but diagramming doesn't fit all situations.

The Sequential Pattern is nice, but it, too, does not fit all situations.

The ground truth is that *everything* is *asynchronous* and *decoupled* at first.  You can layer skins over this ground truth to emphasize certain aspects of a system.  Physicists call this layering "simplifying assumptions".  

Once you discover a *skin* that works for a certain aspect of a solution, does that mean that that same *skin* is *good* for expressing other aspects of *every* system?  Does it mean that the same *skin* should be applied to *every* aspect of the same solution?

No.

Text is good at expressing things like `a = b + c`.  Diagrams are more verbose and bloated for things like this.

Diagrams are good at expressing things like networks of nodes.  Text is not so good at this kind of expression.  

Example: you rarely see someone whiteboarding a computer network by writing text and tables on the whiteboard, they usually use boxes connected by arrows.  In fact, they usually use a hybrid expression - diagrams annotated with bits of text.

Another example: business ORG charts are usually laid out as diagrams.  These diagrams express very simple aspects of how businesses are structured.  (ORG charts also relate to *Structured Message Passing*, but, I regress). 

When most people draw diagrams containing a bunch of rectangles connected by arrows, they implicitly assume that the boxes are completely isolated. "Asynchronous" in programmer lingo.  When programmers try to transcribe such diagrams to code, they run into problems.  That's because *code* contains a hard-wired Patten - Synchronocity/Sequentialism - which conflicts with the implicit assumptions contained in the diagrams.  Once you have one underlying Pattern, layering other Patterns on top of the hard-wired Pattern is just plain difficult.  When expression becomes sluggish, don't persevere and continue using the same Pattern - switch to another Pattern.  Insanity is doing the same thing over and over again while expecting different results.

Simplifying assumptions have a *sweet spot* that makes them good for expressing certain ideas and makes them cumbersome for expressing ideas outside of their *sweet spot*.  When you take a *simplifying assumption* too far and try to solve *every problem* with it, you turn the assumption into a *religion* and a *fad*.  I would suggest that this is what has happened to programming.  The Sequential Pattern - a *simplifying assumption* - has been taken too far.  The result is bloatware and epicycles, like thread libraries, preemption, function calling and the huge size disparity between most programming languages and tiny languages like Sector Lisp and BLC.

What is today's *fad*?  The idea that *mathematical notation* is applicable to every problem.  Mathematical notation (notation, not thinking) was designed for use on clay tablets and papyrus, not computers.  Can mathematical notation be used to model computers?  Yes.  Is this a good idea? No.

Gedanken experiment:  If you want to see *notation worship* at work, just suggest that static type checking is a bad idea.  Bible thumpers will howl at the notion. Notice how programmers conflate *coding*, in textual, function-based form, with *programming*.  Most programmers cannot even conceive of controlling a computer using anything other than a textual language.  Textual languages are clumsy IDEs for programming, invented in the 1950s based on the limitations of 1950s hardware.  Again, the ground truth is that computers are isolated bits of electronic machines that start out life as being completely *asynchronous*.  Textual coding is only *one way* to program computers and to get computers to do what you want.