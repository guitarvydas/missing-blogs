# 2023-06-19-Sequential Pattern# Sequential Pattern
## Synopsis
- The Sequential Pattern
- CPUs
- Timing and Propagation Delay
- Function-Based Notation
- Rust, Python, Etc.
- Do All Programming Languages Need To Be Sequential?
- Programmability
- What The Sequential Pattern Is Good For
- What The Sequential Pattern Is Mediocre For
- Electronics Is A Throbbing Mass Of Asynchronous Units
- Timesharing
- Memory Scarcity
- Single Stack
- Arduinos, Raspberry PIs, Etc.
- Single-Threading
- The Human Body

## The Sequential Pattern

The Sequential Pattern specifies solutions to problems as a sequence of steps.

The Sequential Pattern is like a recipe.

First, perform step one, then perform step two, third, perform step three, and, so on.

### Recipes Are Not Strictly Sequential
Note that recipes are not always strictly sequential.  

Sometimes, recipes use two patterns 
1. sequential
2. parallel.

For example, we often see recipes that specify two activities, like "while the potatoes boil, cut up the carrots then cut up the green onions".

So, maybe recipes aren't the best example of the sequential pattern, but, recipes are something that most people encounter and understand.

## CPUs
The sequential paradigm resulted in our ability to control ad hoc combinations of asynchronous electronic circuits, and to step them in a particular manner using what we call opcodes.

An opcode is a numeric code that represents a cluster of actions that the machine will take when commanded to do so by the opcode.  The actions, themselves, are not necessarily sequential, but, the clusters are stepped through in a sequential manner.

We create scripts of opcodes, then the machine executes each of the steps in a sequential manner.  First, the CPU performs the cluster of actions specified by the first opcode, then the CPU performs the cluster of actions specified by the second opcode, and, so on.

## Timing and Propagation Delay
Each opcode takes a certain amount of time to execute. 

That's called *timing*.  

It takes a bit of time for the machine to access and read-in the opcode.  

Then, it takes another bit of time to run the opcode and to perform the bits of logic.

The time needed to enact each action is caused by the fact that electrons cannot travel instantaneously.  That is called *propagation delay*. 

When the machine wants to read-in the next opcode, it must send electrons to certain circuits, then, it must wait for the circuits to send electrons back.  Electrons travel quickly, e.g. about 15cm in 0.000000001 second[^propagationdelay] in a copper wire, but, they don't travel instantaneously.  All of those tiny bits of time add up. The speed of an opcode is usually governed by the worst case propagation delay in the circuits that make up the cluster of actions grouped together by a single opcode.  CPU designers try to build each opcode cluster using parallel circuits in an attempt to reduce the worst-case path through a cluster.  

Advances in miniaturization also help reduce worst-case timing.  The closer we can crunch bits of circuitry together, the shorter the distance that electrons have to travel.  Miniaturization is governed by our manufacturing processes.  We usually build CPUs using electronic circuits in tiny chips using chemicals called *oxides* which are the basis for the chemicals called *semiconductors*. The closer that we can push semiconductors together, the faster everything runs.  That's the manufacturing process. If we push the chemicals too close to each other, they slop over and destroy nearby circuits.  We manage to push chemicals closer together without slopping over, every year.  We get better at doing this over time.

[^propagationdelay]: https://news.ycombinator.com/item?id=25106730

## Function-Based Notation
Function-based mathematical notation assumes no propagation delay.  In a way, this is weird, but in another way it is liberating.  We can ignore propagation delay as long as we use the notation for describing effects that take *waaay* more time than the actual propagation delays involved.  When we want to describe effects that are tiny enough to be affected by propagation delay, we must stop using that notation and switch to using something else.  The same is true of systems that stack up propagation delays deep enough to make the delays noticeable.  Kinda like a VISA bill that contains nothing more than a bunch of $10.00 charges but involves a come-to-Jesus moment at month end.

Function-based notation is Sequential in its own way
1. Function-based notation requires that all parameters be "evaluated" before a function can be called.
2. Function-based notation involves ad-hoc *blocking* when one function calls another and must suspend itself waiting for an answer.

In the end, CPUs are Sequential.  If you use a function-based notation to program a computer, the notation must boil down to a set of sequential opcodes - "assembler".

Note that (1.) - evaluation before calling - above results in epicycles (aka "accidental complexity").  For example, the concept of *promises* allows programmers to create parameters that get "evaluated" before a function is called, but, actually defer evaluation until later.  The tower of epicycles grows and grows.  By the time you find it necessary to describe a computer program using *promises* and *monads* you know that you should have switched notations a long time ago.

