# 2023-06-10-DaS - Diagrams as SyntaxSeveral drawing (visual) editors exist, e.g. draw.io, Excalidraw, etc.  They all boil diagrams down into textual representations.  The resulting text is not very human-readable, but, that doesn't matter.  Humans don't need to read the text, only machines - PEMs (Programmable Electronic Machines, aka "computers") - need to read the text.  Humans can draw diagrams, machines can transpile the diagrams into text.  The fact that these diagrams boil down to text means that we can use existing textual language tools to further compile the diagrams into binary code.  Coupled with the trick of using existing compilers, this means that programmers can build diagram-based programs, then, compile the diagrams to binary code using only a small amount of effort (e.g. hours/days instead of years or never).

There is no need to use technologies that transpile text to diagrams, like Planet-UML, xstate, Graphviz. Instead, programmers can draw diagrams and have machines transpile the diagrams into binary code.  I call this DaS - Diagrams as Syntax.

Note that this is not the same as *modeling* action code.  It is the same as *compiling* program text.  

Furthermore, I'm not suggesting that we can compile any Rembrandt painting into binary code.  I am suggesting that we can pick-and-choose various figures and compile diagrams based on this small set of figures, to code.  

For starters, we could choose figures such as:
- rectangles
- ellipses
- arrows
- text
- groupings of the above and of other groupings.

Note that this set of figures is already covered in a notation called SVG.

SVG was intended to be used to create and display fancy artwork.  We can pick-and-choose a very small subset of SVG and use that small subset as a programming language.

Note, also, that I am not suggesting that graphics be used to the exclusion of text.  There are some things that text expresses better - more succinctly - than diagrams, for example `a = b + c`.  I am suggesting a hybrid syntax - text plus a small set of graphical figures.

Maybe the biggest difference here is that graphical figures, including figures that contain text, are resizable.  Most of our programming editors rely on grids of fixed-sized bitmap cells that we call "characters".  I am suggesting the use of cells - "figures" - but, also allowing the cells to be resized by the programmer.  Cells are vector-based instead of being bitmap-based, like 1950s on-screen characters in EBCDIC and ASCII.
