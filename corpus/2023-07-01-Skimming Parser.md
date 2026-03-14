# 2023-07-01-Skimming Parser
[This note is a copy of of a working paper for 0Dv2.  (See full repo in appendix)].

## Sub-goal
I hope to skim the Odin source for 0D and to strip off all type annotations.  

Dynamic languages, like Python and Lisp, don't expect programmers to waste their time figuring out, in painstaking detail the types for all elements in programs.  These languages provide a small set of pre-defined variable types tuned for *design* and allow programmers to elide the issue of mapping these types to more concrete - "efficient" - internal representations.  

Allowing programmers to ignore this set of "efficiency" issues, then, allows programmers to think at higher levels and to concentrate on *design* work instead of *production engineering* work[^pe].  

[^pe]: Note that *production engineering* is but a subset of *engineering*.  Engineers don't write code, they *think deeply* about what code needs to be written.  One aspect - but only one - of *engineering* is *thinking* about low-level "efficiency".  Ideally, engineers should be able to separate *engineering* from *production engineering*, but, in reality, most current programming languages encourage doing exactly the opposite, resulting is more difficulty than is necessary. 

I hope to use an electronic machine to help me do this.  I.E. a "computer".

Traditionally, most programs intended for use on electronic machines are written using *text* and are read sequentially, top-to-bottom, left-to-right.  Odin is such a "programming language".

Skimming such code and deleting type annotations should be a simple task of text manipulation, but isn't very simple using most text-based technologies.  One should be able to do this using only Microsoft Word, but cannot.

The traditional way of grokking text involves the use of *parsers* based on CFG (Context-Free Grammar) theory.  Thinking this way has led to the development of two technologies
1. REGEX - REGular EXpressions
2. LR(k), etc. *parser*s.

Both of these technologies fail to help with the simple task described above.

- REGEXs cannot recur.
- CFG *Parser*s require programmers to create definitions of the *full* programming languages before operating.  Clearly, a task which does not fall into the "quickie" category.

Both of the above technologies fail to understand the concept of matched pairs of brackets.  This has led to horrid design decisions like the use of a single character to delineate, both, the beginning and end of *string*s in programming languages (`"`).  Note that the tool M4 uses two different characters for delineating strings, but, that revelation was ignored in subsequent tools and programming languages.  Note that tools designed for *non*-programmers, like Microsoft Word, also use two different characters (`“` and `”`) for delineating quoted text, but, this idea has not made its way into programming language design.

## Skimming Over Parameter Lists

What we'd like to do is to take a string like `(a : U(V), b : W(X))` and reduce it to a string like `(a b)`.

The possibility that *type*s might contain brackets confounds most CFG-based parsing technology.

You can almost do this using REGEXs, but there are edge-cases that cause grief, say `(a : U(V(W)), b X(Y))`.  Where the stuff inside of the parentheses of `U(...)`can contain an arbitrary number of nested, parenthesized expressions.

Reducing the problem to a test case we get something like `(a:(n),b)`.  This isn't a legal Odin parameter list, but is good enough for testing our approach.

Let's draw a diagram of the string and note the skimming operations that could be used.

![Skip.drawio.svg](Skip.drawio.svg)

Reading from left to right, we see the operations:
1. accept a single character "("
2. accept a single character "a"
3. accept a single character ":"
4. skim over all characters until you see a ","
5. accept a single character ","
6. skim over all characters until you see a ")"
7. accept a single character ")"

The skimming operations (4 and 6) need to be recursive and need to skim over the insides of text enclosed in matched parentheses.  The insides *can* contain "," characters, even though the top-level skim is on the lookout for such characters.

### How do you do this kind of skimming?

In 2004, an alternate form of *parsing* was formalized and called PEG (Parsing Expression Grammar).

PEG-based parsers *can* recognize matched pairs of brackets (and parentheses).  PEG parsers work on different principles, different theories, than CFG-based parsers.

We've had such parsers since time immemorial and called the idea *recursive descent*.  But, recursive-descent parsers are clunky to build and often lead to ad-hoc, buggy code.  

This all changed in 2004 with the introduction of PEG parsing.

Currently, I feel that Ohm-JS is the most convenient parsing technology that is PEG-based.  Most PEG parsing libraries require programmers to sully their grammars with excessive detail, like matching of whitespace and *semantic operations*.  Ohm-JS doesn't require this level of detail.  Ohm-JS grammars are cleaner and more understandable than most other PEG grammars.

I believe that one can create skimming parsers that can handle skimming strings like `(a : U(V(W)), b X(Y))`.  I've built several tests that work in this direction.

I am working on writing a grammar that handles everything needed to skim Odin parameter lists and to break them apart into blobs without worrying about the details of parsing *all* of the Odin language spec.

Note, too, that I am not constrained to grokking *all* of Odin.  I just need to grok enough to handle my problem and to grok *only* my target code (which happens to be the Odin/0D code).

This is a very REGEX-y way of thinking.  YAGNI.  I don't need to solve *all* problems, just my current problem.  Using the principles of FDD, I want to write a *program'* which writes my program for me.  When I change my mind (not *if* but *when*), I am allowed to change my *code'*, then hit a button and my machine automagically generates new code.  No friction.  Re-think, go back to the drawing board and repeat.

My ongoing work is in the repo https://github.com/guitarvydas/0dv2/tree/dev/syntax-mapper.

## Appendix - Repository for 0Dv2 Work

https://github.com/guitarvydas/0dv2/tree/dev

## Appendix - FDD - Failure Driven Design

https://guitarvydas.github.io/2021/04/23/Failure-Driven-Design.html
