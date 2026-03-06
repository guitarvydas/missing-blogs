# 2023-05-26-Response regarding Call-Return Spaghetti
  > I think having to duplicate the code inside every time you clone a component is a non-starter. 

Components are like Classes.  The code is not duplicated.  Instantiated, yes, duplicated, no.

Even if code gets duplicated, it *is* a starter, not a non-starter.  The *premature optimization*, *efficiency-first* meme makes one think that this is a problem.  If you take this *premature optimization* argument to its conclusion, you must conclude that no assembler program should ever use more than one `LOAD` instruction.  Clearly, we allow compilers to use `LOAD` more than once.  At some point, we implicitly decide not to apply the *premature optimization* argument and to allow compilers to automatically clone code and boilerplates and instructions.

The code that runs inside a component is merely a form of assembler (aka boilerplate).  The compiler should be free to clone the code or inline the code at will.

I wonder if this point needs more clarification?  Here's another try: Python, Rust, Odin, etc. are simply *assembler* instructions for some higher-level notation (Alan Kay 31:50 https://www.youtube.com/watch?v=fhOHn9TClXY&t=859s).

Or, maybe there is some other meme at play here that is making this seem more complicated than need be.  Maybe I haven't put my finger on this meme and squished it out of existence.
  
> You say, "deduplicating code is a compiler concern" ([https://publish.obsidian.md/programmingsimplicity/2023-01-24-0D+Ideal+vs.+Reality](https://publish.obsidian.md/programmingsimplicity/2023-01-24-0D+Ideal+vs.+Reality)) which feels handwavy. 
> ... Compilers are rocket science, ...
  
It used to be the case that compilers were difficult to build.  In 2023, though, compilers are "easy" to build.  You need hash-tables (aka maps), pattern matching, backtracking, RTL/OCG.  Those technologies all exist today, and, are viable on today's hardware.

Pattern matching can be used to detect duplicated code and to deduplicate it.  GCC does it using RTL (Fraser/Davidson).  Cordy's OCG generalized the concepts.

PEG parsing has reinstated a once-verbotten technology (backtracking - Early's parser, PROLOG - exhaustive search - miniKanren, core.logic), which opens the door to making pattern matching simple again, as opposed to  otherwise oppressive CFG technologies.

  > ...
  > risking lots of performance _regressions_...
  > ...
  
There's that *premature optimization* meme creeping in again.  Current programming languages, like Python, Haskell, Rust, Odin, etc, etc. emphasize *performance* at the cost of *design*.  These languages conflate design and optimization and put the onus on programmers to manually rearrange code to appease compilers to help compilers optimize the code.  What is needed is a language(s) that gets out of the way during design then allows incremental optimization (aka "typing", etc.) in places where performance matters (probably only about 5% of the code).  Lisp used to be on this road.  The mad rush towards static typing tilted the tables away from *design* towards *optimization*.

End-users don't care if developers use static typing or not.  I argue that end-users care about:
1. robustness
2. low cost
3. simplicity.

Optimization-first languages, like Python, Rust, Haskell, Odin, etc., deal only with issue #2.  That's only 33% of the problem.  Note that robustness means different things to Production Engineers vs. End-Users.  Production Engineers want to optimize designs specified by Architects (and Engineers), whereas End-Users just don't care, they want programs that work and don't crash and that fit their needs.  Architects need to figure out what those needs are - Python, Haskell, Rust, Odin, etc, don't help Architects determine what those needs are, they only help map (possibly-wrong) understandings-of-the-needs to working code.  If the understanding of the needs are "buggy" then, the results are buggy/unsatisfactory from the End-Users' perspective.  If the End-Users are provided with apps that encounter crashes and security problems, then the results are buggy/unsatisfactory from the End-Users' perspective.  Python, Rust, Haskell, Odin cannot help with those kinds of problems.  (Yeah, we might have gotten rid of buffer-overrun errors, but we haven't gotten rid of phishing attacks (those a bigger problem than anal-retentive improvements in type checking techniques)).

> As a consequence it seems to me that components are strictly higher level than functions. 

OK, if you say so.

> 
> You don't want to put raw code inside components. 

Why not?

Code as we know it, is just *assembler* for better languages.

> Stick a function call into the component,

Lambda-calculus agrees with this point.  Make *everything* a function, remove syntax.  Something called Lisp already did this in 1956.

> Calling these things zero-dependency is not quite accurate. 

Hmm.  I think that *dependency* is a serious problem.  I identify at least 3 ways that *dependency* creeps into current-day code.  Most people see *dependency* as something higher-level - system level - and attack it with epicycles like *dependency injection*.  I try to show that low-level *dependency* exists, is pervasive and is hurting software development.

> As you define it, hardwiring the name of a function call is a dependency. 

Actually, I don't *define* it, I simply *observe* it.

> But you have names of components like `echo` hard-wired into your example. 

Yes, you are correct, my current suggestion includes hard-wired names of components in one part of a 2-level structure - in Container Components, but, not in Leaf Components.  Containers can only name their own children, not their peers.

This is an interesting comment, indicating that maybe more work is needed in this direction.  Maybe my interest in Ceptre is implicitly based on some sort of gut-feel about this issue.

Note that Ceptre and my Containers do not do away with explicit names, but do try to lasso them and to provide scoping for Component names.  The hard-coded names appear only in small units of programs that can easily be replaced like LEGO® blocks.

Note that this scheme tries to encapsulate names.  Only Containers are allowed to name components, and, they can only name components that are direct children.  Containers cannot name peers, or grandchildren, or, ...

>...You just need a better name and positioning to avoid these distracting quibbles and focus the audience's attention on the core idea. ...

@Marcel Weiher made a similar comment.  I argue that the *technical issue* being addressed is *low-level dependency*, but, I agree that a better name for marketing purposes might be needed.  I'm open to suggestions from anyone.  An earlier version of this stuff was called *Arrowgrams*.

> ... Might you need coroutines? ...

These ideas are definitely related to coroutines.  And, green threads, and, mutual multi-tasking, and, closures, and pipelines, and Actors, and State, and Duff's device, and RATFOR, and Software Tools, and EE, etc.

> ...  I'm curious how this program would look with your approach.  ...

I hope to address this in another note.  Feel free to remind me and poke me ...

> ... So that pumping in one input results in multiple outputs? ...

Yes.

> ... and debugging the weird errors when we don't.  ...

I argue that the over-use of synchrony, as in just about all current-day programming languages, leads to even weirder errors.

> ... What are the semantics of a component with two inputs that receives a signal/value on only one of them? You could block and wait for the other, or not. ...

Definitely non-blocking.  Over-use of synchrony leads to implicit blocking which leads to a myriad of self-inflicted complexities and epicycles.  You can't - easily - use the synchronous pattern to implement all other kinds of patterns.  For example, if you insist on making everything a function, then you pepper your code with ad-hoc blocking which drives you into inventing the epicycle called *preemption* (which leads to the epicycle called *thread safety*, which leads to even taller, creaking towers of epicycles).

> ... Functions provide abstraction. Copying components does not. ...

I deeply disagree.  Components provide better abstraction than functions.  I view functions and lambdas and `{...}` as ASCII Art for *rectangle* (or *ellipse* or any closed figure).  I would argue that we wouldn't have wasted time arguing about abstract concepts such as *global variables* if we'd have used diagrams instead of ASCII Art.  But, characters are all that 1950s stunted hardware could provide us at a reasonable cost.  Today, though, we can do better.

Functions have Lambdas and code inside of Lambdas.  Components have Containers and routing inside of Containers and code inside of Leaves.

IMO the true model of distributed programming is a couple of rPIs connected by a pair of wires.  Each rPI runs single-threaded code and doesn't need the likes of Linux (or worse).  In full glory, if you need a driver for an HP printer and a driver for a Samsung printer, you write separate Components for each.  In the interim, though, you write a single Linux (or Windows or MacOS or ...) Component that accesses already-written drivers for these printers.

Thread libraries don't implement the above model correctly.  Closures and anonymous functions come closer, but, are crippled by their over-use of the synchronous pattern.  Thread libraries and 0D are just ways to fake out the true model of concurrency using fewer CPUs than required by Reality.  Obviously, I contend that 0D is a better way to fake this out, needing fewer epicycles than so-called "concurrency".

> ... On the whole, this needs a whole lot more examples. ...

I totally agree.

So, why haven't I done this yet? 

> Components include two concerns: what code runs inside them, and what queues are wired up to them. 

This was your first point. I choose to defer discussion of this point, since I think that it contains deeper meaning that needs to be addressed in a better way than I can at thiw time.

## Summary
I apologize for the delay in responding.  I was incrementally trying to make this perfect, but am suffering from "life gets in the way" and now have decided to post a snapshot...

Components are like Classes.  The code is not duplicated.  Instantiated, yes, duplicated, no.
...
In 2023, though, compilers are "easy" to build. 
...
What is needed is a language(s) that gets out of the way during design then allows incremental optimization (aka "typing", etc.) in places where performance matters (probably only about 5% of the code).
...
End-users don't care if developers use static typing or not.
...
Optimization-first languages, like Python, Rust, Haskell, Odin, etc., deal only with ... 33% of the problem.
...
Code as we know it, is just *assembler* for better languages.
...
I think that *dependency* is a serious problem.  I identify at least 3 ways that *dependency* creeps into current-day code. 
...
Note that this scheme tries to encapsulate names.  
...
These ideas are definitely related to coroutines.  And, green threads, and, mutual multi-tasking, and, closures, and pipelines, and Actors, and State, and Duff's device, and RATFOR, and Software Tools, and EE, etc.
...
I argue that the over-use of synchrony, as in just about all current-day programming languages, leads to even weirder errors.
...
Components provide better abstraction than functions.
...
the true model of distributed programming is a couple of rPIs connected by a pair of wires.
...
Thread libraries don't implement the above model correctly. 
...
... was your first point. I choose to defer discussion of this point, since I think that it contains deeper meaning that needs to be addressed in a better way than I can at this time.
...
The rest of this note is at: https://publish.obsidian.md/programmingsimplicity/2023-05-26-Response+regarding+Call-Return+Spaghetti
