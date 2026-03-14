# 2023-06-19-Sector Lisp Synopsis
Yes, I think that BLC is the next step after Sector Lisp.

No, I haven’t truly understood BLC yet.  I did truly understand Sector Lisp by implementing it in Python.

On the surface, it looks like Sector Lisp and BLC are amazing assembler tricks, but, I think that there is something deeper going on.  Lua is 24x the size of Sector Lisp and Lua is considered to be small.  You don’t get a size difference like that using only assembler tricks.

From my perspective, Sector Lisp is purer-than-pure Functional Programming.  It contains no facilities for mutation (assignment).  I think that *that* is the secret.  The Sector Lisp GC (garbage collector) is only 40 bytes long.  It works because it can make assumptions about the arrangement of data (stack-based only, no random access to locations, no “mutation”).  There is no bloat due to concerns for random access to variables.  No edge-cases to worry about.

As for doing something powerful and real with Sector Lisp, it depends on your perspective.  I believe that *syntax* is the way to provide for control flow in languages.  Sector Lisp has just about no syntax and is pure Functional Programming.  My take is that Sector Lisp forms the basis for data, while *syntax*, e.g. using Ohm-JS, forms the basis for control flow.  Combine the two and you get power and simplicity.

The current crop of programming languages use some syntax for control flow, but, they also allow the mis-use of mutable variables and the mis-use of COND (conditional function values) for some control flow.  This is bad.  It's so low-level that compilers can't check for stupid mistakes, and, the overall architecture of a program is very hard to discern.  You have to play "air computer" to simulate `if-then-else` based control flows to understand what was intended.

So, if you want to save a resulting value in a mutable variable, you call a pure-pure lambda (e.g. Sector Lisp or BLC) to calculate the value, then you wrap a tiny bit of syntax around the call that *save*s the result.  Similar to a SAVE button on a cheap calculator.  Conditionals in the pure-pure functional code must not leak back into the control flow code.  They are completely orthogonal and kept separated from one another.

Cordy's Orthogonal Code Generator research worked like that.  It compiled the control-flow-y stuff in the first pass, then compiled the operand-y stuff in the second pass.  That's what was meant by *orthogonal*.  Operands were dealt with separately from control-flow-y sequential stepping of opcodes.

How do you do this today?  Use OOP to describe and evaluate *operands*.  Use Ohm-JS, or PEG, or whatever, to create control-flow-y syntax that moves *operands* around.  For example, let's say that you want to use Python.  Use Python's classes and Python's conditional evaluation to deal with data as *operands*.  Then use syntax to generate Python mutation code - local variables, assignment, etc. - which gets combined with the *operands* and forms a combined final executable program.

Writing control-flow-y code as diagrams becomes trivial with this approach.  Or, writing control-flow-y code as text is equally acceptable.

I might even have a repo with code that experiments with doing something like this.  I need to sleep on it to try to remember what those repos might be, though...

A lot of programming languages get real close to this kind of ideal.  The supply classes and methods for dealing with data as *operands*.  These languages supply various kinds of mutation (but try to claim that they don't believe in mutation).  Then, they allow the concepts to leak into one another which leads to edge-cases and bloatware.

I think that 0D - the full isolation of components from one another using simple constructs like queues (FIFOs instead of LIFOs) - makes it easier to draw rigid lines between control-flow-y code and operand-y code.  Imagine my favourite syntax - diagrams - where you only have boxes with ports and arrows.  The boxes are the control-flow-y part and the data flowing on the arrows is the operand-y stuff.  

Do you want type-checking?  Just create a set of boxes that do type checking (aka "input validation") and plug them into the sequence.  Each box has two outputs
1. the data if it passes the type check
2. an error if the data does not pass the check.
Boxes are not constrained to *always* produce output data when given input data.  Downstream boxes don't even wake up when a type error occurs.  Downstream boxes deal only with inputs. When they don't get an input, they don't do anything.  If *any* type-check box in the pipeline detects non-passing data, the type-checking box does not produce data on its data port (and, downstream boxes don't even wake up).  Instead, a type-checker box that detects a non-pass condition, simply outputs an error object on a different port.  This is a lot like *exceptions* in functional syntax, but the Architect gets to define how the error object control flow is wired up, instead of relying on the compiler implementor to build that control-flow into the language.

When you think this way, new possibilities open up.  Type-checking begins to look quite meagre.  It becomes possible to create design-rule-checking-boxes instead of just type-checking boxes.  It becomes possible to create checking-boxes that are tuned for the problem instead of being pre-tuned to whatever the language designer thought was important at the time.

The secret is: you need 2 syntaxes.
1. A syntax for classes and methods.
2. Another syntax for control flow.

Most General Purpose Languages (like Python, Rust, etc.) conflate the two concepts resulting in making code harder to write than is necessary.

I feel like I've said it all, but, it wouldn't surprise me if all of the above sounds airy-fairy and doesn't appear to connect the dots.  I need to "sleep on it" some more to think of examples that appear to be more concrete.

Back to Sector Lisp: I think of Sector Lisp as the syntax for describing data and operands.  I think of Ohm-JS as the syntax tool for inventing new control-flow-y syntaxes.  I think that given these two elements, you should be able to slap together new languages in a few hours, not days/weeks/months/years.  This approach, though, does require one to stop believing in "one language to rule them all".  There are at least two languages.  General Purpose Languages are too general and become watered down with concessions and trade-offs in an attempt to conflate two completely orthogonal concepts into a single syntax.