# 2022-07-09-Old Reality vs New Reality
# Synopsis
Old Reality - clay tablets and sticks.  New Reality - scalable vector graphics on electronic displays.

SVG subsumes text.  One kind of "markdown" syntax for SVG is: text.

Old reality markings must be arranged in strict, non-overlapping grids.  New reality markings do not need to use grids.

New reality media is not yet popular for programming.

# Media
## Old Reality
- clay tablets and sticks
- paper and sticks (graphite, opaque liquid dyes (ink, paint))
 
### Implications
Markings must be arranged in strict grids of non-overlapping cells.

Old reality cells are so common that humans created a name for these cells: "characters".

Hardware assist, in the form of fixed-sized bitmaps, was invented in mid-1900s.

(x,y) used as coordinates for cells, with restrictions on the values of (x,y)
	- left-to-right orientation
	- sequential line-based  orientation.

Time (t) ignored.

Grid mentality permeates all programming language designs.

Github attempts to introduce (t) into program development.

## New Reality
Vector Graphics on phones and computer displays.

No restrictions on (x,y) values for cells.

Time (t) constitutes an aspect of new reality notations (animations, video).

(x,y,t) used as coordinates for cells.

(x,y,z,t) can be simulated using perspective calculations.

Hardware assist (???, gaming engines?).

New reality media used for non-programming applications, e.g. spreadsheets, word processors.

New reality media not popularly used yet for programming.

Scalable Vector Graphics (SVG) includes text, but is not restricted to using only text.

# Markdown
Markdown is a way of simplifying a complicated notation.

Simplicity: lack of nuance.

Markdown ".md" has many flavours.  There are many directions in which a notation can be simplified, hence, there cannot be "just one" markdown.  Other factors determine which markdown notation becomes more popular.

## Markdown for SVG
Text.

Text is very popular, but SVG can express more than just text.

## Markdown for HTML
Markdown (".md") syntax is based on old reality media.

Availability, such as Github Pages and markdown editors, has influenced the popularity of certain markdown dialects.

# Visual Programming Languages
VPL is currently assumed to mean the act of parsing Art to derive programs.

But, there is a mid-way point between Text and Art.  Technical Diagrams (DaS[^das]).
- Rectangles
- Ellipses
- Lines
- Text.

[^das]: DaS means Diagrams as Syntax.

Professions, other than computer programming, have adopted technical diagrams as media for expression of certain concepts, e.g.
- blueprints in structural Engineering
- schematics in Electrical Engineering
- diagrams of molecules and inter-atomic bonds in Chemistry

Technology improvements supporting (x,y,t) notations are breaking new ground is what is expressible.

# 0D - Zero Dependencies
A prerequisite for (x,y,t) media is that there be no dependencies between cells.

Cells can be placed "anywhere" in the medium, not just on line-oriented grids.

Most current programming languages have dependencies built-into them under-the-hood.  

Functions and stacks create hidden dependencies.

Functions are state machines, containing states such as "blocked, waiting for callee to return a value".  

Functions model clay-tablet media well, but do not model (x,y,t) media very well.

Distributed computing is hampered by function-based notation.  It is not impossible to model (x,y,t) using functional notation, but, the amount of detail required to express such concepts interferes with free-flowing ideas in the realm of distributed ("free-will", "asynchronous") processing.
