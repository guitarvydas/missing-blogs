# 2022-06-05-Lisp BackquoteLisp converts all input text into Lisp lists.

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
	- splicing-in is valid only when it is done in the context of being inside a list