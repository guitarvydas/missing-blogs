# 2022-08-26-Creativity vs Engineering
> Ask FoC: What are your favorite Lisps? Which ones are good for typical engineering work vs which are good for thinking and creativity?

https://futureofcoding.slack.com/archives/C5T9GPWFL/p1661481349386469

# Creativity
Creativity needs a total of 2 types:
1. Things
2. Lists of Things

and, a technique: *iteration*:
3. a Big Red Button that can be used to wipe out all code written up to that point and to start all over again.

There are only 2 Lisps (afaict) that fit that bill:
1. McCarthy's Lisp (the original FP)
2. Sector Lisp

AFAICT Lisp direction was veered into Production Engineering and Waterfall Design.

Most modern languages expect programmers to commit (prematurely) to classifcations of Things, thereby inhibiting change in the future (changing the classifications becomes harder as the Design grows).  

Ideally one should be able to work forward for several years, then hit the Big Red Button and start all over again with a fresh outlook on the Design.  If the Design, up to that point, contains hard-won optimizations, then there is a reluctance to use the Big Red Button.  Optimizations, as we know them today, are applicable only to a specific layout of code - changing the code invalidates all optimizations up to that point.

Things like:
- rapid prototyping
- restarts
- dynamic classes, prototypes
- type inferencing
- etc., etc.

were being invented, but, because they are harder to formalize, the ideas were discarded in lieue of formalizable Production Engineering techniques.

Clockwork synchronization inhibits creativity and promotes Waterfall thinking.

# Engineering Redux

- Engineering
- Production Engineering
- Test Engineering
- Maintenance Engineering

Engineering = thinking deeply about details to implement something.

In computing, implemention == automation.

Current languages, like Rust, Python, etc. target Production Engineering and Waterfall Design (lack of iteration) and premature optimization.

Ideal language for Creativity:
- accomodate "changing your mind" and revamping everything up to that point
- modern languages inhibit "changing your mind" and insist on premature-detailing, which tends to paint you into corners

Other
## Actualization

- Agile
	- Agile is an attempt to gather requirements in an iterative manner using a *very slow* REPL (called "sprints")
- CI/CD
	- Maintenance Engineering

side: A list of very-useful-looking Atoms is ASON, invented by Amiga's inventor Carl Sassenrath (who, also invented REBOL.  REBOL inspired the invention of JSON).  altscript.

# Lisp - Why?

Lisp is a tree-oriented assembler.

What we usually think of as "assembler" is a line-oriented assembler.

Assembler is a high-level-language, if you look at the underlying transistor networks that it elides.  (Other wording: Assembler is an API for dealing with complicated lumps of electronics.  API == set of restrictions, a "simplified" notation)

Some people *love* working in assembler (line or tree oriented), while others hate it and want to drape syntax over the assembler.

# Layered Creativity
Towers of notations.

E.g. Feyman diagrams instead of mathematical equations.

The diagrams did not supercede the math, but only elided the math, allowing Feynman to think deeply about a slice of the problem.


Accused of *reusing* ideas from other domains.  True.
- If you want to know about scalability, look at Business Organization
- whiteboards