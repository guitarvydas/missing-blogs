# 2022-07-07-TN-Machine-Writable Python
[TN means "Tech Note"].

# The Problem - Writing Programs That Write Programs in Python

Creating programs that write programs is easier if the target syntax is normalized and bracketed ("structured" text).

Examples of easy-to-generate target syntaxes are:
- assembler
- Lisp.

In assembler, everything is a triple (`MOV R0,R1`) and each instruction occupies no more than one line of text.  Generated lines of text can be glued together in whatever order is convenient.

In Lisp, all syntax is normalized to lists, and, all instructions are expressions.  All code sequences are bracketed in list form and all code sequences return a value, even *if statements*.  For example, in Lisp, an *if statements* is written as:
```
(if *expr1* *expr2* *expr3*)
```

where *expr1* is a test function, *expr2* is the *then* part (an expression) and *expr3* is the *else* part (an expression).  In Lisp, *if* is a function that returns a value.

In Lisp, expressions can appear in only 2 forms:
- a basic *atom*, like a number or a string
- a *function call* which appears as a list.

In Lisp, a block of statements is wrapped inside a function called *progn*.

This simplicity - only 2 choices and barely no syntax - makes it easy to write programs that write Lisp programs, and, is probably the reason why *macros* were first invented in Lisp.

Lisp functions, and, atoms, can be glued together in simple ways by code generating programs.

# The Problems With Generating Python Code

Python, though, presents several problems for code generation:
- Python has syntax, not every command is an expression. Some commands are statements, like the *return* statement
- Python uses indentation instead of bracketing to format its textual code.

# A Solution
One way to write programs that write Python, is to to create a pseudo-Python target language that is bracketed.

I use `(.` and `.)` as brackets because the ASCII parentheses are understood by emacs' auto-indenter (pretty-printer).  I use emacs to develop, view and debug generated Python programs.  If I knew how to (easily) change the bracket character in emacs' auto-indenter, I might have used a character that is outside of the usual ASCII character set, like a Unicode bracket character.  As it stands, I use the 2-character glyphs `(.` and `.)`.

For example, an *if* statement in pseudo-python might be emitted as:
```
(.if (x > y):(.
z = a.).)
```
I generate pseudo-Python and keep the target in pseudo-python syntax as long as possible.

As a last step, the pseudo-Python is converted to human-readable Python syntax by a small function that counts brackets, creates appropriate indentation and removes the brackets.

I've include the source code for the indenter function in the Appendix.

# Github - Actual Use-Case
I generate Python in the experimental repo `pypm`.

[indenter ()](https://github.com/guitarvydas/pypm/blob/dev/tbx/index.html#L683)

# Appendix - Indenter
```

  let indentation = [];
  // we emit code using bracketed notation (. and .) which is compatible
  // lisp pretty-printing, which allows easier debugging of the transpiled code
  // then, for Python, we convert the bracketing into indentation...
  function indent1 (s) {
      let opens = (s.match (/\(\./g) || []).length;
      let closes = (s.match (/\.\)/g) || []).length;
      let r0 = s.trim ();
      let r1 = r0.replace (/\(\./g, '');
      let r2 = r1.replace (/\.\)/g, '');
      let spaces = indentation.join ('');
      let r  = spaces + r2.replace (/\n/g, spaces);
      let diff = opens - closes;
      if (diff > 0) {
          while (diff > 0) {
              indentation.push ('  ');
              diff -=1;
          }
      } else {
          while (diff < 0) {
              indentation.pop ();
              diff += 1;
          }
      }
      return r;
  }

  function indenter (str) {
      let result = '';
      str.split ('\n').forEach (line => {
          let s = indent1 (line);
          result += '\n' + s;
      });
      return result;
  }
```