# 2022-09-20-Bloatware Caused By Type-Checking
# Overview
This is an informal discussion.  I don't propose solutions, but, hope that the discussion might trigger creation of solutions by others.

I argue that bloatware is caused by compiler-appeasement languages which cause programmers to (manually) worry about types.

# Simplistic Example
## Bloated Version
```

float add2if (int a, float f) {
  ...
}

float add2ii (int a, int f) {
  ...
}

float add2ff (float a, float f) {
  ...
}

float add2fi (float a, int f) {
  ...
}


void main_bloated () {
  int a;
  float f;
  float result;
  result = add2if (a, f);
}

```
Programmers use programming language syntaxes ("static languages") that cause them to unroll - manually - descriptions of their programs.

## Less-Bloated Version
```
normalized add2normalized (normalized a, normalized f) {
  ...
}

void main_not_bloated () {
  normalized a;
  normalized f;
  normalized result;
  result = add2normalized (a, f);
}
```

Programmers use programming language syntaxes ("dynamic languages") that allow code to be written without specializing on types.

Type checking performed at lowest levels.

Type errors at low levels might not "relate" to higher-level code
- e.g. if "f" is a String, we might see an error "not an int nor a float", which isn't informative enough for  debugging the higher-level code.

# Successful Normalization
- UNIX File Descriptors (FDs)
	- normalized access to all files & devices
- The SELF programming language
	- determine un-normalizing (unrolling) at runtime, not compile-time
	- unrolling done on-the-fly
		- "JIT" Just In Time
- Concurrency via Message Passing -> normalized inter-process communication (simple)
- Sector Lisp
	- successfully small
	- one reason is that there are only 2 types
	- very little code is needed to check types 
		- "type checking" is but a binary decision 1/0 (List/Atom)

- FORTH
	- aka Postscript
		- helped Apple corner the desktop-publishing market
- "Dynamic Languages"
	- REPLs were invented in pre-CL Lisp
	- macros were invented in pre-CL Lisp
	- garbage collection was invented in pre-CL Lisp
	- stacks (LIFOs) were invented in pre-CL Lisp (McCarthy's alists)
- Spreadsheets
- HyperCard
- Assembler

# Unsuccessful Normalization
- USB : appears "complicated" because it is a union of possibilities instead of a normalization (reduction of possibilities)
- Concurrency via locking -> specialized, not normalized, per use-case (difficult, too much nuance)
- APIs
	- supposed to be a reduction of possibilities
    - simplicity thwarted by gradual addition of parameters
	    - resulting in too much "complication"
	    - too much "nuance"
		    - simplicity ≣ lack of nuance
		    - too many details to remember
		    - too many details to deal with
			    - elide details, don't delete delete details
- **TBD** *if-then-else* done in Racket (vs. in pre-CL Lisp)
- "Static Languages"
	- SICP mentality leads to bloatware

# Type Checking
- checking for combination of types must be done, but, where to put it?
- normalized ("dynamic") variables allow most code to be small
	- dynamic languages push unrolling/checking down to lowest levels
- specialized ("static") variables are handled in every function, pervasively

# State Explosion Problem
- State Explosion is the main reason why people avoid state machines
- State Explosion is caused by lack of encapsulation 
	- deal with all possiblilities in a "flat" manner instead of in a "layered" manner
	- adding a possibility causes number of states to multiply
	- too many states quickly explodes into unmanageable code
	- **TBD** *example from Harel paper ... **
	
- YACC handled the State Explosion Problem by elision
	- YACC creates State Machines, but hides this detail from programmers
- Harel's StateCharts encapsulate state explosion problem
	- feature of StateCharts is top-down overriding
		- not bottom-up (like inheritance, where children methods can override parent methods)
	
- sync code experiences the state explosion problem
- strong type-checking experiences the state explosion problem
	- lots of types leads to lots of possible states


# What Does This Suggest? 
- check types only at low levels
	- macros devolve all code to sequences of low-level operations
		- Lispers understand "macro mentality"
		- OTOH, compiler writers / language designers build full-blown compilers instead of macros
	- Ohm-JS => macros for the rest of us
- text-based languages 
	- grids of non-overlapping bitmap cells, sync left-to-right & top-to-bottom
	- working outside of this box - non-sync, overlapping, etc. - requires epicycles (aka workkarounds)

- type stacks - progressive type checking
	- allow higher-level code to be written generically using normalized types
	- express types incrementally, in layers
	
- check types only in development code
	- eschew type unrolling in production code
	
- divide type checking away from higher-level coding
	- OPL - Orthogonal Programming Languages
		- express all operands in a normalized format
		- e.g. Objects with only one way to operate on them
			- e.g. operators = functions (only), no extra syntax, like `+`
		- Objects check whether operations can be applied
		- Objects unroll type info and contain/encapsulate bloated code