Note that (2.) - ad-hoc blocking - above results in the invention of epicycles.  For example, preemptive operating systems were invented to control ad-hoc blocking.  A different approach might have been to use a general piece of hardware that runs only one program at a time, being repurposed by the insertion of new shopping lists consisting of opcode scripts.  Computer games took this approach.  Early on, games were sold on floppy disks, and, when inserted took over control of the whole computer.  Later, Nintendo invented cheaper game cartridges.

Most popular programming languages are - currently - function-based, taking after a trend set in 1954 by FORTRAN.  Some other languages are not function-based nor sequential, for example PROLOG.

We hit the limits on using function-based notations when we try to design systems that are fundamentally non-sequential
- e.g. internet (a bunch of hardware-based nodes connected by wires)
- e.g. robotics (a bunch of hardware-based activators connected together into a larger whole)
- e.g. p2p
- e.g. blockchain
- e.g. GUIs
- etc.

One characteristic of function-based notations is that the problems and the solutions contain only one *happy path*.  This characteristic is quite different on some of the above systems - there are more than one *happy path*s in such systems.  

For example, when programming for the internet, it is *not* a exception if one routing path fails - it is just part of life, a part of the problem, something that must be solved.  Treating this kind of thing as *exception*s mis-characterizes the problem and forces a tunnel-vision view on the possible solutions to this problem.

## Rust, Python, Etc.

Note that most popular programming languages, like Rust, Python, etc. are function-based and sequential.

Programs are constructed as *code* files containing lines of text.

These languages are composed of functions that contain lines of code.  The lines of code are executed in a sequential manner, from top-to-bottom, left-to-right.  When a function calls another function, the caller blocks until the callee returns a value(s).

Due to the underlying functional nature of these languages, the issue of *time* is ignored.  Functions appear to receive multiple inputs and produce multiple outputs, but these are just different destructurings of single input parameters and single output values.

This model implies sequentialism.  A function first receives its input, then, it produces an output.  Every function must produce an output after it receives an input.  This model is amply supported by a single, shared callstack.

Other models, like *daemons* and *buffers* are difficult to express in this Sequential Pattern.  Daemons don't need to wait for an input before producing an output and buffers do not necessarily produce one output for every given input.  We have found ways to express these kinds of actions in the over-burdened Sequential Pattern.  The resulting expressions are common, but not necessarily natural to the problems-being-solved.

## Do All Programming Languages Need To Be Sequential?

Does the fact that the sequential pattern worked for organizing asynchronous bits of hardware into CPUs mean that all high-level languages *need* to be sequential, too?

No.

The fact that CPUs are sequential does not necessarily imply that higher-level programming languages need to be sequential, too.

PROLOG, again, is not sequential and covers a problem domain that is just plain hard to express in a sequential manner - exhaustive search.  SQL and Datalog are languages of this ilk.

HTML is non-sequential, but, relies on another sequential language - JavaScript - to do the heavy lifting when the HTML notation becomes insufficient for expressing what needs to be done.

State machine notation, e.g. Harel StateCharts, are not sequential in nature.  State machines allow the expression of control flow branches in a number of directions from any one state.  Using function-based notation plus `if-then-else` mixed with *variables* to express such solutions is courting disaster and leads to bloatware.  This combination of mis-used features is common in most programs today and has led to the mis-characterizations that "state is bad" and that "control-flow is bad".

## Programmability

End-users don't want programmability.

End-users want simplicity.

Simplicity is defined as "the lack of nuance".

Providing options, and, programmability is the antithesis of simplicity.

We should not be providing programmable devices to end users. We should relegate programmable devices only to developers, who can live with the costs and the dangers of programmable devices.

Programmability helps developers reduce development cost, but does not help end-users.  As it stands, end-users are forced to buy expensive computers / laptops / smart-phones, instead of just walking into Radio Shack and buying a Tetris device off-the-shelf for $7.99.

Worse yet, end-users are forced to pay for, and, use programmable computers which can be reprogrammed in the field.  This has at least the following effects:
- programmers feel entitled to deliver buggy, under-tested software to end-users, knowing that programmers can download updates later
- field-programmable computers invite criminal hacking - the devices can be reprogrammed on-the-fly to steal money and valuable information from end-user devices.

## What The Sequential Pattern Is Good For
The best use for the Sequential Pattern is for expressing *calculators*.

The name "computer" belies the early beliefs about electronic machines.  

It was assumed that electronic machines could replace rooms full of humans calculating equations on paper.  

Compute-ers.

An example of such calculation is to figure out the trajectory of military ordnance when fired.  Today, we can create smart bombs and drones by sticking electronic calculating machinery directly into the ordnance itself.

