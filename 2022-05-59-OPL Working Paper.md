# 2022-05-59-OPL Working Paper[OPL  means Orthogonal Programming Languages.  Splitting operations from operands].

operand:
.name - name of a slot of an object
«name» - name of an arg (function parameter)
λname - name of a  function in current module
!name - name of a local within the current function
'xyz' - constant string
[0-9]+  - constant number
%yes - constant (AKA true)
%no - constant (AKA false)
:name - name in heap / RAM
=name - name of module
$name - name of a prototype (user-defined structure)
@Name - invokes a constructor for the Name object (e.g. @Stack ≣ "new Stack ()")
◦name - symbol "name" (e.g. a symbol in Lisp, string in Python/JS/etc.)

%cons [2 args]

attributes
- (type) shape / type
- name[NN] - indirect NN, ...[0] means constant, ...[1] means value of a variable, ...[2]-> means pointer to a variable, ...[3]-> means pointer to a pointer to a variable, and so on
	- e.g. 'abc'[1] is the string 'abc'
	- e.g. 'abc'[0] is the address of the string 'abc'
	- e.g. 'abc'[2] is a pointer to the string 'abc'
	- e.g. 'abc'[3] is a pointer to a pointer to the string 'abc'
- for example
	- :x(int16)[1] is the value of a slot of type int16 located in the heap
	- !x(int16)[1] is the value of local temporary of type int16 located in the temp space for the enclosing function (usually the stack)
	- .x(int16)[1] is the value of the slot of type int16 located in the object that prefixes this expression
	- :x(int16)[2] is a pointer to a variable of type int16, located in the heap
	- *x*(int16)[1] is the value of a variable of type int16 that is an argument to the current function
	- !x(int16)[1] is the value of a variable of type int16 that is a local (temp) in the current function
	- :x(string)[1] is the value of the string in variable x
	- :x(string)[0] is the address of the string in variable x