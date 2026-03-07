# 2022-06-08-Compilation vs FEXPRs`EXPR`s eval args.

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
