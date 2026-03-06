# 2022-05-28-Functions Are Not Atomic`f(a,b,c)->(w,x,y,z)`

means:
- `f` is a function of a *single* synchronous parameter
- `f` returns a *single* synchronous block of results
- `f` is a 2-state state machine.

It *appears* that `f` takes 3 parameters and returns 4 results, but, actually, `f` takes a *single* parameter which can be deconstructed into 3 other things.  The parameter is a non-homogeneous array containing objects.

`f` is a state machine, because it might call another function.  The 2 states of `f` are:
1. ready
2. blocked.

On transition from the *ready* state to the *blocked* state, `f` executes some code.

When `f` calls another function, `f` blocks itself until the callee signals a `resume` event.

In current CPU apis, the transition from *ready* to *blocked* is written as several sequential assembler instructions followed by a `CALL` instruction.  The CPU hardware blocks `f`, modifies global variables (the SP register and the in-memory array called *the stack*), then modifies another global variable (the PC register) and executes the code in the callee.

The transition from *blocked* to *ready* is implemented by the `RETURN` instruction, which is, also, hard-wired into the CPU.

Destructuring of the parameters in the callee is performed by reading the in-memory array and executing several sequential opcodes.

Destructuring of the return value is done in the caller in a process similar to the destructuring of the parameter block.

The parameter data and the return data is *synchronous* - the data is sent in a block and is received in a block.

The individual elements of a data block are not distributed in time, as would be if they were truly asynchronous.

This model of computing is simple for single-cpu systems, but is strained in the presence of distributed computing (e.g. internet, IoT, blockchain, etc.).

This model, also, distributes the responsibility for *blocking* to many places in the code, affecting locality-of-reference.

Traditionally, it is thought that *blocking* is controller by the operating system (e.g. Linux, MacOS, Windows, RTOSs, etc.).

This non-locality-of-reference results in epicycles being added to operating systems. Operating systems need to use a sledge-hammer approach to wrench control away from functions, in the form of *preemption*.


## preemption

Preemption is not necessary in a truly asynchronous system, since processes run at their own speed and handshake when synchronization is necessary.  

Imagine 2 rPIs connected by a wire.  

The rPIs are asynchronous and can run at their own speed.  Maybe one rPI is a cost-reduced version and the other is souped-up for speed, and, they truly run at different internal speeds.

The rPIs send blips (messages) to each other across the wire, when they want to communicate or synchronize.

[Aside re. optimization: In fact, the general model would use multiple one-way wires in each direction.  Reducing the system to a single wire is an optimization which costs CPU time for packing and unpacking the messages. In the ultra-general case, one would expect one one-way wire for each *type* of information, e.g. control message, int, float, compound object, etc.]

Preemption is not necessary in a truly asynchronous system, since processes run at their own speed and handshake when synchronization is necessary.  Imagine 2 rPIs connected by a wire.  The rPIs are asynchronous and can run at their own speed (maybe one rPI is a cost-reduced version and the other is souped-up for speed).  They send blips (messages) to each other across the wire, when they want to communicate or synchronize.