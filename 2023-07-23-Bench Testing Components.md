# 2023-07-23-Bench Testing ComponentsThis is an abstract, contrived example.

Imagine that we have a component such as in this drawing

!![100](BenchTesting.drawio_12.svg)

and that the abstract specification of this component - C - is:
1. if *input* satisfies some property, then the component C produces some kind of outputs on ports *output1* and *output2*
2. In all other cases, component C produces some kind of output on port *output3*.

Ideally, we should be able to put C into a test jig - provided by the IDE - and inject various messages into the input port *input*.  After injecting a message, we observe the output ports to see that the correct results are generated.

We inject *objects* into the input port *input* and observe the generated *objects* on the output ports.

I call the injected objects *Input Messages*.

I call the generated objects *Output Messages*.

*Input* and *Output* Messages are, both, kinds of *Message*.

Any kind of *Message* contains 2 attributes:
1. a port identifier, recognized by C
2. a datum, containing data.

*Input Messages* refer to *input ports* of the component, in this case C.

*Output Messages* refer to *output ports* of the component, in this case C.

Note that *output messages* contain port identifiers that are recognized by C.  Component C is not connected to any other components, yet, so the *output messages* cannot refer to ports on other components.  For flexibility, output messages *never* refer to ports on other components, they must only refer to ports on the outputting component (in other words "scoping", or, "output API").

All *input ports* must be distinct within C.

All *output ports* must be distinct within C.

Input port identifiers can be the same as output port identifiers.  In other words, component C uses different namespaces for its input ports and for its output ports.  For example, if one of the inputs is called "xyz", it is valid to, also, call one of the output ports "xyz". There can only be one input port named "xyz" and only one output port named "xyz".  Or, for example, if we were to use numbers[^indexing] to identify ports, we might have an input port called 1 and an output port called 1.

[^indexing]: It might be possible to increase efficiency by treating ports as indexable arrays instead of as hashmaps.

# See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity (see blogs that begin with a date 202x-xx-xx-)
- https://guitarvydas.github.io/ (up to about mid-2022)
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
WIP - leanpub'ed (leanpub encourages publishing books before they are finalized)
https://leanpub.com/u/paul-tarvydas
### Discord
https://discord.gg/Jjx62ypR
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice needed)