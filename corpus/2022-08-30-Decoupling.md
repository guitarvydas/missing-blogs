# 2022-08-30-Decoupling
# The Fundamental Problem
All programming languages and all operating systems have one (1) thing in common:
- over-use of synchronization.

Programmers have built towers of epicycles to work around this fundamental issue.

Once understood, it is easy to overcome this commonality.

# Discussion
For example, programmers need to employ elaborate schemes to decouple applications built with implicitly-synchronous languages - like Haskell, C++, Python, etc.

One such elaborate scheme is the invention of *operating systems*.  Operating systems employ the brute-force technique of *preemption* to yank control away from overly-synchronous applications.

Applications, that use the very common technique of function-calling, actually employ *ad-hoc* blocking.

> [!information] Functions perform ad-hoc blocking
> Functions - even in FP (functional programming) languages - are State Machines that mutate a global variable.  At their most basic, functions contain 2 states: (1) pre-call, and, (2) post-return.  When a function calls another function, the caller *blocks* waiting for the callee to return a value.  Since function calls can be inserted into code at any point, they represent ad-hoc *blocks* that take away control-of-blocking from the Operating System. 

> [!information] Functions mutate a global variable
> The call-stack is a shared piece of memory, a "global variable" supported by hardware (using the CALL and RETURN instructions).  All routines in a single CPU share the same call-stack.  The call-stack is used for bookmarking return-points ("continuations").  The call-stack is essentially a dynamically scoped list of bookmarks (space-optimized to be an array).
> Early CPUs did not have a call-stack.  The call-stack was added later.

> [!information] Functions inhibit routing
> In the function-call paradigm, data / message routing is reduced to a single choice - the data is *always* routed back to the caller.  Any other kind of routing strategy is reduced to second-class status and given the derisive name *side-effect*.


What systems should not be strongly coupled?

What systems should be strongly coupled?
- operating system processes -> concurrency -> decoupling
- preemption
- thread safety
- libraries vs. testing
- loops
- internet, IoT, Robotics, NPCs, Blockchain
- concurrency
	- decouple
	- libraries of functionality
- bookmark mutates callstack
- function call overrides blocking control and takes it away from O/S
- text-based programming languages
	- due to 1950's hardware limitations and premature optimization
- thread safety
	- due to mutation
	- remove mutation -> Sector Lisp -> anti-bloatware

# Syntax for Decoupling
... ideas ...

Send (port, data) *- function call syntax*

snd[port, data] *- special syntax*

port << data *- special syntax, less-less-than*

port = data *- assignment-like syntax, requires checking of LHS to see if it's a variable or a port*

port ⇠ data *- unicode operator*
data ⇢ port *- unicode operator*

all of the above transpiled into a function call to Send (...)
when simulating decoupling in sync paradigm