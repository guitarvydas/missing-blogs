# 2022-08-05-Functions Are State Machines That BlockA *function* is a 2-state state machine:
1. pre-call
2. post-call

A *function* that *calls* another function, *blocks* waiting for the callee to *return*.

The difference between 1 and 2 is not noticable when writing functions on clay tablets and paper, because there appears to be no latency incurred by the *call*.

When you map *functions* onto CPUs, call latency becomes real (non-zero).

To keep the *fiction* of zero-latency calls alive...
- programmers have invented workarounds like *node.js* using terminology like *asynchronous*.
- operating systems resort to *preemption* to yank control away from functions.
