# 2022-07-18-CPS is GOTOThe classic paper "GOTO Considered Harmful" introduces "structured programming" and appears to say that GOTO should not be used.

---

GOTO not needed in 95% of all use-cases.

---

programming in the past (mid-1900s)

ad-hoc

there was no "standard" way to organize code / use of GOTO

some programmers wrote structured code, most did not

---
unstructured programming

criss-cross lines of control flow

allowed due to use of text notation 

wouldn't have happened if nested diagrams were used 
- it is immediately obvious when boxes are not properly nested
- humans have a natural tendency to avoid overlapping boxes over edges of other boxes

---
flowcharts

used unnested boxes

lines represented control flow

lines could cross

---

Structured Programming

1 entry point

1 exit point

essentially: 
- lasso code with a box
- ensure that boxes do not overlap

---

Violations of Structured Programming

violated by any language that supports exceptions (1 entry point, 2 exit points)

viloated by UNIX® *stdin*, *stdout*, *stderr*