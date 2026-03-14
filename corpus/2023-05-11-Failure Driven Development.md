# 2023-05-11-Failure Driven DevelopmentWriting code that attempts to predict the future is, also, called "Waterfall Development".

In Waterfall Development, one never throws previous code away, but, simply adds to it.

In other words, one discovers that the code did not correctly predict the future, so options and fixes are applied to make sure that the code predicts the future.  Correctly *this time*.  The implication is that the code has been modified to predict the future - and - that this is *the last* upgrade needed to make the code predict the future correctly.

This is a problem.  It leads to ad-hoc Architecture - the resulting code is hard to understand.  The problem is caused by conflating two concepts:

1. business rules
2. control of an electronic machine (a PU (formerly called CPU))

## Solution?
A solution to this problem is to reduce the friction against throwing code away and "going back to the drawing board", i.e. writing new code.

We want to preserve the hard-won knowledge - the business rules - while tossing away code that doesn't correctly convert the business rules (newly re-understood) into machine code.

We want to get the business rules right.  I think that the easiest way to figure out the business rules is to iteratively try out little MVPs, each one incorporating the hard-won knowledge gained in previous MVPs.  Once we feel happy with our understanding of the business rules, we want to smoothly transition the business rules into code that controls a machine.

One way to do that is to write code that writes code.  Express the business rules in some pseudo-language, then press a button and generate code for controlling a PU.

Advances in pattern-matching (aka *parsing*) technologies such as Ohm-JS (PEG) make this a reasonable proposition.  Unlike in the past, where CFGs were used to laboriously define new languages, one can build new syntax - SCNs - in an afternoon.  

The ideal IDE for such quickie language development is something like Ohm-JS plus a *toolbox* of functionality. Most existing languages make pretty good *toolboxes*, except for their pesky syntaxes.  

Lisp is a fairly syntax-less language.  Lisp has been developed and extended for decades.  Lisp makes a pretty good *toolbox* language.  Lisp's lack of syntax makes it easy to target code generation using something like Ohm-JS.  Lisp is, essentially, a bag of functionality and its syntax-less makes it least necessary to jump through hoops when generating code.

## See Also
Previous discussion of FDD - Failure Drive Development - https://guitarvydas.github.io/2021/04/23/Failure-Driven-Design.html