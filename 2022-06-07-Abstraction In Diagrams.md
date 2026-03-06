# 2022-06-07-Abstraction In Diagrams# Abstraction in Diagrams
In diagrams, *abstraction*s are created by wrapping rectangles around components and then pushing the details onto another diagram.

A group of components are *abstracted* by lassoing the group and making a single component out of th group.

Abstraction in diagrams is structured by using nesting.

Connections (lines) and components cannot cross the boundaries of an abstraction. 

Containers can refer only to children that are directly contained.  References cannot cross boundaries, hence, a Container can refer to (and route messages for) components that are 1 level inside the Container, but cannot refer to children within the children, nor refer to peers.  Containers, like Leaf nodes, are components and can send messages upwards only to their own parent Containers. This process is analogous to business organization - each level of management summarizes information before passing the information up the tree (ORG chart) and managers can only command their direct reportees (children).  

The entire structure is hierarchical.  Container Components at one level only know about their directly-contained children and cannot know how the Children are implemented (as Leafs or as Containers - the children are components whose Implementation is hidden (elided) from their Containers and all levels above them).