It turns out that electronic machines can do a lot more than just acting like glorified calculators, but, the name - "computer" - stuck.

## What The Sequential Pattern Is Mediocre For
The Sequential Pattern is mediocre for any problem that has multiple *happy path*s, like internet, robotics, blockchain, etc.

Each *single* happy path can be expressed using a Sequential Pattern, but, the overall whole is more difficult to express using only the Sequential Pattern.  Forcing ourselves to over-use the Sequential Pattern for problems that don't fit that kind of treatment results in bloatware, like callbacks, preemption, threading libraries, promises, etc.

## Electronics Is A Throbbing Mass Of Asynchronous Units
Not all electronic consumer devices are based on Sequential operation
	- e.g. stereo systems
	- e.g. guitar stomp boxes
	- etc.

Electronics consists of using chemical compounds to create isolated clumps of electron-driven machinery.

One *trick* for reasoning about such clumps of asynchronous electronics is the use of the Sequential Pattern - espoused as CPU *opcodes*.  

The Sequential Pattern is *not* the only way to deal with clumps of asynchronous electronics.  It is a useful Pattern when used within its sweet spot, but, it gets in the way when over-used.

## Timesharing
In the 1950s, machines based on electronics were very expensive and scarce.

So, the concept of a Central Processing Unit (CPU) was invented and such CPUs were time-shared to fake out the unobtainable ideal of using lots of programmable, electronic lumps.

The Sequential Pattern fits this model very well.  A single CPU can do only one thing at a time.  Figuring out what order to do things in was vital to making electronic machines work.

Today, though, CPUs are cheap and there is no reason to continue using the Sequential Pattern to create larger solutions.

In fact, there is no longer any need to designate a single CPU as being the Central one.

## Memory Scarcity
In the 1950s, electronic memory was very expensive and scarce.

It made sense to conserve memory by using temporary variables and Garbage Collection and File Systems to off-load less-needed data to less expensive storage.

Today, though, memory is very abundant and cheap.  We blithely talk about gigabytes and terabytes, whereas we used to talk about kilobytes in the past.

This should change the way that we treat memory, but, we're still stuck using techniques developed for the kilobyte meme.

## Single Stack
Hardware CPUs provide hard-wired access to a single Stack, usually governed by a special memory location called the Stack Pointer Register.

The Stack is a global variable.

The Stack is shared.

This should be a give-away that hardware CPUs are meant to run single threads. CPUs are, actually, just one kind of FPGA[^fpga].  

[^fpga]: FPGA == Field Programmable Gate Array

Instead of using CPUs to run single processes, we've spent a great deal of human resources on inventing epicycles to allow us to run multiple processes on single CPUs.  The invention of multi-core CPUs is an outgrowth of this kind of epicyclic thinking.

One would not be inclined to pour Linux onto an FPGA, but, we do this all of the time for a special brand of FPGAs called CPUs.

## Arduinos, Raspberry PIs, Etc.

Layering multi-tasking on top of single-stack CPUs is an example of the over-use of the Sequential Pattern.  Any problem that can be solved with one CPU plus Operating System software can be re-expressed as a solution using multiple CPUs each running single-threaded software.  

A lot of software accidental complexity just dissolves away when this more appropriate model of multi-tasking is used.  Programming this way is *simpler* than using towers of epicycles to force-fit too much Sequentialism onto solutions.

## Single-Threading

Lumps of electronics can be used to solve certain sub-problems.

Ideally, a solution containing many such lumps, would run the lumps in parallel to get the maximum throughput.  Running the lumps in Sequence slows the solutions down.

Coordinating the asynchronous lumps becomes an issue.

Sequential treatment is not necessarily appropriate in all situations.  Coordination of isolated, asynchronous processes is one such situation.

## The Human Body
The human body consists of two main lumps of functionality:
1. the autonomous system
2. consciousness.

The autonomous system consists of some 500 asynchronous actuators.

Consciousness appears to be a Sequential layer that dictates intention to the autonomous system, but does not directly control the autonomous system[^micromanagement].

[^micromanagement]: Called "micro management" in business circles.

In the book "The Inner Game of Tennis"[^golf], author Gallwey names the two systems "self 1" and "self 2".  He avoids the use of the phrase "sub-conscious" to avoid the implication that the autonomous system is somehow inferior to consciousness.  The systems work together as peers, not in a master-slave relationship.

Consciousness - coordination - can be expressed in the Sequential Pattern, but, autonomous operation of 500 actuators is less-well expressed in the same Sequential Pattern.

[^golf]: The best book for golfers.

