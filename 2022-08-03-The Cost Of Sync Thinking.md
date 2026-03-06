# 2022-08-03-The Cost Of Sync ThinkingI'm reading about John Walker's [Atlast](https://www.fourmilab.ch/atlast/atlast.html) language.

As I read this, I feel further enlightened about how deeply "sync-thinking" runs in the veins of most people (including John Walker's).

The cost of using a *static language* is very high in terms of creativity.

The Design of *Atlast* is filled with considerations for so-called "efficiency". 

If the language, and Design, were based on asynchronous principles, "efficiency" would matter less and would not affect every aspect of the language.

If a program were like a set of isolated beads on a string, loosely coupled, one would Design the program and "get it working" first, without regard for efficiency.  We "know" that only a small percentage of a program takes up most of the running time.  Knowing this, and using the assumption of loose coupling, we would
1. get a Design to work
2. measure the result
3. buff only the parts of the program that cause inefficiency, leaving the other parts alone (and "inefficient").

If we had used *static languages* from the start, we wouldn't have invented *macros*.  We backed into macros because they were easy to implement, using FEXPRs.  FEXPRs are a feature of dynamic languages and were, later, expunged in the design of *static languages*.  It is *possible* to implement macros in static languages, but it is unlikely that the concept of macros would have occurred to anyone steeped in thinking about *efficiency* and *static languages*.

Dynamic languages are UXs for programming.  Static languages are UXs for optimizing programs.

The Design of *Atlast* specifies the use of *floating point* and *32-bit integers*.  These are optimizations of the more general concept of *numbers*.  *Atlast* is designed for *optimizing* programs instead of *designing* programs.

From my perspective, Sector Lisp is the ultimate expression of FP (*functional programming*).  Sector Lisp is *orders of magnitude smaller* than most programming languages (512 bytes not Kbytes, not Mbytes, not Gbytes).  

Garbage collection in Sector Lisp takes only 40 bytes to express.  I believe that it is so small because the Garbage Collector does not need to worry about prematurely-optimized data structures.  There are only 2 types in Sector lisp - Lists and Atoms.  Otherwise foreign concepts - like mutation - are simply prohibited in Sector Lisp.

Garbage Collection in Sector Lisp only needs to clean up unused results left on a stack.  A strick stack involving no mutation.  The stack-based Design of Sector Lisp lets the GC make simplifying assumptions that save code space, and, beat other languages in terms of efficiency.

This kind of *creativity* ("thinking outside of the box") has been beaten out of so-called *static* languages.

Racket - the latest permaturely-optimized manifestation of Lisp - is much larger than Sector Lisp.  Racket specifies tail-call optimization, but, that optimization is only necessary for optimizing away the epicycles caused by the Design of Racket (prematurely optimized). 

How do you use Sector Lisp for "real" programming?  

Divide and Conquer.

1. Use Sector Lisp for *only* what it is good for.  Functions without mutation.  Synchronous, strictly stack-based evaluation.
2. In places where you need mutation and persistence and RAM, use *another* notation in place of Sector Lisp.  Don't pay for mutation in places you don't need it.  How?  Wrap a thin syntax-skin around uses of Sector Lisp.  Maybe Sector Lisp becomes an embedded language inside of C-like control-flow syntax.  

For a concrete example, consider multitasking, the way it used to be in early game programs.

We might write multitasking using *lambda*s as:

```
Loop:
  call λFunction_to_decide_whether_to_continue ();
  jump on-quit to End;
  call λFunction_to_eval_next_step_in_the_game ();
  jump Loop;
End:
```

Early games were chopped up into *steps* and wrapped by what-is-called-today *event loop*s.

No step in the game ran for a very long time.  Long-running loops and deep (or infinite) recursion were considered to be bugs and were expunged before the game was shipped.  The *shipped* version of the game did not need elaborate workarounds, called *operating systems*, for prying control away from the cold, dead hands of misbehaving *steps*.  The *development* version of the game - running on souped-up hardware - used various tricks to kill misbehaving *steps* (including the *biblical flood* version of Garbage Collection (ie. UNIX) or the dreaded power-down-and-reset.  Why does my 97-year-old mother need to pay for a souped-up laptop, for running Tetris and browsers and email, that can catch development errors?).

Consumers would expect the games to run on their cheap hardware and to never crash.  Producers would give *guarantees* to consumers.  This kind of non-crashing Design exists in just about every product, except Software products.  We've become accustomed to using preventative reboots, and receiving quarterly updates instead of suing manufacturers or giving them bad reputations.  When I bought a 4-banger calculator, it didn't crash.  My calculator on my laptop is rendered useless by crashes in unrelated software and in the operating systems, themselves.

Is this just because "software is complex"?  I think that manufacturers would Design differently if their feet were held to the fire - they would stop building brittle gearboxes and find ways to isolate parts of their systems to make them simpler to Design and optimize and ship.  

Clearly, Sector Lisp shows that software *can* be built to be small.  The rest is due to premature optimization and misdirected thinking.  Sector Lisp is simple - it is easy to reason about and to "get right".

It is my opinion that simplicity begins with 0D.  Striving for 0D - zero dependencies.  Make software pieces that are loosely coupled.  The biggest problem in achieving this is not technical, but, cultural.  Remove all implicit synchronization from code.  For example, I count 3 ways that `f(x)` causes unwanted coupling - all of them are easily remedied even using exising languages.
1. hard-wiring of callee's name into caller's code
2. blocking protocol - a function *blocks* waiting for an answer from a callee (rhetorical question: does the callee block waiting for its callees?)
3. routing - a function *must* return a result to the caller, it cannot send its results (if any) elsewhere.

All of the above can be remedied by replacing all function calls with FIFOs.  Instead of calling a function, code inserts a *message* into its *output queue (FIFO)*.  The *output queue* is emptied by the Container (Parent) of the function.  The Container decides on the routing of messages between its children (a message can be routed to another child, or to multiple children (fan-out) or nowhere (No Connection).  The function, itself, does not get to decide where its messages are routed).

The weirdness of (2) self-blocking, just *goes away*.  A "function" never blocks, it simply stuffs messages into its own output queue.  The Container (or its Container, recursively upwards) decides on the dispatching policy, i.e. who gets to run when.

If a Design really needs synchronization, it can be explicitly designed-in, the way it is done in TTL hardware.

Ironically, implicit synchronization using LIFOs (stacks) was not present in early CPUs (the IBM 360 did not have a hardware callstack, programmers had to build one explicitly using BAL instructions).

Implicit synchronization cannot exist in the internet, in blockchain, in distributed rPIs, etc, etc.  The award-winning pBFT paper showed how to create explicit synchronization in distributed computers (the technique looks ridiculously simple from an async mindset).

Now, we have bulk-editing tools like Ohm-JS and PEG, that can replace syntax that looks like function calls with code that implements output queue stuffing.

One can structure message-passing in ways similar to *structured programming*. 
## 2022-07-27-Structured Message Passing

---
tags: 
copied_to_pages: "true"
---

---
# Structured Message Passing
video: [Structured Message Passing](https://share.descript.com/view/pDyKpgerYRq)

---
# Structured Message Passing

"Structured message passing" implies that we must encapsulate every aspect of Components

- data flow

and 

- control-flow

---
# Scalability
Scalability comes from Structured message passing 

You can only scale a system where Components are not tangled together.

---

# Existing Languages
   - simply stop using hardware-supported CALL / RETURN for communication between Components
   - create 2 classes of Components

---

# Don't Use CALL/RETURN
- Don't use hardware-supported CALL/RETURN for communications between Components

- use FIFOs instead

- it's OK to use CALL/RETURN for code *inside* a component, but not as a means for communicating between Components

---

# 2 classes of Components
- Leaf Components (code)
- Container Components (routers)

---

Structured message passing implies that we must encapsulate every aspect of components.

That includes data flow and control flow.

We can't just concentrate on data flow.

Scalability comes from structured message passing.

You can only scale a system when components are not tangled together.

How do you do this using existing languages? Simply stop using hardware supported call return for communication between components. And create two classes of components, not one class.

So, how do you not use call return? It's simple. Just use FIFOs.

It's okay to continue using call return for code inside a component. But don't use call return as a way of communicating between components.

Creating two classes of components. I see there being leaf components for code and container components for routers that compose components and route messages between them, but they don't actually do anything.They can run other components.

Container components devolve into other container components or leaf components.  Stepping means we finally get down to a leaf and a leaf just does something and stops.

Technically, this is not rocket science.  It is cultural.  Don't call functions, send messages, write code that does not know where it results will end up.  Code must not rely, implicitly, on receiving results from other components.

Humans intuitively think this way already (inter-personal relationships, freedom, free will, business ORG charts).  Programmers, though, are painting themselves into a corner, using implicit-synchronization-thinking.