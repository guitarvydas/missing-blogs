# 2022-06-03-Java What It PopularizedJava popularized
- VM (virtual machines)
- GC (Garbage Collection)
- Classes
- JIT

Most of this stuff was invented before Java, but, Java brought these ideas into the mainstream. 

## Virtual Machines
Opcodes for instruction sets that mimicked CPU instruction sets.

Software, instead of hardware.

APIs.

I first saw this idea in Tiny Basic and LAP (Lisp Assembly Program).

## Garbage Collection

Invented in Lisp 1.5 to allow heaps and mutation in the FP (functional programming) paradigm.

## Classes
Classes are inheritable data types optimized for compilation.

Most languages, e.g. Common Lisp, jumped directly to specifying / implementing Classes.

### Self

The Self programming language was based on prototype inheritance.

### JavaScript Inheritance

JavaScript implemented prototype inheritance.  Later, classes were implemented using prototype inheritance in JavaScript.

## JIT (Just In Time Compilation)

I first saw early forms of this concept in early Lisps, under the name "fastcall".

Subroutine calls are encoded as indirections through pointers.  After the first indirect call, the target routine is cached and the indirection is modified to point directly to the target routine. ("Self-modifying code").

This technique allows circumenting declaration-before-use by allowing routines to be defined (added to the global environment) after the caller is "compiled" (added to the environment).

This technique is similar to what a linking-loader does.  Compilation units do not specify targets for calls, but specifies *stubs* for the calls.  The linker "fixes up" the stubs replacing indirect stubs with absolute addresses of the target routines.

The Self language explored this concept using *types*.  Instead of inserting type-checking code into the cached routines, Self created routines - on-the-fly, just-in-time - that handled specific combinations of typed data.  Indirection is usually "compiled away" by a compiler, but with JIT, the compiler is invoked at runtime to produce specific routines based on parameter types.  Interpreters were thought to be "too slow" because they checked types at runtime on each call.  Self moved the type-checking compiler code into the runtime and cached the results.

Most modern Lisps do not directly interpret code, but compile it first, then call the compiled code.  The assumption is that runtime calls to compiled code would happen more frequently than calls to the compiler to compile the target code.  Instead of running parts of the compiler at "compile time", those parts would be called at "run time" and the compiled results would be cached.