# 2022-06-10-The Pattern Matching Paradigm> [!important] PEG is like REGEX, only better.  

> [!important] Ohm-JS is better than PEG.

With Ohm-JS you can sprinkle pattern-matching into your apps like candy.  With Language-Theoretic Parsers, you can't.  You Just Don't Bother(tm) to think that way, because pattern-matching becomes a mega-project.

> [!important]- Pattern-matching is a paradigm
> - e.g. like GC, say.  
> - Compilers need to use the pattern-matching paradigm.  Pattern-matching is called "parsing", when used by a compiler.  
> - You can, also, use the pattern-matching paradigm in non-compiler apps.

> [!EXAMPLE]- 5-line grammar that slurps C code.
> I am allowed to think that way with Ohm-JS, but not with LR(k). 
> https://github.com/guitarvydas/cparse/blob/main/cparse.ohm

> [!EXAMPLE]- Prolog.scm -> prolog.js
> 
[aside: I, also, built a Scheme->JS converter to transpile Nils Holm's prolog.scm to prolog.js.  This was one of the first things I built in Ohm-JS, so not exactly rocket science.  If I can do it, anyone can do it...]
> https://computingsimplicity.neocities.org/blogs/OhmInSmallSteps.pdf
> I would write this differently today, given what I've learned.  I would probably use *prep*.

https://publish.obsidian.md/programmingsimplicity/2022-06-10-The+Pattern+Matching+Paradigm