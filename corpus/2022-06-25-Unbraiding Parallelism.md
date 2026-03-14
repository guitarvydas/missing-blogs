# 2022-06-25-Unbraiding Parallelism
# Unbraiding Parallelism
I apply divide-and-conquer to the concept of parallelism and I unbraid it as:

1. 0D
2. scheduling

# 0D
Zero Dependencies

You can't create parallel components unless they are completely independent of one another.

"Encapsulation" is not enough.  I've used the term "isolation" to describe components that are independent in terms of data-sharing and control-flow behaviour.

Now, I use the term *0D* to describe components that are completely isolated in data and in control-flow.

Note that just about every common programming laguage uses function calling and return.  This creates implicit dependencies and blocking control-flow behaviour.  Most standard programing languages - Rust, Python, JavaScript, Haskell, etc. - create implicit dependencies through the use of function calling.  Smalltalk *methods* are based on function calling, hence, Smalltalk encapsulation does not isolate control flow.  PROLOG and other relational languages delegate control-flow behaviour to the underlying kernel and, hence, appear not to create implicit depedencies in this way.

# Scheduling
Simultaneity:
- *Parallel* activities are multiple copies of the same activity, done "at the same time".
- *Concurrent* activities are different activities, done "at the same time".

Doing something "at the same time" as something else is purely an *optimization*.  The activities don't change, but, when combined into a system, the sytem's final result might be reached more quickly if the activities are carried out simultaneously rather than being done serially.

You can't schedule activities simultaneously unless they are, each, written in 0D style.  NB. this is one of the aspects of what is currently called *parallelism* - code is written to avoid sharing data (state) and control flow is regulated by *preemption* in process wrappers supplied by operating systems.

A system composed of simultaneous components will take as least as long to run as its slowest component. For example, a system composed of 3 components, A, B and C must wait until all components have finished executing.  If A and C finish before B does, the system must wait for B to finish before finalizing its result.

# Message Passing
The most straight-forward way to implement 0D components is to ensure that they have
- input APIs
- output APIs.

Each component is fully defined by what it inputs and what it outputs.

Message-passing is a technique that allows components to be defined this way.

Function-calling is a technique that inhibits such component definitions, especially when function-calling is implemented with current CPU assist (CALL/RETURN assembly instructions).

Most modern operating systems (Windows, MacOS, Linux, etc.) provide for message-passing between processes (AKA "IPC").

# Rob Pike "Concurrency is not Parallelism"
https://www.youtube.com/watch?v=oV9rvDllKEg

# Blocking
It is assumed that *operating systems* control *blocking*, but this is not entirely the case.

Functions that call other functions (e.g. calling library functions) *block* waiting for a reply from the callee.

Blocking due to function calling, thwarts the efforts of operating systems to control behaviour of applications, and, requires operating systems to implement blunder-buss approaches like *preemption* to regain full control of applications.

Implicit blocking, due to the use of function calls, breaks the principle of "locality of reference"

Implict blocking also creates implicit dependencies and thwarts attempts to create 0D components.  Various complicated work-arounds ("epicycles"), such as package managers, have been created to deal with the problems of implicit dependencies.  IMO, it would be better to create true 0D components rather than creating N0D components that require epicycles to handle the gotchas created by the implicit dependencies.

# /bin/sh `&` and `wait`

The UNIX shells - /bin/sh, /bin/bash, /bin/zsh, etc. - allow programmers to create 0D components, then compose the components simultaneously and *wait* for their termination.

The input APIs of such programs are called `stdin`

The output APIs of such programs are called `stdout` and `sterr`.

Note that these APIs are restricted versions of a more general model, wherein there might be many inputs and many outputs, not just 1 and 2 respectively.

Under-the-hood, UNIX allows the creation of more-rich APIs using *file descriptors* (FDs), but these need to programmed at a low-level (e.g. using C code).

The choice of such restricted APIs stems from the paucity of using *text* for writing programs.  Text can be used to easily express mathematical expressions, but text is stretched beyond its "sweet spot" when richer APIs are needed.

# Raspberry Pi Model of Simultaneity
Biases about programming were formed in the mid-1900s based on hardware of the day 
- CPUs were very expensive and needed to be time-shared
- Memory was very expensive and needed to be preserved, and, memory use needed to be optimized and garbage collected.

Modern hardware invalidates many of these biases:
- CPUs are cheap and plentiful
- Memory is cheap and plentiful.

Operating systems and programming languages based on mid-1900s biases must be replaced by programming models that reflect the new reality in hardware.

For example, the out-dated concept of *thread safety* becomes a non-issue when apps are located on physically distinct computing platforms like inexpensive rPIs or phones or IoT, etc.
