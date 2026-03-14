# 2022-08-31-Lambda Model
λ is a stack operator:

# (lambda (x) ...)
1. scope enter
	- performs a stack.push 
	- performs assign-once for names "x" and "0"
	- mutates the global stack (push (change stack-pointer) and assign a value to the top stack entry)
2. lookup
	- makes "x" available as a value in "..."
	- makes "0" available as the value of "x" in "..."
3. scope exit
	- pops the stack
	- mutates the stack (pop (changes stack-pointer) and discards the top value (the top value could be GC'ed at this point))