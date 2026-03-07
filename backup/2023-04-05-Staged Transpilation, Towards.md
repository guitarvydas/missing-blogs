# 2023-04-05-Staged Transpilation, Towards# Towards Staged Transpilation (WIP)

## Goal
I think that compiler-building is a lot simpler when *divide-and-conquer* techniques are used.

I think that it is vital to allow *composition* of syntax.

I think that it is helpful to build compilers as little barnacle processors arranged in neat pipelines.

To this end, I think that it is necessary to normalize all source code into some normal form, thus, breaking up the task of building compilers into roughly 2 stages
1. compile all syntaxes into the normal form
2. compile the normal form into all target languages, like Python, Common Lisp, Odin, etc.

## Background

I'm building a transpiler to compile Ceptre source code into Common Lisp, and, later, Python, etc.

The work in progress is in the repo https://github.com/guitarvydas/ceptre.

I've chopped the work up into 2 main pieces, based around something I call RT (recursive text).  RT is meant to be a generalized *syntax* for holding program source code, without ascribing meaning to the source code.

The steps then become:
1. Compile Ceptre syntax in RT syntax
2. Compile RT into {Python, Common Lisp, etc.}

IMM[^1]  each of the above steps is a lot simpler than trying to write a Cepter-to-{Common Lisp, Python, whatever} compiler as one big blob of code.

[^1]: In My Mind

RT allows me build the transpiler by *composing* bits of text-manipulation[^2] into a larger whole.

[^2]: Note that *text manipulation* is the main schtick of mathematical notation and of functional progamming.  All of the cabalistic rules of FP amount to nothing else but making it possible to find-and-replace text.  For example, the "no side effects" rule is necessary for allowing textual replacement (also called "referential transparency").  Note, that "mathematics" breaks down into largely 2 pieces: (1) a notation and (2) lots of thinking.  I'm only addressing part (1).  The goal should be to allow thinkers to think, instead of wasting their time learning how to do find-and-replace.

RT is a normalized form of source code that makes it easier to build compilers (at least IMM).

In fact, the RT used here is specific to Ceptre, and is, thus, suffixed with .CST.  The second step compiles Ceptre-specific .RT (called .CST) into {Python, Common Lisp, etc.}.

It is _possible_ to used a generalized syntax, .RT, to house the program, but, the program is meant to contain Ceptre-specific instructions, hence we rename the .RT as .CST. 

I believe that it is not possible to generalize .RT to cover every use-case, and, hence, I don't bother to try.  At some point, specialization, instead of generalization, becomes necessary.

IOW: RT is a syntactic skin that allows us to represent all programs in a textual form that is easier to transpile into other languages.  The meaning of what is _contained_ in the .RT file is dissected by step 2 and is meaningful only in a context of compiling whatever - e.g. Ceptre - into other languages.

Aside: if you squint, you'll see that Lisp is actually a 2-part language.  A syntactic skin - a lot like RT - and a fixed set of meanings (the "semantics").  The meanings, in Lisp, are that Lists are recursive things that are bracketed, syntactically, by parentheses and that non-bracketed things are Atoms (non-recursive).  In Lisp, the first item in a list is ALWAYS a function and the rest of the items in the list are arguments to the function.  If the first item is an Atom, then it is taken to be the name of a function, or, if the first item is a List, then it is taken to be an anonymous function (a "lambda").  Note that this set of rules - meanings - applies ONLY to Lisp's understanding of what is contained in the .RT-like text that makes up a Lisp program.  Ceptre, for example, doesn't have the same set of rules, yet, can, also, be represented in .RT syntax.  So, what is contained in a Ceptre-specific .RT - .CST - file?  It depends on the Ceptre-CST "compiler" app.  It is _very_ convenient to split everything up into only 2 camps: Functions and Atoms.  Maybe the Cepter-CST transpiler will use that convenient meaning, or, maybe not. The final decision is up to the person(s) who writes the Cepter-CST transpiler.  That decision affects how the front-end (1) is written, too.  Whatever technology is used (e.g. compiler-compiler, Python, JS, etc.), the resultant transpilation of Ceptre syntax to CST MUST match what the Ceptre-CST transpiler expects.

Aside: Once we have pounded any syntax into .RT syntax, then, we can use a simple set of tools - like Ohm-JS - to do further work with the .RT file.  For example, if we know that the input - if it doesn't have any syntactic errors - is meant to be a Ceptre program and that Ceptre-CST semantics apply, we can "more easily" generate the Ceptre-CST compiler using Ohm-JS.  Most of the Ohm-JS turns out to be boilerplate.  Further, we can chunk the task of writing a Ceptre-CST compiler, by using divide-and-conquer.  We can create a pipeline of tiny barnacles.  Do a little bit of textual manipulation, then pass the work on to the next stage in the pipeline.  In the future, we might avoid step (1) by simply not creating languages that aren't already in .RT syntax.  OTOH, many people won't want to work directly with .RT syntax, and, for those people, we can build syntax skins to make their eyes hurt less.

Aside: boilerplate is "good".  Compilers are simply boilerplate-generators.  Machines are stupid.  We need to dumb-down HLL syntaxes to make it easy for machines to generate code.  The more boiler-plate-y something is, the more likely it is that it can be automated, i.e. turned into instructions for a dumb machine.  Techniques - such as RTL (Fraser/Davidson, then, GCC), OCG (Orthogonal Code Generation) exist for optimizing extremely-stupid boilerplate code into less-stupid code.  It's difficult - boringly repetitive - to build compilers.  Boilerplate-ing makes it easier.  Post-processing makes it look less stupid.