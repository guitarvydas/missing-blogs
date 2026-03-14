# 2022-06-29-BRS Towards A Syntax For Technical Diagrams Of Software
[aside: BRS means "brainstorming", something like maybe a Working Paper]

Step 1:
Draw technical diagrams of a simple program script.

Step 2: 
Transpile the diagrams to structured text form, so that they can be processed using existing tools.

Step 3:
Use Ohm-JS to transpile the structured text to Python (or whatever).

...

Step NN:
Transpile the diagrams from draw.io to JSON using das2py technology.

Step NN+1:
Transpile the generated JSON to .tbx (toolbox) format.

Step NN+2
Use Step 3 to transpile the .tbx files to Python (or whatever).


0D (zero-dependency) components can be described in .tbx format using Orthogonal Programming language ideas...

The OPL principles are:
- conquer and divide work into two camps
	- operands
	- operators.

Of course, *operands* and *operators* can, each, be divided-and-conquered some more...

# Operands
## Atomic Operands
❲...❳ - id
ė❲...❳ - function
č❲...❳ - procedure (:proc)
ą❲...❳ - state (:state)
◦❲...❳ - output port (:oport)
➢❲...❳ - input port (:iport)
≈❲...❳ - component prototype (:proto)
ž❲...❳ - child component name (:child)
š - self component
{ ... } - list / box
➢y❲...❳ - inherited input port
◦y❲...❳ - inherited output port
⟪` ... `⟫ - verbatim procedure - blocking
⟪` ... `⟫? - verbatim function - blocking, must return an atomic operand
"..." - string constant
'...' - string constant
◇❲...❳ - string constant name
ū❲...❳ - net name
[0-9]+ - numeric constant
𝜏❲temporary synonym❳ :temp❲temporary synonym❳


## Compound Operands
`{ š ➢❲...❳ }` - sender: self input
`{ ž❲...❳ ◦❲...❳ }` - sender: child component output
`{ š ◦❲...❳ }` - receiver: self output
`{ ž❲...❳ ➢❲...❳ }` - receiver: child component input
`{ ` *r* ` }` - list of receivers, where *r* is a receiver
`{ ` *s* *lr*  ` }` - connection, where *s* is a sender and *lr* is a list of receivers
`{` ...+ `}` - code block, where ... is one or more atomic operand(s)

# Operations
There seems to be only 2 kinds of operations:
- define
- send

## Operation Phrases
*Operations* are like Assembler opcodes, but with a richer syntax (possible using PEG, TDPL, Ohm-JS, etc. and segregating *operands* into their own cubby-hole)...

- define
	- define container
	- define leaf
	- define connection 
	- define state machine
	- define signature
	- define container implementation
	- define leaf implementation
	- define synonym
- send
	- send: non-blocking input to blocking box
	- send: blocking box to non-blocking output
	- send: non-blocking input to non-blocking input port
	- send: non-blocking output to non-blocking input
	- send: non-blocking output to non-blocking output
	- send: nb inherited input to nb inherited socket
	- send: nb inherited output to nb inherited socket
	- send: constant initializer to non-blocking input
	- send: constant initializer to non-blocking output
	- send: constant initializer to blocking input

Note: The Big Win technologies, like Relational Languages, describe *what* and leave the *how* to the underlying engine(s).  In this case, we can use Ohm-JS to transpile *operations*+*operands* into some existing programming language (I'm using Python for now.  I used JavaScript and Common Lisp in the past.  I believe that it should be easy to transpile to other languages, like Rust and WASM, but, there is little to be gained in doing so.  Most other languages, like Rust, use syntax that appeals to humans and less-so to machines.  They end up doing the same work under-the-hood.

## Details of Operation Phrases
- define
	- define container
		- `container *name* { ... }``
	- define leaf
		- `leaf *name* { ... }``
	- define connection 
		- `{ *sender* ⤇ { *receiver* } }`
	- define state machine
		- `machine ❲...❳ { ... }`
		- define transition
			- `on` *p* *c* - where *p* is a source port, and *c* is a code block
		- define state
			- `state ❲...❳ { ... }`
		- define start state
			- `start ❲...❳`
	- define signature
	- define container implementation
		- `container ž❲` ... `❳ {`
	- define leaf implementation
	- define procedure
		- `proc č`...` {` ... `}`
	- define function
	
- send
	- send: non-blocking input to blocking box
	- send: blocking box to non-blocking output
	- send: non-blocking input to non-blocking input port
	- send: non-blocking output to non-blocking input
	- send: non-blocking output to non-blocking output
	- send: nb inherited input to nb inherited socket
	- send: nb inherited output to nb inherited socket
	- send: string constant initializer to non-blocking input
	- send: string constant initializer to non-blocking output
	- send: string constant initializer to blocking input

# Goals
## No Overloading
Every operator and every operand kind gets a unique syntax.
## Machine Readable
Favour machine readability over human readability, regardless of apparent clumsiness.

If human-readability is required, create an SCN layer that maps human-readable syntax to machine-readable syntax.