# 2023-01-31-Model of Computing
# Model of Computing

An electronic machine consists of 2[^more] CPUs connected by 2 one-way wires, sending compact messages at each other, running essentially single-threaded software.

[^more]: 2 CPUs is but the lower limit and is used to make this description's basics more clear.  In general, multiple CPUs can be used, arranged in a hierarchy.

In this model, everything else is unnecessary, i.e. Operating Systems are unneeded and Programming Languages are just cave-man IDEs for creating electronic machines.

Everything else is bloatware based on 1950's phobias against wasting expensive CPU time and expensive Memory. The assumption was that it was better to waste programmers' time than to waste CPU time or Memory.

In the model described here, the answer is always: "just throw another rPI at the problem".

In this model, there are two (2) kinds of Components
1. Leaf - software applications, as we already know them
2. Container - recursive, contains Components (Leaves or other Containers) and Routing information between the contained Components.

Obviously, all of this *can* be implemented using our current crop of general programming languages.  But, this results in too many low-level details. The reasons *why* the software is written the way it is (aka Architecture) become lost in low-level detail.

Another way to say the above might be: the model is:
1. Systems - recursive
2. Leaves - bottom.

# How to "reuse" what already exists?  

VirtualBox, Docker.  

Most existing software is meant to be dropped into envelopes provided by Operating Systems.

Software written against the model described here doesn't need all of that cruft.  It simply needs to send messages (HTTP? UDP?) to existing software on the same computer that is enveloped in VirtualBox and Docker, and/or, to software running on other computers. 

# How Did This Begin?

I wanted to draw technical diagrams of device drivers without needing to resort to ad-hoc C and Asssembler.

Harel StateCharts are a good notation - a starting point - for writing device drivers in this way. 

I read, then promptly discarded as unpractical, Harel's follow-on paper on the semantics of StateCharts in micro-synchronized form.

## Diagrams

Diagrams are easy to compile to code, if you don't over-use synchrony.  

Technical diagrams are the result of culling compilable things out of Art, e.g.
- rectangles
- ellipses
- arrows
- text
- groups.

Technical diagrams are *hybrids*.  We need both, resizable-glyphs and text.  Text is better at expressing some concepts than diagrams.  Diagrams are better at expressing some concpets better than text.

Text is good for expressing equations.

Diagrams are good for expressing networks.

# Bloatware

Operating systems are state machine wrappers for otherwise single-threaded, calculator applications.

Bloatware occurs when the "calculator" model is stretched beyond its comfort zone.

For example, when programmers try to build sequencers using only calculators and state-hiding operating systems, bloatware is the result.

As a counter-example, Sector Lisp is a good example of using the functional paradigm only within its own bounds.  The Sector Lisp garbage collector is only 40 bytes [sic] long and the whole language is less than 512 bytes [sic] long.  It is easy to blame Sector Lisp's smallness on Assembler tricks, but, something more profound is at work, i.e. simplicity, staying within the bounds of the simplifying assumptions.

# The Fiction of Code Libraries

It is believed that code libraries create re-usable blocks of code.

In fact, code libraries create synchronous blocks of code that resist reuse without the addition of epicycles.

Creating synchronous blobs of code - e.g. using the callstack (a LIFO, not a FIFO) - creates unwanted, tiny bits of inter-code dependency.

Because of this inter-code dependency, code libraries are not LEGO® blocks.

## What Are the Hidden Dependencies?

"Code Libraries" *look* like building blocks, but, contain subtle bits of coupling that discourage building-block-iness.

For example, the very common idiom of a function call `f(x)` introduces at least 3 kinds of coupling:
1. The name `f` is hard-wired into the caller's code.  The calling code cannot be cut/copy/pasted into some other solution without also dragging in the called code, or, by futzing with the source code.
2. The function call `f(x)` waits for the callee to return a value.  This is also known as *blocking*.  Function call notation works fine on paper, where functions can be evaluated instantaneously.  It's different when you map function call syntax onto hardware that has propagation delays wherein functions take finite amounts of time to "run".  This subtle difference in behaviour leads to hidden gotchas.  A glaring example of the impact of such a difference can be seen in the Mars Pathfinder disaster[^pathfinder].  
3. The function return `v = f(x)` hard-wires a routing decision into the callee's code.  The callee *must* direct its response back to the caller.  This is called "returning a value".  Again, this doesn't look like a problem when you just want to build fancier calculators, but, this hard-wired routing decision discourages simple solutions to non-calculator problems, like machine control.
[^pathfinder]: https://www.rapitasystems.com/blog/what-really-happened-software-mars-pathfinder-spacecraft. at first glance, the Pathfinder problem doesn't look like a big deal, but, if you dig backwards through the tower of epicycles that resulted in over-confidence in the Pathfinder software, you can see that the fundamental problem was the use of the wrong paradigm for describing electronic machines which caused unforeseen gotchas, e.g. the Pathfinder problem was caused by "priority inversion" which was caused by the use of a real-time operating system which was caused by the use of function-calling which caused ambiguity in which piece of software was responsible for control of *blocking* which caused the use of preemption in the real-time operating system which caused the invention of *priorities* to reclaim control of preemption by the boxed-in application software which caused lack-of-encapsulation (priorities allow programmers to break through the walls of the sandbox, and, to blow their own feet off), etc. 

