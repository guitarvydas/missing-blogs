# 2022-06-04-Transpiling Markdown to Structured Text# Synopsis

Markdown can be used as a textual format for programming languages.

Markdown is similar to other indentation-based languages, like Python, in that markdown is based on lines of text.  

Most structured programming languages are based on the notion of balanced brackets (where  brackets are actual bracket characters, like `{}`, or textual constructs like `if ... end if`).

Most tools for language-building are, also, based on the notion of balanced bracketing ("structured text").

The main technological step in using line-based languages is to convert line-based languages to structured text, allowing further processing using existing tools.

This paper develops a simple, experimental tool for converting line-based to structured-text-based syntax using PEG-based technology, in particular Ohm-JS.

# Input
```
# a b 
## c d
## e f
```

# Output
```
{a b
{c d
}
{e f
}}
```

The markdown-flavoured input syntax is converted to brace-bracketed syntax which can then be parsed and processed using existing tools.

Note that the output syntax is not very human-readable.  It doesn't matter whether human programmers find this syntax readable, I only wanted to transpile to code that is machine-readable, for further automated processing. Ohm-JS skips whitespace and parses structured text, so the above output is acceptable.  The main goal is to make the transpiled code readable by Ohm-JS. Human-readability is unneccessary in this stage.  So-called "readability" (taken to mean human-readability) is YAGNI.

# Algorithm
A section beginning with an octothorpe `#` is composed of 3 parts:
1. The octothorpes `#`
2. The first text up to `\n`
3. The rest of the text up to the next octothorpe (incl. `\n`s).

1. Set two counters to 0. (depth and openbrackets).
2. Read text, line by line.  
3. When a `#` is encountered, determine new depth as the number of `#`s in the current line. If newdepth > depth, emit an open brace `{`, if newdepth === depth emit close and open `}\n{`, otherwise panic. Set depth to newdepth, increment openbrackets by he tnumber of `{`s that were added.
4. The above grammar matches all parts of a line that do not contain octothorpes.  Such captured matches are emitted to the output as complete lumps without needing to parse them fully.  One of the features of PEG parsing (hence, of Ohm-JS) is the ability to specify patterns (parses) that contain balanced brackets and to ignore "the rest".  This allows one to write grammars that are small and succinct while not needing to worry about patern-matching (parsing) the rest of the input data.
5. During finalization, emit one `}` for each openbracket.

No judgement is made about the contents of the markdown text. That is left up to other tools.

Syntactical errors are ignored at this stage.  Markdown is simply bulk-converted to structured-text.  Syntax checking is provided by tools for structured-text parsing.

# Usage

To use the code in this experiment, load the .html file into a browser and hit the "transpile" button.  See below for the github link.

# Code
This experiment is currently couched in HTML, using Ohm-JS for parsing.

Note: the `rewriteRules ()` code is purposefully made to be very repetitive (and boring).  In another paper, I show how to automate the process of creating semantics code.

Note: every parameter is tree-walked, regardless of whether the result is used or not.  This inefficiency leads to more regular code and easier automation (in another paper).  It is likely that such inefficiencies will be automatically removed in the future, not by human programmers.


## Grammar
```
  ToBrace {
    main = line+
    line = indent? spc? toEOL+ linetail
    linetail =   newline toIndent* -- withContent
               | newline? end -- withoutContent
    indent = indentChar+
    indentChar = ("#" | "*")
    toIndent = !indentChar any
    toEOL = !newline any

    newline = "\n"
    spc = " "
  }
```
The above grammar matches lines of text using Ohm-JS syntax (PEG-like).

A pattern-matcher application is automatically constructed from the above specification (AKA "grammar") by the Ohm-JS processor.

Standard markdown uses the octothorpe character `#` for depth.  The emacs editor allows for `*` (in *org* mode).  Both characters are accepted by this grammar.

## Semantic Rules for Conversion
Note: All rewrite functions return exactly one string.  In some places, functions that create side-effects are needed and are called inline during string building.  Such functions return the empty string `""`.  Examples of this are the calls to `closebrackets ()` and `emitbrackets ()`.

Note: All captures are tree-walked.  In some cases, the results of the tree-walk are not used.  Tree-walking in such cases is moot and inefficient.  These inefficient sequences have been purposefully left in the code, normalizing the code and making it repetitive and boring.  The purpose of such inefficiency is to allow automated processing of the code sequences.  Normalization, however inefficient, makes automation easier.  An example of such automatable normalization would be the use of the stack for passing parameters between assembler routines, instead of using registers.  It was easier to spot oppurtunities for automation / compilation, when the assembler code was normalized instead of being hand-optimized (ad-hoc optimized) by human assembler programmers.  At first, compilers were made to emit apparently inefficient code, but, later, such code sequences were optimized away by automated optimizers.  The opportunities for compilation and optimization were not apparent except when the code looked - first - to be inefficient.  I believe that the same kinds of automation can be developed for code sequences written in current-day programming languages, like Python and Haskell.  It should be possible to treat these languages as "assembler", using transpilers to compile even-higher-level languages to these languages.  A example of normalization can be seen in the various syntaxes for PEG libraries.  Some syntaxes require that programmers pick names for certain pattern-match-captures, leaving other matches unnamed.  Ohm-JS, on the other hand, creates a "name" for *every* capture (in the form of parameters to functions), regardless of whether the capture is meaningful to a particular pattern-matching program or not.  This redundancy allows easier transpilation of Ohm-JS code, one example being the *prep* tool.  The *prep* tool blindly tree-walks all captures.  Removing *just this simple level of detail* from the programming process, allows the programmer to consider more-interesting problems.

