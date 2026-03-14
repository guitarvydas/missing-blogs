# 2023-10-18-Software Atoms
An *atom* is the smallest stand-alone unit that we *choose* to think about.

An *atom* is like a "line in the sand" - we *choose* not to discuss details below the atomic level and only *choose* to discuss compositions of these atoms, i.e. *molecules*.

Atoms are
- stand-alone
- composable
- asynchronous.

Function-based programs do not satisfy these criteria.

For example, user-defined functions only *appear* to be stand-alone, but, if they incorporate calls to other functions, they cannot stand alone without dragging the other function(s) into the mix.

User-defined functions *appear* to be composable, but the rules of composition are strongly defined by the underlying language.  Usually, the rules insist on sequential composition of lines of code and insist on an order of evaluation of arguments to functions, i.e. that all arguments must be evaluated before a function is invoked.

Functions are definitely not asynchronous, since a calling function must *block* until the callee returns a value.

## Work-Arounds

We have been trained to use workarounds - aka *epicycles* - that make functions appear to be atoms.



A low-level call, like `print(x)`, might be an *atom* if `print` is built into the underlying programming language.

On the other hand, a user-defined function, like `f(x)`, cannot be an atom