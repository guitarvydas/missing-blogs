# 2022-12-25-Economy of Expression
# Economy of Expression

How easily you can write down an idea - matters.  

EoE - Economy of Expression.

If you write programs as text, then writing 1 line of code is easier than writing 1,000 lines of code.

The BASIC language did not have a "global variable problem" because most early BASIC programs were only a few lines of code long.

As soon as we allowed BASIC programs to grow beyond 7±2 lines in length, we started encountering new *gotchas*, like the concept of global variables.

REGEX is more popular than BNF for writing pattern matchers for strings of characters, because REGEX specifications are very much shorter than BNF specifications.

REGEX specifications have a major flaw when compared to BNF specifications.  REGEXs are not recursive and are restricted to matching single lines of text.

Yet, REGEXs are used by many more programmers than BNF (YACC, LR(k), CFGs, etc.).  REGEX addresses only 80% of the problem.  

That's "good enough".

Theorists and Production Engineers want 100% solutions, practitioners get by with 80% solutions.

# Small is Good

One approach to programming is to devise notations that "dot every i, and cross every T".

Another approach to programming is to use notations that solve "most of" the problem.

The second approach implies:
- we want all program units to be no more than 7±2 "things" in size (thing = line of code or rectangle or ...) 
- we want to build programs up recursively by bolting small program units together to make larger systems, where no unit breaks the Rule of 7.  
	- Each unit stands alone.  A unit's behaviour cannot be changed by other factors (composition, inheritance, etc.)
	- A unit does not need to solve 100% of the problem, just "enough" of the problem to chip away at the problem while remaining understandable to other readers.

How do you create a notation that satisfies those constraints?

1. use the most expressive syntax for a given sub-problem, i.e. text for function-based problems, LaTeX for mathematical problems, node-and-arrow diagrams for networking problems
2. break specific problems down into sub-problems, and use the most appropriate notation for each sub-problem, using multiple, different notations for each sub-problem
4. Example: building parsers for strings of text - Ohm-JS makes it easier to express parsers, 
	- easier than FP, 
	- easier than C, 
	- easier than Rust, 
	- easier than Haskell, 
	- etc.

# EoE Example: Pattern Matching
There is "lightweight" pattern matching and "heavyweight" pattern matching.

REGEX falls into the lightweight category, while CFG-based parser generators fall into the heavyweight category.

The terms "lightweight" and "heavyweight" refer to Economy of Expression.

Examples:
C is lighter-weight than Assembler.  Smalltalk is lighter-weight than C.

Pattern matching is a paradigm. When we write compilers, we, first, solve the pattern matching problem and give the solution the distinguished name "parsing".  You can build parsers in multiple ways:
- ad-hoc code (C, Rust, Haskell, JavaScript, etc.)
- using CFG technologies, like YACC
- using REGEX technologies

Ohm-JS falls into the lightweight category.  Ohm-JS can do things that REGEX can't do, like recursive matching and matching of balanced constructs.  And, Ohm-JS has a nicer syntax than REGEX.

There is no point in using Ohm-JS to compete with YACC.  Ohm-JS loses the first-to-market battle in that arena.

So, what is Ohm-JS good for?

Ohm-JS's big win is that it fills the gap between REGEX and CFG technologies.  Ohm-JS enables a new niche.

## REGEX vs. CFG?
REGEX solves one niche of problems - string matching.  

You can probably solve these kinds of problems using CFG technologies, but, you don't bother, you don't even think that way. 

REGEX doesn't solve 100% of pattern-matching problems, but the 80% of the problems it does solve is "good enough" to be useful.

If only REGEX could recursively match balanced brackets....

# Syntactic LEGO® Blocks
There is no reason to hack that capability into REGEX - Ohm-JS already does this, i.e. Ohm-JS can match balanced brackets, whereas REGEX (and CFG) can't.  

What is needed is a way to bolt partial solutions together, allowing one to use REGEX when appropriate, and, to use Ohm-JS when appropriate, and, ...

Ohm-JS, also, has the ability to skip over uninteresting bits of incoming syntax.  This feature makes it possible to build pipelines at a syntactic level.  One node in the pipeline can deal with one nano-DSL syntax (e.g. bracket matching) and then next node can deal with another nano-DSL syntax (e.g. REGEX) and so on.  We don't need to conflate all of the necessary features into one-language-to-rule-them-all, we simply need to write filters that skip over previous work that doesn't apply.  

This leads to the notion of incremental compilation.