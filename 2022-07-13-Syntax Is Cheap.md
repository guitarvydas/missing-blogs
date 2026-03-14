# 2022-07-13-Syntax Is Cheap
# Syntax Is Cheap

There is no need to build DSLs using tortured function-calling syntax.  You can build any syntax you want.

For example, instead of saying
```
fadeToBlack(40)
```
you can say
```
fade to black over 40 frames
```
or, even better ...
```
fade to black
```
which, then, is undestood to mean "fadeToBlack(40)"

# Syntax-Driven Programming

You can map any syntax to any intermediate syntax, then into "programming API" syntax, e.g.
`fade to black` -> `fade to black over 40 frames` -> `fadeToBlack(40)`

You *could* go directly from the first to the last phrase, e.g.
`fade to black` -> `fadeToBlack(40)`

But, using an intermediate syntax ultimately gives you more flexibility.  In this particular case `over 40 frames` is a parameter which might be different in every project.  

Maybe, in one project, you want `fade to black` to mean `over 40 frames` while, in another project, you want it to mean `over 30 frames`.

Maybe, in another project, you want it to mean `over 1 second` (regardless of how many frames that turns out to be).

The traditional way of dealing with this problem is to build a library function which is parameterized, and then is parameterized some more as users play whack-a-mole with the function.

In the end, the ultra-parameterized function is so abstract that it becomes hard to understand and to use.

Instead, you can build a unique *syntax* for every project and let Production Engineers deal with the meaning (mapping) of the phrase `fade to black` and how it gets converted to a library API call.

# Why Don't We Already Do This?

Until recently, it has been difficult to build syntaxes.  

Syntaxes have been considered to be tangled up with compiler-building, and, it has been assumed that compiler-building is a mega-project that usually takes years (not minutes) to build.

If you could cleave *syntax* away from compiler-building *and* make syntax-building really, really easy, it would make your approach to solving the problem different.

You *could* imagine building little-syntaxes that are unique to every project.

In fact, we kind-of already do this by using REGEX in our projects.  The problem is that REGEX isn't sufficiently powerful and has a fugly syntax.  REGEX is just a DSL for pattern-matching.

Enter: Top-Down Parsing.  TDPLs[^tdpl].

[^tdpl]: TDPL means "Top Down Parsing Language".  "Parsing" is just a fancy word for "pattern matching".

ATM (At The Moment), I think that Ohm-JS is the most-convenient TDPL that exists.  

# Ohm-JS
Ohm is a DSL for pattern-matching.

Ohm is better than REGEX in that Ohm can handle nested text and nested brackets[^theoretical].

[^theoretical]: Theoretical approaches don't seem to be able to handle nested brackets.

Ohm needs more lines-of-code than REGEX does, but, that makes Ohm specifications more readable IMO.

When you match a phrase (a "rule"), what happens?

In pure Ohm-JS, you get dumped into JavaScript.  Ohm-JS gives you the first part of the equation - the pattern matching DSL - but leaves you in JavaScript-land after the match.  Each sub-match is passed as a parameter to a JavaScript function.

REGEX is even worse.  When you get a match, you end up writing formatting scripts using yet another DSL, using constructs like `\1`.

# FMT
The answer to the above JavaScript conundrum is to *not write JavaScript* by hand.

Use Ohm to create a DSL for generating JavaScript for you.

Worry only about 80% of the use-cases.

Don't even try to cover 100% of all possible use-cases ("here be dragons" (https://en.wikipedia.org/wiki/Here_be_dragons)).

Deal with the low-hanging fruit, leave the other 20% to raw JavaScript code.

An attempt at this strategy is what I call *fmt*.  An example of using *fmt* is [Ghost Stars index.html](https://github.com/guitarvydas/ghost_stars/blob/main/index.html) found in [Ghost Stars repo](https://github.com/guitarvydas/ghost_stars).  I would be glad to expand on *fmt* elsewhere.


# How?  The Trick To Making Syntax Cheap...

## Orthogonal Syntax
The key concept is to separate `operations` (control flow) away from `operands` (data).

Cordy's Orthogonal Code Generator thesis shows how to build orthogonal syntax for assembler.

Now, we can build orthogonal syntax for just about any phrase(s) using Ohm-JS.

## Syntax Pipelines
The second trick is to use *divide and conquer* on steroids.

Create a pipeline of little-compilers, each with its own, unique DSL.

Write little-compilers that compile only a bit of the work, then hand-off the results to the next little-compiler in the pipeline.

This isn't the same as building a bunch of little-compilers that work on the *same* input.  The idea is to build unique little-DSLs and plug them together into a pipeline.  

Each little-compiler gets rid of one (1) problem, then punts the rest of the work along to the rest of the pipeline.

![](images/syntax pipeline.png)

For example, the first stage of the pipeline might be a tokenizer.  It picks off various keywords and marks them in some special way, e.g. by inserting a character at the front (say "`:`"), or replacing each keyword with a single-character Unicode character (we could use Greek symbols, but Unicode offers more possibilities).  The tokenizer leaves the rest of the text alone, it deals only with pattern-matching keywords.

This reduces the complexity of the subsequent parts in the pipeline. The rest of the parts in the pipeline don't have to worry about keywords - less code in each of those parts (less bloatware, less complexity, easier-to-understand and to reason-about).

The next pass might check to see that the text (and tokens) form valid phrases.

The next-next pass might recognize definitions and create a table of definitions (e.g. a table of functions and variables), or, it might mark-up defined names in some way, or, maybe it can create output in some little-DSL that includes all of the definitions at the front of the text, e.g. a "declaration section".

The next-next-next pass might check to see that all names have been defined in the "declaration section".  If it finds any undefined names, it stops the pipeline and declares an error (in fact, it would pile up as many such error messages as possible, before quitting).

The next-next-next-next pass might worry about *where* things will reside in memory (static, auto, parameter, function, temp, etc).

The next-next-next-next-next pass might worry about how to transpile the code to some existing language (say, C++).  This next-next-next-next-next pass doesn't need to worry about tokens, name-uses (definitions vs. checking-for-defined names), allocation (*where*), etc.  If the code gets this far into the pipeline, it is known to have passed all of the earlier checks.  The task of transpiling is hard-enough on its own without conflating error checks and allocation with it.  The programmer writing the code for this next-next-next-next-next pass doesn't need to worry about anything else, except how to transpile the code.

# Face Palm

So, if this is such a good idea, why haven't we been using it?

Syntax has traditionally been considered to be expensive.

If you think that syntax is not cheap, you think about solving the problem in some other way.

If you think - know, believe deep-down - that syntax is cheap, you open up new avenues for different kinds of solutions.
