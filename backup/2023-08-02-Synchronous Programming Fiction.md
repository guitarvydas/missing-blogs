# 2023-08-02-Synchronous Programming FictionCurrent software methodologies make for "easier" DX (Developer eXperience), but, ignore UX (User eXperience).  

For example, the fiction of *synchronous* software programming languages is only possible due to the use of elaborate, bloated preemptive operating systems.

What is the co$t of that fiction?  

Your users must suffer to allow you to use this "solution".  Your users are beholden to uSoft and Apple and must pay for an expensive computer or an expensive phone before being able to use your software that makes it convenient for *YOU* to program the devices.  

Ideally, customers should have to pay only a few $s for a console, then buy and plug cheapo cartridges into the console.  Instead, they have to buy full-blown computers with too many options (unwanted complication) and suffer with buggy software and frequent updates.

I strongly believe that the emphasis should be on UX, not DX (Developer eXperience).  

How many Developers are there?  How many Uses are there?  What should we be focusing on, primarily?  

Yes, improving DX helps reduce final cost, but a 50-year nerd-out aimed at improving only DX - UX be damned - is the wrong emphasis.  The DX-only mindset has given us a bunch of tools that encourage us to deliver buggy software, e.g. CI/CD.  Decreasing quality is the wrong emphasis, IMO.

Every minute spent on development of further improvements to static type checking should be quantified in terms of cost saving for Users, not Developers.

Companies have reduced their internal costs by eliminating Q/A departments, but, they now rely on getting free Q/A from customers.  

Oy Vey.

## Hidden Costs

The fiction of synchronous programming languages has a deleterious effect on programming.  The effect is subtle, but increases bugginess and makes DX harder.

Libraries are not pluggable Components.  Programmers are conditioned to think that libraries are pluggable, but end up wasting time testing and debugging code that relies on libraries and worrying about version hell and packaging issues. 

https://guitarvydas.github.io/2020/12/25/The-ALGOL-Bottleneck.html

### Aside: a simple solution to version hell 
A simple solution to version hell is to simply clone what you need.  But, the effects of
- manual, laborious application of DRY (Don't Repeat Yourself)
- the misbelief that Libraries are pluggable components
discourage the use of this simple solution.

## Synchronous Programming is a Good Idea, But...

Synchronous programming is a Pattern.

It works well when it applies to the problem-at-hand.

The Synchronous Programming Pattern causes epicycles and bloatware and time-wasting when the problem-at-hand pushes this Pattern out of its sweet spot.

One should use the Synchronous Programming Pattern for bits of a solution, but use other Patterns for other bits of a solution.  Then, bundle all of the bits together to create the solution.

## The One-Size-Fits-All Fiction
GPLs (General Purpose Programming Languages) are necessarily watered-down, wishy-washy solutions that try to address too many problems at once.

A *textual programming language* is simply an IDE for *programming*.  That style of IDE was invented in the 1950s.  We can have better IDEs in 2023.

For example, if you need to perform an exhaustive search against a factbase, then use a notation (SCN, Programming Language, DSL) suited for the purpose.  But, if you need to format output text, use a different notation for that purpose.  Let the 2023s IDE tie your notations together into a program that does what you want.  Crafting exhaustive search using GPL *if-then-else* and variables is but a cave-man approach. PROLOG, PEG, backtracking, miniKanren, core.logic, etc. express exhaustive search more easily than *if-then-else*.

In 1950, electronic machine (aka "computer") hardware was very limited and had to strain to simply manipulate small, fixed-size bitmaps (aka "characters")[^moad].  But, in 2023, electronic machines can easily handle such tasks and can add new possibilities, like windows, reactivity, SVG, image handling, speech-to-text, etc. to the mix.  

[^moad]: We can conveniently ignore the fact that vector graphics was demonstrated in the early "Mother of All Demos" by Englebart. https://www.youtube.com/watch?v=yJDv-zdhzMY