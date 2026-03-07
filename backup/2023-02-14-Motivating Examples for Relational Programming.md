# 2023-02-14-Motivating Examples for Relational ProgrammingI find it necessary to have a concrete example in mind when studying a new concept.  I find it more difficult to simply accept the details of a concept without knowing what it might be used for.

In that spirit, in case it helps anyone else, I've included a simplified concrete example of how relational programming could be used.

First, though, I set up the discussion by giving my beliefs about the essence of relational programming...

# The Essence of Relational Programming

I conclude that Relational Programming breaks down into very simple concepts:
- triples - {subject, relation, object}
- exhaustive search

## Exhaustive Search
Exhaustive search is enabled by the concept of Unification.  

Exhaustive search can be accomplished in at least two ways:
- backtracking
- feed-forward.

The concept of backtracking is like writing loops within loops.  Some of the loops contain *pause* mechanisms that display intermediate results before moving on to finding more matches.

Backtracking was explored in languages like PROLOG.  Writing algorithms for correct backtracking can be a tricky business.  Backtracking is motivated by the desire to conserve and reuse memory.

Feed-forward is a simple technique that maintains a list of all possible matches and prunes options from the list as information is developed.  MiniKanren, I believe, uses a feed-forward strategy.  In feed-forward, use of memory is not an issue.  Naive implementations (i.e. correct ones), create duplicate information to represent each active match possibility.  Complications arise in attempts to optimize-away duplication, e.g. through the use of DAGs.  Optimization destroys scalability, since optimized data structures are shared between match paths and cannot be easily distributed except as whole units of bundled-up information.  Various optimization strategies, such as caching, have been invented, but usually involve unexpected gotchas.

Parsing tools based on PEG technology, such as Ohm-JS, perform some kind of backtracking.  PEG is a set of rules that limits the possibilities for backtracking and (in Packrat parsers) caches the results of partial matches.  In other words: PROLOG does more general backtracking than PEG parsers.  PEG technology is optimized for the act of parsing ("pattern matching" of text) and eschews other forms of generalized backtracking. PEG doesn't exhaustively "try" every possibility, but it is sufficient for most uses of pattern matching.  The original PEG paper was written using Haskell.

## Triples

Every operation breaks down into a triple - two agents and a relationship between them.

Triples are hard for Humans to read due to the overwhelming amount of detail.  Triples, though, are easy for machines to understand[^asm].

[^asm]: N.B. The programming languages that are called Assemblers are based on the concept of line-oriented triples, e.g. `MOV R0,R1`

Layers of syntactic skins, such as Currying and Functors, have been invented to elide tripleness.  For example, a curried function *appears* to be a double - a function of one argument - but breaks down into a triple nonetheless, just being chunked differently.  One agent is wrapped together with the relation to create the appearance of a single entity which must be resolved by applying the wrapped function to a second agent.

!
## 2023-02-14-Motivating Examples for Relational Programming 2023-02-15 06.23.29.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Subject ^3Dp2UgJd

Object ^gaETIl2p

Relation ^C9G1OWvT

Triple ^zOk7iVhq

Subject ^Sjm5OgqY

Object ^npTKoXBY

Relation ^AcdyUvqq

Curried Function ^yn6cf4aM



# Motivating Examples

Exhaustive search can be used for parsing and for pattern-matching.

Below, I list some simple examples of parsing.

Syntax, such as that of PROLOG, can make it easy to write patterns and to match for them.

Commonly accepted syntax for parsing, such as BNF, are essentially subsets of PROLOG syntax in disguise.

In PROLOG, textual identifiers that are capitalized represent "logic variables".  The *unification* algorithm inserts concrete values into such logic variables and rewrites logic variables as needed, changing the values of the variables automagically.

# text
bob talks to alice
alice talks to john

Who talks to alice?
Who <- bob.

Who2 does alice talk to?
Who2 <- john.

