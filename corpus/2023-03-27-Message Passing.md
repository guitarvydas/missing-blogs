# 2023-03-27-Message PassingSuggestion: separate the notation from an implementation of an editor for the notation.  

Rhetorical question: can you draw your intentions on a whiteboard / napkins?  

What are the rules?  

If you figure that out, then you can tell the Designer what the rules are, and, you can tell the Software Implementor what the rules are and what the editor should do.  

Make "components" purely stand-alone, then you can rearrange them on any diagram or any diagramming tool.  Processes make components that are stand-alone, FP does not.  Call/Return (aka function calling) interferes with stand-alone-iness.

What does that mean?  A Component has one input queue and one output queue.  Queues contain Messages.  Message are tuples of {tag X data}.  

Queues are FIFOs not LIFOs (duh).   

Functions that call other functions can only be used to implement the innards of components.  

Components that want to communicate with other Components must send messages.  Output messages are FIFOed into an output queue.  Messages are one-way only, no return value is expected and the message-sender can continue asynchronously.

Components do not get to decide where messages go. Only their parents can make such routing decisions.

When you draw diagrams on a whiteboard, it is "obvious" what the diagrams mean.  Make software that implements such intentions.  Ignore all of the other possibilities.

Conclusion: begin with white-boarding.  Then ask Implementors to implement the diagrams on the white-board in their programming language of choice.  If they can't - or if they ask too many questions - then you haven't been specific enough.  You don't need a diagram compiler - you only need a set of well-defined rules of what your diagrams mean.
