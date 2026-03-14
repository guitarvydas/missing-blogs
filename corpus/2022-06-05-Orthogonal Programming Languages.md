# 2022-06-05-Orthogonal Programming Languages
## 2022-06-05-Orthogonal Programming Languages Background

Cordy discussed the concept of Orthogonal Code Generators for compilers in his thesis. The concept is to cleanly separate *operations* from *operands*.  This separation made it much easier to compile code sequences to other languages (in this particular case, the other languages were *assemblers* for various CPUs).

Holt wrote about Data Descriptors.  

Data descriptors describe all aspects of a piece of data, e.g.
- where the data is allocated (on the stack as a temporary, on the heap as persistent information, inside the scope of a function, etc.)
- the shape and size of the data (in the case of the original Data Descriptors, the shape of the data related to assembler-level descriptions, but, it should be possible to describe the shape of data as more abstract *types*)
- indirections to the data ...
	- is the datum a constant? 
	- is it a direct item in RAM? 
	- is it a *pointer* to a datum in RAM?
	- etc.

The  concept of normalizing all data to a single form - the Data Descriptor - (including constants) made it much easier to compile code to other languages (in this case, assemblers).

Smalltalk popularized the notion of Objects as modules containing data plus code snippets to operate on the data.  This notion provided locality-of-reference to data and its operations (called *encapsulation*), making it much easier to organize and scale programs.

The notion of independent *closures* made it possible to isolate control-flow.  Operating systems tend to implement closures as ad-hoc libraries of system-level code called *processes*.  It is thought that control-flow can be unified with data description, but, it appears that the data structures for describing control-flow are different from the data structures required for describing data.  In fact, the data structures for describing data depend on particular problems and solutions, so it is not even possible to unify data descriptions with other data descriptions.  New languages, with new suggestions on the organization of control-flows, appear periodically.

Functional programming and lambda calculus achieve certain kinds of encapsulation at the expense of other kinds of encapsulation.  Lambda calculus attempts to describe *all* data as executable functions, including conditional control-flows.  Lambda calculus produces methods for analyzing textual programs, at the expense of UX.  For example, spareadheet users would rather use spreadsheets for their programming rather than expressing their work in lambda calculus.

The advent of internet, IoT, distributed programming, blockchain, p2p, etc. is putting new pressures on the analysis of software.  Existing programming languages are based on the notion of tight coupling, e.g. CALL/RETURN, e.g. the fact that synchronization is hard-wired into the lowest-levels of code, etc. 
 Distributed programming, though, requires solutions based on looser coupling and asynchronous operation of computers.  We witness this pressure as problems in current abstractions, such as the invention of callbacks.

With the advent of PEG and, now, Ohm-JS, it is possible to apply the above principles to the design of programming languages.

Syntax is cheap.  

Syntax is unnecessary in the same way that variable names are unnecessary in functional programming (esp. de Bruijn indexing).

Syntax is interchangeable, but, paradigms remain constant.

In the past, it was difficult to build new syntaxes, hence, programming language design progressed slowly needing months or years of time, whereas, using PEG-related technologies, such as Ohm-JS, it is possible to create new syntaxes in several hours.  Coupled with the idea of using existing languages as "assembler" makes it possible to generate new compilers in a time-span of hours. 

The difference is that PEG-based technologies allow one to specify grammars that "skip" over details.  It is not necessary to create syntaxes that pattern-match every possibility found in the input.  Bottom-up parser generators, based on technologies like LR(k), require that every detail be specified.  Top-down parser generators, like Ohm-JS, allow programmers to specify only the top-levels of a parser and subsuming the rest into coarse-grained blogs of characters without the need to parse their contents.

In Ohm-JS, it is possible to say:
- match "(" *recur* ")"
- or `...`

where `...` doesn't contain any interesting characters, like parentheses.

In this case, the parser "comes up for air" only when it encounters a delimiter, like a parenthesis (the choice of delimiters depends on the application).  The parser then dives down again, expecting to find a matching ")" (close parenthesis) when it comes back for air again.

This means that we can create *syntax stacks* and *syntax pipelines*.  We can pattern-match "only enough" of the input to get a small task completed, passing the result on to another step in the stack/pipeline that performs another small task, and, so on.

It is possible to bracket, hierarchically, portions of text that should be skipped and passed over.  This technique of hierarchical parsing is already used in Lisp macros.  You can embed Lisp macro calls within Lisp macros.  The language compiler/interpreter unwinds the macros hierarchically and produces runnable code through hierarchical composition (AKA layering) of the sub-constituents of a program.

