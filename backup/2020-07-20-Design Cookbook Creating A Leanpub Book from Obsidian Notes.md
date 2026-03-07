# 2020-07-20-Design Cookbook Creating A Leanpub Book from Obsidian Notes# The Problem
I have written most of a book in Obsidian and I want to publish the Obsidian notes as a book in Leanpub. 

---

# Divide And Conquer
Let's divide this problem up into smaller problems and solve each one separately.

---

## Divide and Conquer

# The Point of Divide And Conquer

The point of divide and conquer is to take a problem and divide it up into two simpler problems.

The definition of *simple* comes in two parts 
1. The base case
	- the problem is so simple that it can be implemented using any technology that we have access to.
2. The recursive case
	- the  problem is not simple-enough, and, needs to be further subdivided. We keep subdividing until all parts of the problem fit the base case, and, are simple enough to be implemented using existing technology.

## How Divide And Conquer Can Fail
The base case fails if it is altered by the addition of code for other parts of the problem.

In other words, if there are dependencies of *any* kind - implicit or explicit - in the implementations, where making a change in one place inadvertently changes existing code - then divide and conquer fails.

See 
### Dependencies

# Dependencies
Dependencies come in two kinds:
1. Explicit dependencies
2. Implicit dependencies

The simple function call, `f(x)`, creates both kinds of dependencies.

# Explicit Dependencies

The explicit dependency is that of referring, by name, to the function `f`.

DLLs (Dynamic Shared Libraries, .so, .dylib, etc.) attempt to solve this kind of dependency using indirection that is fixed up a load time.  DLLs address this problem in only one direction (*call*)

# Implicit Dependencies
## Blocking

The written function invocation `f(x)`, expects the caller to *block* until the function `f` returns a value.  

In mathematics this does not matter since it is expected that function calls take zero time.

In computers, though, function calls take non-zero-time and use the call stack as a bookmarking data structure.

In both cases the function invocation causes a dependency.  

In mathematics it doesn't matter, whereas, with computers it does matter.

Using a computer, a function call takes some time and we cannot calculate the final amount of time needed for any function call.

This means, that on a computer, the caller is dependent on the callee.

This is a hidden dependency.

If we change code in a library function we also change the code in the caller because the caller is dependent on the library function.

## Return Bookmarks
stack used as a dynamic data structure to record bookmarks

# Scalability

Operating systems isolate components using large-grained processes.

Code inside processes may contain dependencies, hence, cannot be broken apart and scaled.

Operating systems need to use *preemption* to regain control of blocking.


# 0D - Zero Dependencies
more than encapsulation
## How To Reason About 0D 
Don't use technologies that cover up the problem and make it easy to deal with dependencies, e.g.
- make (don't use make)
- package managers (don't use package managers, packages, etc.)
- don't use preemption
## 0D Using Python
Don't use function calls (across components).

Break call dependencies by using deferred Send ().

Queues - input and output.

Components cannot refer to other components, they can only send messages.  Messages are routed by Parent Containers, not by the components themselves.

2 types of components:
1. Leaf
2. Container (Router)

Processes.

Make everything explicit, including stacks.  Recursion becomes feedback loops that modify stacks (this is implicitly done with FP languages now).

 for what kinds of dependencies might exist.

## When To Iterate 
We need to iterate when our understanding of the problem changes.

For example, we may discover new details about the problem, or, we may find unanswered questions about the problem.  When we get answers to the questions we may need to go back to the top and start again.

# Tools For Iteration
We need to use tools and languages that support iteration and wiping out what we had before replacing it with something new

When we use a systems programming language like Rust or C, we are reluctant to change existing code.

When we use a dynamic language like Lisp, we have less resistance to throwing away existing code and starting again.

# Types
Type systems work in two ways:
1. Type systems help us understand a problem 
2. Type systems constrain our Designs and make us reluctant to make changes in what we've already written.

In essence we want to use a typeless language and apply types only where types help our Design process.

Later, when we want to Production Engineer the code, we want very tight type checking to help remove errors in the code and to check the consistency of the code.

# Provenance
We want to Design in dynamic languages and Production Engineer (optimize) in static languages.

Ideally, we want to track the *provenance* of optimized code back to its original Design.

We want this tracking to be automatic.

