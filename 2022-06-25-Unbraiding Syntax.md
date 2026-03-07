# 2022-06-25-Unbraiding Syntax# Unbraiding Syntax
## Textual Programming Was Caused By History
Programmers and programming language designers settled on textual progamming languages due to the fact that mid-1900s hardware supported characters more easily than it supported overlapping bitmaps of graphical entitities.

Text-based programming languages are based on grids of non-overlapping small bitmaps (AKA characters).

*Programming* consists of controlling a machine (an electronic computer).

There is no inherent reason that control scripts need to be written in textual form.  

The choice of text for expressing programming scripts was purely pragmatic, based on the abilities of mid-1900s hardware.  

Some textual programming languages use mathematical notation which was invented for use with pen-and-paper and clay tablets.  Mathematical notation carries baggage with it - in the form of blocking function calls - that use only a subset of the available functionality of electronic computer hardware.  Functional programming is a suitable notation for parts of computing (functions which need synchronous parameter blocks, exhibit blocking behaviour and always return synchronous value blocks), but is less suitable for non-mathematical operations, such as distributed programming (witness the problems incurred by JavaScript's callbacks (which are twisted expressions of distributed computing that are forced to fit into the functional paradigm)).

# Extending Syntax
## ASCII Art
Most humans understand diagrams to contain isolated units of functionality.

Non-programmers, like CEOs, spontaneously create whiteboard diagrams to express their intentions regarding software products.

Whiteboard diagrams tend not to use a standardized "syntax" (sets of symbols).  This non-standardization issue is misunderstood to mean that diagrams - in general - cannot be used for creating program scripts.   One needs to look only at non-standard forms of text, e.g. human language, to see that such an argument against using diagrams is specious.  Programming language designers found ways to standardize text and to make text suitable for creating program scripts.  Programming language designers would have found ways to standardize technical diagrams, if other factors (such as hardware inabilties) were removed.  Also, consider the fact that technical diagrams are used in many fields of Engineering, e.g. blueprints in construction and schematics in electronics.  Such examples make it clear that diagrams can be used as technical documentation.

Programming lanuage designers try to capture diagrammatic ideas using ASCII Art.  The ASCII notation was prematurely optimized and does not faithfully represent concentric containment of layers (e.g. boxes within boxes) which led to gotchas like "the global variable problem".  One would not, naturally, draw concentric boxes on diagrams and include global variables, but, this happened in ASCII Art because full-bracketing was optimized away during language design.

For further discussion and examples, see 
## 2022-06-04-Global Variables Caused By Textual Coding Practices

I argue that the "global variable problem" was caused by the use of text-based programming languages.

For example

```
var x;
function f (...) {
  var y;
  y = 1;
  x = 2;
}
```

Would be written in diagram form as:
![globals-freevariable.png](globals-freevariable.png)

Upon seeing this, we would be compelled to rewrite it as:

![globals-boundvariable.png](globals-boundvariable.png)

Which immediately wraps a *scope* around the global variable `x` and makes it obvious, to the reader, what the scope of `x` is and where it can be used.

Note that λ-calculus does exactly this, but, in textual form, by wrapping a λ around the global variable `x`.  

Note that λ-calculus uses a more politically-correct name for the word 'global'.  It is called a *free variable*.

The "global variable problem" was ultimately solved by wrapping variables in textual scopes, mimicking diagrammatic expressions of programs. `{ ... }` means `box`, but isn't as visually obvious as a drawing of a box.


### 2022-06-07-Abstraction In Diagrams

# Abstraction in Diagrams
In diagrams, *abstraction*s are created by wrapping rectangles around components and then pushing the details onto another diagram.

A group of components are *abstracted* by lassoing the group and making a single component out of th group.

Abstraction in diagrams is structured by using nesting.

Connections (lines) and components cannot cross the boundaries of an abstraction. 

Containers can refer only to children that are directly contained.  References cannot cross boundaries, hence, a Container can refer to (and route messages for) components that are 1 level inside the Container, but cannot refer to children within the children, nor refer to peers.  Containers, like Leaf nodes, are components and can send messages upwards only to their own parent Containers. This process is analogous to business organization - each level of management summarizes information before passing the information up the tree (ORG chart) and managers can only command their direct reportees (children).  

The entire structure is hierarchical.  Container Components at one level only know about their directly-contained children and cannot know how the Children are implemented (as Leafs or as Containers - the children are components whose Implementation is hidden (elided) from their Containers and all levels above them)., and, 
## 2022-06-19-Evils of Premature Optimization - The Dangling Else Problem

Devising a syntax for conditionals, e.g. `if`, is straight-forward as a technical drawing.

`IfThen` is a box with 2 boxes inside of it.

`IfThenElse` is a box with 3 boxes inside of it.

E.G.

![ifthenelse.png](ifthenelse.png)

This technical diagram can be compiled to an executable program, but, if one insists on using ASCII Art to represent the diagram, we get

```
{ ifthen
  {
    // test
    ...
  }
  {
    // then
    ...
  }
}
```

and

```
{ ifthenelse
  {
    // test
    ...
  }
  {
    // then
    ...
  }
  {
    // else
    ...
  }
}
```

Both of these ASCII forms are parse-able by existing technologies, such as Ohm-JS.

Ostensibly, one grammar can handle both cases:

```
ifbox {
Main = Box
Box = "{" Statement "}"
Statement =
  | IfThenElse
  | Other
IfThenElse = "if" Box Box Box?
Other = OtherChar+
OtherChar = !separator any
separator = "{" | "}" | "(" | ")"
comment = "//" (!newline any)* newline
newline = "\n"
space += comment
}
```

This grammar parses both cases, if-then and if-then-else
![t1.png](t1.png)
![t2.png](t2.png)
![t3.png](t3.png)

# Readability
A problem arises when the ASCII Art form is made "more readable".

*Readability* comes in at least two (2) forms:
1. Human readable
2. Machine readable.

Assembler is machine-readable.  

Most modern programming languages, e.g. Python, Rust, emphasize human-readability at the expense of machine-readability.

The problem which arises is caused by the optimization of the ASCII Art form to make it more human readable.

This problem caused much hand-wringing in the mid-1900s and was given the name "dangling else problem".

The actual problem is one of premature optimization - jumping directly to making a human-readable ASCII Art version of the syntax, without consideration for the original, technical drawing form.

The problem is that the following phrase:
```
if (expression) {block} {block}
```
is ambiguous.  The parser does not know if the second block is the "else" part of the "if" statement or is a stand-alone compound statement block.

# Solutions
## Bracketing
The solution to the dangling-else problem is to bracket the *if* statement.

Lisp inadvertantly had no problem with this syntactic construct.  Lisp converts all textual source code into lists.  A Lisp *if* statement is a list with, either 3 or 4 items in it
1. The keyword "if".
2. The test.
3. The then-part.
4. The optional else-part.

List items can contain other lists (recursively), so nested *if*s are handled in this scenario.  Each nested *if* contains 3 or 4 items and the parse is "obvious", even to a machine (computer).

## Keywords As Brackets
One can use whole words as brackets, e.g.
```
if ... end if
```
Note that, in the UNIX shell, "end if" is spelled "fi".

## Characters As Brackets
One can use single characters as brackets.

The problem here is that ASCII provides too few bracket characters which leads to syntactic overloading which leads to gotchas.

The other problem arises from optimization for human readability.  A text looks "complicated" if it contains too many symbols.  Language designers try to reduce the syntactic sugar of their visual UXs for programming languages by using syntactic overloading.  This leads to gotchas.  Efforts were expended to formalize the syntactic overloading which resulted in syntaxes that resemble the above technical diagram.

## Unicode

Language designers are no longer restricted to using characters from the ASCII alphabet.

Ohm-JS, for example, makes it possible to write grammars that include a wider range of characters.

Language designers can choose to represent *every* syntactic/semantic construct with a different character (or set of characters).  

Fully-qualified syntaxes can be culled for human-readability by creating SCNs[^scn] to drape over the fully-qualified syntaxes.  Tools based on PEG, like Ohm-JS, can be used to quickly create such SCNs.

[^scn]: SCN means Solution Centric Notation.  This is essentially a DSL, but fine-tuned on a per-*project* basis, instead of being generalized to handle a wide class of problems.

## Else Keyword

Language designers can insert an extra symbol - a single character or a keyword like "else" - to qualify the meaning of statements.

For example
```
if ... { statements } else { statements }
```
is an *if-then-else* statement, whereas
```
if ... { statements } { statements }
```
is an *if-then* statement followed by a *compound statement*.

# Transpiling Human Readable Syntax to Machine Readable Syntax
The screenshot below shows a quickie grammar for recognizing human-readable if-else statements.  The code for a full transpiler follows.  This screenshot uses the Ohm-JS Ohm-editor...

![t4.png](t4.png)

## Transpiler Example Code
This code runs in a browser and uses Ohm-JS for parsing.

```
<!DOCTYPE html>
<html>
  <head>
    <style>
      textarea {
      }
    </style>
  </head>
  <body>

    <h1>If Unprettyfier</h1>
    <br>
    <label for="src">source:</label>
    <textarea id="src" rows="9" cols="60" placeholder="src" style="background-color:oldlace;">
if ( ...expr... ) {
  ...statements...
} else { 
  if (...expr...) {
    ...statements...
  } else {
    ...statements...
  }
}
    </textarea>
    <br>
    <label for="output">output:</label>
    <textarea id="output" rows="15" cols="60" placeholder="transpiled"  readonly style="background-color:whitesmoke;">
    </textarea>
    <br>
    <p id="status" > READY </p>
    <p id="regression" > incomplete </p>

    <!-- Ohm-JS -->
    <script src="https://unpkg.com/ohm-js@16/dist/ohm.min.js"></script>


    <br>
    <button onclick="transpile ()">Transpile to Machine Readable Syntax</button>
    <script>

      const grammars = ohm.grammars(String.raw`
      
humanReadableIf {
Main = Statement
Statement =
  | "if" "(" Expression ")" Block "else" Block -- ifthenelse
  | "if" "(" Expression ")" Block  -- ifthen
  | Other -- other
Block = "{" Statement Block? "}"
Expression = Other
Other = OtherChar+
OtherChar = !separator any
separator = "{" | "}" | "(" | ")"
}

ifbox {
Main = Box
Box = "{" Statement "}"
Statement =
  | IfThenElse
  | Other
IfThenElse = "if" Box Box Box?
Other = OtherChar+
OtherChar = !separator any
separator = "{" | "}" | "(" | ")"
comment = "//" (!newline any)* newline
newline = "\n"
space += comment
}

`);

      const dinc = 2;
      function indent (n) {
          var s = "";
          while (n > 0) {
              s += " ";
              n -=1;
          }
          return s;
      }
      
      const hooks = {
          
          Main: function (Statement) {
              var depth = this.args.depth;
              return `{\n${Statement.mr (depth)}\n}`;
          },
          
          Statement_ifthenelse: function (kif, lp, Expression, rp, ThenBlock, kelse, ElseBlock) {
              var depth = this.args.depth;
              return `${indent (depth)}if {${Expression.mr (depth)}}${ThenBlock.mr (depth+dinc)}${ElseBlock.mr (depth+dinc)}`;
          },
          Statement_ifthen: function (kif, lp, Expression, rp, ThenBlock) {
              var depth = this.args.depth;
              return `if (${Expression.mr (depth)})${ThenBlock.mr (depth+dinc)}`;
          },
          Statement_other: function (other) {
              var depth = this.args.depth;
              return `${indent (depth)}${other.mr (depth)}`;
          },
          Block: function (lb, Statement, OptionalBlock, rb) {
              var depth = this.args.depth;
              return `\n${indent (depth)}{\n${Statement.mr (depth+dinc)}${OptionalBlock.mr (depth+dinc).join ('')}\n${indent (depth)}}`;
          },
          Expression: function (x) { 
              var depth = this.args.depth;
              return x.mr (depth); 
          },
          Other: function (stuff) {
              var depth = this.args.depth;
              return stuff.mr (depth).join ('');
          },
          OtherChar: function (c) { 
              var depth = this.args.depth;
              return c.mr (depth); 
          },
          
          _terminal: function () { return this.sourceString; },
          _iter: function (...children) {
              var depth = this.args.depth;
              var mapped = children.map(c => {
                  var r = c.mr (depth);
                  return r;
              });
              return mapped;
          }
      };

      function transpile () {
          let src = document.getElementById('src').value;
          let grammar = grammars["humanReadableIf"]
          let matchResult = grammar.match (src);
          if (matchResult.succeeded ()) {
              document.getElementById('status').innerHTML = "OK";
              let sem = grammar.createSemantics ();
              sem.addOperation ('mr (depth)', hooks);
              let treeWalker = sem (matchResult);
              let text = treeWalker.mr (0);
              document.getElementById('output').value = text;
              {
                  let regression_src = document.getElementById ('output').value;
                  let regression_grammar = grammars["ifbox"]
                  let regression_matchResult = regression_grammar.match (regression_src);
                  if (regression_matchResult.succeeded ()) {
                      document.getElementById('regression').innerHTML = "regression Test OK";
                  } else {
                      document.getElementById('regression').innerHTML = "regression Test FAILED";
                  }
              }
          } else {
              document.getElementById('output').value = grammar.trace (src);
              document.getElementById('status').innerHTML = "parse FAILED";
          }
      }
    </script>
  </body>
</html>

```

## Github
[if](https://github.com/guitarvydas/if)
.

The choice of text-only for programming languages has hidden repercussions on expressivity.

## SVG
Computer hardware in the 2020's is capable of drawing overlapping windows containing simple graphical elements.

It would be possible to upgrade our notion of programming atoms from characters-only to a hybrid system that included:
- rectangles
- ellipses
- lines
- text.

Note that SVG already supports these atomic units, and, it allows them to be overlapped instead of being arranged in strict grids.

Most SVG editors that I have encountered are ill-suited to editing technical diagrams.  The effect 
is like being forced to use Microsof Word for writing programs instead of using vscode/vim/emacs/etc. Presently, I use a severely restricted subset of `draw.io` for my technical drawings of programs.