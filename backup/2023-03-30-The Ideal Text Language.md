# 2023-03-30-The Ideal Text LanguageThe ideal *text* *based* language is:

*all* text-based languages.

One language can't solve all problems conveniently.  The ideal is to be allowed to choose any lanuage to solve a problem.  The ideal is to use multiple text-based languages for any one complete solution.

# How?
So, how can you use more than one language in a solution?  I see at least two ways...

## Verbatim
PEG parsing technology - epotimized by Ohm-JS - allows parsing matched sets of brackets.

With matched brackets - and Unicode
- it is possible to compose grammars 
- it is possible include bits of unparseable text, recursively


For example, one can create a mini-syntax and embed snippets of Python (or Rust, or whatever) into it.

My current suggestion is to use the Unicode brackets `«` and `»` to surround bits of *verbatim* code.  Verbatim code does not need to be parsed and is emitted "as is" to the output.  Verbatim code can contain other bits of verbatim code, so the act of creating verbatim code can be done in small, simple stages, like un-peeling an onion.

A meaningless example can be found in https://github.com/guitarvydas/verbatim and uses a test file that looks like:
```
const src = String.raw`
a b 
«
  {
    run : function () {
      «var h = 'hello';»
        «
          var w = 'world';
        »
          «return (h + ' ' + w);»
    }
  }
»
c d
`;
const src_42 = String.raw`«42»`;
const src_nothing = String.raw`42`;

```

## Recursive Text - Projectional Editing

Another option is to use some base syntax that can be expanded (groked and fabricated) into any existing language.

IMO, such a base syntax would need the following features:
- almost no syntax
	- brackets and characters
- recursive - allows nesting of constructs.

Such a syntax already exists. It is called *Lisp*.

In pure Lisp, there are only three kinds of things:
1. Lists
2. Atoms
3. Separators (spaces, newlines, tabs, etc.).

The "problem" with Lisp syntax is that it is intimately tied with a single interpretation (meaning) of what can be contained inside the brackets.  In a Lisp program, every list represents a *function*, where the first item in the list is a function name[^anon] and the rest of the items are parameters to the function.

The above "problem" can be alleviated by simply simplifying and segregating Lisp syntax from Lisp program meaning.  I call this *recursive text*.  It consists of 
1. bracket characters, 
2. printable characters,
3. separators (non-printable characters).

Nuances include some way to bracket-quote strings of characters that include separators.  Again, PEG thinking allows us to break away from the accepted standard, used by ASCII-based languages, wherein the same character is used to denote the beginning and the end of a string, whilst disallowing the concept of nested strings.  At this moment, I use square brackets `[...]` to write strings that contain non-printables, but, this decision might change as I refine the concept further.

[^anon]: Aside: if the first item in a list is a list instead of a function name, that list is assumed to be an anonymous function (usually signified by the keyword *lambda*)

# Why Use Anything But Text?  What Can't Text Express?

Text is great for expressing equations and grade-school mathematics, in a function-based manner.

This representation arose from the use of clay tablets and written language.  We can do better than this, now, using advanced electronic machines (often called "computers").

Text is less great for expressing non-functional details, such as daemons and multi-port software components i.e. components that have more than one input and/or more than one output, including zero inputs or zero outputs.

Everyone knows how to write such multi-port, non-functional components, e.g. by using drawings on whiteboards, napkins, etc.  

For example, a *rectangle* might represent a software component and *arrows* might be used to represent data flows between components.  The key here is to stop thinking that software components having exactly one input and exactly one output [^2] and to allow drawings of components with multiple inputs and outputs.  The other key is to stop thinking that every dataflow opertion will "return" a result.  Dataflows are, fundamentally, one-way operations that may, or may not, produce results and other data flows.  Each dataflow event might cause zero, one or more events.

[^2]: Functional syntax allows for two outputs, using the epicyclic concept of *exceptions*.  The idea of treating everything that isn't on the happy path as an exception is a mind-locking concept that prevents developers from writing code to - conveniently - handle software intended to run on the internet, robotics, IoT, blokchain, etc.

# What Concepts Need to be added to our Fundamental Concepts of Programming Languages?
- containment ("inside", nesting)
- touching
- intersection
- connected

All of the above concepts can be easily coded up using only grade-school mathematics.


# How Can We Use Existing Parsing Tools?
Note that the use of PEG-based parsing technologies, and, nesting, makes these concepts imaginable and simple to implement.

We need to convert diagrams to text, then to apply existing text-based parsing tools.

I favour using:
- Ohm-JS
- Excalidraw
- draw.io
- SVG