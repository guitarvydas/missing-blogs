# 2023-03-05-Else is a Bad IdeaOver-classification of languages is an insidious form of premature optimization.

Language theorists wasted huge amounts of time solving the "dangling else" problem.

The presumption was/is that "else" is a valid programming language feature, and, therefore needs to be formalized.

In my view, this is a "can't see the forest for the trees" kind of problem.  The real issue, IMO, is that "else" is a bad idea and should not be allowed in language design.  Figuring out how to parse "else" is a red herring. If you disallow "else", you don't need to bother figuring out to parse it.

The point of language design is to help programmers catch problems sooner.  End-users only care if the product you sold them works in a robust manner.  They don't care if you used assembler or a theorem prover to create the robust product.  

It's all assembler in the end.

Syntax errors are one kind of helper for programmers.  

Type checking is another kind of helper for programmers.

Getting rid of "else" would be yet another kind of helper for programmers.  "Else" allows ad-hoc code design.  "Else" allows ad-hoc use of State.  Programmers are allowed to get away with murder, usually resulting shooting of their own feet. "I don't want to be bothered to think about these other possibilities, so I'll just lump them all into the same bag using Else".  Forcing programmers to explicitly address every possibility is the basic tennet of Type Checking.  "Else" allows programmers to do an end-run around this basic tennet when describing control flow.  

This often leads to erroneous conclusions such as "State is bad", and "eschew Control flow".

## The State Explosion Problem
So, if you get rid of "else" don't you run into the State Explosion problem?  There are just too many possibilities to list them all, so using "else" as a catch-all seems like a good idea.

Yes.

This is yet another "can't see the forest for the trees" issue.

The issue is scalabiity.  How do you deal with systems that are "big"?

One solution is to lay out all of the possibities flat on an infinite canvas.  Soon, you encounter the State Explosion problem and begin to fret about how to create epicycles that allow you to continue down this path.

Another solution to scalability is to follow the "Rule of 7".  No code component can have more than 7+-2 lines of code in it and every code component is entirely self-contained and doesn't leak information implicitly.  

No layer in a system can have more than 7+-2 elements in it.

When you try to grok a system, you are never forced to understand more than 7 things at a time.  If you want more detail, you dig down into other layers, each of which can have no more than 7 things in them, each.

My suggestion is to build software using components.  Each component has a set of very-well-defined inputs *and* a set of very-well-defined outputs.

Early BASIC programs were like this - each program had only a few lines of code in it.  Every program was understandable.  

There was no "global variable problem".  The "global variable problem" was created by using an infinite canvas mentality for scalability (and, I would argue, by using text uber diagrams).

Can you follow the Rule of 7 and still build "big" systems?  

Yes.

Create abstractions in the form of code islands.

Early programming languages gave us "functions".  Functions worked OK as abstractions as long as each function had only 7+-2 lines of code in it AND as long as there were only 7+-2 functions in a system.  Function-based syntax doesn't enforce the Rule of 7.  Functions can contain only 7 lines of code, or, they might contain more.  A text file containing functions might contain only 7 functions, but, it might contain more.  Functions might depend on other functions, so you have to count the lines in those other functions when counting lines for the Rule of 7.

Good programmers arrange things this way by instinct.  Most programmers don't.

LabView draws diagrams of code, but doesn't enforce the Rule of 7.  Diagrams can be arbitrarily complex.  Components on diagrams can leak information into other components.

Most programing laguages don't make it easy to follow the Rule of 7.  OOP makes it even worse with the concept of overriding methods.  You can't look at an uber-class and guarantee that you know what it does without looking to see if any of its children override a method.

Push necessary details down onto their own islands.  Don't get rid of details, just elide them.  Express details in layers.  A lower-level layer must not be allowed to change the meaning of what its parent (or other descedants) do.  Parental Authority, not over-riding. 

