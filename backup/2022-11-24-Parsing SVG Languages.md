# 2022-11-24-Parsing SVG Languages- SVG is a text representation of a diagram
- as such, we can use existing text-parsing technologies
	- my favourite parsing technology, ATM, is Ohm-JS
	- PEG is better than LR(k) (Language Theory)
		- because PEG can specify patterns that include matching brackets, Language Theory can't
	- Ohm-JS is based on PEG
		- Ohm-JS makes PEG easier-to-use
		- Ohm-JS allows unicode
		- Ohm-JS's Ohm-Editor is a god-send - a REPL for developing grammars
		- Ohm-JS does "the right thing" by separating semantics away from grammars
			- the result is much easier to read, not a jumble of issues
		- Ohm-JS makes it easier to write identity transpilers
			- no change to uninteresting characters, including whitespace
- restrict "syntax"
	- in the same way that 1950s Programming Languages don't parse all of English prose, 2022++ VPLs can restrict themselves to parsing only a subset of what can be drawn
		- I favour only a few kinds of drawing elements:
			1. rectangles
			2. ellipses
			3. lines
			4. text
			5. groups
			6. attributes, colour?
		- missing
			- containment (e.g. "box B is inside box A", ...)
			- x,y position relationship shortcuts ("intersects" (maybe "above", "below", "left of", "right of"))
			- src/dest for connections
				- can be inferred using existing techniques
		- (x,y) allows overlapping elements (e.g. rectangles that overlap and contain, text windows that overlap, etc.)
		- (x,y) makes names moot (unique instances are visually obvious, names are not needed (similar to de Bruijn indices in Lambda Calculus?))
- draw.io format
	- drawio.io uses GraphML
	- GraphML is like SVG (and XML)
	- drawio.io allows multiple tabs, each tab containing one drawing
		- each drawing is compressed, but, can be easily decompressed to text
		- a .drawio file is not compressed overall
			- text is used to express multiple drawing tabs, where the drawings, though, are compressed