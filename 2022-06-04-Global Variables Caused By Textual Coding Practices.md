# 2022-06-04-Global Variables Caused By Textual Coding PracticesI argue that the "global variable problem" was caused by the use of text-based programming languages.

For example

```
var x;
function f (...) {
  var y;
  y = 1;
  x = 2;
}
```

Would be written in diagram form as:
!![globals-freevariable.png](globals-freevariable.png)

Upon seeing this, we would be compelled to rewrite it as:

!![globals-boundvariable.png](globals-boundvariable.png)

Which immediately wraps a *scope* around the global variable `x` and makes it obvious, to the reader, what the scope of `x` is and where it can be used.

Note that λ-calculus does exactly this, but, in textual form, by wrapping a λ around the global variable `x`.  

Note that λ-calculus uses a more politically-correct name for the word 'global'.  It is called a *free variable*.

The "global variable problem" was ultimately solved by wrapping variables in textual scopes, mimicking diagrammatic expressions of programs. `{ ... }` means `box`, but isn't as visually obvious as a drawing of a box.


## 2022-06-07-Abstraction In Diagrams

# Abstraction in Diagrams
In diagrams, *abstraction*s are created by wrapping rectangles around components and then pushing the details onto another diagram.

A group of components are *abstracted* by lassoing the group and making a single component out of th group.

Abstraction in diagrams is structured by using nesting.

Connections (lines) and components cannot cross the boundaries of an abstraction. 

Containers can refer only to children that are directly contained.  References cannot cross boundaries, hence, a Container can refer to (and route messages for) components that are 1 level inside the Container, but cannot refer to children within the children, nor refer to peers.  Containers, like Leaf nodes, are components and can send messages upwards only to their own parent Containers. This process is analogous to business organization - each level of management summarizes information before passing the information up the tree (ORG chart) and managers can only command their direct reportees (children).  

The entire structure is hierarchical.  Container Components at one level only know about their directly-contained children and cannot know how the Children are implemented (as Leafs or as Containers - the children are components whose Implementation is hidden (elided) from their Containers and all levels above them).