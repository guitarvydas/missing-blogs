# 2022-07-10-Parsing Short Phrases# **Parsing Short Text Phrases**

Paul Tarvydas
July 10, 2022

---

# Goal:

- How to parse a simple phrase?
- Example "Show prolog_bg at 0x-550."

---

# Example 
Data Structure Phrase from  [Ghost-Stars](https://oofoe.itch.io/ghost-stars)
	- https://oofoe.itch.io/ghost-stars

```
❖ Show prolog_bg at 0x-550. Move prolog_bg to 0x0
over 300 frames. Wait 150 frames.

		    CHEL:NA
	  The last time I saw
	  her... She was smiling. As
	  if she had some secret that
	  she couldn't wait to tell me.
	  
	  And then, in a sudden wash of
	  red, she was gone.
	  
	  Gone as if she had never stood
	  beneath the uncaring stars.

❖ Fade to black over 40 frames. Jump INTRO.
```

---

# How to parse 

"Show prolog_bg at 0x-550."?

---

# Step 1
Accept any character -> simple grammar.

---
# Step 2
Write a "grammar" for the phrase "Show prolog_bg at 0x-550."

---

# Step 3
Join (1) and (2) together.

Ohm-JS' *applySyntactic<...>* feature comes in handy.

---

# Demo Step 1

---

# Demo Step 2

---

# Demo Step 3.

---

# Step 4. 

Go to Town

Parse other phrases.

---

# Step 4 Gotchas

- Need to keep formatting (whitespace) intact for spoken bits.
- Don't care about whitespace for other bits.

---

# Lexical Rules
- PEG-like
- explicit handling of whitespace

---

# Syntactic Rules
- Ohm-JS feature
- skips over uninteresting whitespace
- preserves grammar purity
	- Grammar-programmer "UX"

---

# Demo Step 4.

```
  const grammar = String.raw`
GhostStarts {
text = macro+

macro = 
  | applySyntactic<ShowPhrase>
  | applySyntactic<MovePhrase>
  | applySyntactic<WaitPhrase>
  | applySyntactic<FadeToBlackPhrase>
  | applySyntactic<JumpPhrase>
  | lex_CHELNAspoken
  | lex_MEspoken
  | lex_RADIOspoken
  | period
  | separator
  | any
  
ShowPhrase = "Show" filename "at" Coordinate
MovePhrase = "Move" filename "to" Coordinate TimeSpan
WaitPhrase = "Wait" number "frames"
FadeToBlackPhrase = "Fade" "to" "black" TimeSpan
JumpPhrase = "Jump" ChapterName
lex_CHELNAspoken = "CHEL:NA" space* spoken
lex_MEspoken = "ME" space* spoken
lex_RADIOspoken = "RADIO" space* spoken

Coordinate = number "x" number
TimeSpan = "over" number "frames"
ChapterName = name
filename = name

spoken = spokenchar+
spokenchar = !separator any

separator = "❖"
period = "."

name = nameFirst nameRest*
nameFirst = letter
nameRest = "_" | digit | nameFirst
number = "-"? digit+
}
`;
```
---
# Format Matches

"Semantics" in Ohm-JS-speak.

---
# Ohm-JS
- write *semantics* in JavaScript

---
# FMT 
- use Ohm-JS grammar to create a DSL for writing *semantics*
- writes JS boilerplate
- SCN => Solution Centric Notation (YAGNI)

---

# Identity Transpiler
```
  const identityfmt = String.raw`
text [@macro] = [[!{macro}]]

macro [x] = [[!{x}]]
  
ShowPhrase [kShow filename kat Coordinate] = [[!{kShow}!{filename}!{kat}!{Coordinate}]]
MovePhrase [kMove filename kto Coordinate TimeSpan] = [[!{kMove}!{filename}!{kto}!{Coordinate}!{TimeSpan}]]
WaitPhrase [kWait number kframes] = [[!{kWait}!{number}!{kframes}]]
FadeToBlackPhrase [kFade kto kblack TimeSpan] = [[!{kFade}!{kto}!{kblack}!{TimeSpan}]]
JumpPhrase [kJump ChapterName] = [[!{kJump}!{ChapterName}]]
lex_CHELNAspoken [kCHELNA @spaces Spoken] = [[!{kCHELNA}!{spaces}!{Spoken}]]
lex_MEspoken [kME @spaces Spoken] = [[!{kME}!{spaces}!{Spoken}]]
lex_RADIOspoken [kRADIO @spaces Spoken] = [[!{kRADIO}!{spaces}!{Spoken}]]

Coordinate [number1 kx number2] = [[!{number1}!{kx}!{number2}]]
TimeSpan [kover number kframes] = [[!{kover}!{number}!{kframes}]]
ChapterName [name] = [[!{name}]]
filename [name] = [[!{name}]]

spoken [@cs] = [[!{cs}]]
spokenchar [c] = [[!{c}]]

name [nameFirst @nameRest] = [[!{nameFirst}!{nameRest}]]
nameFirst [letter] = [[!{letter}]]
nameRest [c] = [[!{c}]]
number [@kminus @digit] = [[!{kminus}!{digit}]]

period [c] = [[!{c}]]
separator [c] = [[!{c}]]
`;

```
---
# Lisp Transpiler
```
  const lispfmt = String.raw`
text [@macro] = [[\n(onenter\n!{macro})]]

macro [x] = [[!{x}]]
  
ShowPhrase [kShow filename kat Coordinate] = [[\n(image "!{filename}" !{Coordinate})]]
MovePhrase [kMove filename kto Coordinate TimeSpan] = [[\n(moveto "!{filename}" "???" !{Coordinate}!{TimeSpan} easin)]]
WaitPhrase [kWait number kframes] = [[\n(wait !{number})]]
FadeToBlackPhrase [kFade kto kblack TimeSpan] = [[\n(fadeout !{TimeSpan})]]
JumpPhrase [kJump ChapterName] = [[\n(jump "!{ChapterName}")]]
lex_CHELNAspoken [kCHELNA @spaces Spoken] = [[\n(say "CHEL:NA" "!{Spoken}")]]
lex_MEspoken [kME @spaces Spoken] = [[\n(say "ME" "!{Spoken}")]]
lex_RADIOspoken [kRADIO @spaces Spoken] = [[\n(say "RADIO" "!{Spoken}")]]

Coordinate [number1 kx number2] = [[!{number1} !{number2}]]
TimeSpan [kover number kframes] = [[!{number}]]
ChapterName [name] = [[!{name}]]
filename [name] = [[!{name}]]

spoken [@cs] = [[!{cs}]]
spokenchar [c] = [[!{c}]]

name [nameFirst @nameRest] = [[!{nameFirst}!{nameRest}]]
nameFirst [letter] = [[!{letter}]]
nameRest [c] = [[!{c}]]
number [@kminus @digit] = [[!{kminus}!{digit}]]

period [c] = [[]]
separator [c] = [[]]

`;
```
---
# JSON Transpiler
```
  const jsonfmt = String.raw`
text [@macro] = [[\n{ onenter:\n[!{macro}true]\n}\n]]

macro [x] = [[!{x}]]
  
ShowPhrase [kShow filename kat Coordinate] = [[\n["image","!{filename}",!{Coordinate}],]]
MovePhrase [kMove filename kto Coordinate TimeSpan] = [[\n["moveto","!{filename}","???",!{Coordinate}!{TimeSpan},"easin"],]]
WaitPhrase [kWait number kframes] = [[\n["wait",!{number}],]]
FadeToBlackPhrase [kFade kto kblack TimeSpan] = [[\n["fadeout",!{TimeSpan}],]]
JumpPhrase [kJump ChapterName] = [[\n["jump","!{ChapterName}"],]]
lex_CHELNAspoken [kCHELNA @spaces Spoken] = [[\n["say","CHEL:NA","!{Spoken}"],]]
lex_MEspoken [kME @spaces Spoken] = [[\n["say","ME","!{Spoken}"],]]
lex_RADIOspoken [kRADIO @spaces Spoken] = [[\n["say","RADIO","!{Spoken}"],]]

Coordinate [number1 kx number2] = [[!{number1},!{number2}]]
TimeSpan [kover number kframes] = [[!{number}]]
ChapterName [name] = [[!{name}]]
filename [name] = [[!{name}]]

spoken [@cs] = [[!{cs}]]
spokenchar [c] = [[!{c}]]

name [nameFirst @nameRest] = [[!{nameFirst}!{nameRest}]]
nameFirst [letter] = [[!{letter}]]
nameRest [c] = [[!{c}]]
number [@kminus @digit] = [[!{kminus}!{digit}]]

period [c] = [[]]
separator [c] = [[]]

`;
```
---
# Github
https://github.com/guitarvydas/ghost_stars