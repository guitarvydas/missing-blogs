# 2022-08-29-Programming Creativity
AFAICT, all languages inhibit creativity.  Computer Science is, currently, about mapping mathematical notation onto computers instead of about modeling computers in a notation invented expressly for the purpose of modelling electronic computers.  We witness all sorts of epicycles caused by this over-use of the mathematical paradigm for computers, e.g. preemption, thread safety, etc., etc.

Debuggers represent the bombed-out remains of creative-thinking about computers.  As such, the best debugger I've encountered is Lispworks (which is available in a Personal edition, which is free, I think).  Debugging is about UX+feature set, not +just+ about feature set. Type systems (dependent types, monads, etc.) and classes are great if you implicitly believe in premature optimization and waterfall development, as most programmers have been indoctrinated to believe.  IMO, vscode is an ugly manifestation of debugging which misses the point[^point].

[^point]: The point being: UX, UX, UX.  Having multiple views on a problem to (1) help you explore the design space, and, (2) to help you track down "bugs" (insufficiencies) in thinking about a problem.  Mapping a known solution to a clockwork solution is not the primary purpose of debuggers.

Debugging is about iteration, and, exploring how to structure a solution, and, how-to-understand-someone-elses-code (or your own code after you've forgotten how it works).

If you are confident that a solution should be programmed in a clockwork manner from the get-go, then you implicitly believe in waterfall design.  AFAICT, all current programming languages are biased towards clockwork programming (my jury is still out regarding Relational languages).

Programming can be untangled into at least 2 activities: 
1. Design and exploration
2. Production Engineering.  

AFAICT, all languages enhance (2) and, thereby, inhibit (1).

Engineering, itself breaks down into many sub-fields
- just-get-it-working (i.e. figure out what details are needed)
- production engineering (optimization, make it smaller, or, faster, or, ...)
- test engineering (make it testable - break the solution up in different ways to enhance testability - stop Production Engineers from over-optimizing and inhibiting testing)
- maintenance engineering (make it maintainable/extendable - stop Production Engineers from over-optimizing and inhibiting maintenance and extensibility)
- etc., etc., etc.

# What Is Lisp?
What we think of as being "assembler", is, but, a line-oriented assembler.

Lisp is, basically, a tree-oriented assembler.

Clojure (invented by a Lisper), is a tree-oriented assembler for FP.  I wouldn't call that Lisp.

Racket is the most modern version of Scheme.  Scheme and CL were both invented as compiler-appeasement languages.  Both promote attention to detail (i.e. Production Engineering), and, neither promotes true creativity.  Racket is just more of the same.

## Lisp - The Good Parts
- no syntax
- expression language
- everything looks like a function call or an atom
- tree structured
- no types[^lisptypes]
- dynamic[^dynamic]

[lisptypes]: Actually, Common Lisp has types and gradual typing for massaging Production Engineering concerns after-the-fact.
[^dynamic]: Actually, Common Lisp is (often) compiled.

## Lisp - The Bad Parts
- no syntax
- everything looks like a function call or an atom
- tree structured
- no types
- dynamic

## Automation and Generating Code
There is a chasm between *human* readability and *machine* readability.

*Human* readable languages tend to resist automation, e.g. they contain too much syntax and special cases and left-out details.

*Machine* readable languages:
- are regular (normalized)
- are very, very repetitive
- usually look horrible to *human* readers
- contain a lot of detail, much of which gets in the way of understandability by *humans*.

Note that macros came from early lisps, before lisp was converted into a compiler-appeasement language.  This is no accident.  It was natural to bolt normalized functions together, so it was done - without thinking nor planning - and it was automated to gift us the concept of "macros".  A different form of macros came from line-oriented assemblers.  The units of bolt-ability were small and automatable - trees in one case, lines in the other.  The units of bolt-ability were normalized - everything returns a value in one case, everything affects the global state of the machine in the other - no edge cases to worry about.  As an example of non-boltability, imagine JavaScript.  It is *almost* a lisp, but it has too much pesky syntax - *human* readability appeasement - to be naturally boltable (you *can* generate and bolt JS code together, but, you aren't naturally drawn to the idea).  Other languages are even worse in this regard, e.g. Python's syntax screams out "edge case"s.  Note that Haskell has 2 syntaxes - one for type programming and one for Production Engineering.  Note that every language is just a honking big macro preprocessor for Assembler.  Note that Assembler is just an API for building programs using transistors.  (Well, and, transistors are just an API for dealing with Chemistry and Electronics, and, and, and, ...)
