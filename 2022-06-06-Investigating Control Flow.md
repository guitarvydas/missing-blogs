# 2022-06-06-Investigating Control Flow---
tags:
- 20220606
---

Control flow has been, generally, ignored.

It is believed that control flow can be subsumed into data flow.  This assumption has led to epicycles and bloatware in software development.

It is recognized that each application requires different data structures.  

Yet, all control flow is subsumed into a single form.

The data structures for control flow are distinct from the data structures for data.

# Taxonomy For Control Flow - Topmost Layer

!![routines.png](routines_16.png)
The programming community has tried building applications using only the left-hand-side of the above taxonomy.

Functions are calculators - they accept a block of synchronous parameters and always produce a block of synchronous outputs.

A block of synchronous parameters is actually just *one* parameter that is an inhomogenous array that can be destructured into several different data types.

The "rest" of computing - internet, distributed, IoT, blockchain, p2p, etc. - falls into the right-hand-side of the above taxonomy.

At present, programmers have few programming languages for creating asynchronous components (UNIX pipes were an attempt in this directions, but were later bloatified), hence, programmers use ad-hoc code to implement asynchronous components.  The code often includes ad-hoc libraries called "thread libraries".

Worse, programmers use languages designed for synchronous programming to write programs in the asynchronous paradigm.  This has caused bloatware and epicycles and bugs.

Various language designs have tried to escape the synchronous paradigm, but are pervasively synchronous under-the-hood.  Javascript callbacks are an example of square pegs being forced into round holes.

# Taxonomy for Control Flow - More Detail
!![syncasyncprogramming.png](syncasyncprogramming_16.png)
# Notes
!![syncasyncprogramming-layernotes.png](syncasyncprogramming-layernotes_16.png)
# Syntax
!![syncasync-syntax.png](syncasync-syntax_16.png)