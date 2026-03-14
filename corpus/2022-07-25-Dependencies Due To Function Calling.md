# 2022-07-25-Dependencies Due To Function Calling
# Problem

`f(x)`

1. The name of the callee (`f`) is hard-wired into code of caller.
2. The caller is a state machine exhibiting blocking-wait behaviour, i.e. the caller blocks until the callee is finished.
3. Routing information is determined dynamically at runtime.  The callee *must* route its result to the caller.  When the callee tries to route information elsewhere, we use the derisive term *side-effect*.

# Solutions
1. Prohibit naming other components explicitly.  Names are strictly relative (local, namespaced) only.  A Component has no control over "where" its information will be routed.
2. Never block.  All components are async by default.
3. Create a 2nd class of components ("uber-functions") that are responsible for composition of components and routing between them.  A component can send messages ("commands") to its direct children, or, can send summary information ("data") to its Parent.  A component cannot send messages directly to peer components, a component can leave a message on a FIFO that can be routed to a peer by the Parent.  Routing is at the discretion of the Parent.  The Parent can decide:
	- to route the message to a single child, or,
	- to route the message to multiple children, or,
	- to discard the message entirely (NC - No Connection).

## Today

1. Class Leaf
2. Class Container.

*Leaf* contains "code".  

*Container* contains
- list of children (instantiated)
- routing table (connections) between children and/or itself.

All Components take input from an input FIFO.  All Components produce output to an output FIFO.  All input/output done via message-passing.

All Components are asynchronous by default (closures + Dispatcher).

- Class Message
- Class Component

### Synchronization
All Components are asynchronous by default.

When synchronization is necessary (in the Architecture), then a request/response protocol can be implemented by passing messages.

### Loops
All Components are asynchronous by default.

A Component finishes its business promptly and returns control to the Dispatcher ASAP.

If a Component needs to Loop, it sends itself feedback messages.

Looping is an ad-hoc form of Recursion.  Recursion works the same as described in this section.
