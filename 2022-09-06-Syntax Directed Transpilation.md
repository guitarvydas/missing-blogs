# 2022-09-06-Syntax Directed Transpilation# Overview Syntax Directed Transpilation
I want to transpile JSON *component* description to code, e.g. Python, Javascript, etc.

I want to use pattern-matching to avoid *if...then...else* statements in my code.

Pattern-matching generalizes to *parsing* - a technique explored in the 1960's for compiler building.

The technique can be used for other kinds of software, not just compiler-building.

I describe the technique in this set of slides.

---
# General Idea
The idea is to create code in a series of steps that can use pattern-matching.

Basically, I build a pipeline, where each stage does a little bit of work, then passes the modified data further down the pipeline, like a baton.

At this time, the most common pattern-matching tools work with *text* data.

So, I'll go with those text-based tools.

The most general pattern-matcher for *text* is PEG ("parsing expression grammars").

The easiest-to-use tool I've found is Ohm-JS - a pattern-matching language built on PEG principles.

The general idea is to build a mini "syntax" for each stage in the pipeline, then, use a text pattern-matcher to match the text at each stage, and to hang bits of code off of the matches (match captures).

I describe my pipeline below.

Each step in the pipeline is a code transformer.

Some steps transform the code and pass it down the pipeline.

Other steps simply output a chunk of code and discard the rest of the input.

At the end of the pipeline, all transformed chunks are glued together into a final program.

The code bits are wrapped in *verbatim brackets*.  The pattern-matchers simply skip over *verbatim* code and leave it alone.  PEG makes it possible to create nested *verbatim* chunks, so we don't need to worry about trying to create chunks in only a flat manner.  Worrying about keeping the chunks flattened is like premature optimization - worrying about flattening adds complication.  It is best to remove complication at first, then to add it back in later - after the basic design is working.

# Pipeline
!![sdt/syntax directed transpilation.png](images/syntax directed transpilation.png)
# The Successive Transformations
## Source JSON
```

[
  [
    {
      "children": [ {"kind":"Hello", "name":"cell_7"},  {"kind":"World", "name":"cell_8"} ],
      "connections": [
	{
	  "receivers": [ {"receiver": {"component":"cell_7", "port":"b"}} ],
	  "senders": [ {"sender": {"component":"cell_6", "port":"a"}} ]
	},
	{
	  "receivers": [ {"receiver": {"component":"cell_8", "port":"d"}} ],
	  "senders": [ {"sender": {"component":"cell_7", "port":"c"}} ]
	},
	{
	  "receivers": [ {"receiver": {"component":"cell_6", "port":"f"}} ],
	  "senders": [ {"sender": {"component":"cell_8", "port":"e"}} ]
	}
      ],
      "id":"cell_6",
      "inputs": ["cell_17" ],
      "kind":"HelloWorld",
      "name":"HelloWorld",
      "outputs": ["cell_15" ],
      "synccode":""
    }
  ],
  [
    {
      "children": [],
      "connections": [],
      "id":"cell_7",
      "inputs": ["cell_12" ],
      "kind":"Hello",
      "name":"Hello",
      "outputs": ["cell_10" ],
      "synccode":""
    }
  ],
  [
    {
      "children": [],
      "connections": [],
      "id":"cell_8",
      "inputs": ["cell_11" ],
      "kind":"World",
      "name":"World",
      "outputs": ["cell_14" ],
      "synccode":""
    }
  ]
]

```
## Self-Insertion
This step simply inserts 1 line before each component - `.="cell_..."`.

`.` means `self` here.

This is automated *declaration before use* and helps *syntax directed transpilation* in the later steps.
```
[
.="cell_6" [{
"children":[{"kind":"Hello","name":"cell_7"},{"kind":"World","name":"cell_8"}],
"connections":[ {"receivers":[{"receiver":{"component":"cell_7","port":"b"}}],"senders":[{"sender":{"component":"cell_6","port":"a"}}]} {"receivers":[{"receiver":{"component":"cell_8","port":"d"}}],"senders":[{"sender":{"component":"cell_7","port":"c"}}]} {"receivers":[{"receiver":{"component":"cell_6","port":"f"}}],"senders":[{"sender":{"component":"cell_8","port":"e"}}]}]


"kind":"HelloWorld"


}],
.="cell_7" [{
"children":[],
"connections":[]


"kind":"Hello"


}],
.="cell_8" [{
"children":[],
"connections":[]


"kind":"World"


}]]
```
## Self Replacement
In this step, the above `.=...` self declaration is used to replace all references to a specific id with `.` (self)

In this particular example, "cell_6" is the specific id.  All references to `cell_6` are now changed to `.`.

Again, this transformation makes the work easier for the succeeding passes.

```
[
    [{
	"children":[{"kind":"Hello","name":"cell_7"},{"kind":"World","name":"cell_8"}],
	"connections":[
	    {"receivers":[{"receiver":{"component":"cell_7","port":"b"}}],
	     "senders":[{"sender":{"component":".","port":"a"}}]}
	    {"receivers":[{"receiver":{"component":"cell_8","port":"d"}}],
	     "senders":[{"sender":{"component":"cell_7","port":"c"}}]}
	    {"receivers":[{"receiver":{"component":".","port":"f"}}],
	     "senders":[{"sender":{"component":"cell_8","port":"e"}}]}]
	"kind":"HelloWorld"}],
    [{
	"children":[],
	"connections":[]
	"kind":"Hello"}],
    [{
	"children":[],
	"connections":[]
	"kind":"World"}]
]
```
## Code Generation
The above transformations have added enough information to make it possible to generate code.

In this example, we will generate Python code.

It should be possible to generate code for many languages.

### Stock Imports
The first step in code generation is to create the boilerplate *imports* statements.

This can be done by creating a simple string.
```
      const boilerPlateImports = `
${lv}
from message import Message
from container import Container
from connect import Connect
from sender import Sender
from receiver import Receiver
${rv}
`;
      
```
We wrap the boilerplate in *verbatim brackets* to ensure that this code is not touched, nor parsed, in later passes.

We use ${lv} and ${rv} from `chars.js` for the definitions of the *verbatim brackets* (`lv` means *left verbatim* and `rv` means *right verbatim*).
### Child Imports
This next step actually does some work.

It parses out the *child* description from the JSON and creates *imports* statements for each child.

Do we need to ensure that only one *imports* is defined, regardless of how many times a class is instantiated by different children?  I don't know.  What does Python do with multiple *imports* statements that overlap?  I don't know.  In this example, there is exactly one child instantiated from every class.  We can side-step the issue for this example.  

Ideally, we would want a library function that deletes duplicate entries, then, emit the *imports* statements for each non-duplicated string.

In the end, we want to generate this...

```



‹from Hello import Hello›
‹from World import World›
```
What about capitalization?  Do we want to generate`‹from hello import Hello›`.  I don't know, yet.  MacOS ignores case in filenames, but Linux doesn't.

# Pipeline Description
1. The first stage of the pipeline inputs the JSON source file, modifies it a bit, then sends it down the pipe.
	- In this example, the first pass just looks at the incoming JSON and inserts a declaration of *self* at the front.  This is like enforcing declaration-before-use, but is done by the machine, not the programmer.  Another way to approach this problem is to build a *tree* then walk up and down the tree to extract the required information.  I find that syntax-directed transpilation is easier than tree-walking - it lets me concentrate on only one problem at a time.
2. The second state of the 

# Verbatim
