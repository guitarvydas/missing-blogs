# 2022-07-12-BRS-Organizing Anything# Components
- Leaf
- Container

## Leaf
A Leaf is/produces content.  A URL, a piece of code, etc.
# Container
- contains a list of Chidren Components
- contains a list of connections between Components
- can send Request *down* to direct children
- can receive (summarized) information *from* direct children
- can react to requests from Parent
- can send information *up* to Parent
# Component
1. a Leaf, or,
2. a Container

Containers are "recursive" and may contain other Containers (as well as Leaves).

Containers cannot know how a Child is implemented, e.g. cannot know if a Child is a Leaf or another Container.

# Sending Messages
Messages cannot be sent sideways.

Information messages can be sent *upwards* to a Parent.

Request messages can be sent *downwards* from a Parent to a direct Child.

Implication: all messages are relative

# 0D, Isolation
All Components are 0D (zero dependency).

A Component cannot name another component, it can only leave messages to be processed (routed) by its Parent (deferred messaging).

# Tags
# Unix
# Obsidian
# Kinopio
