# 2022-06-18-Shuhari - Elements of SHU
The *shu* part of *shuhari* is 
- _shu_ (守) "protect", "obey"—traditional wisdom—learning fundamentals, techniques, [heuristics](https://en.wikipedia.org/wiki/Heuristic "Heuristic"), proverbs

According to [wikipedia](https://en.wikipedia.org/wiki/Shuhari)

To enable *shu* for programming...
- the program must be human readable, understandable, simple
- the program must be clonable and hackable.

A *program* is a script of instructions that control a machine ("computer").  

Note that there are no fundamental rules specifying *how* a script must be represented.


## Programs as Text
Historically, programmers have represented programs in text form.

This historical represenation is due to the limitations of mid-1900s computing hardware and accompanying biases towards optimization of program representation.  This historical representation is, also, based on the idea of forcing the paper-and-pencil notation of mathematics onto programming.

Programs are often thought of as being composed of grids of non-overlapping, small bitmaps, read from top-to-bottom and left-to-right.  This format is text composed of characters.  Typically, text programs are written using QWERTY keyboards.

### Runtime Inefficiency

CPU APIs, called *assembler*, tend to contain runtime grouping constructs for forming islands of progamming instructions and invoking the islands at runtime via CALL and RETURN instructions.

The islands are called routines (functions).

The islands pack and unpack data using CPU runtime operations.  Incoming data is called *parameters* and outgoing data is called *return values*.  Programming languages formalize the concepts of packing and unpacking, calling the processes structuring and destructuring.

Representing program scripts in this way entails a certain amount of runtime inefficiency, since CPU cycles are expended to create routines and data structuring.

## Programs as Technical Diagrams

Many longer-lived Engineering professions use diagrams instead of text, to represent designs.

For example,
- building construction is specified with diagrams called "blueprints"
- chemical analysis uses diagrams called molecular models, atomic models and [structural fomulae](https://en.wikipedia.org/wiki/Structural_formula)
- electronics engineering uses diagrams called schematics
- Feynman diagrams are used in a section of Physics
- etc.

Presently, the field of Software is young and a diagrammatic form for programs as not been standardized.

One of the blocking factors in developing diagrammatic programs is the over-use of synchrony in current-day programming languages.  

Program units need to be 0D (zero-dependency), but, tend to be N0D (non-zero-dependency).

The concept of 0D is usually tangled up with other concepts such as parallelism and concurrency.

Programmers have created work-arounds to the 0D problem, in the form of package managers, makefiles, etc.  These work-arounds have allowed practitioners to continue using N0D programming notations without improving the state of the field of programming.

## Editors
To allow for the basic elements of SHU, program representations must be easy to read, clone and hack.

Programmers use editors to create program representations.

Editors for textual programming are mostly based on the character model.

Editors for diagrams are most often based on creating paintings instead of creating technical diagrams.

Editors for non-programming tasks, such as word-processing, spreadsheets, etc., have advanced further than editors for programming tasks.

## Simplicity
Simplicity is defined as "the lack of nuance".

Options are nuances, hence, give the appearance of complexity.

Parameters are nuances, hence, give the appearance of complexity.

Up-front decisions, like "where do you want to create this file?" are technical nuances, hence, are perceived as complex.  I have encountered only two (2) applications that allow you to jot ideas down without being confronted with up-front decisions, (a) Scapple, and (b) Kinopio.  So-called "mind maps" generally fail at simplicity, by imposing structure on the thinking process.  Jotting ideas down on the back of envelopes is a simple process that allows after-the-fact structuring and organization.  Most software applications do not achieve this level of simplicity.

## Making Do
Currently, I use [draw.io](https://app.diagrams.net) to create technical diagrams.

I transpile these diagrams to "structured text" then process the structured text using text parsing tools such as Ohm-JS.

Transpilation from technical diagrams (`.drawio`) to textual form (`.das`) can be done:
- in an automated fashion, using a combination of Javascript and PROLOG (or other technologies)
- manually, e.g. sight-reading diagrams into a brace-bracketed textual format, for example, 
## Diagram Handling



![](handling.png)


The *handler* code is part of the Cos (component O/S) code.  

I've used diagrams to show the workings of this code as an example that this technique can be used for systems programming (i.e. writing low-level synchronous code).

I drew out the logic for the *handler* code as diagrams of nested boxes.

I, then, transpiled the diagram to `handling.das`.  The transpilation was done manually, to avoid excessive details in this example, and, to show the 1:1 correspondence of diagrams to `.das` code.

I used Ohm-JS to transpile `handling.das` into `handling.js`.  The transpiler is located in https://github.com/guitarvydas/duct, and invoked by `make handling.js`

The code for the transpiler (grammar plus re-format) are discussed in 
### Transpiler DaS

## Grammar
dia.ohm
```
dia {
  Main = Implementation+
  Implementation = ContainerImplementation | SynchronousLeafImplementation

ContainerImplementation =
  | "implementation" name "(" NameList ")" SequenceOfBoxes -- withParam
  | "implementation" name SequenceOfBoxes -- noParam

SynchronousLeafImplementation 
  = "sync" name "<=" DatumList Box -- withFormals
  | "sync" name                Box -- withoutFormals

SequenceOfBoxes = NestedBox+
NestedBox = Box
NB = NestedBox
Box = "{" BoxOperation Box? "}"
OrElse = "{" "orelse" Box "}"

BoxOperation
  = ForEvery
  | Synonym
  | FindConnectionFromMe
  | Find
  | Lookup
  | WithLock
  | Cond
  | VarBox
  | WhenAll
  | When
  | Return
  | CheckReturn
  | SynchronousCall
  | Pass

WhenAll = "when" "all" PredicateBlock NestedBox
When = "when" "messages" NB?
Return = "->" DatumList NB?
CheckReturn = "check" "return" string NB?
FindConnectionFromMe = "find" Datum "from" "me" "on" "port" Datum NB OrElse NB?
Pass = "pass"

Cond = "cond" FirstCondClause RestCondClause*
FirstCondClause = CondClause
RestCondClause = CondClause
CondClause = "{" Predicate Box "}"

WithLock = "lock" Datum NB?

Find
  = "find" name "in" Datum "given" ParameterList "=>" name NB OrElse NB? -- withParams
  | "find" name "in" Datum                       "=>" name NB OrElse NB? -- withoutParams

VarBox =
  | "var" name "<=" "$i" "{" "{" DatumList "}" Datum "}" NB? -- inputmessage
  | "var" name "<=" "$o" "{" "{" DatumList "}" Datum "}" NB? -- outputmessage
  | "var" name "<="          "{" DatumList "}" NB?           -- array

Synonym =
  | "synonym" name "=" "{" DatumList "}" NB? -- obj
  | "synonym" name "=" Datum NB?             -- solitary

Lookup =
  | "lookup" Datum "=>" name NB?

ForEvery
  = "for" "every" "item" "in" Datum "given" ParameterList "=>" name NB? -- sugaredWithParams
  | "for" "every" name "in" Datum "given" ParameterList "=>" name NB? -- withParams
  | "for" "every" "item" "in" Datum  "=>" name NB? -- sugaredWithoutParams
  | "for" "every" name "in" Datum  "=>" name NB? -- withoutParams


SynchronousCall =
  // no nesting here - Call is a Leaf, not a nested box
  | "@" Datum "<=" Datum -- params
  | "@" Datum            -- noparams
  | "#" Datum "<=" Datum -- external_params
  | "#" Datum            -- external_noparams


Datum
  = Datum "of" Datum -- field
  | Datum "." Datum  -- dottedField
  | kwPORT          -- port
  | kwME            -- me
  | name            -- name

Predicate =
  | Datum "is" "not" "me" -- notme
  | Datum "is" "me"      -- me
  | Datum "==" Datum -- eq
  | Datum "!=" Datum -- ne

PredicateBlock = "{" Predicate PredicateMore* "}"
PredicateMore = Predicate

ParameterList
  = Datum "X" ParameterList -- list
  | Datum                   -- solitary

DatumList 
  = Datum "," DatumList -- list
  | Datum               -- solitary

NameList 
  = name "," NameList -- list
  | name              -- solitary

  separator
    = "<="
    | "=>"
    | "->"
    | "//"
    | "=="
    | "!="
    | "$i"
    | "$o"
    | "="
    | "{"
    | "}"
    | "("
    | ")"
    | "@"
    | "#"
    | "."
    | ","
    | eol

keyword
  = &(!namecharFirst)
          ( "implementation"
          | "messages"
          | "orelse"
          | "return"
          | "given"
          | "lookup"
          | "every"
          | "check"
          | "pass"
          | "lock"
          | "find"
          | "from"
          | "cond"
          | "with"
          | "when"
          | "item"
          | "sync"
          | "port"
          | "for"
          | "all"
          | "not"
          | "is"
          | "in"
          | "on"
          | "of"
          | "me"
          | "X") 
   &(!namecharRest)

kwME = &(!namecharFirst) "me" &(!namecharRest)
kwPORT = &(!namecharFirst) "port" &(!namecharRest)

string = dq (!dq any)* dq
dq = "\""
    
eol = "\n"

name = namecharFirst namecharRest*
namecharFirst = !separator !keyword ("_" | "A" .. "Z" | "a" .. "z")
namecharRest = !separator !keyword ("_" | "A" .. "Z" | "a" .. "z" | "0" .. "9")

space
 += comment

comment
  = "//" (!"\n" any)* "\n"  -- singleLine
  | "/*" (!"*/" any)* "*/"  -- multiLine

}
```
## Re-Formatter
dia.fmt
```
Main [@i] = [[const msg = require ('./message');\n${i}]]
Implementation [x] = [[${x}]]

ContainerImplementation_withParam [ki name lp formal rp b] = [[exports.${name} = function (_me, ${formal}) \{\nvar _ret =  null;\n${b}\nreturn  _ret;\n\}]]
ContainerImplementation_noParam [ki name b] = [[exports.${name} = function () \{\nvar _me = this;\nvar _ret = null;\n${b}\nreturn _ret;\n\}]]

SynchronousLeafImplementation_withFormals [ksync name karrow dl b] = [[

${name} = function ([${dl}]) {${b}
\}]]

SynchronousLeafImplementation_withoutFormals [ksync name b] = [[

this.${name} = function () {${b}
\}]]

SequenceOfBoxes [@b] = [[${b}]]
NestedBox [b] = [[${b}]]
NB [b] = [[${b}]]

Box [klb bo @b krb] = [[\n${bo}${b}]]
BoxOperation [op] = [[${op}]]
OrElse [klb korelse b krb] = [[${b}]]

Pass [kpass] = [[]]

When [kwhen kmessages @nb] = [[if (_me.inputQueue.length > 0) {${nb}\n\};]]

FindConnectionFromMe [kfind d kfrom kme kon kport d2 b e @nb]
  = [[var ${d} = _me.find_connection (_me, ${d2});
if (${d}) {${b}
} else \{${e}\}${nb}]]

WhenAll [kwhen kall pb nb] = [[\nif (${pb}) \{${nb}\n\}]]
Return [karrow d @nb] = [[\n_ret = ${d};${nb}]]
CheckReturn [kcheck kreturn s @nb] = [[if (_ret === null) {\nconsole.error ("no value returned");\nconsole.error (\`${s}\`);\nprocess.exit (1);}\n${nb}]]

Cond [kcond ccf ccr] = [[${ccf}${ccr}]]
CondClause [klb p b krb] = [[(${p}) {${b}
\}]]
FirstCondClause [cc] = [[if ${cc}]]
RestCondClause [cc] = [[ else if ${cc}]]

WithLock [klock name @nb] = [[${nb}]]

Find_withParams [kfind name kin d kgiven pl karrow name2 b e @nb]
  = [[var ${name2} = this.find_${name}_in_${d} (this, ${pl});if (${name2}) \{${b}\n\} else \{${e}\};${nb}]]
Find_withoutParams [kfind name kin d        karrow name2 b e @nb]
  = [[var ${name2} = this.find_${name}_in_${d} (this);if (${name2}) \{${b}\n\} else \{${e}\};${nb}]]

VarBox_array [kvar name karrow klb dl krb @nb] = [[var ${name} = \[${dl}\];${nb}]]
VarBox_inputmessage  [kvar name karrow ki klb0 klb dl krb d krb0 @nb] = [[${kvar} ${name} = new msg.InputMessage (${dl},${d}.comefrom,"?",${d});${nb}]]
VarBox_outputmessage  [kvar name karrow ko klb0 klb dl krb d krb0 @nb] = [[${kvar} ${name} = new msg.OutputMessage (${dl},${d}.comefrom,"?",${d});${nb}]]


Synonym_obj [ksyn name keq klb dl krb @nb] = [[var ${name} = \[${dl}\];${nb}]]
Synonym_solitary [ksyn name keq dl @nb] = [[var ${name} = ${dl};${nb}]]

Lookup [klookup d karrow name @nb] = [[var ${name} = _me.lookupChild (${d});${nb}]]

ForEvery_sugaredWithParams [kfor kevery kitem kin d kgiven pl kassign name @nb]
  = [[${d} (${pl}).forEach (${name} => \{${nb}\n\});]]
ForEvery_withParams [kfor kevery name1 kin d kgiven pl kassign name @nb]
  = [[${d} (${pl}).${name}.forEach (${name1} => \{${nb}\n\});]]
ForEvery_sugaredWithoutParams [kfor kevery kitem kin d kassign name @nb]
  = [[${d}.forEach (${name} => \{${nb}\n\});]]
ForEvery_withoutParams [kfor kevery name kin d kassign name1 @nb]
  = [[${d}.${name}.forEach (${name1} => \{${nb}\n\});]]


SynchronousCall_params [kat d1 karrow d2] = [[${d1} (${d2});]]
SynchronousCall_noparams [kat d1] = [[${d1} ();]]
SynchronousCall_external_params [kat d1 karrow d2] = [[_me.${d1} (${d2});]]
SynchronousCall_external_noparams [kat d1] = [[_me.${d1} ();]]


Datum_field [n kof d] = [[${d}.${n}]]
Datum_dottedField [n kdot d] = [[${n}.${d}]]
Datum_name [n] = [[${n}]]
Datum_me [n] = [[_me]]
Datum_port [n] = [[port]]

Predicate_me [left kis kme] = [[(${left} === "_me")]]
Predicate_notme [left kis lnot kme] = [[(${left} !== "_me")]]
Predicate_eq [left eq right] = [[(${left} === ${right})]]
Predicate_ne [left eq right] = [[(${left} !== ${right})]]

PredicateBlock [lb p1 @pm rb] = [[${p1}${pm}]]
PredicateMore [p] = [[ && ${p}]]


ParameterList_list [d kx pl] = [[${d}, ${pl}]]
ParameterList_solitary [d] = [[${d}]]

DatumList_list [d1 kcomma d2] = [[${d1}, ${d2}]]
DatumList_solitary [d] = [[${d}]]
NameList_list [d1 kcomma d2] = [[${d1}, ${d2}]]
NameList_solitary [d] = [[${d}]]

name [first @rest] = [[${first}${rest}]]
namecharFirst [c] = [[${c}]]
namecharRest [c] = [[${c}]]

separator [sep] = [[${sep}]]

keyword [kw] = [[${kw}]]

eol [c] = [[${c}]]

space [c] = [[${c}]]

comment [c] = [[${c}]]

string [dq1 @s dq2] = [[${s}]]
dq [c] = [[]]

```

## Makefile Entries
```
...
find_connection.js: find_connection.das $(DIA)
	./dev.bash <find_connection.das >find_connection.js

find_connection_in__me.js: find_connection_in__me.das $(DIA)
	./dev.bash <find_connection_in__me.das >find_connection_in__me.js

routing.js: routing.das $(DIA) $(IDIA)
	./dev.bash <routing.das >routing.js

handling.js: handling.das $(DIA) $(IDIA)
	./dev.bash <handling.das >handling.js
...
```

dev.bash
```
#!/bin/bash
prep=!/tools/pre/pre
cdir=`pwd`
${prep} '.' '$' dia.ohm dia.fmt --stop=1 --support=${cdir}/support.js
```

# Appendix Handling.das
```
implementation deliverInputMessageToAllChildrenOfSelf (message)
      { find connection from me on port message.etag
        { lock connection
          { for every receivers in connection => dest
            { synonym params = {me, message, dest}
              { cond
                { dest.name is not me
                  { #deliver_input_from_container_input_to_child_input <= params }
                }
                { dest.name is me
                  { #deliver_input_from_container_input_to_me_output <= params }
                }
              }
            }
          }
        }
        { orelse
          { pass }
        }
      }
```.

Note that editors edit.  Editors must not have hard-wired notions about what they are editing.  For example, *emacs* edits characters that are arranged in text files.  It has plugins that will colorize text, but none of the colorization is hard-wired into the basic editor.

Editors should allow the creation of "incorrect" programs.  Later stages can check for programming errors.

These ideas also define what is needed for editing technical diagrams.  Editors edit rectangles, ellipses, lines (arrows), and, text[^svg].  The rest of the error checking and semantics inferencing comes later and must not be hard-wired into technical diagram editors.

[^svg]: Note that these kinds of things - rectangles, ellipses, lines, text - are supported in SVG.