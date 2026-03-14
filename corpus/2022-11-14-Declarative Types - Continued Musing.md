# 2022-11-14-Declarative Types - Continued Musing
A question arises about the previous musing:

> ```
> dtype ⟨Other x y⟩
> dtype ⟨Dest target ⟨Other⟩ port message⟩
> 
> Is 'Other' flattened so that Dest is essentially `dtype (Dest target x y port message)`. If so, what if Dest had already defined an `x'`. I guess that should never happen or the compiler would fail anyways  

Here’s a question (not a challenge):

Why should you care?

“Efficiency” has been grossly over-emphasized.  If we use divide-and-conquer, we see two (2) versions of efficiency:
1. efficiency for the end-user
2. efficiency for the developer

Just about all of our programming languages & indoctrination have been in aid of (1). At the expense of (2).

I think that the above question arises out of consideration for (1) - efficiency for the end-user, developers be damned.

## Lisp 1.5

McCarthy had a simple view.  Every symbol contained a stack of values, and the symbol's "current value" was the top of its stack.  McCarthy implemented this as *alists*.

McCarthy's Lisp 1.5 was *pure* functional programming.

Since then, the programming community has jammed all sort of "features" into McCarthy's simple vision with the result being: bloatware.

Mutability was inserted into the simple concept.  This caused epicycles around memory management, since memory was not *always* arranged in a stack-like manner. GC (garbage collection) needed to be invented to manage this subtle change.

Then, the simple vision was pushed well out of its sweet spot through the insertion of *concurrency*.  Concurrency doesn't work cleanly with little stacks, so lots of epicycles had to be invented, e.g. "thread safety", "semaphores", "priority sharing", etc., etc.  These problems were worsened by the fact that the *call stack* is implemented - in hardware - as a shared, global variable.  There used to be a time when CPUs did not have call-stacks hard-wired into them (e.g. IBM 360) and compilers had to implement *call-stacks* using multiple instructions.

Rhetorical question: was Lisp 1.5 the last instance of *pure* functional programming?  

Hmm, now, maybe, the circle has been closed with Sector Lisp.

## Sector Lisp

Sector Lisp is a re-implementation of McCarthy's Lisp.

Sector Lisp has a newer, purely functional, garbage collector which is only 40 bytes[sic] in length.

Sector Lisp's GC is so small, because it can rely on *pure* functional programming and true immutability.  Lists are little stacks, you can tack things onto the top of the little stacks (CONS) and you can pull things off of the top of the little stacks (CAR) and you can pop things off of little stacks (CDR).  Structure sharing is free.  Scoping is free.  You can tack an item onto a list and pass the extended list to a function.  When the called function returns, the original list, without the tacked-on item, is restored, due to structure sharing.  Cheap.  Magical.

You can't do that with heaps and OO.  But, you can do concurrency with OO objects, and you can't do concurrency with *pure* functions.  You have to impurify the functions and invent an epicycle called an *operating system* and it needs to invent the epicycle called *preemption* to thwart the blocking behaviour of functions.

# Back to the Question

So, what happens when we have
```
dtype ⟨Other x y⟩
dtype ⟨Dest target ⟨Other⟩ x y⟩
```
?

I think that something like the following might work:
```
--> ⟨Dest target {"x": ...} {"y": ...}⟩
```
Where ... is a little stack.  A left-to-right List.

Each variable, like `x` and `y`, are maps that contain an ordered set of values.  In raw Lisp, we might say that `x` is a list.  The *current value* of the *variable* named `x`, is the first item on that list, i.e. (CAR x).  Note that `x` appears to be used twice. The subtle difference, though, is the use of the word *variable* and the phrase *current value*.

## Considering Efficiency
1. Does the answer run "fast enough" on end-user hardware. No. Can it be made faster? Yes.
2. Does the answer run "fast enough" on developer machines? Yes. Can it be made faster?  Who cares?  It can be made to run faster if we make developers suffer and appease compilers, by insisting on things like declaration-before-use, strong typing, etc., etc.  But, development machines are fast and it is OK to burn CPU cycles on development machines when this saves Development Time.  We don't mind burning CPU cycles on development machines, but, we *do* mind burning CPU cycles on end-user machines. Developers should be using languages specifically designed for development.  After an app is working, developers can punt the optimization work to Production Engineers (or do the work themselves) using tools that ingest the development code and produce faster code (kinda like *lint* and kinda like gradual typing - it is not OK to butcher the development code, but it is OK to transpile it into faster code).

Note that original JavaScript began to leak the little-stack (alist) concept back into development.  More recent tweaks to the JavaScript language have made it more 1-ish at the expense of developer effort.

## Side Benefit of Small Is Beautiful Languages

Note that there is a side benefit to the *small is beautiful* version of development languages: it becomes a *lot* easier to automatically generate (transpile, compile) code into *small is beautiful* development languages.  

I argue that a code generation paradigm will speed up development time.  

As an example, consider why programmers love UNIX and UNIX pipes. 

As a counter-example, consider the Python indentation syntax and programming languages that require declaration-before-use.  Most of the current crop of code-generation tools are based on structured syntaxes (not indentation syntaxes) and on byte-oriented characters and on a single stream of output.  

It is painful to generate code for declaration-before-use languages.  Not impossible, just more painful than necessary. Think of this subtle difference as a UX issue[^ux].  

Assembler has a regular syntax and no restrictions like declaration-before-use.  Assembler is hard to read for humans, but, is a breeze to read and write, for machines.  

Likewise, Lisp has a regular syntax and no declaration-before-use restrictions.  It would be "easy" to write programs that write Lisp programs.  In fact, it is so "easy" to generate Lisp code, that it has already been done.  Lispers call such magical code-generating programs "macros"[^scheme].

[^ux]: If a tool sucks, it won't get used and it won't sell. If tooling sucks, programmers will avoid generating code, even if they know it is good for them.

[^scheme]: Scheme, and Racket, also, have macros.  Macros were invented in Lisp, then revamped for Scheme and Racket.  In unhygenic Lisp macros, *if-then-else* is about a 1-line macro.  In hygenic Scheme macros, *if-then-else* is about a page of code.  Is it any wonder that macros were invented in Lisp?  Aside: C uses the word *macro*, but, doesn't really have macros like Lisp and Scheme and Racket macros.