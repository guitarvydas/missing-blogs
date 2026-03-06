# 2022-06-15-Control Flow and Data FlowI think that it is beneficial to separate "control flow" from "data flow".

There is no "right" or "wrong", just "easier".

The term "data flow" means various things to various people.  Usually the term refers to some kind of ad-hoc thinking which tangles up operations with operands.

I like to think of *operators* as being orthogonal to *operands*.

To me, *operands* are OO objects with methods that are functions.  You ask the object for information, it returns the information to you.  Like in math, a method might return an answer based on a set of conditions.

*Operators*, though, are bits of code that, well, are not natural functions.

*Send* is an example of an *operator*.  It has a side-effect and does not, naturally, return a value.  *Send* causes a message to be sent in a one-way direction.  Better yet, *send* works in a *deferred* manner.  A *deferred send* simply appends a message to an output queue.  The output queue is emptied, later, by a *router*.  *Deferred send* creates more flexibility during Design.  The *sender* cannot know where its message will be routed, nor, if the message will be routed at all.  This implies that the *sender* is truly *0D* (has zero dependencies) and can be shuffled around in the design.

It is *possible* to force *Send* to *look* like a function by adding epicycles and complexity.  In the worst case, *Send* can be converted to a function with hard-wired synchronization.  In this case *Send* becomes a multi-step molecule
1. send the message
2. block until the Receiver replies
3. continue.
This sequence has hidden implications.  It requires that the Receiver *send* a response to the caller - and only to the caller.  This sequence constrains what the Receiver is allowed to do.

For some purposes, e.g. building distributed calculators, a function-like *send* can be a useful organizing principle.  For other purposes, though, this sequence does not describe the reality of distributed computing.  For example, internet *Servers* can be made to look like functions only by adding complexity.

Thinking that all programs must be couched as functions has led to the invention of RPCs and to the renewal of interest in GOTO-based programming, rebranded as "CPS".  In some cases, this is useful, but it does not model what is really going on at the most basic level.  It would be better to handle some of the cases by creating new SCNs that elided the operation of *send* instead of re-defining *send* in the bowels of basic programming languages.

It is my belief that the concept called "data flow" is meant to be a restricted variant of message-passing.  The idea is that, both, the *sender* and *receiver* are made to look like functions that send messages, containing data, to each other.  On top of that, the *receiver* is constrained to avoid asynchronous behaviour - it waits until *all* data inputs have arrived before doing anything.  This idea makes sense for simple functional components, like `response := b + c`.  In  this case, the `+` and the `response` are not triggered until, both, `b` and `c` have arrived.  The underlying system sorts out the partial-arrival state machine, handling the cases where `c` arrives before `b` and where `b` arrives before `c` (physics says that there is no case where `b` and `c` arrive at the same time, although slow hardware can make it look like that).  This model might be useful in a minority of cases, but it does not faithfully model what is going on in a distributed version of the system.  The fact that the model does not correspond to reality means that the model cannot be use to *program* the underlying distributed system, leaving such programming to be done in a mostly ad-hoc manner.  This probably led to the invention of *callbacks*.
 
I argue that system programmers need to model *programming* in a way that is a true model of the underlying reality.  Systems programmers can, then, decide whether to elide parts of the detailed model by creating SCNs for use by other programmers.

I would argue that we cannot program distributed systems by lying to ourselves about what is really going on at the most basic levels.  We need a model(s) that describes distributed programming as a set of atomic operations, not a combination of such operations.

To this end, it appears that segregating *operands* from *operators* is beneficial.  This worked for assembler programming.  GCC, for example, used a model based on the concept of Orthogonal Programming (Fraser-Davidson's "peephole" RTL technology).  "Code" is generated in 2 phases:
1. first, code is generated without regard to the *operands* - all operands look like *registers*
2. second, *operands* are re-considered, without regard for the *operations* (the code generated in step (1)) and the code is modified (improved) based on the *operands*.
Cordy's thesis, "Orthogonal Code Generation" explains a more general version of this model.  BTW, Cordy's *condition descriptors* look a lot like today's λ-calculus-based programming constructs.  *Condition descriptors* were invented in the 1970's.  Cordy describes the algorithms and a declarative syntax for generating code based on orthogonal principles.  

I argue that programmers can create Orthogonal Programming Languages by using **OO** ideas for *operands* and **Ohm-JS** ideas for writing *operations* as text phrases.

[I, further, argue that programmers should reconsider their religious belief that programming can only be done with text.  Programming is about controlling machines, and only secondarily about building scripts in text form.]
