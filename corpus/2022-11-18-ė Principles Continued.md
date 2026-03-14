# 2022-11-18-ė Principles Continued
> can a function change the values of the free variables in it's closure? 

No.  If you want to change a value, that is "mutation".  Use another notation, don't try to butcher the FP mutation to add "mutation".  

I would not be surprised if adding "mutation" to FP is the cause of bloatware.

Mutation is necessary, but, ad-hoc mutation is bad.

Pick off mutation use-cases and give them each a unique syntax.

For example, HSMs are a use-case for mutation.  A "state" is a valid reason for needing mutation.  HSMs wrap "state" with syntax that allows "state" but puts a constraint on what you can do with "state", e.g. update it, check it/case on it (making sure that you've addressed every possible angle).  The "update" operation can check that only "state" is being updated and does not allow more ad-hoc use of variable mutation.  The case-on-state operation can insist that you list every possible state and explicitly write code for each (including "pass"), instead of something more ad-hoc like "if-then-else".

> ...What's your definition of closure? ...

I use the terms "closure" and "anonymous function" interchangeably.  The correct meaning of closure is more restricted than "anonymous function" - closures are arranged so that they can be pre-compiled, whereas "anonymous functions" cannot be - in general - pre-compiled.

McCarthy's Lisp 1.5 invented "anonymous functions" (he called them Lambdas).  McCarthy's "anonymous functions" had to - in general - be interpreted.  Later, it was found that a certain use-case of "anonymous functions" *could* be pre-compiled (pre-compiled ≣ "static") and everyone jumped on that bandwagon.

I am not so sure that pre-compiling is *always* a good thing.  For example, I find it to be OK to use interpreted languages to give me "more power" during development.  I wouldn't want to leak interpretation out to end-users, so I would want to compile developed code into a smaller/faster product for end-users.  I argue that worrying about pre-compilation too early in the development process is bad, it is "premature optimization" and stunts what your imagination.  The pre-compiler might be some kind of *barnacle* that ingests working code and spits out smaller/faster working code.  *Barnacles* might be invented for helping developers, e.g. type checkers and *lint*ers.  Twisting a language design to appease *only* pre-compilation is *not OK* in my book.  At the moment, all of our programming languages are compiler-appeasement languages and insist that developers waste time (and imagination) on dealing with compiler-appeasement and pre-compilation issues, long before the program works.

Barnacle-like pre-compilation was researched in the mid-1900s with work like Fraser/Davidson peephole technologies[^rtl].  This was called RTL and formed the basis of *gcc*.  Cordy's Orthogonal Code Generator is another work along these lines.

Peepholing is *so easy* that I built a peepholer using *AWK*[^awk] for my Small-C-like compiler (for the 8080).

Cordy's OCG defines a declarative tree structure, called MIST, for choosing code sequences that line up with what the target is capable of doing, i.e. declarative portability.

RTL and OCG work in 2 passes.  In pass 1, generate code for a ficticious architecture. Then in pass 2, clean up the code for a specific architecture.  RTL treats *everything* as a *register* in pass 1, Cordy's OCG uses something more general (but equally abstract) called Data Descriptors and Condition Descriptors.

Data Descriptors  embody *allocation* information in the data structure, i.e. is the datum a function parameter?, is it a temporary?, is it on the heap?, should it be put in a register?, etc., etc.  Compilers need to figure this kind of stuff out anyway.  DDs embody such hard-won knowledge in the DD notation itself.  In my mind, this leads to simplification, e.g. if you want to deal with the issue of *allocation*, you simply concentrate writing code *only* for that issue and augment the DDs.  *Allocation* becomes a filter that tweaks DDs.  The allocator breathes in generic DDs and spits out DDs containing more information.  Everything else is ignored and passes through unfiltered.  Further, if your DD notation is syntax-based (a DSL), then the job devolves into a job of pure text manipulation.

I, currently, think that *all* programming languages should be based on *orthogonal* principles:
1. operations (syntax)
2. operands (OO objects+methods).
I think that OPLs (Orthogonal Programming Languages) would simplify language design and make it easy to create SCNs (little DSLs) in an afternoon.

I believe that lifting developers out of the 1950s and into the 2022s will leak into the writing of better apps for end-users (the trickle-down theory of Computer Science :-).

People who know me, know that I champion the use of diagrammatic programming languages.

Yet, the above discussion appears not to be related to diagrams.

Why?

It's because diagrams - in my mind - are just syntax.

When I want to write `a = b + c`, I write it in text form.

When I want to write a wrapper that encloses a piece of code, I want to draw a box or a circle.  I don't want to write this kind of thing in text (e.g. *lambda*).

[^rtl]: https://www.researchgate.net/publication/220404697_The_Design_and_Application_of_a_Retargetable_Peephole_Optimizer
[^ocg]: https://books.google.ca/books/about/An_Orthogonal_Model_for_Code_Generation.html?id=X0OaMQEACAAJ&redir_esc=y
[^awk]: https://en.wikipedia.org/wiki/AWK

