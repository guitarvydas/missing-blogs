# 2023-08-16-Structured State## Demo

code repository: https://github.com/guitarvydas/kartik

The above is a demo of how to solve problems using DW (Drawware, diagrams + 0D) and State Machines and how to go about testing this kind of stuff in small pieces working your way up.  

Thankfully, the proposed State Machine is simple enough to be coded in hand-written Odin.  There is no technical issue preventing the use of draw.io or Excalidraw for drawing State Machines expressed as diagrams that devolve to XML, but, this hasn't been written in Odin yet. (Or CL, or Python, or JS, or ... (It once existed written in C without XML, sigh)).  

## Aha! States, Transitions, State Machines
The "aha!" is:
- A State is a unit of control-flow that contains 3 functions (enter, exit, body)
- A Transition is another unit of control-flow that contains 1 function.  
- A State Machine is a but collection of:
	- States
	- Transitions
	- some unexported data.

A State Machine invokes the State and Transition functions at the correct time(s).  

The unexported data can only be accessed by the functions in the States and Transistions within the same closure.
## HSM - Hierarchical State Machine

An HSM - also known as a StateChart without orthogonal behaviour -  enforces "parental authority".  

Parental Authority is like Inheritance, except, if an enclosing parent is exited, all children States are exited without being given a choice or the chance to override the parent's behaviour.

In an HSM, a State can contain other States, i.e. an enclosing State is actually an HSM. 

In other words, an HSM is but a collection of:
	- States
	- Transitions
	- some unexported data
	- other HSMs
	- 2 Functions and 1 Behaviour (enter, exit, body, resp.)
## Structured State vs. Ad-hoc State
A State Machine is "structured state", whereas "if-then-else plus variables" is "ad-hoc state".

## Research Question:
Observation: HSMs and Components are *very* similar in structure.

HSMs contain:
- children (HSMs or States)
- transitions
- incoming events.

whereas Container Components contain:
- children (Containers or Leaves)
- connections
- input ports
- output ports.

Question: Is a Container just a kind of HSM?  Or, do both inherit from a common ancestor class? Or are they completely separate kinds of entities?

I tend to think that HSMs are used for writing synchronous code, where Components are used for writing asynchronous code.  What, if any, is the similarity between HSMs and Components?

# See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity (see blogs that begin with a date 202x-xx-xx-)
- https://guitarvydas.github.io/ (up to about mid-2022)
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
leanpub'ed (disclaimer: leanpub encourages publishing books before they are finalized)
https://leanpub.com/u/paul-tarvydas
### Discord
https://discord.gg/Jjx62ypR  all welcome, I invite more discussion of these topics
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice needed)