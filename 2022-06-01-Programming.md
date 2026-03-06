# 2022-06-01-ProgrammingBasics, fundamental to the rest of this discussion is here: 
## Programming is Setting Switches

Computers are machines.  

Computers are more flexible than mechanical machines.

When we build a mechanical machine, we "program" it by designing-in mechanical doo-dads, like gears and pulleys and ... .

For example, textile looms.  My mother's loom can be set up to produce big swaths of cloth or thin belt-like sashes.  The loom is a machine.  Reprogramming the loom to do sashes instead of swaths is possible, but slow and a PITA.

When we build an electronic machine, we "program" it by designing-in eletrical doo-dads.  

We found that we could design-in ON/OFF switches. AKA "front panel".

Then, we found that we could use numerical codes instead of actual mechanical switches.  

We designed electronic switches that were activated by electrical codes instead of by physical finger-pushing.  AKA "programs" and "scripts".

Then, we found that we could change the behaviour of the machines simply by setting the switches in different configurations.

This graduated to scripting the soft switches.  

We would change the scripts, and the *scripts* would change the configurations of the switches, and the machines would change their behaviour.

We ended up using electronic machines for all kinds of things like,
- Balance sheet what-ifs (spreadsheets)
- games
- phones
- flying rockets to other planets and moons
- etc.

1.  `lack of syntax (due to mid-1950s fear of parsing)`

Parsing is "pattern matching".

For example, REGEX is a form of "pattern matching", but is more restricted than "parsing".  

REGEX was first developed for compiler techonology, then was jail-breaked out and used for other kinds of work.  Now, REGEX is included in various programming languages like JavaScript and Python, and is used for all kinds of things, not just for building compilers.

Parsing, esp. PEG (esp. Ohm-JS) was developed for compiler technology.  

I favour the idea of jail-breaking *parsing* technology and using it for other kinds of work.

Applying *divide and conquer* to the act of programming results in 2 steps (utterly obvious to most programmers):
1. grok (understand the input)
2. re-format (take the understood pieces and spit them out in a different order, for fun and profit).

"Parsing" is just a bag of tricks for doing (1).

Re-formatting (2), can be fairly basic, like using printf ().

I get bored with the repetitiveness of *printf* and use helpers like Bash scripts, JavaScript template strings, etc.

Some people invent DSLs for (2), like IBM's RPG, but, it's all really the same at the most basic level - format the output.

Some people attach big words to the act of doing (1), like "input validation", but, it's all really the same at the most basic level - read in the current state-of-the-world (or some restricted state-of-the-world, like a text file) and use whatever tricks you know to understand what's there.  Collect up the bits that you understand and pass them on to (2).

Example: using a computer for cashflow what-ifs.
1. Read keystrokes from the keyboard and give them meaning, like "arrow keys" vs. letters and numbers.  Breathe in .CSV files and pattern-match them for fields of info.
2. Present (re-format) the data in what looks like a 2D grid.  A 2D grid looks familiar to accountants and CEOs and lets them think in terms of cashflows instead of bits and switches.
3. Repeat.

Example: using a computer for gaming.
1. Read electrical inputs from the gaming controller and give them meaning, like joystick vs. button pushes.  Use a data structure to represent the saved-state of the game.  Read the state in and grok it before resuming the game.
2. Present (re-format) the game state on a 2D electrical screen.
3. Repeat.

4.  Can you elaborate?
5.  I know we've gotten a lot better at writing parsers, but was it really worth it?What do we _really_ get out of more complicated syntax?

Use a different word than "parse".  "Parse" has religious connotations.  When people hear the word "parse" they think of compilers instead of what else parsing can be used for.

I suggest using the phrase "pattern matching" instead of "parsing".

The phrase "pattern matching" is re-gaining popularity with the FP crowd.  If you want to learn what FP can teach you, jump to Ohm-Editor and play with pattern matching.  Don't stop at GO.  Don't bother to read the Dragon Book.

At one point, early on, building compilers was considered to be a difficult program.  By digging in to specific code (e.g. for building compilers), we developed more-general techniques.  Unfortunately, the general techniques have become related *only* to the specific code that they were originally devised for (compilers) instead of being recognized as being generally useful.



1.  Can you elaborate on `The premature-optimization clique expunged FEXPRs with a vengeance.` ? Specifically, what was being optimized away and how this limited exploration in newer languages?


## 2022-06-08-Compilation vs FEXPRs

`EXPR`s eval args.

`FEXPR`s don't eval args.

If you don't eval args -> you can imagine / invent macros.

For example (roughly):

```
var x = 2;
var y = 3;
def EXPR func (a, b) { return a + b }
def FEXR mac  (a, b) { return a + b }
func(x,y) --> 5
mac(x,y) --> "{return a + b}" --> "{return x + y}""
```

I don't really mean that "{return x + y}" is a string, but the real details get in the way of this overview.

## Compiling `func(x,y)`
`func(x,y)` becomes 
```
tempA <- eval (x)
tempB <- eval (y)
return tempA + tempB
```

If `x` and `y` are `consts`, then we can pre-compile them even further...

```
const x = 2;
const y = 3;
def EXPR func (a,b) { return a + b }
//func(x,y) --> 5
return 5
```
The compiler can evaluate 2+3 at compile time and hard-wire (ahem, *optimize*) it into the result.

Similarly, if only one of the args is a const, we get:
```
const x = 2;
var y = 3;
def EXPR func (a,b) { return a + b }
```
```
tempB <- eval (y)
return tempB + 2
```

## Compiling `macro(x,y)`
The compiler does not know - cannot know - what `x` and `y` are going to be at rutime, so it can't pre-compile anything and must leave the expression alone, to be evaluated at runtime.

