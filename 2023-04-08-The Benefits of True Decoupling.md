# 2023-04-08-The Benefits of True Decoupling# The Benefits of True Decoupling
- probes
- incremental compilation
- reshuffle architecture
- LEGO-like software blocks
- unit testing
- incremental type checking
- syntactic composition
- nested packaging

## Unit Testing
Unit testing without dependencies is possible.  But, existing unit testing frameworks drag in other software due to dependencies.  0D decoupling reduces dependencies and makes unit testing leaner and more focussed on the unit under test.

## Syntactic Composition - Macros vs Hygienic Macros vs User-Friendliness
Syntactic composition is the same as phased compilation, and, macros.  

The whole issue of "hygienic macros" is the creation of macros without using phases[^swoop]. The advantage of hygienic macros is rigor without respect for UX issues. The drawback of hygienic macros is that they are not very user-friendly, aka "too complicated" for normal use. 

[^swoop]: One fell swoop technique ≡ crush all phases into a single phase, disregarding accidental complexity that is caused by doing things this way.  Accidental complexity is fixed using the application of ad-hoc, epicyclic band-aids.

Phased compilation produces hygiene, and, chops compilation up into smaller bits, i.e. phased compilation is *divide and conquer*.

### Why Hasn't Phased Compilation Been Used Until Now?

Historically, building syntax has been considered to be difficult, thanks to CFGs.

Up until now, building more than one syntax phase has been considered to be too much work.

Now, though, PEG parsing has re-opened the door on what can be done syntactically, easily.  In my view, Ohm-JS is the most advanced form of PEG parsing.

It is - now - possible to build many little syntax-based phases.  We don't do this at the moment, because of the "we've always done it this way" mind-virus.  CFGs address the concerns of the 1950s.  PEGs allow us to mollify 1950s-based concerns.

## Insidious, Hidden Coupling
- call-return
- hard-coded routing
- hard-coded removal of *t* dimension (*time*)
- hard-coded name-calling
- 1 in, 1 out

## True Decoupling (0D)

!![400](images/2023-04-08-The Benefits of True Decoupling 2023-04-09 17.53.46.excalidraw.png)


0D is laugingly easy, especially with closures and queues.

Examples of 0D are:
- CL0D - Common Lisp - Alists and Lambdas (no need for *self* nor *classes*) - https://github.com/guitarvydas/cl0d
- PY0D - Python3 - https://github.com/guitarvydas/py0d
- Odin0D - Odin - https://github.com/z64/odin0d

0D decoupling defines two APIs for each software unit
1. the input API
2. the output API.
Software components cannot call other software components.  Software components *must* use their own output API, instead.

Probes need fan-out.  Forbidding fan-out due to academic reasons discourages use of the probing technique.
!![200](images/2023-04-08-The Benefits of True Decoupling 2023-04-10 17.54.20.excalidraw.png)


In electronics, probes suck a tiny bit of current away from the circuit being probed.  Electronics probes are "high impedance" and tend not to interfere with circuits under test.  Oscilloscopes and ohm-meters are electronic probes, but, lower-cost, stand-alone probes exist, too.

In software, fan-out requires data copying and atomicity[^ad].  All easy to do.

[^ad]: Atomicity is required for message delivery.  Only.  Atomicity is not required for other operations.

Processes in operating systems rely on true decoupling.  The operating system is free to schedule execution of software components in various ways.  True decoupling (0D) can be done much more efficiently than by using processes.  There is nothing new here.  Making processes cheaper ("more efficient"), though, encourages their use in subtle, new ways.

The main feature of operating systems is that operating systems isolate - using hardware assist - adversarial processes and address spaces from one another.  A drawback is that such isolation requires sledge-hammer techniques like preemption.

Preemption is *not* necessary for multitasking within a single software app, where *bugs* are just *bugs*.  Much less hardware-assist is needed in such cases, reducing cost and running time.  Contrary to popular belief, multitasking *can* be done using cooperative multitasking techniques.  Loops and deep recursion must be forbidden in such systems. Long running loops and deep recursion are simply considered to be *bugs* that need to be repaired.  Internet-y problems make Loops and Recursion unusable, anyway[^loops].

[^loops]: Loops and deep recursion can be used to describe the innards of single nodes in distributed systems, but are useless for describing the distributed systems themselves. Current popular programming languages are, at best, assembly languages for the expression of distributed systems.