!
## 2023-02-14-Motivating Examples for Relational Programming 2023-02-15 06.37.47.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
bob ^Btbr6PE3

talks to ^5wgcdLtE

alice ^L6cntDZJ

john ^JrF4sj7V

talks to ^nX17Z64M

alice ^CYXwlrpW

Who2 ^8pui35fX

talks to ^tPk1nBmD

alice ^YbseQ9qs

Who ^B4FJpqVY

talks to ^u7iR3P3L

alice ^JdnwisL4



## re-ordering
The following phrases have the same meaning as "Alice talks to John"...
- alice john talks to
- talks to alice john

Exercise: write code that converts the above post-fix and pre-fix notation into the infix notation of the preceding section, e.g.  change "alice john talks to" into "alice talks to john".

Rhetorical question: is it easier to parse if you know that *everything* is written in pre-fix notation instead of a mixture of pre-fix and in-fix notations?

Rhetorical question: what programming language(s) use pre-fix notation only?

Rhetorical question: what programming language(s) use post-fix notation only?

Rhetorical question: which kind of syntax, pre-fix, post-fix, in-fix is more amenable to Human consumption?

Rhetorical question: which kind of syntax, pre-fix, post-fix, in-fix is more amenable to Machine consumption?


# drawing
Technical drawings can be easy to parse, if one is careful to select figures that can have concrete meanings.

This kind of thing is *exacly* how textual programming languages were developed.  Instead of groking all of the English language, language designers selected only a few constructs, like "if then else" and parsed and compiled those phrases into Assembler.

I argue that a useful subset of Art can be reduced to a small set of figures that can be parsed and compiled to Assembler.

I argue that a useful subset of graphical figures consists of:
- rectangles
- ellipses
- arrows
- text
- groups.

Note that there is a difference between the graphical figures above and textual languages.  The graphical figures can be resized, they can overlap and need don't need to be arranged on grids.  "Selection" is kind-of built into drawings, as grouping, instead of being relegated only to the editor.  "Grouping" is a recursive, nesting relationship which is represented in a mostly ad-hoc manner in textual languages as "scoping".

What are the relationships that we need to grok in order to understand drawings?  We already know how to parse sequences.  I argue that we only need a few more constructs, like
- containment
- connection.

The motivating examples listed below explore these issues...

## simple containment
!
## 2023-02-14-Architecting Software 2023-02-14 13.58.15.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
A ^HwO1VudK

B ^dFBSHZbZ



B is contained in A
A contains B

The drawing has 4 figures on it:
1. rectangle
2. rectangle
3. text "A"
4. text "B"

