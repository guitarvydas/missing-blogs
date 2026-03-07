# 2022-11-22-Little Languages are SCNs - The Future of Programming
I agree that "little languages" are the future of programming.

I think, though, that the word "language" is over-loaded and evokes the wrong imagery.

I have switched to using the phrase SCN - for Solution Centric Notation.

You should be able to build an SCN in an afternoon (or less) using Ohm-JS and some underlying toolbox language.

Currently, I use Ohm-JS and JavaScript / Python / Common Lisp.

There is no reason to suffer with building a "complete" language when all of the bits and pieces are already there in other GPLs.  In my mind, Common Lisp has been around a looong time and has collected a bunch of useful, programming features and libraries, albeit in a syntax that only Lispers can love.  Lispers have been using "little languages" for a long time.  They call these things "macros".  Macros allow programmers to create thin veneers of syntax and then to punt the real work to the underlying language/libraries.  Today, with the advent of Ohm-JS (based on PEG), it is possible to build "macros" for languages other than Lisp (you could already do this with other technologies, like YACC, BISON, ANTLR, etc., but they suck you into the mindset of building Languages instead of little notations - SCNs).  Note that Ohm-JS (PEG) can do pet tricks that YACC and friends can't, like parsing balanced brackets.  I think that such tricks are vital to freeing one's mind when designing little notations.

The most common "little language" is assembler.  Assembler abstracts hoary electronics concepts and restricts what you can do, down to a small set of useful use-cases.

Assembler is horrible for human-readability but great for machine-readability (almost no syntax, what syntax there is, is very regular (normalized) and operations are split away from operands (see Cordy's "Orthogonal Code Generator" and GCC's use of RTL which comes from Fraser/Davidson peephole technology (a subset of Cordy-like OCG)). [Aside: Lambda Calculus is re-learning these lessons - operations are split away from operands and the syntax is horrible.  There is essentially one operation: "call function" and all operands are normalized and easily manipulable by machinery (i.e. an "expression language", like Lisp))].

Maxwell's Equations do not describe electricity.  Maxwell's Equations describe a view - a useful view - of electricity.  Electricity is a multi-dimensional effect (3D, maybe more), while the useful view provided by Maxwell's simplifications allow us to use certain properties of electricity in a 2D medium (i.e. clay tablets, paper, oscilloscopes, etc.).


Alan Kay said
> In a 'real' Computer Science, the best languages of an era should serve as 'assembly code" for the next generation of expression.
> 31:50 [https://www.youtube.com/watch?v=fhOHn9TClXY&t=859s](https://www.youtube.com/watch?v=fhOHn9TClXY&t=859s)

[thanks to Rajiv Abraham for pointing this video out to me]

I use Ohm to generate new SCNs that transpile to code in existing languages.

What "assembly" features would I want to re-purpose with new syntax?  Ad-hoc use of "if-then-else" for one.  Lambda-lovers talk about "pattern matching".  In my mind, pattern-matching is just a way to paper-over one kind of  ad-hoc use of "if-then-else".  In the pre-politically-correct days of the 1960s, pattern-matching was called "parsing".  Have we found other ways to elide "if-then-else"?  Yes. OOP elides the use of "if-then-else"for testing operands' Types (we call that "method dispatch"), and, StateCharts elide the use of "if-then-else" for testing objects' State, and, PROLOG elides the usually-insufficient use of "if-then-else" to perform exhaustive search, and, ...