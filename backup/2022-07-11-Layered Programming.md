# 2022-07-11-Layered Programming# Structured Programming 2.0

- layers
- down -> commands
- up <- summaries
- across -- not permitted
- call/return -- not permitted
- analogy: business organization, biz ORG Charts
- composition through explicit communication, 
- if synchronization is necessary, make it explicit
	- no implicit synchronization
		- no implicit communication
		- no implicit dependencies

# Orthogonal Programming Languages
- GCC <- RTL - Fraser/Davidson, 
	- normalize all operands to a single kind
	- resolve operands later
- OCG <- Cordy
	- normalize all operands to *data descriptors*
	- generalization of RTL technique
	- Cordy invented a declarative MIST notation to resolve operands - later
- Ohm-JS TDPL enables easy division between operators and operands
- Ohm-JS *applySyntactic<...>* makes for easy phrase-parsing
	- using operators (keywords, syntax)
	- using separate operands (operand-parsing rules)
- OOP 
	- model *operands*
		- (not for operators)
- λ-calculus for programming
	- models all values as a single type (callable function)
		- so-called "typed parameters" are, actually, sub-types
		- so-called "typed parameters" are destructurings of single input type (a block of data bytes)
		- so-called "typed return values" are destructurings of single output type
		- dimension *t* (time, history) is simply ignored
			- or modelled explicitly (painfully, noisily) as function parameters/returns
	- very similar to Cordy's *condition descriptors*


# 0D

---
# Scalability
---
# Syntax Stacks - Layered Syntax

---
# Appendix Call Return Spaghetti
---

# Appendix ls.0d in Python
---


# Appendix References
- OCG
- RTL
	- Peephole optimized using Ohm-JS
- scalability
- 0D
- Concurrency
- Concurrency is not Parallelism
- FBP