# 2023-08-19-Failure Driven Design (Slight Return)
# Failure Driven Design
Paul Tarvydas, April 2021

---

# Failure is the Best Way to Learn

---

# Two Ways of Looking at Development
1. It's going to succeed
2. It's going to fail

---

# Outlook Determines Workflow
- How do you write software when you are convinced that it will work the first time?
- How do you write software when you are convinced that it will fail?

---

# FDD vs. Regular Design
## FDD
- build-in easy recovery from changes / failures
- meta-design, write code that writes code
## Regular Design
- ignore possibility of changes / failures
- straight-ahead design, write code

---

# Assuming Success
- design to implementation flows in one-way manner
- no plan to iterate
- failure is a "surprise"
- therefore, hard to recover from failure

---

# Waterfall Workflow
- antithesis of FDD
- over-confidence

---

# Waterfall Workflow (2)

- early attempts fail to completely solve the problem
- but, no recovery from failure is built into the workflow

---

# Mythical Man-Month
- Fred Brooks
- fail, fail, succeed

---
# Assuming Failure (1)
- The first several attempts at solving the problem will fail.

---
# Assuming Failure (2)
- how to fail fast?
- how to recover quickly?

---

# Failure vs. Success
- when software works, we abandon it (ship it)
- when software fails, we continue to work on it
- most of the time, we work on failed code

---

# What Aspects of a Solution Can Fail?

- requirements
- design
- architecture
- engineering
- implementation
- testability
- etc.

---

# Learning by Failure
## What do we need to learn?
- what the requirements are, details
- the gotchas within the problem space

---

# Learning Details

- most non-programmers do not WANT to specify details
- at best, non-programmers give hand-waving specifications
- non-programmers can be skilled in other areas, they are domain experts, not programmers
- Architects need to gather the specifications
- Engineers need to tighten up the specifications, dot all i's and cross all t's
- Implementors need to write software that matches blueprints specified by Engineers

---

# FDD Strategies
- Goal: Make failure less painful
- iteration
- automation, rebuild solution at the push of a button (after changes)
- layering design, recursive design, iterative design
- indirection
- use as many SCNs as necessary (low-cost notations)
- ask "Why?" 5 times re. requirements, drill down to real problem

---

# FDD (Reprise)
- Failure-Driven Development
- most of the time, the requirements will change
- most of the time, a design will have flaws in it
- most of the time, an implementation will be buggy
- number of failures greatly outnumbers the number of successes
- plan for failure

---

# FDD How? (Reprise)
- fail fast
- encourage backtracking through automation
- transpilation, compilation
- SCNs - low-cost notations, not Languages nor DSLs

---

