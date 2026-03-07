# 2023-02-22-Ceptre as a Programming Language for GamesQuestions:
1. Is Ceptre a good language for game programming?
2. Can Ceptre be broken down into a handful of primitives ("assembler") and implemented in PROLOG, Lisp, Scheme, JavaScript?
3. can we write a transpiler from Ceptre to Common Lisp in cl0d?

# 2. Primitives

If we can define Ceptre in terms of primitives, then we can implement Ceptre programs in PROLOG.

If we can implement Ceptre programs in PROLOG, then we can use Nils Holm's prolog6.scm to implement Ceptre programs in Scheme.

If we can implement Ceptre programs in prolog6.scm, then 
- we can implement the same programs in CL-HOLM-PROLOG.
- we can implement the same programs in JavaScript using JS-PROLOG.

## What Are The Primitives?  First Take.

Looking at https://github.com/guitarvydas/ceptre/blob/dungeoncrawler/dc/dc.cep, the source code to the Dungeon Cralwer game in the Second Case Study of the paper https://github.com/guitarvydas/ceptre/blob/dungeoncrawler/doc/ceptre.pdf ...

### Use Triples Everywhere.

`relation(subject,Object).`

### Element Mappings

```
max_hp 10.
```
can be written as
```
max_hp(10,_).
```

```
damage sword 4.
```
can be written as 
```
damage(sword,4).
```
and 
```
cost sword 10.
``` 
becomes
```
cost(sword,10).
```

Context results in facts asserted in the PROLOG factbase.
```
context init_ctx = {init_tok}.
```
becomes
```
init_tok(_,_).
```

A `o-` rule is composed of two parts:
1. a pattern match, consisting of a conjunction of predicates
2. a replacement pattern, consisting of a conjunction of predicates.

(2) breaks down in two phases in order:
- delete matching facts
- add new facts.

PROLOG has operators for each of these.  (1) 

1. pattern match of a conjunction of predicates becomes PROLOG clauses separated by commas
2. each deletion becomes a PROLOG `retract` clause
3. each addition becomes a PROLOG `assert` clause.

Each `stage` in Ceptre contains a set of named rules.

For our purposes, we simply need to prepend two PROLOG clauses for each named rule, and, we need to put a *cut* operator at the end of each match.  The *cut* operator will cause PROLOG to chose only the first matching rule without trying other Ceptre rules in the same `stage` after a successful match has been made.  We guard each rule within a `stage` by checking that the rule is not quiescent with the PROLOG negative match `\+ qui(_,_),` and we append a finalization of the `stage` by asserting `qui(_,_)`

```
stage init = {
  i : init_tok * max_hp N  -o  health N * treasure z * ndays z * weapon_damage 4.
}
```
becomes
```

2```

Global - non-staged - steps, like, 
```
qui * stage init  -o  stage main * main_screen.
```
becomes
```
step :-
  qui(_,_),
  stage(init,_),
  !,
  % o-
  retract(qui(_,_)),
  retract(stage(init,_)),
```

## Interactive

I don't know what to do with this yet, so leave it alone and fix it up manually.

## Parenthesized Expressions
The replacement rule can have parenthesized expressions, including `()`.

Emit these as PROLOG expressions.

`()` becomes nothing.
`(NDAYS + 1)` becomes raw PROLOG.

...check 