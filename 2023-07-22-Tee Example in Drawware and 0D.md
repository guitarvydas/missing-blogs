# 2023-07-22-Tee Example in Drawware and 0D# Tee Example in 0D
I discuss how to build a simple *tee* operation using 0D diagrams.

There are many ways to implement this function, I focus on only three conceptual versions and one version with all the bells and whistles.

The *tee* operation is similar to *echo*.  It takes a text input and copies it to the output and writes the output to a named file.  Essentially, a no-op, with the addition of writing a copy of the output to a file.

I addition to the text input, *tee* also has a filename input.  The input text is also copied to the file.  If the file does not exist, it is created, if it exists, it is overwritten.  

If something goes wrong, an error message (probably a string) is sent to the error output and nothing is sent to the string output.  What happens to the file is undefined, when any error occurs.

# DI - Outline

!![DrawIO/Tee-Tee Outline.drawio.svg](images/Tee-Tee Outline.drawio.svg)

The Tee component has two inputs and two outputs.

Inputs:
1. text - the string to be copied to the output
2. filename - the name of the file to be written with the contents of the string

Outputs:
1. text - the copied string
2. error - an error string.

# DI - Design Intent 3 Ways

Note that I ignore the *error* outputs when discussing only DI...

## Tee 1

!![500](Tee-Tee1.drawio.svg)
One Echo component.  Its output is split two ways
1. to the output
2. to the filewriter

## Tee 2

!![500](Tee-Tee2.drawio.svg)
The input is split 2 ways
1. to the first Echo which feeds the output
2. to the second Echo which feeds the filewriter

## Tee 3

!![500](Tee-Tee3.drawio.svg)
The input is split 3 ways
1. to the first Echo which feeds the output
2. to the second Echo with an unconnected output (it generates its output, but the router drops the output)
3. to the third Echo which feeds the filewriter

Obviously this version is *contrived* and not very useful in this example form.  In general, though, it is desirable to use components while ignoring input ports and output ports.

# Bells and Whistles


!![500](Tee-Tee.drawio.svg)
This version uses the layout of Tee 1, but adds error handling.

In the specification, we say that Tee generates no output if an error is encountered.  This requires a Gate component that checks whether the File Write succeeded before allowing Echo's output to feed through to the output.

Echo is written (in Odin) to produce no output if an error is generated, i.e. it fires only one of its outputs
1. Echo generates an output if nothing went wrong
2. Echo generates an error if something went wrong, but does not generate an output in this case.

Ideally, the editor should show the DI layer separately from the Error layer, but, I haven't figured out how to accomplish this yet with draw.io (apparently, draw.io containers do not span across layers - a draw.io container is defined on only one layer which makes it impossible to draw only some of its ports (e.g. *error* ports) on another layer).

Note that one could create a different kind of *tee* component that had two inputs and four outputs

Inputs:
1. text
2. filename

Outputs:
1. text
2. error during the Echo operation
3. error during the file open operation
4. error during the file write operation.

This kind of component would have a different specification from that above.

Again, in this simple example, this kind of error nit-picking does not seem to be useful, but, there are use-cases where errors can be grouped into several classifications instead of all being lumped together under one umbrella.  In general, most problems have multiple *happy paths*.  Picking only one *happy path* and designating all other *paths* to be *error path*s is arbitrary.  A program needs to handle *all* paths.  In essence, every *path* is a *happy path* from a (full-blown) program's perspective.

For example, a File Selector screen widget might have several different *paths*:
1. user selected a valid, existing file
2. user cancelled the operation (e.g. by hitting ESC - escape)
3. file open error
4. file does not exist
5. invalid path
6. invalid filename.

In *function-based* programs, it is typical to consider one path to be the *happy path* and to lump all other paths together, considering them to be *unhappy path*s and to create *condition object*s describing the *unhappy* results. Such error condition overloading can lead to bloatware, where each caller must case-on the returned error condition. This kind of thing is seen in many textual languages. In the happy/unhappy paths given above, though, the error conditions are split (cased-on) by the Component, once, and, the "calling code" can deal with the separated conditions as necessary.  Note, also, that the "calling code" is free to lump several conditions into a single dataflow, if that makes more semantic sense and reduces code bloat. 

# Appendix - Building a Component
Components can be written in at least two ways:
1. Leaf: raw code in the underlying language, e.g. Odin
2. Container: composition of other components - Leaves or Containers

Components of any kind, Leaf or Container, can be placed on a working *palette*, like coloured paints on an artist's paint palette, then used to compose new Components (Containers) and / or full systems.

Coding breaks down into two categories
1. Writing code for a Leaf component
2. Composing Container components by simply wiring up components. This approach might be called *low-code*.  Only two "programming" operations are needed for editing components in this manner:
	1. drag'n'drop existing components
	2. connect ports.

Ideally, programmers should be allowed to use *any* language for implementing Leaf components, not just Odin.  We don't address this issue at this time, other than in a brute-force way, for example using *vsh*.

## Incremental Compilation
The current division of expending CPU cycles is typically broken down into
1. compile-time
2. run-time.

This division is arbitrary, and, too rigid.

We witness various sub-versions of this division in:
- JIT compilers - some compilation is done at run-time
- UNIX *ar*.  The UNIX archiver tool incrementally resolves some addresses at archiving-time and subsumes some of the work typically performed by operating system *loader*s.

In *drawware*, the composition of Containers using pre-existing Components can be incrementally compiled into new, opaque, components which can be used in subsequent compositions.

Partial, incremental compilation enables building of large systems that would otherwise be too cumbersome to compile in one fell swoop.

The concept of incremental compilation encourages thinking about sub-systems in layers, instead of using an "infinite canvas" perspective.

# Appendix - Namespace Issues
A Component is defined by three attributes:
1. its name
2. its collection of input ports, each with a name
3. its collection of output ports, each with a name

Each port in a namespace - input or output - must be unique within that namespace, i.e. each input port must be distinct from all other input ports (case matters).

The attributes are distinct.  For example, an output port can have a name that is the same as some input port or the Component name.

Names, control flow, etc. *inside* a Component cannot not leak out, hence, names within a Component are unique to the component and cannot conflict with names *inside* other Components.  Note that this kind of name scoping appears as the concept of *namespaces* and *packages* in other languages.

Note that Component and port names are *scoped* within whatever Container they reside in, hence, there is no global namespace. Scoped namespaces, typically, never grow very large.

# Appendix - Instantiation
A Component - Leaf or Container - may be used more than once inside a composed Component, i.e. a Container.  Each "copy" of a child Component is uniquely instantiated and, hence, has its own namespace and working memory.

In textual languages, each such instance must be uniquely named, whereas in drawware, such instance names are not needed - the (X,Y) position of a component on a diagram is sufficient to uniquely identify it. This is intuitive to most people, i.e. when they draw two boxes on a diagram, it is "obvious" which box is which.  Under-the-covers, though, a machine might need to assign some kind of unique ID to each Component on a diagram, but, users don't have to know about this detail.  

Note that memory addresses *are* unique IDs.  Most textual languages map user-defined names to unique memory addresses.  This is very apparent in the language C, which allows programmers to treat memory addresses as first-class language constructs, using operators like `&` and `*`.


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
