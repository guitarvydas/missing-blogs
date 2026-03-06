# 2022-05-27 Isolation 

> ... "how to have Isolated processes" ... doing that in an efficient manner ...

Quick answer:


## Operating System Based Isolation

Currently, I use sledge-hammer approaches for isolating processes.

In JavaScript, this means something like 
```
require('child_process').execSync('rm -rf "/tmp/iwantahamburger/*");
```

Other languages (like Python) probably have similar break-outs.


### Docker

Docker kills a problem that occurs in *bash* scripts
- the use of `PATH`.

`PATH` is a shell variable.

`PATH` is usually different on different machines and is settable by users (developers).

`PATH` is a *free variable* (the politically-correct way of saying *global variable*).

*Docker* wraps apps in envelopes.  

The envelopes are set up using scripts, scripted by the developer of the app.

*Docker* envelopes contain *only* the shell variables that are specified in *Docker scripts*.  All local variable values are hidden.  Shell variables, like `PATH`, are set up by the scripts and are unaffected by local, user-defined values.

In this way, the *app* sees *only* the variables as they were defined in the *Docker script* and the *app* runs "the same" on every machine that it is downloaded to.

This situation is bound to change as developers write more complicated apps.  For example, what happens if the app wants to know more about its surroundings - is this a desktop machine, or, is this a tablet, or, is this a phone?  Will the app look only at the variables defined in the *Docker script*, or, will it try to reach around the script and peek at its surrounding?  If the app looks at *only* the variables in the script, who sets those variables?  Does the app come with a user manual that tells the user how to parameterize the app?

Flat-anything has this problem.  It solves the immediate problem, but will encounter headaches in the future.  Incremental fixes are like golf tips.  They work for a while, then "stop" working when things get more interesting.

Opinion: what is needed is a way to transpile diagrams to Docker components.  That would be a start.  Later, someone will figure out how to optimize this combination. is another sledge-hammer approach.

Why do I do this?  See [2022-05-27 Isolation](#2022-05-27-isolation).

Why?


## Efficiency

I’ve been trying to get over my own biases, rooted in the mid-1900’s notion of “efficiency”.

My current thinking is to use divide-and-conquer to split programming up into 2 camps:
1. design
2. production engineering.

“Efficiency” means completely different things in each camp.

In camp (1), "efficiency" means "rapid prototyping".  Getting the bugs out of the design, getting the requirements, etc.

In camp (2), "efficiency" means squeezing blood out of the final product cost.

We have been trained to think that production engineering trumps everything else.  I currently believe that that is a bad idea. I currently believe that this idea is rooted in a fundamental misunderstanding of what Engineers do (Engineers don’t write code, Implementors write code).  

I feel that most of our programming languages are geared towards production engineering.

I feel that big-O analysis is silly in certain contexts, yet, useful in production engineering contexts.  In my experience, big-O doesn't really matter, but, what matters is only the question "is it fast enough?".  This question is, of course, answered by "it depends".  If you are a developer using a souped-up development machine costing lots of $'s, then "fast enough" means that you can waste CPU and memory resources in aid of getting-things-done.  If, on the other hand, you are a consumer who wants to use this app on a $5 rPI, the answer is different - the app shouldn't waste CPU and memory resources and should be aware of the limitations of the rPI.  Developers can use bloatware to speed up their task, like Linux (MacOS, Windows), but consumers shouldn't have to pay the costs of, also, using that same bloatware[^rpi].

[^rpi]: Yes, I feel that dropping Linux onto an rPI is blasphemous.  I feel that we do this only because we haven't figured out how to isolate software components, yet.  Isolation means (1) data isolation AND (2) control-flow isolation, not just (1) data isolation.  Operating systems gives programmers a sledge-hammer solution to (2) the control-flow isolation problem.

For years, I was obsessed with finding optimal ways to implement components.  Using *closures*, say, instead of bloatware operating systems.

Today, I am trying to force myself to overcome knee-jerk premature optimization.

You can prematurely-optimize code, but, worse, you can prematurely-optimize Design.

When you prematurely-optimize Design, you cut off consideration for other design possibilities, e.g. "thinking out of the box".

The "big wins" in optimization come, first, from Design.  Later, Production Engineering can create further wins, but, they must be tuned for specific purposes (like optimizing cost to the user).

So, currently I use this workflow:
1. Just Design It.  Using horribly inefficient code, e.g.  [Operating System Based Isolation](#operating-system-based-isolation)
2. Worry about "efficiency" when it is time for Production Engineering.

Using "one language to rule them all" seems like a good idea at first, but, it tangles considerations for "efficiency" with different considerations for "design".  The effect is to *reduce productivity*.

CEOs draw their ideas on a whiteboard and hand them over to software developers for a reason.  Whiteboard designs address only the *design* aspects of a product, unencumbered by the Production Engineering aspects.

Product ideas are often quite simple.  The minutae of making a product workable and saleable tend to be more complicated, but, these details don't affect the product idea much.  When the details do affect the original design, we create a "Change Order" and bubble the suggestions back up to the designers for re-thinking.


See also: 
## Hamburger 0D

WIP.

I tried to create the simplest example I could imagine, for demonstrating how to use Ohm-JS.

Then, I evolved the example.

Currently there are 4 steps:
1. totally ad-hoc, manual
2. ad-hoc, manual code, using 0D[^zerod] components
3. Start with a diagram, transpile it to HTML and see the results in a browser
4. wip: Create another diagram (a simple file-copy example) and convert it to command-line code.
5. future: hmm, maybe make (3) poop out a Dockerized solution.  Docker requires a huge learning-curve for me, but, maybe someone who is already familiar with Docker could do this in a few hours? ...

[^zerod]: 0D means "zero dependencies"  In my (current) view, this is a way to achieve full isolation by addressing two fronts (1) data isolation, and, (2) control flow isolation.

Through the magic of divide-and-conquer, (4) has become a sub-project that develops OPLs (Orthogonal Programming Languages) - a set of layers that transpile the example from a diagram into smaller and smaller sub-languages until culminating in "pseudo code" that can be transpiled, using Ohm-JS, into most popular programming languages.  ATM, I'm doing the easiest thing I can imagine - simply writing the transpiled code out by hand to show what happens under-the-hood.  Building a "compiler" that transpiles diagrams to text code is just a bag of details (blogged about elsewhere) and I want to avoid details to get at the meat of the solution.  ATM, I *think* that the best way to do this is to show the steps in a very manual way.  Later, I will try to describe (again) how to automate the steps (e.g. how to use Ohm-JS, and, how to transmogrify draw.io diagrams into something that Ohm-JS can grok).  If I feel particularly industrious, I will simple do this and produce a downloadable lump of code[^contribute].

[^contribute]: Contributors welcome.  If someone (regardless of experience) wants to try to write this code, I would be glad to help/advise.

github:
https://github.com/guitarvydas/hamburger
https://github.com/guitarvydas/hamburgerworkbench0d
https://github.com/guitarvydas/hamburgerworkbenchD0D
wip: checkout branch dev: https://github.com/guitarvydas/hamburgerworkbenchT0D.git

appendix:
code (messy? brainstorming?) for converting a draw.io diagram into JSON:
https://github.com/guitarvydas/das2json

appendix:
code (messy? brainstorming?) for converting a "Hello World" diagram to Python:
https://github.com/guitarvydas/das
also, converts a diagram of a script to Python

appendix:
PREP, code for the work-horse behind all of the above, boils down to one command-line program...
https://github.com/guitarvydas/prep