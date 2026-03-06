# 2023-03-01-Progress Towards Recursive TextNot finished wrapping my mind around what I mean, but…

rt has 3 kinds of things:
- trees
- leaves
- separators

The emphasis is on recursveness and divorcing all interpretations.  .rt is not a language, but a format (aka “data structure”)

For compilability … sameness, boringness, normalization, etc. is preferred.  Lisp “syntax" is very boring - 
1. tree nodes where the operator (“function”) is always first, and,
2. Atoms.  

Trees are recursive, Atoms are not recursive.

Lisp “syntax” is actually 2 things: (1) a format (“lists") and (2) an interpretation of what is in the format (e.g. functions are always first, the rest of a list consists of args to the function).  This “syntax” is fugly.  This “syntax” + interpretation is what is usually called an AST (calling it a CST would be more accurate).

Many people hate this “syntax”, but some people love it and the “power” it affords them (they are Lispers, they are compilers, built with wetware and non-AI).  In Lisp there is only 1 way to do something - it’s always a function (well, or it’s a bottom-feeding Atom).  Learning to live without syntactic sugar frees your mind to think of haughtier code - you don’t have to worry about syntax, it’s always the same.

Lisp macros are a wonderful example of the power of freeing one’s mind.  Lisp’s sameness is what made thinking of macros possible.  Later, clockwork specialists slathered precision onto the syntax and invented “hygienic macros”. "IF-THEN-ELSE" is about 1 line in Lisp, and some 10’s of lines as a hygienic macro.  Hygienic macros are bullet-proof and cover every edge-case, but, we wouldn’t have invented macros at all if we had to think - first - in hygienic macrology.

So, my thinking about .rt is to peel the format of Lisp away from Lisp and to apply that format to everything.  Some people call this “projectional editing”.  It surely looks a lot like Yunit’s tree language, but it comes from a a different emphasis.  I’m still reading up on tree language, but see similarities.  For now, .rt uses parens to delimit trees, tree language uses indentation.  .rt chooses to use runs-of-characters to be Atoms.  Tree language uses runs-of-characters to be Atoms.  .rt uses whitespace as delimiters, tree language uses newlines as delimiters.  In .rt, if an Atom contains whitespace, the Atom is bracketed by some sort of begin and end quotes - definitely not the same character, as we have in most current programming languages. (I can make Atoms recursive, they CAN contain other atoms, but, I’m not yet sure if that is a good thing).

Currently, I’m enamoured with Ceptre.  It seems to be a formal notation that encompasses states and transitions (it refuses to use those very words, though).  I am hacking together a Cepter-to-rt transpiler then expect to hack together a cepter-as-rt-to-prolog transpiler.  I’ll probably learn about new gotchas as I proceed...

My intermediate work on Ceptre-to-rt is at https://github.com/guitarvydas/ceptre/tree/dc4.  I'm trying to make the Dungeon Crawler (dc) example run as a PROLOG program.