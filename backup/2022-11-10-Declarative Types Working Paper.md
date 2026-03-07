# 2022-11-10-Declarative Types Working PaperA Declarative Type is a type that has named fields, but, the implementation is not specified, e.g. a *dtype* cannot be defined in terms of Classes, Lists, Arrays, Floats, etc.

Declarative types are not new and are seen in:

- handles in Operating Systems (e.g. Windows handles)
- PROLOG functors
- types in S/SL
- interfaces (?)

## Syntax of DTypes

I suggest the use of Unicode brackets `⟨...⟩`.

The brackets contain a list of names, whitespace separated, i.e. commas are not used.  Commas are whitespace.

The first name is the name of the *dtype*, which distinguishes a *dtype* from all other *dtypes*.

The rest of the names are names of fields of the *dtype*.

A field is specified only by its name - no other details are supplied.

## Declaration
`dtype ⟨Dest target port message⟩`

(where the names "Dest", "target", "port" and "message" are but examples).

### Inheritance
Can a *dtype* inherit from another *dtype*?

Suggested syntax for declaration of dtype using inheritance:

```
dtype ⟨Other x y⟩
dtype ⟨Dest target ⟨Other⟩ port message⟩
```

Inheritance consists of simple pasting the field names from the parent into the *dtype* being defined.

Field ordering cannot matter.  

Existence of field names is the only aspect that can be specified.


## Usage
`⟨Dest target port message⟩`

where "Dest" is the name of the dtype and "target", "port" and "message" are expressions that evaluate to values for the corresponding fields.

## Symbols
Since the fields of a dtype are opaque - names only - the fields can act as symbols.

What is the syntax for this kind of usage?
- Maybe hashtags from Twitter and Markdown can provide inspiration?
- need to know: the basic *dtype* and the specific field name
- or, is a *dtype* that only contains symbols a different kind of animal?
	- where a field name used as a symbol guarantees that it has no implementation
	- or, do we have a syntax like assembler's Effective Address and C's `&` for using field names as symbols?
- What operations are allowed on symbols? Case (equality)
---

# Comments and Observations
- PROLOG is declarative - Code is specified in a declarative fashion, but, the PROLOG engine determines implementation(s)
	- PROLOG uses *backtracking* to implement declarative code
	- Ohm-JS & PEG use *backtracking* to implement declarative code
	- miniKanren uses a different technique (I think of it as *feed-foward*) to implement the same kinds of things - declarativity
- S/SL opaque types
	- I consider opaque types to be one of the "hidden gems" of S/SL (Syntax/Semantic Language, Holt, et al) 
	- what is really going on is: S/SL allows you to specify the *existence* of a type, but not its details
		- the implementation details - e.g. is this an *int*?, a *float*?, an *array*?, a *sub-class*?, etc. are provided in the underlying implementation language (e.g. C, Pascal, etc.), but, are not specified in the S/SL code
- DI
	- DI - Design Intent - is the idea of writing code purely for human readers
		- DI code expresses only the *intentions* of the designer (Architect, Engineer), but, not the details
	- in the Construction industry, DI comes in the form of *blueprints* - Architects and Engineers devise solutions to problems and encode their ideas in technical drawings (call *blueprints*).  Construction workers know what to do with *blueprints* and how to read them (they've been trained).
- Production Engineering
	- Production Engineering is the idea of *optimizing* code along some dimension, e.g. speed, size, etc.
	- conflating Production Engineering and DI makes it more difficult to get a design correct while juggling its implementation details
		- mature disciplines, like Structural Engineering, separate Engineering from Construction
		- (in fact, further separation is, also, used: Architecture is separated from Engineering and both are separated from Construction ; Architecture is like "requirements gathering", Engineering is like "thinking about the details to make an MVP" and Construction is like "coding, optimizing, testing, deployment, CI/CD")
	- reverse engineering
		- Production Engineered code is more difficult to understand, understanding it requires Reverse Engineering
		- Production Engineered code is, generally, not scalable - trees are scalable, graphs are not scalable
			- by "scalable" I mean "can I take an arbitrary node in the tree and move it elsewhere without dragging a bunch of other nodes along with it?"
			- example: imagine cutting the source code for *printf* out of a C compiler and using it in a different app - do I need to drag a bunch of other source code along with the *printf* source to make it work elsewhere?  Our - very common - CALL/RETURN (function-calling, call-stack) protocol inserts hidden dependencies into the code, making the code unscalable at the function level ; UNIX pipelines broke this indoctrinated protocol by using Queues instead of the Call-Stack for pipes between pipe-able commands (leaving Call-Stack-based functions for the implementation of the internals of such commands)
	- existing languages, GPLs
		- General Purpose Languages emphasize generality
		- as such, GPLs tend to conflate Production Engineering and DI
			- usually, GPLs, being a *union* of features, tend to address neither Production Engineering nor DI very well (you can't do both at once, in general)
				- the result is usually a bland combination of ad-hoc language features that address only the biases of the language designer(s) (currently in vogue: optimizing for speed at the expense of expressing DI and at the expense of size (-> bloatware))