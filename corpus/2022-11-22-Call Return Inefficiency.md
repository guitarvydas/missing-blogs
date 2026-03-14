# 2022-11-22-Call Return Inefficiency
Call and Return instructions are used in 2 ways
1. to help developers build software in a DRY (Don't Repeat Yourself) manner, and, 
2. to reduce code size by sharing code chunks.  

Programming languages abuse Call/Return and cause runtime inefficiency by solving the DRY issue (1) at runtime.  

This problem could be fixed by the creation of better editors. In fact, much of OOP could be done by creating better editors instead of punting code reuse to the runtime use of Call/Return.  

Any language that uses function calls at its core is probably using Call/Return inefficiently.

# Simple Example
Here's a very simple example.  A developer might write:
```
function firstapp () { return 5 + 1; }
function secondapp () { return 8 + 1; }
```
This code can be DRY-ified as:
``` 
function add1 (x) { return x + 1; }
function firstapp () { return add1 (5); }
function secondapp () { return add1 (8); }
```
The helper function `add1` has been added to help the developer *only*.  The machine doesn't care if it sees:
```
firstapp:
  LOAD R0,5
  ADD R0,1
  RET
secondapp:
  LOAD R0,8
  ADD R0,1
  RET
```

or, if it sees:

```
add1:
  ADD R0,1
  RET
firstapp:
  LOAD R0,5
  CALL add1
  RET
secondapp:
  LOAD R0,8
  CALL add1
  RET
```
The inserted CALL in the second code sequence adds CPU cycles and is inefficient.

The machine doesn't care if code is duplicated, only developers care. DRY is a way of avoiding bugs due to Copy/Paste during development.

If our editors tracked which blocks of code were "the same", we wouldn't need to use runtime Call/Return for DRY.  *Diff* and *git* demonstrate that we know the algorithms for tracking code similarity.

Interesting reading might include: 
- [Framing Software Reuse](https://www.amazon.ca/Framing-Software-Reuse-Lessons-World/dp/013327859X)
- [NiCad](https://www.cs.usask.ca/!croy/papers/2011/CR-NiCad-Tool-ICPC11.pdf)

# Inline Functions
In fact, we see programming languages attempting to back out of the corner created by abuse of Call/Reutnr, by detecting "inline" functions and compilng them differently.

# Aside - Hard-Wired Global Variables
Note that the second code snippet uses a global variable to store return bookmarks.  

We call this global variable "the call stack".  

Note that the Call and Return instructions, both, mutate this global variable and its associated pointer (SP).

