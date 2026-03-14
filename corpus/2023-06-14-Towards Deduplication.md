# 2023-06-14-Towards Deduplication# Toward Deduplication
## Synopsis
Can compilers de-duplicate code?

I think so.

We know that names are inconsequential.  DeBruijn indexing formalizes the idea.  Compiler-ists already knew this in the 1970s.

Text-manipulation tools make it easy, *iff* you convert the code-under-consideration into very, very explicit text.

I favour diagrams for human consumption.  But, CPUs and our existing tools are all based on sequential lines of text.  So, to humour me, we need to figure out ways to map diagrams to sequential text.  I argue that is not at all difficult.  This note, "Towards Duplication" shows my thinking on how to map a once-thought-to-difficult problem ("compiling") into the text domain.  Compilers are easy if one maps high-level languages into explicit (fugly) text.  The idea is to map human-readable notations into machine-readable text (DaS[^das] in my opinion).

[^das]: DaS == Diagrams as Syntax.

As an added bonus, one might note that function-based thinking is leaning towards Lambda Calculus.  Most of functional thinking aims at achieving the nirvana of "referential transparency".  I.E. the ability to replace one textual function with another.  In Microsoft Word, that is called "Find and Replace".  The "rules" of functional notation - e.g. no side-effects, scoping, no globals, etc. - snipe away at the basic tenets of making find-and-replace possible without surprises and gotchas.

This note is an early cut.  I have written the code manually and haven't checked it using a machine.  There are likely errors, and, I expect to change my mind as I move forward.

I hope to write this code as 0D components and to show that a simpleton machine can understand what I want to do.  I haven't done this yet.

## Method: 
- Convert human-readable code into a factbase.  
- Convert all names into scoped names.  
- Create synonyms for all scoped names `(var ...)`.  I choose to use `@` as a prefix for each synonym and to use unique characters (digits) to identify each unique synonym.
- Make allocation, types and offsets very, very explicit.  Write them in textual form. This allows the use of text tools (like Ohm-JS) to manipulate the text.
- Express the body - a script - for each function in terms of the normalized synonyms.
- Pattern-match the bodies looking for similarities.  
- When a similarity is found, check that the synonyms are similar, too.
- When everything lines up, delete the duplicates and substitute function names.  Given the code below, one would replace all calls to function "ghi" with calls to "abc".

The technique is: convert all details into text.  Eschew data structures in the code (data structures are obviously useful, but use them at runtime, not necessarily at compile-time).  Existing text-based parsing tools can be used, when *everything* is expressed in text.  

Technique: express all details as text in PROLOG format, allowing one to use PROLOG to do the exhaustive searching.  Currently, I use SWIPL.  I used to use GPROLOG, and, I used to use LISP.   I think that miniKanren and Clojure's core.logic would work, but, I haven't actually tried to use them.

```
int abc (int x) {
  int c = 75;
  return x + c;
}

int ghi (int y) {
  int d = 75;
  return y + d;
}

```

```
(function "abc" nil)  ; declare existence of function "abc"
(scope "abc"
 (var @0 ("abc" "c")) ; declare existence of @0 in scope of "abc"
 (var @1 ("abc" "x")) ; declare existence of @1 in scope of "abc"
 (var @2 ("abc" ""))  ; declare existence of @2 in function "abc", @2 has no given string name
 (var @3 ("abc" ""))  ; @3 is invented by the compiler to hold a temporary result
 
 (allocation @1 ("abc" parameter)) ; say where @1 is allocated (in parameters pool)
 (type @1 "int")                    ;; @1 is an int
 (offset @1 0)                      ;; in location 0 of parameters pool
 
 (allocation @0 ("abc" temporary)) ; say where @0 is allocated (in locals pool)
 (type @0 "int")
 (offset @0 0)                      ;; in location 0 of locals pool
 
 (allocation @2 ("abc" return))    ; @2 is located in the return value pool
 (type @2 "int")
 (offset @2 0)
 
 ;; temp value
 (allocation @3 temporary)
 (type @3 "int")
 (offset @3 0)
 
 (body-script "abc"
              (assign @0 (constant "int" 75)) ; c = 75
              (assign @3 (op+ ("int" "int") @1 @0))
              (return @3)))
 
(function "ghi" nil) ; declare existence of function "ghi"
(scope "ghi"
 (var @0 ("ghi" "c")) ; declare existence of @0 in scope of "ghi"
 (var @1 ("ghi" "x")) ; declare existence of @1 in scope of "ghi"
 (var @2 ("ghi" ""))  ; declare existence of @2 in function "ghi", @2 has no given string name
 (var @3 ("ghi" ""))  ; @3 is invented by the compiler to hold a temporary result
 
 (allocation @1 ("ghi" parameter)) ; say where @1 is allocated (in parameters pool)
 (type @1 "int")                    ;; @1 is an int
 (offset @1 0)                      ;; in location 0 of parameters pool
 
 (allocation @0 ("ghi" temporary)) ; say where @0 is allocated (in locals pool)
 (type @0 "int")
 (offset @0 0)                      ;; in location 0 of locals pool
 
 (allocation @2 ("ghi" return))    ; @2 is located in the return value pool
 (type @2 "int")
 (offset @2 0)
 
 ;; temp value
 (allocation @3 temporary)
 (type @3 "int")
 (offset @3 0)
 
 (body-script "ghi"
              (assign @0 (constant "int" 75)) ; c = 75
              (assign @3 (op+ ("int" "int") @1 @0))
              (return @3)))
 

```