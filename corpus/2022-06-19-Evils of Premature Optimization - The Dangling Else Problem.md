# 2022-06-19-Evils of Premature Optimization - The Dangling Else Problem
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