When you don't have complete isolation, you don't have building blocks.  Imagine a LEGO® set where all the pieces are joined together with a single, long sewing thread glued to each LEGO® block.  Or, imagine that you have two real-world objects, e.g. one apple and one orange.  You cut the apple in half.  What happens to the orange? (Answer: obviously, nothing happens to the orange).

As humans, we are used to the idea that objects are completely isolated.  Programs don't work that way.  We have to stop and think hard when writing programs.  


# The Fiction That Mathematical Notation is a Good Model for Electronic Machines

Grafting mathematical notation onto electronics that has physical limitations violates fundamental mathematical notation[^notation] principles.
[^notation]:  not all of mathematics, just the notation.  The other part is *deep thinking*.

For example, the mathematical model does not incorporate RAM, mutation, propagation delay, etc.  You *can* model these ideas in mathematical model, but, that's not sufficient.

The mathematical model hard-wires the concept of "function" - `f(x)` - into the notation.  Everything else is second-class.

Most existing mappings of the mathematical model onto electronic machines, involve the callstack - a LIFO, not a FIFO.

Language influences thought.  Most problem solutions are insidiously mapped onto the functional domain before the problems are even understood and evaluated for their suitability of a function-based approach.

For example, the functional abstraction is suitable for building fancy calculators, like ballistics computers for military hardware.

As a counter-example, the functional abstraction does not work as well for developing sequencers, such as timeline-based movie editors, or, for extremely distributed, electronic machines, such as the internet.  It is *possible* to use the functional abstraction to solve these problems, but, it is less convenient.  

The current solution is to enforce the use of "operating systems" in end-user devices.  

For example, my 97-year-old mother wants a box that plays Tetris, another box that reads/writes email and another box that browses the internet.  To be able to do this in the current environment, she needs to pay for a "computer" that runs "Windows", but, has no real use for either of these things.

# Early Games

Games began as scripts of opcodes stored as binary blips on 8.5" floppy disks (plastic disks coated with a thin layer of magnetic oxides).

You inserted the disk into the machine the software took over the machine, with the sole purpose of turning the machine into a game. 

A game consisted of three aspects:
- visuals
- inputs (controllers)
- logic.

# Allowing Programmers to Create Electronic Devices Without Learning How To Solder

Programming of electronic machines using our current Programming Languages and Operating Systems allows programmers to create electronic devices without learning how to solder.

But, programmers need 4+ years of university education to learn how to lather epicycles onto every such design problem.

And, this current environment requires all end-users to pay for expensive electronic hardware and software that act like substrates for the products produced by programmers.

Is this an appropriate trade-off?

# $ Accounting for Computing Time

Early on, CPU time was meted out in $'s.

Day 1 of a university course in computing consisted of getting an "account" and being made aware of how many $'s were in the account, with the implication that all homework had to be done within the $ budget.

This bean-counting attitude influenced the way work-arounds for programming were invented.

# Apple Postscript Printers

Apple made it its business to attack niches of computing that were related to "artistic" use of electronic machines.

Early Apple machines enabled the Desktop Publishing market by installing CPUs into printers.  The CPUs ran Forth software tuned for placing dots of ink onto paper in eye-pleasing manners.  The Forth software was called *Postscript*.

Before Apple did this, printers were fairly dumb pieces of mechanics, containing the minimal amount of electronics.  Printers were controlled from afar solely by electronic, single-CPU devices called "computers".  

The burden of figuring out the details of how to control dumb printers fell on the over-taxed software of such single-CPU "computers".  To make matters worse, each dumb printer model contained different bits of mechanics and electronics, making the bookkeeping task more onerous for "computers".  "Computers" were tasked with the job of figuring out which printer control software to use.

# Premature Optimization

The use of synchronous mathematical notation made it easier to think in terms of of single machines instead of in terms of distributed machines.

The view of electronic machines as "calculators" (aka "computers") doesn't model electronic machines in their full glory.

The knee-jerk concept of using an already-existing notation for a new medium is a form of *premature optimization*.  This decision - unconsciously - cuts off certain avenues of thought.

# Computers are a New Medium for Thought

Computers are a new medium for thought, but, we continue to use an old notation, which affects how we solve problems with electronic machines.

Mathematical notation was invented to map 4D reality onto 2D clay tablets and paper (x/y/z/t -> x/y).  

Physicists call this "making a simplifying assumption".

True physicists, though, remain aware of their own simplifying assumptions and switch to using other notations when a specific notation is stretched beyond its comfort zone.

Electronic machines allow us go beyond 2D.  We can, now, examine and manipulate concepts in more than two dimensions.

## Example Use of the New Medium

I watched someone go beyond written equations to describing and calculating visual distortions required to represent a visual scene projected onto several screens, in a way that made the human visual system believe that it was looking out of a window at a real scene.  

The medium for this description was a program called Blender.  Blender made it possible to visualize the multi-screen environment and, then, to use the visualization to create a solution for the specific problem at hand.  

This took only several days to do, whereas if this had been done using paper and graphite and rubber, the solution might have taken a lifetime to work out.  As a consequence, this problem has never been addressed - it was avoided because it was too onerous.

Even though, at the bottom, equations were used, Blender allowed thinking at a new level and allowed convenient cloning of equations without needing to resort to simplifications that would have stopped the development of the solution.  Blender allowed the problem set-up to be viewed from multiple angles in "3D".  Once the problem set-up had been verified, the solution was much easier to develop.

# What We Really Want

We want software development to allow us to build new layers of thought upon existing layers of thought.  

We want software LEGO® blocks.

Over-use of synchrony prevents us from achieving this, conveniently.

