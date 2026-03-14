# 2022-07-08-Peephole Optimizer Using Ohm-JS
**Peephole Optimizer Using Ohm-JS**

Paul Tarvydas, July 8, 2022

---
Previous: 
## 2022-07-08-Using Ohm-JS Intro


**Using Ohm-JS to Transpile a Snippet Of Code**

Paul Tarvydas
July 8, 2022

---
snippet of code
```
CONST cache TO ARR ZERO SEP ONE END
FN fibonacci num DO
  IF cache OF length GT num DO
    RETURN cache OF at CALL num END
  END
  RETURN fibonacci CALL num SUB ONE END ADD fibonacci CALL sum SUB TWO END
END
```

[Snippet taken from repo of Kinect3000](https://github.com/KinectTheUnknown/WrittenScript)
https://github.com/KinectTheUnknown/WrittenScript

---
Javascript:
```

const cache = [0,1] ;
function fibonacci (num) {
if (cache.length  >  num) {
return cache[num] ;
}
return fibonacci (num - 1) + fibonacci (sum - 2);
}
```
---
How?
- 3 steps 
- +1 extra dev step
---
Separate Functions

- each step is implemented as a separate function
- each function uses a separate Ohm-JS grammar
	- and a separate formatter specification ("Semantics" )
- each step is implemented and tested separately
- the output of a step is fed forward to the next step
- step 1 -> step 2 -> step 3

---
Why Separate Steps?

- Reduce dependencies (to zero, if possible (0D))
- build-and-forget, do 1 job well
- optimize later (premature optimization impacts thinking processes)

---
Step 1:
- tokenize
---
Step 2:
- transpile
---
Step 3:
- optimize

Match 
```
cache.at (num)
```
and optimize to 
```
cache[num]
```

---

Step 2.0 - Extra Dev Step
- Identity Grammar
- Create skeleton parser/formatter where output=input
- hack on skeleton to create Step 2 transpiler

---
Use Ohm-Editor

write/debug grammars using [Ohm-Editor](https://ohmjs.org/editor/)

https://ohmjs.org/editor/

---
Appendix demo
- load index5.html into a browser
- click "Test" button 
---

Appendix 
[github](https://github.com/guitarvydas/nl)
https://github.com/guitarvydas/nl
see index5.html

youtube: [Ohm-JS for transpiling snippets of code](https://youtu.be/HDDQHW6mnvY)
https://youtu.be/HDDQHW6mnvY

---

Optimizer changes Javascript -> Javascript.

---
Match 
```
cache.at (num)
```
and optimize to 
```
cache[num]
```

---

Peephole Optimizer
- small grammar
- uses Ohm-JS features
	- lexical rules
	- syntactic rules
	- applySyntactic

---

- technique used in GCC (RTL)
	- [Fraser/Davidson](https://www.researchgate.net/publication/220404697_The_Design_and_Application_of_a_Retargetable_Peephole_Optimizer)
	- J. Cordy's [Orthogonal Code Generator](https://books.google.ca/books?id=X0OaMQEACAAJ&dq=bibliogroup:%22University+of+Toronto+Computer+Systems+Research+Institute+Technical+Report+CSRI%22&hl=en&sa=X&ved=2ahUKEwig1Legm8bqAhWvlHIEHYzzBYEQ6AEwBHoECAEQAQs) further generalizes the technique

[References](https://guitarvydas.github.io/2021/12/15/References.html)
https://guitarvydas.github.io/2021/12/15/References.html
"The Design and Application of a Retargetable Peephole Optimizer"
"An Orthogonal Model for Code Generation"

---
Peephole Optimizer Grammar
```
NLPeepholer {
top = peephole+
peephole =
  | applySyntactic<AtFunctionCall>
  | any
AtFunctionCall = "." "at" "(" Arg* ")"
Arg = 
  | "(" Arg* ")"  -- nested
  | !"(" !")" any -- basic
}

```
---
Peephole Optimizer Reformatter
```
top [@peephole] = ⟦⟦!{peephole}⟧⟧
peephole [x] = ⟦⟦!{x}⟧⟧
AtFunctionCall [kdot kat klp @Args krp] = ⟦⟦\[!{Args}\] ⟧⟧
Arg_nested [klp @Args krp] = ⟦⟦!{klp}!{Args}!{krp}⟧⟧
Arg_basic [c] = ⟦⟦!{c}⟧⟧
```

---
FMT Tool 
- evolving
- previously called Glue, Grasem

latest documentation: [PREP Tool (see the Glue Format section)](https://github.com/guitarvydas/prep)

earlier documentation: [Glue Tool](https://guitarvydas.github.io/assets/2021-04-11-Glue%20Tool/index.html)

---

# Appendix 
Github Code

[index4.html]((https://github.com/guitarvydas/nl/blob/main/index4.htm)
https://github.com/guitarvydas/nl/blob/main/index4.htm
