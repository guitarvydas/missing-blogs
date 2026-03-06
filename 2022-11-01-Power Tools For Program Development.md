# 2022-11-01-Power Tools For Program Development
# Basics
The Machine - the Computer - doesn't care if a program is "correct".

The Machine simply executes opcodes given to it by developers.

Making a program "correct" is purely the responsibility of developers.

We have created various power tools to help developers create "correct" programs.  "Correct" from their perspective.

We continue to research better ways to speed up the development process.

# Basic, Everyday Tools

## Banks of Switches
## Assembler
- textual mnemonics representing each opcode and possible operands for the opcodes
- opcode = basic command
- operand = parameterization of basic commands
- it possible to treat opcodes and operands orthogonally
## Textual Programming Languages
### C
### Lisp
### Algol, Pascal, etc.
## Syntax Checking
## Type Checking
## Debuggers
## Development Systems - Hardware and IDEs
Developers often use souped-up computers and operating systems that are orders of magnitude more expensive than the computers and operating systems needed by Users using computerized products
## Compilers
## Interpreters
## REPLs
## Operating Systems
### Preemption
### Gotchas
### Single CPU Paradigm
- 1950s biases
## Existing Operating Systems
### Windows
- for Users
### MacOS
- for Users
### Linux
- schizophrenic
- began as "for Developers"
- some distros[^distro] evolved into "for Server Developers"
- some distros evolved into "for Users"
- some distros evolved into "for App Developers"
- some distros devolved into "for nobody, yet"
	- e.g. Ubuntu comes with almost nothing built-in

[^distro]: "Distro" means "distribution".  A "distribution" is a packaging of Linux created by a group of Linux developers.  Examples of "distros" are: Redhat, Debian, Ubuntu, etc.
### Thread Libraries
- *assembler* for a new set of opcodes representing distributed operations

## Paradigms
### Structured Programming
### OOP
### Functional
- enclosures, wrappers
- Word Search-and-Replace rules
- Lambda == wrapper
- textual wrappers -> global variable problem
### Relational
- declarative programming using Relations
#### PROLOG
- uses backtracking to implement engine that executes declarative rules
	- see, also, backtracking in PEG/Ohm-JS
- SWIPL
- Nils Holm "PROLOG Control in 6 Slides"
#### miniKanren
- core.logic (clojure)
#### visual
## Declarative
### HTML
- led to XML
	- XML is too complicated, too generalized
## Independent or Synchronous?
- independent (asynchronous) is "easier" for developers
	- "build and forget"
- synchronous is "easier" for analysis
	- "clockwork"
	- brittle programs 
		- everything must work simultaneously
		- any failure implies total failure
			- fail-fast is "good" for development, "bad" for production
		- full synchrony and fail-fast is opposite of "build and forget"
## Iterative Design
## Code Generation
- /bin/bash
### Actors
### Spreadsheets
### Hypercard
# Emerging Tools
## VPLs - Visual Programming Languages
- the COBOL of diagrammatic programming.
- attempt to incorporate a very rich subset of Visual Phrases that are above and beyond the very minimum set of Visual Phrases needed at a rudimentary level
### Prograph
### Scratch
### LabVIEW
- diagrams are too busy, too complicated
## Node and Wire Diagrams
## PEG Parsing
### Ohm-JS

# Strategy
- paradigms
# Tactics
- syntax draped over paradigms
# Correctness
- What is "correct"?
- mapping from programmers' intent to a set of opcodes
- mapping from Users' desires to programmers' intent
# Testing
## Q/A
## White Box Testing
## Black Box Testing
# Workflow
1. Architecture
	- requirements gathering
2. Engineering
3. Implementation
	- programming
	- optimization
4. Deployment
5. Maintenance