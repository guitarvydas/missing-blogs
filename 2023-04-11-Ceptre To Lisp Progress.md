# 2023-04-11-Ceptre To Lisp Progress# Ceptre To Lisp Progress

---

## Why Is Ceptre Interesing?
- formal game-design language
- NPCs
- Robotics
- time, formalism

---
Game-design language needs sequencing

Robotics language needs sequencing

Ceptre mixes formal methods with sequencing

---
Formalism
- islands of formal logic
- stages
- no name-calling - `qui`
- formal logic

---

Strangeloop 2015: https://www.youtube.com/watch?v=bFeJZRdhKcI

Paper: http://www.cs.cmu.edu/~cmartens/ceptre.pdf

Thesis: https://www.cs.cmu.edu/~cmartens/thesis/thesis.pdf

---

## Manual Grind-Through

---

Ceptre:
```
max_hp 10. damage sword 4. cost sword 10.

context init_ctx = {init_tok}.
```
Fact base is now
```
max_hp (10 _)
damage (sword 4)
cost (sword 10)
init_tok
stage (init _)
```

The first stage in the source code becomes the default stage.

---

Ceptre:
```
stage init = {
  i : init_tok * max_hp N  -o  health N * treasure z * ndays z * weapon_damage 4.
}
```

Factbase is now:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (init _)
```

Facts `init_tok` and `max_hp (10 _)` were retracted from the factbase because they were used to create a successful left-hand-side pattern match.

---

When *stage init* matches nothing more, it creates a `qui` fact in the factbase.  We have:

Factbase:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (init _)
qui
```
---
Ceptre (top level rule)
```
qui * stage init  -o  stage main * main_screen.
```

Factbase becomes:
```
damage (sword 4)
cost (sword 10)
health (10 _)
treasure (z _)
ndays (z _)
weapon_damage (4 _)
stage (main _)
main_screen
```

...

---

## Compiler

1. Transpile Ceptre syntax to RT

2. Transpile RT to Common Lisp

Hope: Repurpose transpiler #2 for Python, Odin, etc.

https://github.com/guitarvydas/ceptre

---
Text Composing

Create Verbatim code where appropriate 

Downstream passes ignore Verbatim code, pass it down unchanged

Remove Verbatim markers during cleanup

Finished when all text is Verbatim

---

### Ceptre to RT

Begin with dc.cep - Dungeon Crawler source in Ceptre syntax.

Use Ohm-JS and FAB to incrementally transpile to RT syntax.

Currently 8 simple passes

Compose text incrementally

See ceptre2rt in Makefile

---
Example
```
max_hp 10. damage sword 4. cost sword 10.

context init_ctx = {init_tok}.

stage init = {
  i : init_tok * max_hp N  -o  health N * treasure z * ndays z * weapon_damage 4.
}

qui * stage init  -o  stage main * main_screen.
...
```

---

after 1st pass
```
max_hp 10. damage sword 4. cost sword 10.

context init_ctx = {init_tok}.

stage init = {
  name i %
init_tok * max_hp N  -o  health N * treasure z * ndays z * weapon_damage 4.
}

qui * stage init  -o  stage main * main_screen.
...
```

N.B stage init.i transpiled to `name i %`

---

final dc.rt
```
(fact max_hp 10 ) (fact damage sword  4 ) (fact cost sword  10 )

(fact  init_tok  )(defstage [init]
(namedrule [i]
(match(predicate  init_tok  )(predicate  max_hp  N ))(retract(predicate  init_tok  )(predicate  max_hp  N ))(assert(predicate  health  N )(predicate  treasure  z  )(predicate  ndays  z  )(predicate  weapon_damage  4     ))))(rule 
(match
(predicate  qui  ) 
(predicate  stage  init  )
)
(retract 
(predicate  qui  ) 
(predicate  stage  init  )
)
(assert
(predicate  stage  main  )
(predicate  main_screen  )
)
)
```

N.B. not "nicely" formatted, but, the machine doesn't care.

---

### RT to Lisp

Use Ohm-JS to incrementally transpile dc.cst (RT version) to .lisp.

Currently 
- 9 simple passes 
- 1 bash/sed cleanup
- 1 Python cleanup

see devcl in Makefile

---
Example
```

; -*-Lisp-*-
(fact `(max_hp 10))
(fact `(damage sword 4))
(fact `(cost sword 10))


(fact `(init_tok))

 ;;; stage [init]
(defparameter init_rules nil)
(stagerule init i(match «(match? `(init_tok))» «(match? `(max_hp N))»)«(retract `(init_tok))»
«(retract `(max_hp N))»«(assert `(health N))»
«(assert `(treasure z))»
«(assert `(ndays z))»
«(assert `(weapon_damage 4))»)
 ;;; end stage [init]

 ;;; stage [top]
(defparameter top_rules nil)
(stagerule top topsub1(match «(match? `(qui))» «(match? `(stage init))»)«(retract `(qui))»
«(retract `(stage init))»
«(assert `(stage main))»
«(assert `(main_screen))»
)
...
```

N.B. Some earlier pass decided to emit Verbatim code like `«(retract (stage init))»`.  This signals to downstream passes that they don't have to worry about this part ("divide and conquer").

after cleanup:

```

; -*-Lisp-*-
(fact `(max_hp 10))
(fact `(damage sword 4))
(fact `(cost sword 10))


(fact `(init_tok))

 ;;; stage [init]
(defparameter init_rules nil)
(stagerule init i(match (match? `(init_tok)) (match? `(max_hp N)))(retract `(init_tok))
(retract `(max_hp N))(assert `(health N))
(assert `(treasure z))
(assert `(ndays z))
(assert `(weapon_damage 4)))
 ;;; end stage [init]

 ;;; stage [top]
(defparameter top_rules nil)
(stagerule top topsub1(match (match? `(qui)) (match? `(stage init)))(retract `(qui))
(retract `(stage init))
(assert `(stage main))
(assert `(main_screen))
)
 ;;; end stage [top]
```

---

### CL PROLOG
- Nils Holm PROLOG Control In 6 Slides http://www.t3x.org/bits/prolog6.html
- cl-holm-prolog https://github.com/guitarvydas/cl-holm-prolog
- also transpiled to JS (using Ohm-JS) https://github.com/guitarvydas/js-prolog

---

### What Is RT?
- normalized syntax
- 3 elements:
	1. recursive, bracketed items
	2. atoms
		- atoms can contains whitespace, but, need to be bracketed
	3. separators
- like Lisp syntax, without Lisp's meaning
	- use Ohm-JS to parse and ascribe meaning to parsed text
	- per-project basis, not generalized
---
Example

```
(fact max_hp 10 ) (fact damage sword  4 ) (fact cost sword  10 )

(fact  init_tok  )(defstage [init]
(namedrule [i]
(match(predicate  init_tok  )(predicate  max_hp  N ))(retract(predicate  init_tok  )(predicate  max_hp  N ))(assert(predicate  health  N )(predicate  treasure  z  )(predicate  ndays  z  )(predicate  weapon_damage  4     ))))(rule 
(match
(predicate  qui  ) 
(predicate  stage  init  )
)
(retract 
(predicate  qui  ) 
(predicate  stage  init  )
)
(assert
(predicate  stage  main  )
(predicate  main_screen  )
)
)
```

---

## Remaining Questions
- drop_amount ... bwd
- z, none, nat
