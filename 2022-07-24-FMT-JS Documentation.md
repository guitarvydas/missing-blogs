# 2022-07-24-FMT-JS Documentation# Fmt-JS
*Fmt* is a mini-language[^scn] for writing transpilers using [Ohm-JS](https://ohmjs.org/).

It should be possible to cobble together new syntax skins in hours, rather than in days, months, years.

This project contains two apps:
- Workbench for transpiling *fmt* specifications into Javascript, suitable for inclusion in an Ohm-JS application
- A sample game scripting language that is transpiled into JSON (based on a gamejam entry called GhostStars) including pattern-matching and *fmt* specifications for the transpiler.[^jam0003]

[^jam0003]: The game scripting transpiler wasn't finished in time for inclusion in the langjam0003 entry.  The game scripting language transpiler was written the next day after the close of langjam0003.

## Background

A full transpiler application written with Ohm-JS consists of 
1. source code in some newly-invented mini-language
2. a pattern-matching specification (formally called a *grammar*)
3. a rewriting specification.

Ohm-JS performs step (2) while *fmt* (this project) transpiles step 3 into a form suitable for use in building a full transpiler using Ohm-JS.

Ohm-JS allows a programmer to write a pattern-matching specification.  Kind of like REGEX, only better.

After performing a pattern-match, a programmer needs to perform actions based on the matches.

Ohm-JS calls these actions *semantics* and punts to a set of Javascript functions, which the programmer must write. 
Ohm-JS allows programmers to write several sets of actions for each pattern-matching specification.  Each set of actions is called an *operation*.  Operations can be "hung off" of a parse tree like baubles on a Christmas tree.  The pattern-match (the grammar) can be re-purposed by hanging different *operations* on it (then tree-walking the tree and corresponding operations).

Analogy: when using REGEX, one writes actions in REGEX's DSL.  In Ohm-JS, programmers get to use the full power of Javascript to write action code.

[^scn]: I call this kind of mini-language an "SCN" for Solution-Centric Notation.  Some people would call this a DSL, but, I prefer a more specific term.

## 80% Use-Case
In many cases programmers need only to convert input text to output text and don't need the full power of Javascript (or even, REGEX).

Fmt-JS is designed to address this use-case with a much-reduced syntax.

Fmt-JS makes it easier to write *transpilers*.

# Fmt-JS Workbench
The fmt-js workbench is a simple HTML page that is loaded into the browser. The workbench is `fmt-js.html`.

Programmers type in lines of fmt-js text, click a button and generate Javascript code that can be used in an Ohm-JS project.

In the simplest case, programmers type one line of fmt-js text and generate one Javascript function from it.

In more-complicated cases, programmers paste multi-line *fmt* specifications into a window and generate many Javascript functions wrapped in a Javascript *namespace*, suitable for cutting-and-pasting into an Ohm-JS project.

!![transpile-Workbench.png](transpile-Workbench.png)

# Transpile Function
In addition to the workbench, I have included a program called `transpile.js` which can be used to create whole transpilers.

!![transpile.png](transpile.png)

(See below for documentation of the parameters to the *transpile* function).)

# Usage
## Workbench Fmt-JS
- Load `fmt-js.html` into a browser
- Click on one of 4 "Use ..." buttons to load *fmt* source code into the browser top window.
- Click on the "Generate Javascript from FMT specification" button to generate code in the bottom window.

## Transpile
- Load `ghoststars/tester.html` into a browser
- Click on the "Test Game Language (Ghost Stars)" button to load the game source code into the top window and to generate JSON in the bottom window.
- Alternately, click on the "Test Small" button to load the source code for a small example into the top window and to generate an output string in the bottom window.

(In both cases, the full source code for the specifications can be found in `ghoststars/tester.html`)

It should be possible to use the *transpile* function in any Javascript project.  The function must be supplied with 4 parameters:
1. The source code (for the mini-language to-be-transpiled)
2. The name of the grammar (for example, "Test" in this case).
3. The grammar, itself, as a string (see Ohm-JS documentation for the appropriate syntax, links supplied below)
4. The *fmt* specification as a string (see below for the appropriate syntax).

