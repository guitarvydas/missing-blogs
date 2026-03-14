# 2022-06-18-Black Box Software Components
![pm/smallstepswithtbx/fmt-Transpiler.png](fmt-Transpiler.png)

> [!tip] A black box does not know where its output messages will be routed.

In fact, a black box does not even know *if* its output messages will be routed to any receivers.

A black box simply sends messages to its outputs and lets its Container decide how to route messages.  Output messages are simply appended (deferred) to a Component's output queue and are left for the direct Container to deal with.

Message routing is done solely by a component's container.  The container does not care (nor know) how its children components are implemented (as Leaves or as Containers).  

Each component, Leaf or Container, has 1 input queue and 1 deferred output queue.

Messages are tagged by the input they are associated with, and then appended to the input queue of a component.  A tag is a port id.

Containers receive *step* commands, and delegate these commands to their children.  

Containers route messages from each activated child.

Containers contain 
- children components
- a routing table
	- messages can be routed from a child's output to other children's inputs
	- messages can be routed from a container's inputs to its children
	- messages can be routed from a child's output to a container's output
	- (rarely occurring edge-case) messages can be routed from a container's inputs to its own outputs
	- child messages can be routed to NC (No Connection)
	- child inputs can be marked NC ; a child does no work if its input queue is empty
	- container inputs can be routed to NC.

A Container is *busy* if any of its children is *busy*.  

A Component processes 1 input message to completion before pulling another input message for processing.

This implies that a Container must step all of its children to completion before pulling another input message.  

A Container may be activated multiple times with *step* commands.  It must delegate these *step* commands to its children until all children's activity has subsided.

A Container can refer only to its direct children.  A Container cannot refer to children of children.

A component, Leaf or Container, cannot refer to its peers.  

A Container can only send messages to its direct children, or send messages to its direct parent.  

Messages being sent downwards are usually in the form of commands.  

Messages being sent upwards are usually in the form of filtered information.  

A component "sends" messages to its parent by leaving deferred messages in its own output queue.  The direct parent can inspect and deal with the output queues of its direct children.

### Fan-in
A component, Leaf or Container, can receive messages from mutiple sources.

The component must process messages in order of arrival, one input message at a time.

### Fan-out
A component, Leaf or Container, can create messages that are routed to multiple receivers.

This implies that the component's Container must deal correctly with message copying, or, that message data is considered read-only (copy-on-write) by all receivers.  [Note that Javascript objects follow a copy-on-write policy using prototypal inheritance. Object fields are read by recursive lookup, but when written, the fields affect/create only *own* data.]

Fan-out is affected by the "Messages Must Not Interleave" rule.

## Messages Must Not Interleave
A message must arrive "at the same time" at all receivers.

For example, if A sends ẋ to C, D and E, and, B sends ẏ to C and E, then, C and E must see ẋ before ẏ or ẏ before ẋ.  The situation where C and E see ẋ/ẏ in a different order must not happen, i.e. C must not see ẋ,ẏ while E sees ẏ,ẋ.

A simplistic way to ensure this rule is to send messages atomically by locking all of the queues of all receivers before appending a message.  There might exist optimizations to this method that I haven't thought of yet.

