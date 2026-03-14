# 2022-08-13-Wheel Reinvention Snappable Software Components- decoupling
	- decoupled outputs
		- alist for outputs (reversed to make FIFO)
	- decoupled inputs
		- more than one input parameter in time dimension
		- current functions implement parameter list as a single block of data that is destructured, but, all data arrives at the same time in the same block
	- no hard-wired names in code (must not call functions directly)
	- remove blocking mode from components (functions block when waiting for callee)
- HSM dsl
- components with internal concurrency
	- run pure functions as single steps
```
		Loop:
			call continuationCheck λ
			branch on stop to EndLoop
			call step function λ
			branch Loop
		EndLoop:
```
- 0D
	- zero dependencies between components
	- dispatcher has total control over blocking w/o preemption
- SVG tech diagrams
	- containment
	- source/target
	- draw 2-box diagram with 2 wires in draw.io, parse with Ohm-JS
- anti-Bloatware
	- study Sector Lisp - why is it so small? (must be more than assembler parlour-tricks)

- Sector Lisp is pure FP, but, uses LIFOs as the communication medium
- UNIX pipes use FIFOs as the communication medium

Objective:
Marry Sector Lisp and UNIX pipes.

Probable Method:
1. Lift Sector Lisp into Ohm-JS and generate C, JS (again) and Python
2. Jigger the syntax to support inter-component FIFO-based communication
	- I think that this means inventing 2 classes of components:
		1. Leaf
		2. Container / Layer

Leaves are HSMs (Hierarchical State Machines) that contain code.  This is what we commonly call a "program".

Containers are recursive routers that implement structured message passing.

# Collaborators
Yes, please.

Must be willing to ignore modern-programming-based biases, e.g. bad ideas like "implemented in XXX" (where XXX is any modern programming language, like Rust, Python, C++, etc.)

# Structured Message Passing
Messages must travel *only* in the vertical dimension, i.e.
- "down" from Container to child component
- "up" from child component to Container.

Messages cannot be sent sideways to peer components.  Message routing is only handled by Containers.

# Example
old style, LIFO-based:
```
(DEFINE HELLOWORLD .
  (LAMBDA ()
    (HELLO)
    (WORLD)))

(DEFINE HELLO .
  (LAMBDA ()
    (PRINT (QUOTE HELLO))))

(DEFINE WORLD .
  (LAMBDA ()
    (PRINT (QUOTE WORLD))))
```
new style, FIFO-based:
```
(DEFLEAF HELLO .
  (SEND (QUOTE OUT) (QUOTE HELLO)))

(DEFLEAF WORLD .
  (SEND (QUOTE OUT) (QUOTE WORLD)))

(DEFCONTAINER HELLOWORLD .
  (CONTAIN (HELLO WORLD))
  (ROUTE ((HELLO OUT) ((SELF OUT)
		       (WORLD IN)))
	 ((WORLD OUT) (SELF OUT)))
 
```

# Steps
1. clone jart's sectorlisp `git clone git@github.com:jart/sectorlisp.git`
2. checkout `friendly` branch
3. create HTML that runs lisp.js in a browser
4. use [Ohm-JS](https://ohmjs.org/) and [Ohm-Editor](https://ohmjs.org/editor/) to create a parser and code generator for sector lisp that generates the same javascript as in lisp.js
5. hack on step (4) to produce FIFO-style output