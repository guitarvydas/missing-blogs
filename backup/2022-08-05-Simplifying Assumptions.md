# 2022-08-05-Simplifying Assumptions# Simplifying Assumptions - Elementary Physics
In Physics, one creates *simplifying assumptions* if an effect-to-be-analyzed is much, much, bigger than any effect ignored by the *simplifying assumption*.

# Functions Are State Machines That Block

## 2022-08-05-Functions Are State Machines That Block

A *function* is a 2-state state machine:
1. pre-call
2. post-call

A *function* that *calls* another function, *blocks* waiting for the callee to *return*.

The difference between 1 and 2 is not noticable when writing functions on clay tablets and paper, because there appears to be no latency incurred by the *call*.

When you map *functions* onto CPUs, call latency becomes real (non-zero).

To keep the *fiction* of zero-latency calls alive...
- programmers have invented workarounds like *node.js* using terminology like *asynchronous*.
- operating systems resort to *preemption* to yank control away from functions.


# Questions
Functional notation assumes that *calls* have zero latency.

CPUs implement *calls* with some latency.

Is "functional notation" a valid *simplifying assumption* for computing using CPUs?

Does "functional notation" apply to all of computing or only to a subset of computing?

# Simplifying Assumption - Build And Forget
In just about everything designed by humans, it is assumed that the design will continue working "as is" after a bit of bench-testing.

In software design, though, this simplifying assumption does not hold.  Programmers have invented a word for this kind of problem : dependency.  

When a software component is added to an existing software system, it is unclear if the old system will still work they way it did.

Why?

This problem is sometimes referred to as "whack-a-mole".

Build an intricate Swiss clock using many interconnected gears.  Add one more gear to the clock.  Take one gear out.  Does the clock still function as it did?  Maybe, maybe not.

This is how software is currently designed.  Software is a gearbox containing many interconnected gears ("dependencies").

The "Build and Forget" assumption requires zero interdependencies between system components.

In software, programmers should be striving to build systems using 0D (zero dependency) components.

## 0D - Existing Kinds of 0D
The example of 0D that I am most familiar with is the UNIX® pipeline.

Processes are 0D.  The insides of processes are not 0D.

Forcing processes to follow *rendezvous* protocols causes processes to be more gear-like in behaviour and to lose their 0D-ness.

The UNIX kernel goes out of its way to force processes to follow *rendezvous* protocols.  Bash's `&` command coupled with redirection results in surprises.  Generally, forked process hang until all of their input and output files are activated by the presence of other processes at the opposite ends of these I/O files.
# 0D - Implementing 0D Using Current Programming Languages
0D is "easy" to implement in existing languages, if you know that you want it.

Avoid the use of the callstack, i.e. don't call functions or `return` from functions.  Use FIFOs instead.

Hardware-supported `CALL/RETURN` instructions create hidden, dynamic dependencies and use a hidden global variable (the callstack).

The hidden dependencies are hardwired assumptions about data routing, e.g. where parameters are sent and where results are sent.  Internet servers do not hardwire such routing information into their code and, hence, are harder to describe using existing programming languages (that assume routing information has been hardwired).

It is "easy" to continue using function-call-like syntax, e.g. `f(x)`.  Transpilers based on Ohm-JS and PEG can be built to convert function-call-like-syntax into FIFO-stuffing code sequences.  For example, `f(x)` could be rewritten as `send ("request from f", x) ; yield` followed by `handle ("return from f") {...}`.  The latter form is much more verbose, but, can be elided to read as `f(x)` using a transpiler.