# Pattern Matching Specification
See the [ohm-js documentation](https://ohmjs.org/docs/intro)

Use the [ohm-js editor](https://ohmjs.org/editor/) to design pattern matching specifications and test them out against text.

# FMT Specification
```
Test {
//
Rule1 [x] = ‛«x»’
Rule2 [x+] = ‛«x»’
Rule3 [a+ b* c? d] = ‛«a»«b»«c»«d»’
//
}
```
A *fmt* specification consists of a one or more rules and some plumbing (a wrapper, an `=`,  and, comments).

Each rule has 3 parts:
1. Name of the rule
2. Parameter List for the rule.
3. Rewrite string.

## 1. Rule Name
A rule name consists of a letter followed by zero or more letters/digits/underscores.

Case is significant.  For example the name "A" is not the same name as "a".

This naming convention is based on names found in most modern programming languages.

## 2. Rule Parameter List
The parameters to a rule are enclosed in square brackets `[...]`.

Parameters are names separated by spaces (not commas).

Parameter names can, optionally be suffixed by the grammar operators `+`/`*`/`?` (called Kleene Plus, Kleene Star and Optional, respectively).

The parameters can be named anything, but must match in number and operation *exactly* with the corresponding grammar rules.

The *fmt* transpiler walks the tree of matches after pattern matching has succeeded.

The *fmt* transpiler automatically handles tree-walking of iterative matches caused by he use of grammar operators.

## 3. Rule Rewrite String
A rule rewrite string
- is prefixed by `‛`
- is suffixed by `’`
- contains verbatim ASCII and Unicode characters (and emojis) (except for the two bracket characters used for evaluated variables, below)
- contains evaluated variables
	- an evaluated variable is a name, enclosed in Unicode brackets `«` and `»`
### Example Rule
Pattern matching specification (grammar):
```
...
name = nameFirst nameRest*
nameFirst = letter
nameRest = "_" | digit | nameFirst
...
```
The above grammar specifies *name* patterns that begin with a letter and have zero or more letters/digits/underscores.

Fmt specification:
```
...
name [nameFirst nameRest*] = ‛«nameFirst»«nameRest»’
nameFirst [letter] = ‛«letter»’
nameRest [c] = ‛«c»’
...
```
The above *fmt* specification has one rule for every rule in the preceding grammar (name/nameFirst/nameRest).  

This rule specifies that a name is rewritten to contain the first letter followed by the rest of the characters (if any).  The *fmt* engine handles the case where there are no following characters.

Each character becomes a parameter to its corresponding *fmt* rule and the parameter is evaluated to give the actual character that was matched.

Note that the grammar rule *nameRest* specifies underscors or digits or nameFirst (letter) characters while the *nameRest* *fmt* rule does not need to specify further detail.  The pattern matcher sends the matched character - whatever it is - to the parameter *c* of the *nameRest* rule.  The *nameRest* *fmt* rule doesn't care which character was matched and simply evaluates the parameter and sticks the matched character - whatever it is - into the resulting rewrite string.
## Comments
Comments begin with `//` and end at the end of a line (`\n`).

## Wrapper
Every *fmt* specification must be preceded by the grammar name (matching the corresponding grammar) and be enclosed in brace brackets`{ ... }`
## =
An `=` separates the right-hand side of a rule from the left-hand side.  

The left-hand side contains the rule name and parameters.

The right-hand side contains one rewrite string.

# Combining Code To Make An Ohm-JS Project
A sample *boilerplate.html* browser page is provided that contains
- s - the source code string
- gn - the grammar name string
- g - the grammar string
- f - the *fmt* specification string
- <script> elements that include 3 program files (the Ohm-JS program, the fmt-js program and the transpile program)
	- ` <script src="https://unpkg.com/ohm-js@16/dist/ohm.min.js"></script>`
	- `<script src="fmt-js.js"></script>`
	- `<script src="transpile.js"></script>`

# Examples
## Small Test
Fmt Rule
```
Test {
//
Rule1 [x] = ‛«x»’
//
}
```
This *fmt* rule is expected to be matched up with a pattern-matching rule (with name `Rule1`) that contains exactly one matching operation.

This rule simply outputs the value of its parameter, with no change.

The workbench creates Javascript code for the above rule as a single Javascript function called `Rule1` with a single Javascript parameter `(_x)`.

The grammar name, wrapper and comments are discarded (in the current version of the workbench).

The rewrite string `‛«x»’` is converted into a Javascript *template* string containing a reference to the variable `x`.

If a match is made, the Ohm-JS pattern-matching engine binds the match (an internal data structure, a CST) to the parameter `_x` before calling `Rule1`.

The code generated by *fmt* causes the parameter `_x` to be tree-walked and the result (always a string) to be written into a variable named `x`.

The Ohm-JS pattern-matching engine builds an internal data structure - a CST (Concrete Syntax Tree) if the match is successful.  The *fmt* code then "walks" the CST and executes *fmt* rules that are appropriate to each node (rule) in the CST.  In this way, the Ohm-JS rules specify *what* to match and the *fmt* rules specify *how to process* each sub-match.

*Fmt* rules always create strings and bubble them back up to the topmost rule.  The *fmt* strings are recursively glued together to form a single string which is the result of the whole process. 


## Small Test2
```
Test {
//
Rule1 [x] = ‛«x»’
Rule2 [x+] = ‛«x»’
//
}
```

This *fmt* specification is almost the same as that in 'Small Test', except that `Rule2` contains a `+` operator, signifying one-or-more matches.

The *fmt* engine unwinds the multiple-match (by tree-walking it) and creates a single string which is substituted in place of `«x»`.  Note that the programmer does not specify *how* to unwind the multiple-match.  The presence of the `+` operator causes *fmt* to generate different code for the `x` parameter.  The *fmt* transpiler can do this because all rules are normalized to produce single strings.  At this moment, processing the matches in any other way, than producing a string, requires writing code in Javascript without using *fmt*.

## Small Test3
```
Test {
//
Rule1 [x] = ‛«x»’
Rule2 [x+] = ‛«x»’
Rule3 [a+ b* c? d] = ‛«a»«b»«c»«d»’
//
}
```
This example shows multiple parameters to a rule that cause *fmt* to generate various kinds of tree-walking code.  

`Rule3` produces a single string that simply concatenates the string values of its 4 parameters.

## Big Test 
The larger test is not duplicated here, but, can be seen in the variable `bigsrc` in the file `fmt-js.html`.

The larger test contains many *fmt* rules, all grouped together in the wrapper with name `Test`.

The *fmt* workbench generates a Javascript function for each rule.  Each single *fmt* rule generates a multi-line function.

The set of generated functions are grouped together in Javascript *namespace* which is suitable for inclusion in an Ohm-JS application.

## Ghost Stars
The file `ghoststars/tester.html` goes beyond a simple workbench code generator and supplies 3 strings - the game script (`ghostStarsSrc`), the grammar specification for matching phrases in the game script (`ghostStarsGrammar`), and, the *fmt* specification which converts the game strict into JSON (`jsonfmt`).

This example uses the *transpile ()* function which runs Ohm-JS and the code generated by *fmt* to produce a whole transpiler (from game script to JSON).

The code is not duplicated here, but, can be seen in `ghoststars/tester.html`.

A smaller example is, also, included.  The smaller example matches two characters (a sequence of "a" followed by "b") and reverses their order, producing the string "ba".

## Other Examples
## Arithmetic
The canonical example that ships with Ohm-JS is the grammar for an arithmetic mini-language.

I used the arithmetic grammar in [Ohm-Arithmetic](https://guitarvydas.github.io/2021/05/11/Ohm-Arithmetic.html).   Note that a previous version of *fmt* called *glue* (with a slightly different syntax, see below) is used.

## ABC
A previous incantation of *fmt* was called *glue* and used a slightly different syntax (`@` prefix instead of `+`/`*`/`?` suffixes, comments not supported, no wrapper syntax).

A very simplistic mini-language was invented and called `ABC`.

Examples of transpiling, compiling and interpreting of `ABC` using the older *glue* technology are:
[Small Example of Interpreting and Compiling](https://guitarvydas.github.io/2021/09/15/Small-Example-of-Interpreting-and-Compiling.html)
[ABC-glue](https://guitarvydas.github.io/2021/09/15/ABC-Glue.html)

## Ohm-Editor
The Ohm-editor is a very useful tool for designing and debugging grammars.  I would use this tool even if I were not using Ohm-JS in the end, and using some other PEG library.

[Ohm Editor](https://guitarvydas.github.io/2021/05/09/Ohm-Editor.html)

## Ohm In Small Steps
One of my first applications with Ohm-JS was to write a Scheme-to-Javascript transpiler (for a specific program).

I tried to document my progress ih [Ohm In Small Steps](https://guitarvydas.github.io/2020/12/09/OhmInSmallSteps.html)

## PREP
[Prep Tool](https://guitarvydas.github.io/2022/01/20/PREP-Tool.html)

## Other Ohm-Related Essays
[Ohm-JS](https://guitarvydas.github.io/2021/08/30/Ohm-JS.html) (includes a cheat sheet and WASM transpiler example).

### Further Reading
[Table of Contents](https://guitarvydas.github.io/2021/12/10/Table-of-Contents-Dec-01-2021.html)

Search for "PEG", "transpilers", "DaS", "Parsing Diagrams", etc.


## Future Extensions
- pre (down) code
	- There are a few use-cases where one wants to set up an environment before starting the recursive tree-walk of the CST.  The previous version of *fmt*, called *glue*, used `{{ ... }}` syntax to allow any Javascipt code to be executed before the tree-walk was started.  This feature required detailed knowledge of how parameters were named and evaluated in the *glue* transpiler.  I haven't yet lifted this feature into *fmt* and have not yet given it a non-Javascript syntax.
- js objects
	- Ohm-JS can create and return arbitrary Javascript data structures, not just strings, especially JS objects.  A more general version of *fmt* or another completely different tool might capitalize on this ability built into Ohm-JS.
- Ohm-JS operation parameters
	- Ohm-JS allows one to create *operations* that have parameters.  Currently, *fmt* doesn't use any operation parameters.
	- Maybe the lack of generalization makes *fmt* "simpler" (simple ≡ lack of nuance) and contributes to its usability?
- more error checking
	- check that *fmt* rule parameters match exactly with a given grammar
	- check for typos and undeclared variables in the rewrite string eval operations
# Cheating
Building languages and compilers from scratch is difficult.

Cheat as much as possible.

Transpile source from new languages to existing languages/compilers. 

Let existing compilers do the hard work.

# Appendix Source Code
[Latest source code](https://github.com/guitarvydas/fmt-js) including Game Language sample.

[Langjam0003 Entry](https://github.com/guitarvydas/jam0003/tree/main/fmt-js)
