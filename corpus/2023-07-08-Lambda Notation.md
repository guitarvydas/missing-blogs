# 2023-07-08-Lambda Notation## Lambda Notation

Lambda notation represents a function in text format.  The format is:
```
λx.blah
```

1. Where "`λ`" is a code that says "this is a function".
2. Where "x." is the argument list.  
4. Where "`blah`" is the body of the function.  

In lambda notation, there is always *exactly one* argument.  This is called *currying*.  If we had a function with 3 arguments in some other programming language, it would be represented in lambda calculus as
```
λx.λy.λz.blah
```

Note that the body *always* returns its result, so there is no need for the superfluous keyword `return`.

