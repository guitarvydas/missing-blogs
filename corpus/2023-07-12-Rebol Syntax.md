# 2023-07-12-Rebol Syntax## Discussing the Original Sample Code
Discussing this post: https://funcall.blogspot.com/2023/06/tail-recursion-in-rebol.html?hidden=true

## Divide and Conquer
The code in the above article conflates two concepts 
1. Rebol 1 syntax parsing
2. vs. interpretation.

Wouldn't it be nice to be able to apply the principles of "divide and conquer" to the act of compiling/interpreting Rebol?


The Divide-and-Conquer version of the above might be:
1. write code in Rebol
2. transpile the Rebol code into recursive assembler (i.e. Common Lisp)
	1. first, do the transpilation manually, (until you "get the gist" of what is needed)
	2. then, automate the transpiler using a tool that takes Rebol syntax and converts it to recursive assembler.


## Fib Function
Rebol 1:
```
define fib
  lambda (x)                         
   (if lessp x 2
       (x)
       (add fib sub1 x
	    fib sub x 2))
```

Common Lisp
```
(defun fib (x)
  (if (< x 2)
     x
    (+ (fib (1- x)) (fib (- x 2)))))
```

## Fact Function
Rebol 1:
```
     define fact
       lambda (x)
       (if zerop x
           (1)
           (mult x fact sub1 x))
```
Common Lisp:
```
(defun fact (x)
  (if (zerop x)
     1
    (* x (fact (1- x)))))
```

## Fact-Iter Function
An iterative version of *fact* that uses explicit recursion instead of explicit iteration.

Rebol 1:
```
   define fact-iter
       lambda (x answer)
       (if zerop x
           (answer)
           (fact-iter sub1 x mult answer x))
```
Common Lisp
```
(defun fact-iter (x answer)
  (if (zerop x)
      answer
     (fact-iter (1- x (* answer x)))))
```



... to be continued ...
