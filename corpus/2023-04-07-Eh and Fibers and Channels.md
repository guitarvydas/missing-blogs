# 2023-04-07-Eh and Fibers and Channels> In [computer science](https://en.wikipedia.org/wiki/Computer_science), a **fiber** is a particularly lightweight [thread of execution](https://en.wikipedia.org/wiki/Thread_of_execution "Thread of execution").
> ...
>  However, fibers use [cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking "Cooperative multitasking") while threads use [preemptive multitasking](https://en.wikipedia.org/wiki/Preemptive_multitasking "Preemptive multitasking").

url: https://en.wikipedia.org/wiki/Fiber_(computer_science)

# ė vs. Fibers and Channels

ė components *are* fibers...

Fibers are cooperative multitasking processes.

Cooperative multitasking processes are also called *closures*.  *Closures* are simply non-capturing lambda procedures along with data allocated in the heap.

As such, ė (spelled *eh* in ASCII) components *are* fibers.

Fibers are easy to implement explicitly and do not need to be generalized and turned into scary-sounding operating system concepts.

To implement an ė component, you simply need to decouple the component from all other components, *and*, you need to schedule execution of the components in some way.

You can write a scheduler procedure in many ways.  One way would be to create a list, or an array, of ė procedures and to call each procedure when its time comes.

Because of cooperative multitasking, ė procedures need to *yield* back to the scheduler.  The scheduler must not use preemption.

In simpler words, a *scheduler* is just a procedure that calls other procedures.  The called procedures *return* to the caller after completing a small unit of work.  *Yield* manifests itself as *return*.  Most programming languages already support the - very common - concepts of *calling* and *returning*, hence, fibers can be implemented in any programming language without the need using operating systems.

Because of cooperative multitasking - and lack of preemption - ė procedures must not perform long-running loops or deep recursion.  Instead, ė procedures chop up their work into smaller units and *return* to the scheduler as soon as possible.  The *scheduler* must call each ė procedure multiple times in order to allow the ė procedure to complete all steps in their work.

Because of this, ė procedures need to keep track of what they were doing and what *state* they are in on their road to completion.  This concept *is* State Machines, sometimes called *Actors*, sometimes called *StateCharts* and so on.  

*State* is not inherently bad, but, ad-hoc use of *state* can be confusing.  To avoid confusion, one needs to employ *structuring* of some kind.  I suggest structuring along the lines of *across*, *down*, *up*, and, *through*.

The *structured programming* revolution brought *structuring* to sequential control flow, like flowcharts and assembler programs.  I suggest a *structured programming* revolution for ė procedures (aka *fibers*) for non-sequential programs.

I claim that ė makes thinking (aka "reasoning") about non-sequential programs easier and allows cutting through the jargon of over-generalization and operating-system-ification of such simple concepts.

## ė components, Leaves and Containers

To implement an ė component, you simply need to build an *object* that has one input queue and one output queue,  and, ensure that the object never directly calls other ė components.  The ė component must leave its results in the output queue instead of returning its results explicitly.  This is simple to do in any programming language.  Simply allocate queues on the heap, and, enqueue or dequeue bits of data into/from the queues.  Sequential programming languages, like Python, violate this simple concept by allowing direct calling of functions using the call-stack, and, by allocating data on the call-stack instead of in a queue on the heap.

To implement an ė *Leaf* component, you simply need to build a normal function that uses a unique output queue instead of relying on the call-stack to return its value(s).  I suggest using a function called *Send()* to stuff data onto the output queue.

To implement an ė *Container* component, you need to build a normal function that instantiates other ė components as children, and, punts all inputs to such children.  The output queues of ė Containers must also be unique.  Children punt their results into their Container's output queue.

A Container must invoke its children repeatedly until no child has any input messages to process and no child has messages on its output queue.

I suggest organizing these data movements in a *structured* manner, to avoid programming confusion.

I use the word *down* to mean punting inputs to one's children.

I use the word *up* to mean punting childrens' outputs into their Container's output queue.

If more than one child can punt *up*, I call this *fan-in*.

If an input is dispersed downards to more than one child, I call this *fan-out*.

*Fan-in* and *fan-out*, also, apply to how messages from children are dispersed within a Container.  There is nothing magical here - the data movements are straight-forward.  The only consideration is that *fan-out* must be implemented atomically, and, probably involves making copies of the message, but, that depends on your application and your application's specific storage allocation scheme (often generalized and called *garbage collection*).

The *atomic* dispersion of *fan-out* messages is simply a *structuring* rule-of-thumb.  It is easier to program (aka "reason about") messages when you guarantee that they cannot interleave, and, guarantee that all receivers see the messages in the same order.  This rule-of-thumb is akin to getting rid of GOTO in high-level languages.  GOTO is still there - and still useful - but, there are ways to use GOTO that cause less confusion and fewer *gotchas*.

### Fan-out in Sequential Languages
When ė is implemented in sequential languages, like Python, Rust, Odin, etc. using an operating system, there is nothing special that needs to be done.  

The scheduler and Containers are just regular functions / procedures.

All of the atomicity you need is already built into these languages.

### Fan-out on Bare Metal
*Don't read this unless you want to implement ė without using an operating system.  For example, if you want to write code on a Raspberry Pi while not using Linux, you need to know this.*

When ė is implemented in non-sequential ways, like Assembler on bare metal without any operating system, you need to worry about atomicity.

In essence, you need to put *sequential*-ness back in, but, only at this one point.  You don't need to over-generalize and make everything *sequential* just to ensure that *fan-out* works here.

Over-use of *sequential*-ness leads to confusion and creates unnecessary restrictions.  Like handling GOTO, you need to worry about atomic - sequential - operations when coding up *fan-out*, but, you don't need to force atomicity everywhere, just so that this one use-case works.  In the GOTO-less world, we see that most languages expunge GOTO, but, they put GOTO back in, in more restricted ways, using more-structured variants like CONTINUE, BREAK, etc. 

## Channels are Ports
Channels are sequential ports.

Channels are queues

Channels probably imply *blocking*, which implies *preemption*.

*Containers* are structured ways to handle channels without blocking.  Nothing magical. Containers rely on the fact that Components create messages and that Components employ cooperative multitasking, i.e. Components mete work out in small steps and don't rely on preemption.  A *Container* simply polls its children to see if any of them have work to do, i.e. have data in the input queue.  When a child is ready, the *Container* pulls one message off of the child's input queue and tells the child to handle that message.  After which, the *Container* checks to see if the child left any new messages[^plu] in its output queue.  If there are any output messages, the *Container* routes them (across, up) and loops again.  If no child has any inputs nor has created any outputs, the *Container* finishes up and *yields* to its container.

[^plu]: Note the plural form - *messages*.  A Component can react to any input by creating zero or one or more-than-one messages.  The concept of *functions* constrains Components to produce exactly one output for every input.  Zero and more-than-one are not options.  Note, further, that the concept of "multiple parameters" and "multiple return values" is really just a trick of destructuring.  These options are all singular in time.

## HSMs, StateCharts

Harel wrote a paper on StateCharts in 1986.  The key revelations are:
1. You can draw pictures of control flow (ellipses and curvy arrows and bits of text)
2. The use of *parental authority* instead of *inheritance*.  

A parent gets first dibs on any incoming message.  If the parent decides to switch states, it pulls its children out of their current states first.  A child can do nothing to change its parent's behaviour.  A child cannot override a parent's methods.

I have recorded a reading of that paper.  The paper "looks" long, but, it's mostly pictures. https://guitarvydas.github.io/2020/12/09/StateCharts.html.

The follow-on paper, in 1987, about the "semantics" of StateCharts was useless to me.  It required synchronization of every aspect of every state machine.  The result is fake concurrency.  Code is synchronized, but only *looks* like asynchronous code.

Harel's notation conflates two fundamental techniques:
- HSMs (Hierarchical State Machines)
- concurrency, called *orthogonal states*.

I like to separate these concepts in two distinct techniques:
1. ė Components for concurrency
2. HSMs for synchronous, hierarchical state machines.

You don't need concurrency for HSMs.

You do need concurrency if you want to simplify decomposition of applications.  You *can* make everything synchronous, but, you have to invent epicycles along the way (things like "thread safety", "semaphores", etc., etc.).

To use technical diagrams as syntax for programs does not require being able to parse all of Art.  Just like using text as syntax does not mean that we need to parse all of the English language.

## Across, Down, Up, (Through) Routing
The main structuring principles, that I discuss, are:
- containment
- Containers to route messages between Components (flexibility through indirection).

| port | port | routing |
| ---- | ---- | ------- |
| output | input | *across* |
| input | input | *down* |
| output | output | *up* |
| input | output | *through* |

When a Container gets an input and wants to punt the work to its children, it sends the input *down* to its children.

When children want produce results that their Containers want to pass upwards, the child outputs are routed *up* to their Container's output queue.

When a child wants to pass messages to its peers, it cannot directly send the messages to its peers, it must leave such messages on its own output queue.  The child's Container routes such messages *across* to other children.  

It is "more efficient" to allow children to send messages directly from one child to other children - but - this is less flexible and makes it difficult (impossible?) to snap components together like LEGO blocks to form Architectural variations.

The *through* routing is an edge-case which supports stubbing-out of Components.  Input messages are directly funnelled to a Component's output without being punted *down* to any children.

## Functions & Lambdas

Functions, and, lambdas, are ways of wrapping bits of code in a synchronous manner.

Functions tend to do only 1/2 of the job.  Functions specify the input API, but leave the output API as a free-for-all.  Functions can directly call other functions, resulting in loss of flexibility.

The use of output *ports* - output APIs - breaks this kind of hidden coupling and allows greater flexibility and LEGO-ifying software components.

In addition, because *functions* are synchronous, they ignore one dimension (*time*).  It is OK to *sometimes* analyze a process by eliding *time*, but, it is *not OK* to *always* ignore the dimension of time.  Time-lessness is *OK* if you are building *calculators*, but, *not OK* if you are building sequencers.  Calculators are things like ballistics equations for the military.  Sequencers are things like the internet and distributed computing and robotics and blockchain and ...

Aside: I'm currently interested in Ceptre because it combines formalization logic with a way to handle time ('qui'). https://www.cs.cmu.edu/!cmartens/ceptre.pdf.  Further, Ceptre makes it possible to write States in state machines, without needing to mention other States by name.  I don't yet know what I think about this feature.  Maybe it will make sense to distribute States across different machines, hence, no-name-calling would become a desirable feature for decoupling.  I haven't thought this through, yet.

## Drawware
Once you break crippling, hidden coupling, it becomes possible to imagine *programming* in a number of dimensions, not just those based on textual representations of programs.

As seen in StateCharts and FBP[^fbp] (flow-based programming) and computer networks, diagrams of non-coupled processes make more sense and tend not to have the same kinds of *gotchas* that are needed to program only in the synchronous domain.

[^fbp]: https://jpaulm.github.io/fbp/

## UNIX Pipes - The Problem With Pipes

UNIX pipes define connections between software components, but, in an ad-hoc, GOTO-like manner.

Pipes have exactly two ends
1. input
2. output.

Pipes do not encourage connecting software components in some sort of hierarchy.  Some programmers do this automatically, but, most don't.

Pipes need a 3rd component - a routing path - *down*, *up*, *across*.  This routing path would provide *structure* to the interconnections between software components.

Pipes already employ the concept of *Container*, but, allow for only one container.  In the case of UNIX, a *Container* is the whole operating system.  Bloatware.  We should want *Containers* that contain *Containers*.  Elite programmers do this instinctively by writing shell scripts that call other shell scripts, but, mere mortal programmers tend to spaghetti-fy their code, especially when the heat is on to deliver fixes.

A stop-gap measure might be to create tools that compile (transpile) diagrams to shell scripts, and, stop programmers from ever writing shell scripts again (the way that just about no programmers write Assembler any more).

## Processes versus Closures

Processes are big, honking closures, that have hardware support for pointer-violation-checking.

Processes rely on *preemption* to allow old-fashioned programming constructs, like Loop and Recursion.

Closures are smaller entities than processes.  

Closures don't have hardware support for pointer-checking.

Closures don't need preemption, but, do rely on cooperative multitasking.  Cooperative multitasking is *OK* for expressing the innards of programs.  Cooperative multitasking is *not OK* when unreliable applications co-habit the same piece of hardware.  If programs didn't have bugs, then hardware support for pointer-checking would not be needed.  Corollary: when operating systems use hardware support for pointer-checking, programmers are entitled to build buggy, unreliable software that needs frequent updating.

Closures need to keep state on the heap.  This requires memory management.  Often memory management arrives in the form of some sort of GC (Garbage Collector).

Closure-like functions that keep state only on the stack are like Odin non-capturing lambda procedures.

State machines - and StateCharts - need to keep state on the heap.

Very pure functional languages - like Sector Lisp - do not have heaps, but, seem to get along fine without heaps[^sl].

[^sl]: It can be argued that Sector Lisp does not implement a useful language, without mutation and state.  Sector Lisp is less than 512 bytes[sic] for the whole language, plus garbage collector.  Mutation seems to multiply the memory footprint of such languages by at least an order of magnitude.  Is mutation worth such large footprints?  Are the right trade-offs being made?