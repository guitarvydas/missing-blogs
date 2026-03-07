# 2023-07-18-Odin0D in 3 PartsThe current manifestation of 0D (zero-dependency, component-based programming) can be split into three major pieces.

The current version of the code, as one big piece, is in the repo https://github.com/guitarvydas/odin0d.

This version of 0D contains all three major pieces, but, they are not currently split apart.

## Pieces
1. Diagram transpiler.
2. Registry.
3. Kernel.

Currently, the diagram transpiler transpiles diagrams from draw.io format into an intermediate form.  It is simple to dump the intermediate form out as a disk file, e.g. in JSON format.

The Registry code creates an in-memory database of components, based on the output of the diagram transpiler.  This code could, also, be easily converted to read components in disk format.  For example, the code could be converted to read JSON intermediate form components and to convert them into an in-memory database.

The Odin0D Registry code equates to Loader code in traditional operating systems.

The code that runs a component-based system is in `0d/0d.odin`.  Let's call that the *kernel*.  It uses the in-memory component database to instantiate components and to run them.

## Loader and Kernel in Other Languages
To implement 0D in other languages, like Python3 and Common Lisp, it is only necessary to port the Registry and the Kernel code.

The diagram transpiler can remain coded in Odin as long as the transpiler produces an intermediate format that is acceptable to the ported Registry and Kernel code.  For starters, we can use JSON as the intermediate format.  

JSON reading and writing libraries are available in many languages.  This should make it easier to port 0D to other languages.  

For example, creating Python0D should simply consist of 
1. porting the Registry to Python and creating some sort of component database that can easily be used by the Python kernel code
2. porting the Kernel to Python.

## Porting Code
The Odin0D version of 0D is "ideal" in that it doesn't need an underlying garbage collector and includes optimizations for static memory allocation.  

The Odin0D code is rife with static type-checking details.

The Odin0D code is less-than-ideal because of such static type-checking details which make the code more difficult to read at a high level and which discourage experimentation (because every change requires attention to details beyond simple high-level concepts).

It is easier to strip out details than it is to infer them and to put such details back in.

I have been experimenting with automated code porting in the form of a syntax mapper in the repo https://github.com/guitarvydas/0dv2/tree/dev/syntax-mapper based on the use of Ohm-JS.

It seems that this syntax-mapping work can be subsumed by the use of ChatGPT.  Early experiments with ChatGPT show that ChatGPT can transpile code from Odin to Common Lisp and Python in only a few minutes.  

The transpiled code needs to be carefully checked for hallucinations.  This kind of checking can be done via manual eye-balling and the use of existing Python and Common Lisp compilers.

### Future Ports

Once this process is wrung out, we might try porting this code to JavaScript or to WASM.
