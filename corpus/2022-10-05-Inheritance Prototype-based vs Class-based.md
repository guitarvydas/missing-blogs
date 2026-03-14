# 2022-10-05-Inheritance Prototype-based vs Class-based
> https://futureofcoding.slack.com/archives/C5U3SEW6A/p1664945940180779


...

> (Ominous hole in my theory: This doesn't explain why prototypes were brought into Javascript, where they ostensibly no longer had much use.)


> prototypal inheritance was born in Self

Allow me to try to add some more context...


[tl;dr]
- Inheritance is about data structuring.  The only difference between Prototype-based Inheritance and Class-based Inheritance consists of RULES about WHEN it is legal to structure and re-structure data.
- 'Self' corralled prototypal inheritance.  'Smalltalk' corralled class-based inheritance.  Both, borrowed from previous ideas.
- All big inventions in programming stem from the use of dynamic languages.
- Class-based inheritance is Waterfall Design. Protoype-based inheritance allows iterative design.
- JavaScript was based on Lisp.  JavaScript designs-in prototype-based inheritance better than Common Lisp, Scheme, Clojure, Racket, etc., etc.

[background]

In the beginning there was assembler.

There are 2 types of assembler
1. line-oriented
2. tree-oriented

Assembler is characterized by 
- ultra-simple syntax (usually prefix notation)
- commands with operands.

Line-oriented assembler is what we call "assembler".

Tree-oriented assembler is what we call "lisp".

Assembler gives you a toolbox of functionality, but, if you want to structure your data you have to do it manually.

In assembler, nothing stops you from re-structuring your data on the fly.

The result, though, can be hard to understand.  This is part of what we call "readability".  The term "readability" is usually used to mean human readability (aside: but, there's also machine readability ; note that textual "readability" does not mean the use of general English prose, but, only a well-defined, restricted subset of English)

One of the tennets of Computer Science is Don't Repeat Yourself (DRY).

Inheritance is simply a way of structuring data in a DRY way.  If you've structured your data, don't do it again, copy the template.

So-called "prototypal inheritance" is a way of structuring data that can allow changes to the structure at runtime.

"Class-based inheritance" is an optimization of prototypal inheritance.  In class-based inheritance, you separate your Red Smarties from the rest (a Smartie is an M&M, a "red Smartie" tastes "better").  If you apply the class-based optimization, then, you can compile-out data structuring.  The compiler can help make your resulting code tighter and more check-able, but, you are allowed to structure your data ONLY at compile-time.  And, the result is less-confusing.  Nothing should change at runtime.  Dynamic-anything is "bad" (aside: this is a fundamental problem with pub/sub).

Optimization culls creativity, but, results in a notation that has certain "human readability" properties.  Optimization is "bad" during Design ("premature optimization"), but Optimization is "good" during Production Engineering (what we mistakenly call "programming").

Self and Smalltalk are syntaxes draped over assembler.  Self does not insist that you pre-define all data structures, Smalltalk does insist on pre-definition.  The tools for inheritance always existed, but Self coined the phrase "prototype" and Smalltalk coined the phrase "class" (actually, Smalltalk borrowed the concept from a previous language, but we won't go there now).

JavaScript was originally based on Lisp.  In trying to keep the flavour of a "dynamic language", JS does not insist on pre-defining all data structures before runtime.  IMO, JS does this better than the Common Lisp, the Scheme, the Racket, the Clojure variants of Lisp.  In Common Lisp, the designers chose to jump directly to premature-optimization using classes and built that concept in as syntactic baubles ("defclass"), that cause programmers to think in a Certain Way, even though the tools for less-calcified data structuring are still present (but, generally ignored by class-indoctrinated programmers).

Ideas calcified by compile-time optimizations cause programmers to think in Certain Ways and disallow other interesting forms of Creativity.  

There IS another way to optimize - as seen in JIT and 1970's compiler technologies (e.g. gcc, OCG) and linking loaders.  Optimize at runtime.  Treat optimizers as barnacles attacking only already-working programs.  Premature optimization has led us to building and using compiler-appeasement languages and has snipped off other creative avenues of thought.  

Or, we could more simply divide programming into 2 camps (aka "divide and conquer"): (1) Design (2) Optimize.  This division happens all of the time in more mature industries - products are released, and, only later, the products are cost-optimized.  In fact, this division is so severe that it is given the name "Production Engineering".  In contrast, Software uses the single term "Engineering" to mean "Architecture" and "Engineering" and "Production Engineering" and "Test Engineering" and "Deployment Engineering", and ...)

If you Design and Optimize all in one go, you are involved in a Cottage Industry. In a Cottage Industry, the same person, or a group, wears all of the hats. 

Class-based inheritance is Waterfall Design.  You must know everything about the data before you can write correct classes.  Prototype inheritance can be iterative, you can change your mind later, you can incrementally alter the templates as you learn more about the problem space.

Compilers can be built to compile programs if the programs obey the rules of class-based inheritance.  Compilers cannot, in general, compile programs that do not follow the rules of class-based inheritance, e.g. compilers cannot compile prototype-based inheritance, but, can compile class-based inheritance.


[conclusions]

I would argue that Self did not invent prototypal inheritance, but corralled the ideas and created the name.  Self's contribution is the exploration of the space of data structuring and of making optimization be a continuum that can be applied at different times - not just at compile-time.  This exploration ultimately led to the concept of JIT.

JavaScript was designed to allow "dynamic" programming (whether it succeeded, can be argued) and was originally based on Lisp.  Prototypal inheritance is less constraining than class-based inheritance, therefore, was made a part of the design of JavaScript.

To me "system" means "dynamic language".  And "general purpose programming language" means "static language".  Each kind is "good" and each kind is "bad".

IMO, all big inventions in programming stem from the use of dynamic languages, and, ultimately from the use of assembler. GC, first-class-functions, Haskell, REPLs, etc., etc.

The only difference between class-based inheritance and prototype-based inheritance is *when* it happens.  Both, class-based and prototype-based inheritance can structure data at compile time.  In prototype inheritance, though, data can, also, be structured and re-structured at runtime.  Runtime restructuring is not allowed in class-based inheritance.

Class-based inheritance is Waterfall Design.   Protoype inheritance allows iterative design.


miscellaneous:

3 OO-ish data structuring techniques
1. classes
2. prototypes
3. mixins

2 is like 1, with some of the compile-time-only restrictions removed. The mixin idea, 3, looks like OOP, but is very different.  In class-oriented OOP, you have a vector of operations associated with each class.  In mixins, the reverse is true - you have a class without operations.  Operations "decide" on-the-fly if they can be applied to a cross-product of parameters.  All three methods get rid of explicit "if-then-else" based on type (which is the really big win - "if-then-else" is just bad).  Mixins go beyond simple class-based inheritance - you can specialize operations on /value/ instead of type, you can create :before and :after methods. Capability depends on the method ("operation") and not on the class. For a simple, nonsensical example, you can write a "plus" method that works on {int x int} and another "plus" method that works on {int x string} and another "plus" method that works only on {nil x int}

- question to self: can you remove defclass from Lisp and leave only mixins?  lisp already has deftype, why do you need defclass?
- lisp isn't a programming language, it's a soup
- mixins ≣ assembler for constructing various kinds of class / prototype / whatever-based languages.  I like to use the term "atoms" when discussing fundamental building blocks.  In my view, "mixins" are "atoms" whereas classes and prototypes are "molecules" constructed out of "atoms". 
