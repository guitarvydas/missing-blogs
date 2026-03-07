# 2022-11-27-Transpilation Stacks
Lisp, S/SL, PROLOG, UNIX shell all come down to the same idea: separate technical needs from user needs, build an engine, give the user "Declarative" syntax / access to the engine.  Write code that writes code.  Write code that optimizes the Declarative syntax and accesses the engine in various ways.

This used to difficult to do.  You were either stuck with Lisp syntax (non-syntax) or S/SL pre-processing or spending years to write the new Python 4 using stock compiler tools like YACC/Bison/ANTLR/etc.

Now, with PEG, it is possible to knock off syntaxes quickly.

So, the approach might be: 
1. write fake code for both use-cases
2.  write an engine that satisfies both use-cases
3. write syntax skins that look like they were specifically designed for each use-case.

In doing (1), don't restrict yourself to using only text, use a white-board.  Imagine that a CEO has white-boarded his vision, or, better yet, get a real CEO to white-board his vision for you.  Then, write code that transpiles the white-boarded image (probably some sketches of boxes and lines and text) in layers until you get a "script" that invokes the Engine.

I was going to say that, with experience, you go from actually writing fake code in (1) and being able to "do it in your head", but, I just realized that I still do 1. explicitly (using draw.io or small snippets of stuff in Emacs).

As I write this, I realize that this is what I've always done.  In consulting, I've assumed that my Customer knows the target Domain better than I do, so I don't even bother to try to understand their Domain, I just create a stack of scripts that transform the Customer's chicken-scratches to executable Code.  In stages.  I guess that I've built up some kind of experience that says "to write code that transpiles B->C, I need to transpile from A->B first".  Turtles all the way down, transpilers that transpile to meta-syntax for the next transpiler.  My first SateChart compiler was 8 passes (but I understood each pass well enough to implement each pass ; each pass was simple-enough for even me to write a transpiler for using stone-age tools).

That attitude is what Functional Programming is all about.  "No Mutation" isn't just a rule pulled out of thin air.  It's a way of life if you want to transpile text.  But, "Mutation" is a must in computers.  How do you get both?  Start with a syntax that has no mutation, then transpile.  Repeat until you get to the Engine (which has Mutation).

Until PEG, we only had Microsoft-Word (Find and Replace) and REGEX level transpilation at our fingertips - only a line at a time, which ain't good enough in general.  With PEG, you can transpile "structured / nested text".

For example
```
if (A) {
  B
} else {
  C
} 
```
Can you write a transpiler that changes this to:
```
if (D) {
  E
} else {
  F
} 
```
?

Not with REGEX nor Microsoft Word Find and Replace.

You want a "meta-REGEX" that lets you match
```
if (P1) {
  P2
} else {
  P3
}
```
then replace P1, P2 and P3 with whatever you want.

Ohm-JS lets you do that.  (Actually, I learned how to do that using recursive-descent parsing, but that required a lot of attention to detail, which is elided by Ohm-JS).

Hmm, maybe that's all that I'm saying?  Syntax is cheap now.  Re-learn how to approach problems using tiny-transpilers.

0D gives you Referential Transparency. (Without all of the handcuffs that come with FP).

Maybe I need to consider writing a bunch of tutorials - a course - in transpiling A->B->...->Z?

For now, just out write/draw the fake code.  It will become apparent how to transliterate the fake code to real code (say, in Python).  You don't even need a transpiler, you can do it manually and still save heaps of time.

I'm doing that at this very moment.  I wrote a "syntax" that is 2 lines long and I'm grinding through 4 passes to transpile that syntax to something real.  The first pass transpiles to Ohm-JS, which then gets fed to the second pass (Ohm-JS) which then goes to 3 (Ohm-JS) then to 4 (Ohm-JS).  I don't have the tooling to help me do this, so, I'm writing the code from "scratch" (using Ohm-JS).  In fact, the result will be a tool that helps me do this more effectively.  That's what Glue was.  Glue has graduated in small steps to something I call Fab (Fabricator).

# To Do This Effectively

You need:
- Referential Transparency (which comes from 0D)
- A way to crank out syntaxes (which comes from Ohm-JS)