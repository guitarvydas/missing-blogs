# 2022-07-03-Staged Transpilation
Transpile NL (New Language) to JavaScript.

[Example](https://github.com/guitarvydas/nl/blob/main/index5.html)

I use 4 steps in the process of transpiling a language snippet into JavaScript. Some of the steps could be optimized away, but, thinking about solving the problem as a series of small steps helped me write this quickly ("divide and conquer" on steroids).

Of note is the final step which peephole optimizes the JavaScript converting
```
cache.at (num)
```
to
```
cache[num]
```
Peepholing is a technique used by GCC at the assembler level (see below).  Ohm-JS allows me to apply the peephole technique to text languages (in this example, Javascript).

# Source
The original source code for (part) of this new language comes from [Kinect3000 on the OhmLang discord](https://discord.com/channels/779282197152661525/779286160597319680/992714506033692692).
```
CONST cache TO ARR ZERO SEP ONE END
FN fibonacci num DO
  IF cache OF length GT num DO
    RETURN cache OF at CALL num END
  END
  RETURN fibonacci CALL num SUB ONE END ADD fibonacci CALL sum SUB TWO END
END
```
# Step 1
I claim that it is slightly easier to use Ohm-JS to parse a modified version of the above source code.  At this point, I don't care about human-readability, I just want machine-readability, esp. Ohm-JS readability.  It is *slightly* easier to write a grammar in Ohm-JS where the keywords are marked in some way to keep them separated from other identifiers. I happen to use ":", but I could have used Unicode characters (Ohm-JS supports Unicode characters).
```
:const cache :to :arr 0 , 1 :end
:fn fibonacci num :do
  :if cache :of length > num :do
    :return cache :of at :call num :end
  :end
  :return fibonacci :call num :sub 1 :end :add fibonacci :call sum :sub 2 :end
:end
```
For convenience, I've mapped "SEP" to "," and "GT" to ">".
# Step 2
My next step is to build an identity parser using Ohm-JS for the machine-readable code in Step 1.

An identity parser simply outputs what it sees at its input, modulo whitespace.

The point of building an identity parser is to get the parsing mechanics correct.

Once I get the identity parser to work, I can hack on it to output more interesting code.
```
:const cache :to :arr 0,1 :end:fn fibonacci num :do :if cache :of length > num :do :return cache :of at :call num :end :end:return fibonacci :call num :sub 1 :end :add fibonacci :call sum :sub 2 :end :end
```

Note that much of the whitespace has been disappeared.  This doesn't matter, since the result is parsable by Ohm-JS. I don't care if the result is not very human-readable, I am only concerned that Ohm-JS can grok it.
# Step 3
Now, I take the code from Step 2 and hack on it, to produce raw, unoptimized, JavaScript.
```

const cache = [0,1] ;
function fibonacci (num) {
if (cache.length  >  num) {
return cache.at (num);
}
return fibonacci (num - 1) + fibonacci (sum - 2);
}
```

Again, human-readability doesn't matter. The extra spaces will be ignored by Ohm-JS Syntactic rules.  Indentation doesn't matter.

Note that the array access looks like a function call
```
...
return cache.at (num);
...
```

That's OK, I'm going to peephole optimize this function call into a JavaScript array accessor in Step 4.
# Step 4
Tada.

The array access now looks like a JavaScript array access:
```
...
return cache[num] ;
...
```
# Code (github)
[Step 1](https://github.com/guitarvydas/nl/blob/main/index.html).  Load this into a browser (I used Chrome) and press the "Test" button.
[Step 2](https://github.com/guitarvydas/nl/blob/main/index2.html)
[Step 3](https://github.com/guitarvydas/nl/blob/main/index3.html)
[Step 4](https://github.com/guitarvydas/nl/blob/main/index4.html)
[Final](https://github.com/guitarvydas/nl/blob/main/index5.html)

Video - TBD...

# Discussion
## Peephole Optimization
The technique of peephole optimizing appeared in a paper by Fraser/Davidson (see https://guitarvydas.github.io/2021/12/15/References.html) and was used in GCC (at least the original version, I haven't looked lately).

The technique is generalized and normalized in Cordy's thesis - Orthogonal Code Generator (see references, above).
## Development Time
This took me part of Friday, all of Saturday, and, a couple of hours on Sunday morning to build, including the .html files.

I am already familiar with Ohm-JS.

I am already familiar with parsing and language-building (compilers, interpreters).

I am familiar with Lisp and Common Lisp. The Lisp experience, esp. with Lisp macros, invites me to think about language-building differently.  I expect to cheat, I expect to build a language in minutes instead of years.
## Ohm Editor
I used the Ohm Editor heavily in building the various grammars.

Ohm Editor is like a REPL-based IDE for grammar development.

I've used YACC, S/SL, TXL and various PEG libraries.  

Ohm-JS plus Ohm-Editor are the best tools I've encountered for the domain of language-designing.
## FMT Shorthand For Ohm Semantics
Ohm-JS provides a DSL syntax for writing grammars, but, expects the programmer to write re-formatting code in JavaScript. This kind of code is called "semantics" in the Ohm-JS documentation.

I built a shorthand (an SCN, see below) for writing re-formatting code using Ohm-JS. I call it FMT (I used to call this "glue", and, before that "grasem").  99% of my use-cases for Ohm-JS involve pure text-editing/reformatting/batch-editing, so FMT is designed to do only two things[^1]:
1. pattern match the input text
2. rearrange matches and produce output text.

[^1]: Ohm-JS can do much more than this, but, in most cases I don't need all of this power.

In other words, I use Ohm-JS to write Ohm-JS.

I've created very simplistic HTML pages that show this process and the generated JavaScript code. (Index*.html, as above).

The syntax I've chosen for FMT leaves much to be desired and could be improved.  As such, though, the syntax is workable, and machine-readable and helps me avoid writing raw JavaScript.  The syntax is described in [the Glue Format section](https://github.com/guitarvydas/prep), and, previously in [Glue Tool](https://guitarvydas.github.io/assets/2021-04-11-Glue%20Tool/index.html). 
## ApplySyntactic
Ohm-JS is a DSL for building pattern matchers (AKA "parsers").

One of the design goals of Ohm-JS is to remove noise and make-work when designing grammars and pattern-matchers.

Ohm splits the grammar design into 2 categories:
1. Lexical rules
2. Syntactic rules.

Lexical rules are like pure PEG, where the programmer needs to worry about whitespace.

Syntactic rules remove whitespace baubles from the grammar, leaving only the pure essence of grammars.

On top of this, Ohm-JS added the "applySyntactic<...>" command to its DSL.

The "applySyntactic<...>" command makes it possible to conveniently write macros for any text-based language.  Previously, real macros were only available in Common Lisp, Scheme and Racket (and other more-obscure tools, like M4).

The mix of Ohm-JS's "applySyntactic<...>" and PEG's balanced-bracket-matching makes it possible to solve pattern-matching (AKA compiler) problems differently ("better") than what is considered state-of-the-art.

IMO, it should be possible to knock-off *multiple* mini-DSLs for each project.  I call mini-DSLs "SCN"s, for Solution Centric Notation.  Building an SCN should take hours, not days/months/years.
## Future
I have been using technical diagrams instead of text as syntax for projects.  I expect to document this process (transpiling diagrams to code, I call it DaS).
