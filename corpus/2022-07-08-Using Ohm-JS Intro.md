# 2022-07-08-Using Ohm-JS Intro

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