Note: All captures that are generated by grammar rules using the operators `+`/`*`/`?` (Ohm-JS *iterator nodes*) are flattened to a single string via the use of the `.join ('')` function.

The rules for rewriting are written as JavaScript functions within a map:
```
  const rewriteRules = {
      main: function (line) {...},
      line: function (indent, spc, toEOL, linetail) {...},
      linetail_withContent: function (newline, toIndent) {...},
      linetail_withoutContent: function (newline, end) {...},
      indent: function (indentChar) { ... },
      indentChar: function (c) { ... },
      toIndent: function (c) { ... },
      toEOL: function (c) { ... },
      newline: function (c) { ... },
      spc: function (c) { ... },
      // required by Ohm-JS...
      _terminal: function () { ... },
      _iter: function (...children) { ... }
  };

```
I've elided the details within the functions, to more clearly show the 1:1 relationship between the grammar and the rewrite map.  The rest of the details can be found in the Appendix.

Note that the code uses 2 global variables (depth and openbrackets).  Global variables are a manifestation of the use of text, instead of diagrams, to express programs.  The goal is to remove the *cause* of global variables, not necessarily the globals themselves.  Other papers suggest diagram-based syntax which doesn't cause "global variable problems".  Instead of wasting brain power on removing global variables from this code, I assume that the code is transitory and not in need of further preening.

# Github
https://github.com/guitarvydas/20220604md2brace

Load `md2brace.html` in a browser.  Press the "transpile" button.

# Appendix Full Code for This Example
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

<h1>Code Markdown to Structured Text Transpiler Workbench</h1>

<p>markdown source:</p>
<textarea id="src" rows="5" cols="90" placeholder="markdown" style="background-color:oldlace;">
# a b
## c d
## e f
</textarea>

<p>transpiled:</p>
<textarea id="output" rows="7" cols="90" placeholder="transpiled"  readonly style="background-color:whitesmoke;">
</textarea>
<br>
<br>
<p id="status" > READY </p>

<!-- Ohm-JS -->
<script src="https://unpkg.com/ohm-js@16/dist/ohm.min.js"></script>


<br>
<button onclick="transpile ()">Transpile</button>
<script>

const grammar = ohm.grammar(String.raw`
  ToBrace {
    main = line+
    line = indent? spc? toEOL+ linetail
    linetail =   newline toIndent* -- withContent
               | newline? end -- withoutContent
    indent = indentChar+
    indentChar = ("#" | "*")
    toIndent = !indentChar any
    toEOL = !newline any

    newline = "\n"
    spc = " "
  }
`);

  const rewriteRules = {
      main: function (line) {
          reset ();
          var walked_line = line.walk ().join ('');
          return `${walked_line}${closebrackets ()}`;
      },
      line: function (indent, spc, toEOL, linetail) {
          var walked_indent = indent.walk ().join ('');
          var walked_spc = spc.walk ().join ('');
          var walked_toEOL = toEOL.walk ().join ('');
          var walked_linetail = linetail.walk ();
          return `${emitbrackets (walked_indent)}${walked_toEOL}${walked_linetail}`;
      },
      linetail_withContent: function (newline, toIndent) {
          var walked_newline = newline.walk ();
          var walked_toIndent = toIndent.walk ().join ('');
          return `${walked_newline}${walked_toIndent}`;
      },
      linetail_withoutContent: function (newline, end) {
          var walked_newline = newline.walk ().join ('');
          var walked_end = end.walk ();
          return '\n';
      },
      indent: function (indentChar) { return `${indentChar.walk ().join ('')}`; },
      indentChar: function (c) { return `${c.walk ()}`; },
      toIndent: function (c) { return `${c.walk ()}`; },
      toEOL: function (c) { return `${c.walk ()}`; },
      newline: function (c) { return `${c.walk ()}`; },
      spc: function (c) { return `${c.walk ()}`; },
      // required by Ohm-JS...
      _terminal: function () { return this.sourceString; },
      _iter: function (...children) { return children.map(c => c.walk ()); }
  };

  // helper functions
  
  var depth = 0;
  var openbrackets = 0;

  function reset () {
      depth = 0;
      openbrackets = 0;
  }

  function emitbrackets (indentstring) {
      var currdepth = indentstring.length;
      var prevdepth = depth;
      depth = currdepth;
      if (prevdepth === currdepth) {
          return "}\n{";
      } else if (currdepth > prevdepth) {
          var openp = openbrackets;
          openbrackets = openp + 1;
          return "{";
      } else {
          throw "workbench: internal error";
      }
  }
  
  function closebrackets () {
      var openb = openbrackets;
      var result = "";
      while (openb > 0) {
          result += "}";
          openb -= 1;
      }
      return result;
  }
  
  function transpile () {
      let src = document.getElementById('src').value;
      let matchResult = grammar.match (src);
      if (matchResult.succeeded ()) {
          document.getElementById('status').innerHTML = "OK";
          let sem = grammar.createSemantics ();
          sem.addOperation ('walk', rewriteRules);
          let treeWalker = sem (matchResult);
          let text = treeWalker.walk ();
          document.getElementById('output').value = text;
      } else {
          document.getElementById('status').innerHTML = "parse FAILED";
      }
  }
  </script>
</body>
</html>


```