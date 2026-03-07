# 2022-06-12-EXPRs and FEXPRsEXPRs are functions whose arguments are evaluated at the call-point.  This is the norm in today's programming languages.

Programmers might have a hard time understanding what a FEXPR is, because, they've been indoctrinated to believe that all functions are EXPRs.

FEXPRs are functions whose arguments are *not* evaluated at the call-point, but can be explicitly evaluated in the function.

For example, consider:

```
a = 2
b = 3
def EXPR f (x, y) { return x + y }
f (a, b)
```

If `f` is an EXPR, then the above call becomes
```
f (2, 3)
```

This is considered "normal" in today's languages.

But, if `f` is a FEXPR, we get
```
a = 2
b = 3
def FEXPR f (x, y) { return x + y }
f (a, b)
```
...
```
f (a, b)
```

`f` can do anything it wants with its args.  The compiler can't do anything at the call-point, it has to pass `a` and `b` to `f` "as is".

Note that this implies that the FEXPR receives an environment which maps:
```
a: 2
b: 3
```

(Note: this is what McCarthy's original Lisp 1.5 did, it created *alist*s which recorded bindings).

# When Does The Difference Matter?
```
f(a+b,a-b)
```
becomes
```
f(5,-1)
```
when the args are evaluated (EXPR).

It becomes
```
f(a+b,a-b)
```
when the args are not evaluated (FEXPR).  Note that the compiler needs to wrap up the expressions "a+b" and "a-b" and pass them hole-hog to the callee.  It can't optimize (pre-compile) the expressions at all.

In (early) Lisp, this is easy, since everything, including expressions, is converted to a list.  In pseudo-code...
```
f ('(+ a b), '(- a b))
```
and, `f` can call `eval ()` to to evaluate the expressions as needed. Or, `f` can use Lisp list-operators to take the arguments apart and to re-compose them into some other form.

## Example
As an example, imagine an if-then-else expression[^expr] macro, that guarantees that only one of the branches will be evaluated - either the then-part or the else-part, but not both.  Like the `||` operator:

[^expr]: Most languages treat `if-then-else` as a statement, not as an expression.  This example includes a subtle difference - `if-then-else` is like a function that *always* returns a value.  See the section "Target Language Syntax" #targetlanguagesyntax as to why this subtle distinction can be important.

```
ifthenelseMacro ('(if (> a 1) (+ a 5) "Paul")))
```

There is 1 arg, a list containing 4 parts
1. if
2. (> a 1)
3. (+ a 5)
4. "Paul"

Taking the naive approach, we might deconstruct the arg into its 4 parts:
```
deconstruct arg
  .first () -> part1
  .second () -> part2
  .third () -> part3
  .fourth () -> part4
```

Now, maybe, we add some sugar to make things a bit more clear:
```
synonym ifpart ≣ part1
synonym testexpr ≣ part2
synonym thenpart ≣ part3
synonym elsepart ≣ part4
```

(obviously, a Production Engineer who was concerned with the number of characters on a page, would have written this differently)

Now, all that's left is to write a program, which
1. does a sanity check, ensures that *ifpart* is truly *if*, then ignores it
2. creates code to evaluate the test expression
3. creates code to evaluate thenpart only if (2) is true
4. creates code to evaluate elsepart only if (2) is false

We want to create code like this:
```
result = 
  if (a > 1) then
    return a + 5
  else
    return "Paul"
  end if
```

We might write the FEXPR `f`, in pseudo-code, as:
```
if (arg.length != 4) then 
  error ("ifthenelseMacro invalid input: the argument must a list that is exactly 4 items long");
end if
if (ifpart != 'if') then 
  error ("ifthenelseMacro arg does not begin with 'if'"");
end if
newcode = create-code {
  "result ="
    "if" "(" textexpr ")" "then"
      "return" thenpart
    "else"
      "return" elsepart
    "end if" 
}
re-compile (newcode) 
```

In Lisp, the above would look differently, due to the Lisp syntax for creating code-as-lists.  In JavaScript, you create code by gluing strings together and then calling `eval ()` (a compiler IS `eval`).  I haven't explored Python, but, I believe that it uses PEG and, I guess, makes lists of strings.  Failing all of that, the most straight-forward way to write programs that write code is to create strings, write them out to a file, then call *compile* (that's one of the obvious uses of pipelines).  You can create code in just about any language, but, some languages make it easier to do than others.  In the mid-1900s, it was considered frightfully inefficient to manipulate strings, so various work-arounds were invented and those work-arounds were given the name *homoiconic*.

## Recursive Macro Expansion

## Recursive Macro Expansion


What if one of the thenpart/elsepart branches contained another if-then-else?  The Lisp compiler works recursively, looking for macros within macros. One of the beauties of Lisp (non-)syntax is that doing recursive macro-expansions is easy.  Everything *looks like* a function, so the compiler only needs to check whether the thing being compiled is a function or a macro.  If it sees a macro, the compiler calls the macro-expander.  The macro-expander returns a blob of code that contains functions or macros.  The process repeats, until there are no more macros left.


## Target Language Syntax

## Target Language Syntax


#targetlanguagesyntax 

Target-language syntaxes also make a difference for writing programs that write programs.  

Syntax-less languages, like assembler and Lisp, make targetting them easy.  

Expression-based languages, like Lisp, make it easy to glue bits and pieces together build up whole programs.

Languages that support first-class functions and anonymous functions make it easier to glue bits together.

Languages with lots of syntax make harder targets.  

Languages that use text and balanced constructs (`if-then-else-endif`, `{ ... }`) make easier targets.  

Javascript is a reasonable target language.  Lisp is better.  Assembler is even better.  Python indentation-syntax makes it harder to crank out Python code from programs (I guess that you would want to use Python's built-in parsing stuff).  Markdown syntax is hard with the current set of tools.  Markdown is "more human readable", but less-good as a target for automatic cranking.  I've used markdown as a programming syntax, so, it's not impossible, just harder with current tools.
