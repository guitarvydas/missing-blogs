# 2022-12-25-Operand DescriptorsWorking paper on normalizing all access to all data.

The purpose of normalization is to make it easier to automate generation of programs - to write program generators ("compilers" reimagined).


# Data Descriptors
[Data Descriptors](https://dl.acm.org/doi/10.1145/24039.24051?preflayout=flat) were designed to normalize all access to all data to help with the gargantuan task of building software apps called "compilers".

As defined, DDs have the built-in assumption that all spaces are arrays of bytes.

DDs led to work on portable compiler technology such as the [Orthogonal Code Generator](https://books.google.ca/books/about/An_Orthogonal_Model_for_Code_Generation.html?id=X0OaMQEACAAJ&redir_esc=y) .

That work was preceded by [RTL](https://www.researchgate.net/publication/220404697_The_Design_and_Application_of_a_Retargetable_Peephole_Optimizer) which was used in the massively popular app called *gcc*.

# What's Next?

Compilers have become a "solved problem".  

Today, we want to build "transpilers" (source-to-source transformers) and we want to explore syntax elements other than textual characters.

We want to use lessons learned from the past 
- normalize everything to make it possible to automate code generation
- use Orthogonal Code techniques for designing new languages.

# Orthogonal Code Techniques

Orthogonal Code Generations subdivides code up into two broad categories:
- operands (AKA "data")
- operators (AKA "control flow").

## Eschewing Control Flow
It is - currently - in vogue to treat "control flow" as being the same as "data flow".  

This model of computation is useful for building complex calculators and has resulted in a flurry of languages of the Functional Programming ilk.

Electronic machines - AKA "computers" - are capable of doing more work than that required by mere calculators.  

## History - State
For example, "computers" are capable of sequencing events and machines.  Sequencing requires the notion of *history*, and, *state*.  

*History* and *state* is expressly ignored by Functional Programming notations.

Such abstraction leads to useful results, but, discourages results in other dimensions such as sequencing.

When all you have is functions, everything looks like a function.

# Syntax is Control Flow
Control Flow is expressed by syntax.

(Data is expressed by OOP).

Up until now, we have been hampered by the fact that *syntax* has been difficult to deal with and to express.

Now, we have easy access to syntax and so-called "parser generators" in the form of Ohm-JS.

We can re-examine and re-express the relationships between *operands* and *operators*.

We already have OOP for expressing *operands*.

Now, we have Ohm-JS for expressing *operators*.

Now, we can do both, express data-flow *and* express control-flow - easily.

In designing transpilers, 
SDs treat spaces like ordered lists, can be optimized to be mapped onto arrays of bytes

# Where Can Operands Live?
Imagine this bit of code:

```
(lambda (x)
  (lambda (y)
    (let ((z (add x y)))
      z)))
```

In JavaScript syntax, this might be written as:
```
function (x) {
  return function (y) {
    var z = x + y;
    return z;
    } (x);
}
```

As a drawing, we might write:

!
## Drawing 2022-12-25 09.32.52.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
input x ^AnmDqsua

input y ^v5tlW1Yx

synonym z (x + y) ^86408NXo

return z ^LILjZzZY



The variable `z` is an operand.  It represents a temporary variable inside the inner-most expression.  `z` is a *synonym* for the expression `x + y`.

The variable `y` is an operand.  It is a parameter to the inner anonymous function (`lambda (y)`).  The value of `y` is determined only at runtime.

The variable `x` is an operand.  It is a parameter to the outer anonymous function (`lambda (x)`).  The value of `x` is determined only at runtime.

The result `z` (the 4th line is an implicit `return` statement) assigns the value of the variable `z` to the return-variable of the complete expression.  We don't bother to give a name to the return-variable for the expression.


- parameters
- temps
- actuals
- results

Not in the above, but, to be considered:
- pointers
- free, global
- messages (asynchronous)

# Pointers
char \*s = "result = %c\n";

... f (... char **argv ...) { ... }

!
## Drawing 2022-12-25 16.38.20.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
x ^uNsto3QH

ϕ ^50wiX4fU

r ^7T5qAuIW

e ^crgFF5KO

s ^jhYi65VN

u ^CsbgKmng

l ^W8mMbVuZ

t ^XmXhjrGa

= ^dKWXECpe

% ^jnQLEreC

c ^ZgmxrUeo

\n ^uTumHEXk

2 ^3cPqaIxb

*chars* ^qeit00yx

*pointers* ^RkTTQKwi

1 ^e7ja3YJT

*parameters* ^mJfHywr5

argv ^bHfjXj3H


# C Everything Is A Byte
!
## Drawing 2022-12-26 06.53.29.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
C everything is a byte
 ^ZNxXE7OD

C string ^9X7qlbpL

x ^JptzUNDt

ϕ ^R7jAkb1W

r ^ilBzKz40

e ^XIS6yQpr

s ^FPpQf4YR

u ^p4wD6ndD

l ^STEdObX7

t ^7Z9om2D5

= ^rZ6TF4HF

% ^RpI1eCYI

c ^lro7S5lp

\n ^E5FsMSGA

0 ^9YarPRxl

var s1 ^Lava6gqB

2 ^e2ER9DRl

var s2 ^rtv6Xzvn


## Operand Descriptors
!
## Drawing 2022-12-26 07.04.57.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
x ^8f7zBfSI

ϕ ^VcsSkFOH

r ^kh88RT2H

e ^2EkFDzrH

s ^ymXFoIRR

u ^F9geDBZQ

l ^uS3YEriu

t ^kkjHKPyk

= ^AweK54vg

% ^HfoOU2fM

c ^hPteFOTa

\n ^vmKKxl8v

0 ^mvkqKl3E

s1 ^Bk8I3NkH

2 ^rcKwsV92

s2 ^6I9e7S34

char.@¹temps.2 ^p5KhtEyO

char.@⁰bytes.2 ^V7MWH6Gt

2 ^bShXkhi6

*pointers* ^5hPIZNf0

0 ^7F49cFq5

*parameters* ^gTaILL87

argv ^YZlbCBqE

*temps* ^z4RYgdud

*bytes* ^BGWwyz8l

char.@²parameters.0 ^wpK39G71

