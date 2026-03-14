# 2023-02-05-AI Driven Compilation
Compilation is - conceptually - a simple process.

We start out with two things and the "compiler" fills in the rest:

1. A generalized machine consisting of ad-hoc electronics that presents a simple-to-use API, called *opcodes*, of blocks of operations that the machine can perform when presented with a specific code / instruction to do so.
2. A blob of bits that represents a sequence of *opcodes* that - when taken in sequence - cause the generalized machine to perform a sequence of tasks that we - humans - find useful.

A *compiler* is simply an application that maps a blueprint into a blob of bits that can be executed by the generalized machine.

A *compiler* is an application that is used by *software developers* to create *software products* that can be used by end-users - who are, generally, not programmers and want the generalized machine to help them perform tasks that they find useful and too boring to do themselves, like calculating their taxes and filling out their tax forms.

Developers, themselves, find the task of building compilers to be boring - and dauntingly large and repetitive - and leave the task of building *compilers* to a select few developers-for-developers, called "compiler writers", "language designers" and "systems people".

Can AI be used to build *compilers*, or, parts of *compilers*, and automate the rote work of developers-for-developers?

Currently we use blueprints that are but cave-paintings of fixed-shape glyphs - called *characters* - on grids using tools called *programming editors*.

There is nothing - other than rote work - standing in the way of using more elaborate kinds of blueprints, say drawings of rectangles, ellipses, arrows and text.  There is nothing to say that the figures used in such blueprints need to be arranged on grids - the figures could overlap and be resizable.  In fact, SVG already suggests such an arrangement of figures.  SVG, though, has mostly been used to create elaborate artistic drawings instead of forming that basis of programming languages.

We already know how to build compilers in several stages, e.g.
1. scanner
2. parser
3. semantic information gathering
4. semantic checking
5. allocation
6. coding.

Can we teach these kinds of divide-and-conquer task break-downs to AI?  Do we need to come up with a plethora of training examples for each stage, or, can we speed up the training by telling our AI tools to chunk - layer - its work in certain ways?

Suggestion: AI does the rote, repetitive work, while we - creative humans - give suggestions to the AI tools on how to approach the problems.