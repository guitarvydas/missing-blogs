# 2023-06-21-Wart In Static Type Checking
## Wart In Static Type Checking
Odin is better than most statically typed languages, in that Odin allows the use of `:=` as a way of side-stepping having to explicitly know what the type of something is.

For example we can say
```
v := xyz(...)
v.abc(...)
```
and the Odin compiler will figure out the type of `v` without asking the developer to specify it, and, it will check that `v` has a method `abc`.

But, if we try to abstract this away by creating a function for the second line, e.g.
```
v := xyz(...)
def(v)

...
def :: proc (v) {
  v.abc(...)
}
```
Suddenly, the programmer needs to explicitly know the type of `main_controller`.

## Why is this Bad?
This is an edge-case that interrupts Design Flow.  

This seems to be a minor problem, but, is actually a major problem.  

The problem is related to the chasm between *design* and *optimization*.

The problem is that the desire for *static typing* has placed restrictions on how a developer is allowed to think.  This restricts *design*.

During *optimization*, though, we want to *Production Engineer* the code and we want as much automated help as possible.

Production Engineering is not Engineering.  Production Engineering is only a *subset* of Engineering.  Engineering is broader in scope than just worrying about optimization.  At first, Engineers need to worry about how to get the Architects' ideas to just-work.  Later, when the ideas have been debugged, we can spend time optimizing the ideas and productizing them - i.e. Production Engineering the ideas.

I argue that most of our programming languages, like Python, Rust, etc. are geared only towards Production Engineering and do not address the full scope of Engineering.

## Existing Solutions

### Common Lisp Macros
Using a macro, we can write the abstract version and the compiler will transmogrify the abstracted code into the first form.

The problem here is that if there is a type  mismatch the error message will be relative to the transmogrified code and may leave the developer scratching their head as to what is wrong.

### Duck Typing
Duck typing does not have this problem.

The type check is done at runtime, dynamically.

The developer can write the abstracted version without complaints from the compiler.

The problem here is that the type check is done dynamically.  If there is a type mismatch, 
- we only find out about type mismatches at runtime
- we only find out about type mismatches if the program - at runtime - hits this spot in the code.

### ML
I wonder if ML does better?  