# FDD How? Notations, Not Languages
- SCN is a lightweight DSL
- Programming Language: heavyweight, expensive to build
- DSL: heavyweight, expensive to build
- Specialize SCN to the Problem Space *only* - don't generalize
- YAGNI (You Ain't Going to Need It) principle
---
# FDD How? Fail Fast
- divide problem
- choose greatest risk, greatest unknown
- implement and experiment with unknown
- if unknown becomes known, defer it and choose next greatest risk
---
# FDD How? Impossible
- if unknown is shown to be impossible ("impractical"), fail and backtrack, 
- change your mind
- redefine the solution, or, seek to redefine the problem

--- 
# FDD How? Testing
- Testing CANNOT prove that something works
- Testing CAN prove that something does NOT work (does not meet its specification)

---
# Scientific Method
- the Scientific Method is a Fail Fast methodology
- a scientific theory is one which is falsifiable
- 1 data point can SUPPORT a theory, but, cannot PROVE the theory
- 1 data point can KILL a theory, though
---
# FDD How? Backtracking
- script everything - rebuild with a single button-push
- workflow:
- repair requirements
- repair design (Architecture, Engineering, Implementation)
- regenerate
- try again

---

# FDD How? Transpilation and Compilation
- compilers pioneered automated transforms
- compilers pioneered portability
- compilers are transpilers - HLL to Assembler
- compilers are interpreters - interpret HLL input and produce LLL output which contains less type-checking
---

FDD How? SCNs
- don't write code
- write code that generates code
- don't write an app, generate the app

---

# SCNs - Cheating
- transpile SCN notation to some other language (e.g. Python, Rust, etc.)
- let other language worry about compilation issues
- PEG
- Ohm-JS

---

# FDD
- when you assume that you will fail, you feel encouraged to use automation and backtracking
- FDD workflow: repair, push button to regenerate, try again
- Waterfall workflow: overconfidence, success is assumed, write code directly assuming that it will work

---

# FDD How? Factbases
- normalize every down to a triple
- easier to automate
- use compiler technology to automate
- e.g. `MOV R1,R0` is a triple (operator, src-operand, dest-operand)
- e.g. RTL, OCG, portability is normalization-based
- Projectional Editing - normalization is the Holy Grail of P.E.

---

# FDD How? Automation LCD
- triples
- { relation, subject, object }
- e.g. a curried function is an unresolved triple { relation, subject, ??? }

---

# Manual vs. Automated
- manual work resists change
- time spent on manual work is not recoverable
- automated work accommodates change

---
# How Do You Know When You Are Finished?
- the product is never finished
- but, you reach a point where it can be shipped, i.e. it is "good enough" for users
- example: songwriters continuously tinker with their songs, but recording them draws a line
---
# FDD How? DI
- Design Intent
- Declarative programming is a goal
- Declarative programming - not there yet
- instead of full-blown declarative programming, specify code generation
- SCNs aimed at partial tasks, e.g. Ohm-JS is a DSL to specify parsing but not semantics
- Programmer specify WHAT, app(s) choose HOW, apps choose optimization(s)

---
# FDD How? Using Debuggers
- A debugger can be used to observe the operation of someone else's code, or your own code
- Stepping and examining is one way to understand the intended architecture.
- Fixing other people's mistakes can force you to think deeply about the DI

# FDD - Anecdotal Case Study

https://guitarvydas.github.io/assets/2021-04-12-Recursive%20Iterative%20Design%20By%20Example/index.html#0

https://guitarvydas.github.io/2021/04/20/Recursive-Design,-Iterative-Design-By-Example-(2).html


---
# Appendix
## DI
https://guitarvydas.github.io/2021/04/11/DI.html
https://guitarvydas.github.io/2020/12/09/DI-Design-Intent.html
https://guitarvydas.github.io/2020/12/09/Divide-and-Conquer-is-Recursive-Design.html
https://guitarvydas.github.io/2021/03/18/Divide-and-Conquer-in-PLs.html
https://guitarvydas.github.io/2021/03/06/Divide-and-Conquer-YAGNI.html
https://guitarvydas.github.io/2020/12/09/Divide-and-Conquer.html
## Factbases
https://guitarvydas.github.io/2021/01/17/Factbases.html
## Triples
https://guitarvydas.github.io/2021/03/16/Triples.html
## SCNs
https://guitarvydas.github.io/assets/2021-04-10-SCN/index.html#8

## Indirection
https://guitarvydas.github.io/2021/03/16/Indirect-Calls.html

## Toolbox Languages
https://guitarvydas.github.io/2021/03/16/Toolbox-Languages.html

## Why? 5 Times
Daniel H. Pink

MasterClass - Daniel Pink Teaches Sales and Persuasion

"To Sell Is Human"

### 5 Whys of Multiprocessing
https://guitarvydas.github.io/2020/12/10/5-Whys-of-Multiprocessing.html

### 5 Whys of Full Preemption
https://guitarvydas.github.io/2020/12/10/5-Whys-of-Full-Preemption.html
### 5 Whys of Software Components
https://guitarvydas.github.io/2020/12/10/5-Whys-of-Software-Components.html

## Details Kill
https://guitarvydas.github.io/2021/03/17/Details-Kill.html
- don't delete details, suppress (elide) them
- KISS
- "simplicity" is the "lack of nuance"
- "complexity", therefore, is "too many details"