I drew the diagam in Excalidraw.com and saved it.  I've included the saved data below:
```
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "type": "rectangle",
      "version": 260,
      "versionNonce": 1204383383,
      "isDeleted": false,
      "id": "_tRBtKh8ZHB0MpfYZdd8k",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 498.8421173095703,
      "y": 256.41705322265625,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 246.31576538085938,
      "height": 145.1658935546875,
      "seed": 540477640,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "boundElements": null,
      "updated": 1676402154451,
      "link": null,
      "locked": false
    },
    {
      "type": "rectangle",
      "version": 278,
      "versionNonce": 1788080889,
      "isDeleted": false,
      "id": "yOnRrahzlbL5M8ka6WAA4",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 557.4992065429688,
      "y": 309.5814208984375,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 130.78890991210938,
      "height": 62.6619873046875,
      "seed": 1764804536,
      "groupIds": [],
      "roundness": {
        "type": 3
      },
      "boundElements": null,
      "updated": 1676402154452,
      "link": null,
      "locked": false
    },
    {
      "type": "text",
      "version": 136,
      "versionNonce": 1322397817,
      "isDeleted": false,
      "id": "WK4tA0PT2vUFCNYOYFWEg",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 613.9095306396484,
      "y": 267.30113220214844,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 15,
      "height": 25,
      "seed": 350924744,
      "groupIds": [],
      "roundness": null,
      "boundElements": null,
      "updated": 1676402154452,
      "link": null,
      "locked": false,
      "fontSize": 20,
      "fontFamily": 1,
      "text": "A",
      "baseline": 18,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "originalText": "A"
    },
    {
      "type": "text",
      "version": 186,
      "versionNonce": 1693629465,
      "isDeleted": false,
      "id": "FXUeVWVENYAeu1sDGNDtS",
      "fillStyle": "hachure",
      "strokeWidth": 1,
      "strokeStyle": "solid",
      "roughness": 1,
      "opacity": 100,
      "angle": 0,
      "x": 613.6601409912109,
      "y": 313.96826171875,
      "strokeColor": "#000000",
      "backgroundColor": "transparent",
      "width": 17,
      "height": 25,
      "seed": 137302200,
      "groupIds": [],
      "roundness": null,
      "boundElements": null,
      "updated": 1676402154452,
      "link": null,
      "locked": false,
      "fontSize": 20,
      "fontFamily": 1,
      "text": "B",
      "baseline": 18,
      "textAlign": "left",
      "verticalAlign": "top",
      "containerId": null,
      "originalText": "B"
    }
  ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

Ignoring most of the information, we see:
1. rectangle 
	- "id": "_tRBtKh8ZHB0MpfYZdd8k"
	- "x": 498.8421173095703
	- "y": 256.41705322265625
	- "width": 246.31576538085938
	- "height": 145.1658935546875

2. rectangle
	- "id": "yOnRrahzlbL5M8ka6WAA4"
	- "x": 557.4992065429688
	- "y": 309.5814208984375
	- "width": 130.78890991210938
	- "height": 62.6619873046875
3. text
	- "id": "WK4tA0PT2vUFCNYOYFWEg"
	- "x": 613.9095306396484
	- "y": 267.30113220214844
	- "text": "A"
	- "width": 15
	- "height": 25
	- "fontSize": 20
4. text
	- "id": "FXUeVWVENYAeu1sDGNDtS"
	- "x": 613.6601409912109
	- "y": 313.96826171875
	- "text": "B"
	- "width": 17
	- "height": 25
	- "fontSize": 20

Rhetorical question: what inferences can you make given only the culled information?

Rhetorical question: is rectangle (1) larger than rectangle (2)?  Is rectangle (1) smaller than rectangle (2)?  Are they the same size?

Rhetorical question: is rectangle (2) "inside" of rectangle (1)?  How can you tell? (Spoiler: only grade-school math is required).

Rhetorical question: what about texts (3) and (4).  Are they inside any of the rectangles?  Is either text inside more than one rectangle?

Rhetorical question: if you had to write code to get a machine to make the above inferences, what language(s) would you prefer to use?  E.g. Assembler, Lisp, PROLOG, miniKanren, Javascript, Python, Haskell, Rust, etc.?

## slightly more complicated containment
!
## 2023-02-14-Architecting Software 2023-02-14 14.00.08.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
A ^cfQAsvAG

B ^4wybhV9l

C ^p0VThTJw

D ^csTX0Eq1


A contains B
B contains C
C contains D

How do you write code that figures out these facts?

"Writing code" means creating a script that a computer can step through and execute.  The script must contain excrutiating amounts of detail.  A script (aka "assembler program") must contain enough detail so that even a dumb machine can create the expected answer by blindly following the steps specified in the script.

## simple connection
!
## 2023-02-14-Architecting Software 2023-02-14 14.04.47.excalidraw

---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
A ^XnvimRqx

B ^5Z51bjqv


A is connected to B.

Q: How would you write code to figure this out?

Hint: I see 7 figures (rect, rect, text, text, ellipse, ellipse, arrow) and three colours (black, yellow, green).  Is emptiness a "colour"?  If so, maybe there are four colours, or, maybe there is a lack-of-colour property?  Does it matter?  To my eyes, only the colours of the ellipses matters. I don't even care about the fill style - that's for the editor worry about, not my problem.