```
var x = 2;
var y = 3;
def FEXR mac (a, b) { return a + b }
re-compile x + y and return the result
mac(x,y) --> "x + y"
```

## Macros Are Pre-Languages

A good macro language is a language that works on the representation of the program (e.g. text, whatever).

The C macro language is a very limited language.

The Lisp macro language is huge.  The fact that Programs are represented as Lists in Lisp, allows  programmers to use *any* List operation to futz with Programs.

A better-than-Lisp macro language would leave the Program as text and provide a rich set of operations that manipulate the text.

Oh, wait, we already have such languages!
1. Microsoft Word provides some operations on text (e.g. Find/Replace).
2. Mathematics notation (mathematics *notation*, not the rest of mathematical thinking) is a language for manipulating text written on clay tablets and paper.  The rules for this language are familiar-sounding - e.g. no side-effects.
3. JavaScript, Python, Haskell, etc., etc.  Any language that works on characters (bytes), can be used as a macro language.  Some languages make it easier to manipulate characters than others.
4. Ohm-JS (derived from PEG) is, IMO, a very convenient language for manipulating text.  Ohm-JS can be used to manipulate Program text, and, it can be used to manipulate non-Program text (e.g. markdown, .txt, .csv, etc.).

## Compilers Use Eval
Compilation *is* `eval()`.

The trick in compilation is to do as much `eval`ing as possible before runtime, to make the resultant program run faster at runtime.

A goal of compilation is to restrict the use of `eval` so that programmers only use `eval` when they compile their code and never have to put explicit calls to `eval` right inside of their code.

### Concerns About `Eval`
`Eval` can be abused and can cause security concerns.  Using explicit calls to `eval` in a program is like building a web server that allows any input to be compiled and to be immediately executed without further input validation.

Obviously, someone could send in a piece of text that did something malicious and the server would merrily compile and run it.

Or, someone could send in a piece of text that wasn't meant to be malicious, but was buggy and crashed the system.

# FEXPRs vs EXPRs
Function definitions used to be tagged as `expr`s or `fexpr`s.

The compiler/runtime would dutifully `eval` and `not-eval` arguments to functions.

The premature-optimization crowd deleted `fexpr`s and replaced all known uses of `fexpr`s by compilable constructs.  

The function-tagging went away, and there is, now, only one kind of function (EXPR).

All *known* uses for FEXPR behaviour has been replaced by compilable constructs.

The question arises - what about the *unknown* uses of `fexpr`s?  

Crickets.

When you follow very strict rules - you vill write functions this way and you vill only write macros this way - you don't know - can't know - what you are missing.

You haff no freedom.  Ve don't want you to think.  Ve vill do the thinking for you. You vill be assimilated.

Would programming macros have been invented if there were no `FEXPR`s?  

If "dynamic" languages didn't exist, would spreadsheets have been invented?  Smalltalk?  It is obvious how to implement these constructs in "static" languages, but, you can't characterize creativity (at least, yet).  

It's not that you can implement these concepts in static languages, it's about whether you can imagine them at all.

## FEXPRs vs EXPRs


FEXPRs let you do *anything*.  Kinda like EVAL.

If you disallow FEXPRS (and EVAL), then you can pre-compile.

Pre-compiling `func ()` -> 
	load R0, stack[0]
	load R1, stack[1]
	add R0,R1 -> R2

(note that the names "a" and "b" can be eliminated and pre-compiled away).

Pre-compiling `macro ()` ->
```
	PUSH "a + b" onto argStack
	CALL RuntimeCompiler
```

If you allow macros (and EVAL), you have to carry the compiler (interpreter) around as a library.

But, then, if I'm focused on Designing a new product, I don't care about the concerns of Production Engineers and my dev system is so hot that it easily interpret macros on-the-fly.  My Mac even has stunted macros builtin (they are called "keyboard shortcuts").

Let PEng figure out how to translate my Design into cheaper product.  If they get their fingers burned enough each time I make a revision, maybe they'll figure out how to automate the provenance from my design to their Optimized code base, instead of trying to tell me how I should write my designs (by dealing with all of the details that they are too lazy to deal with).

Note that when I say "grok", I do *not* imply grokking only characters.  Anything goes.  Spreadsheet cells, whiteboards, AI recognition of back-of-the-napkin drawings, etc., etc.  Text only when it makes sense, like "a = b + c" (it would be silly to draw that as a diagram, when we are taught this succinct notation in grade school, yet VPL potzers try this one on us all of the time).

[aside: My Apple Newton (now defunct, thanks to Jobs), was able to clean up my stylus-manually-entered drawings using only hardware-of-the-late-1900s]


1.  I'm a little disappoint Greenspun doesn't have a first 9 rules
	
	Left as an exercise to the readers?  
	
	If you know Lisp (Lisp, not Scheme, Clojure, etc), then the first rules are "so obvious" as to not bear writing down.
	
1.  Bret Victors `don't use characters / do use REPLs` : aren't REPLs still just characters? In my mind the difference between a REPL and a script / compiled program isn't the presentation of the characters but rather the interactivity

One guy showed how to input non-character data.

But, everyone thought it was magic and genuflected instead of thinking "Hey, I'll try that, the hardware is expensive right now, but will be cheap after the turn of the century".

Apple made zillions by only implementing part of that vision...  (Actually, Apple made zillions by licensing postscript for their printers, but that's another rabbit hole)

REPL means "live", "interactive".  REPL is not relegated to only be used with textual programs.

4.  `It was/is believed that there must be "one language to rule them all", and, Lisp and Smalltalk tried to cover all of the bases` <- does this matter as much if we just treat them as assembly?
5.  I don't think I understand `the brain-damage that pervasive synchrony has caused` ?