As an example, consider the phrase:
```
a b c ❮ d e f ❯ g h i
```
(I've chosen to use Unicode characters for the brackets, to avoid confusion with ASCII brackets and to avoid confusion with existing languages).

A parser can parse "a b c" and "g h i", but leave "❮ d e f ❯" alone for downstream parsing.

This means, for example, that we could write a mini-language that handles state machine syntax with embedded other-language code.  The state-machine parser recognizes and transpiles only the state-machine portions of the text, leaving the other-language portions alone.  "Leaving" portions alone means that the parser simply skips over the groups of characters that are bracketed in some special way (in the example above, the "leave me alone" brackets are `❮` and `❯` ).

This ability to skip over syntax leads to the notion of orthogonal languages.  We can mix control-flow operations (like `if-then-else`, state-machines, Drakon control-flows, etc.) with OO objects.  We can cleanly separate the two realms - operators vs. operands - using syntax and "leave me alone" brackets.

## 2022-06-05-Toolbox Language Proposed Syntax

A *toolbox* language is a language that provides all of the atomic elements needed to compile any (most) programs, but has little syntax of its own.

Assembler languages are the traditional toolbox languages.  Assembler statements are line-oriented triples:
1. operator
2. subject operand
3. object operand

E.G. `MOV R0,R1` is a triple, with a clean separation between the operator (`MOV`) and the supplied operands (`R0` and `R1`).

Lisp is very much like this.  The "syntax" of Lisp is normalized.  Everything looks like a function call (except atoms, Lisp isn't perfect) and every apparent function call results in a value.  Lisp is an *expression language*.

Other languages tangle bits of syntax up with their utility as toolbox languages.  Most other languages are not *expression languages* and require explicit `return` syntax for creating non-void values.

I argue that it is possible to create a - very simple - syntax that can be transpiled into most any existing language.  The benefits of doing this are:
1. portability
2. no need to write full-blown compilers - existing compilers can be used 
3. rapid creation of new languages, with an attendant change in attitude as to how languages might be used.  I argue that a single project should have multiple, application-specific sub-languages, designed for it and all aspects of the solution.  I use the term SCN (Solution Centric Notation) for these sub-languages, to emphasize that they are lighter-weight than our current notion of what a programming language is.

To devise such a portable syntax, we need:
- operations
- operands
- lists of operands
- verbatim ("don't touch me") embedded syntax.

These requirements boil down to a very simple syntax:
- operations can be any phrases, and, can be transpiled by the likes of Ohm-JS into existing languages
- operations can be nested, like `cond`, to contain, recursively, other low-level operations and phrases
- operands can be fashioned on existing techniques for describing Objects, and, Object attributes and methods
- backquote 
### 2022-06-05-Lisp Backquote

Lisp converts all input text into Lisp lists.

Full-blown macros were invented in Lisp and led to the invention of backquote.

Lisp has a syntax for list constants, e.g.
```
'(1 x 3)
```

Working with macros, it became apparent that parts of constants needed to be evaluated.  At first, this meant not using list constant syntax and using Lisp list operations, e.g.
```
(list 1 x 3)
```

In this case, the atoms `1` an `3` evaluate to the numbers `1` and `3`, whereas the variable `x` evaluates to the value held in the variable.  If `x := 5`, then the final result is a list
```
(1 5 3)
```

This became cumbersome and "better" constant syntax was invented.  Instead of writing the constant in a purely-quoted manner, we could write:
```
`(1 ,x 3)
```
This form quotes all elements, except those preceded by `,`.  Comma-forms are evaluated as the constant is constructed, resulting in the same list:
```
(1 5 3)
```

This, of course, was further extended to allow the `,@` operator which splices lists into list constants.  For example if `x` had a value of a list (instead of having a value of 5), e.g. `x := '(a b c)`, then the final result would be:
```
(1 a b c 3)
```

Lisp was constrained to use ASCII characters.

In Lisp, *quote* was invented before *backquote*.  Later twists on quoting syntax needed to remain backwards compatible with exiting Lisp syntax.

The basic operations in quoting are:
1. quote a symbol/atom/list
2. evaluate a symbol/atom/list
3. evaluate and splice-in a symbol/atom/list 
	- splicing-in is valid only when it is done in the context of being inside a list to allow for "don't touch me, except ..." syntax.

Based on the above considerations, we might imagine a *toolbox language* to have the following syntax:

## Operands
An operand is 
- a name
- a dotted name (recursively)
- a low-level atomic string of characters surrounded by double and single quotes
- a low-level atomic number consisting of one-or-more digits
- - *symbols*

## Lists of Operands
- a list of operands is enclosed in square brackets `[` ... `]`
## Dictionaries of Operands
- a dictionary is enclosed in brace bracket `{` ... `}`
- a dictionary contains a set of pairs, whitespace separated (no commas)
- each pair consists of a *symbol*, a colon `:` character, an operand 
## Operations
## Verbatim
```
❮ d e f ❯
```
## Backquote Verbatim
Unlike Lisp, we are not mixing quoting with evaluating.  We are not creating lists, we are creating text and always splicing the result in.  Hmm.
```
a b c ❮ d e f ❯ g h i ⟪ d e f ⟫
```




