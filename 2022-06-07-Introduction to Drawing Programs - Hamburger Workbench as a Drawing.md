# 2022-06-07-Introduction to Drawing Programs - Hamburger Workbench as a Drawing
My goal is to introduce the ideas of drawing a program in several gentle steps.

Simplistic, ad-hoc, parsing is introduced in the book "Hamburger Workbench - A Gentle Introduction to Parsing".

This paper takes that same code and transforms it into a drawing, in 3 steps.

The final drawing is that of a test bench for the "Order Taker" component.

In the process, I develop a component based on legacy code - the "Phrase Parser".  This component creates a wrapper for legacy Javascript code - Ohm-JS - and makes it possible to use this code in the async design paradigm.

This introduction consists of several steps:

1. An ad-hoc implementation of a browser-based app that performs only a simple function (hopefully understandable and easy to explain).  This implementation is the subject of the previous book "Hamburger Workbench - A Gentle Introduction to Parsing".

2. A less ad-hoc re-organization of the app into *components*.

3. A *drawing* of the component-based app, transpiled into a running app.  Note that this step is simpler than what is often called a VPL (Visual Programming Language), using only
- rectangles
- ellipses
- lines
- text

These basic graphic elements are already supported by SVG and this step presents no new technology, just a different way to organize programs.


I call drawings of programs, *DaS*, for Diagrams as Syntax.

We begin with a look at "what is programming?", then dive into steps 1-3, the development of a simple, frivolous, application as a web client.

We will discuss the question of what makes a good drawing for representing programs.  What ideas can be used to construct DaS syntaxes? 
## What Makes a Good DaS Syntax?


### Drawings Add Information to a Program

I believe that a drawing-based program should *add* information to a program instead of simply re-writing existing textual representations.  

A drawing should contain text where it is appropriate, and, it should contain graphics (drawings) where appropriate and useful.  

For example, the text-based statement `a = b + c` is sufficiently expressive and well-understood.  There is no reason to express `a = b + c` as a drawing.  

It is much more difficult, though, to express networks of interconnected components in textual form, and, that is where diagrams *add* information to programming.  

Note that we already use diagrams in programming, in the form of drawings of computer networks, but we tend not to formalize the syntax for such drawings.


# Syntax For Synchronous Programs
## Nested Boxes
Rectangles within rectangles represent operations that are synchronous and "inherit" information from each preceding step.  

This arrangement is much like wrapping *lambda*s around blocks of code in textual languages.

At some point, the nesting becomes too deep to be visually useful.  At that point, an off-page-connector-like notation is needed.  In the example diagram below, I used squares to represent synchronous ports and dotted outlines to represent boxes that "are implemented elsewhere".  This particular drawing shows the main set of boxes plus the "implemented elsewhere" boxes ("deliver input from Container input to Child input" and "deliver input from Container input to me output").

![](handling.png)
### Nested Diagram As Text
Note that the text form of the diagram is not meant for human consumption.

The only goal is machine-readability, esp. via Ohm-JS.

```
implementation route
{ for every item in children of me => child
  { for every item in outputQueue of child.runnable => output_message
    { synonym message = output_message
      { find connection in me given child X message.etag => connection
        { lock connection
          { for every receivers in connection => dest
              { synonym params = {me, dest, message}
                { cond
                  { dest.name is not me
                    { @deliver_to_child_input <= params }
                  }
                  { dest.name is me
                    { @deliver_to_me_output <= params }
                  }
                }
            }
          }
        }
        { orelse
           { pass }
        }
      }
    }
    {@child.runnable.resetOutputQueue}
  }
}

sync deliver_to_child_input <= me, dest, message
   // map message for receiver
  { var input_message <= $i{{dest.etag, message.data} message}
    { lookup dest.name => receiver
      { @receiver.enqueueInput <= input_message }
    }
  }

sync deliver_to_me_output <= me, dest, message
  // map message for output
  { var output_message <= $o{{dest.etag, message.data} message}
    { @me.enqueueOutput <= output_message }
  }

```
## Statecharts
Harel's paper [Statecharts](https://guitarvydas.github.io/2020/12/09/StateCharts.html) introduced a diagram syntax for nested state machines.

Harel's notation solved the "state explosion problem".

A simple diagram of a state machine is shown below...

![](app-state-diagram.png)
The above diagram shows states as ellipses with solid outlines.

State names are preceded by one octothorpe `#`.

*Non-blocking states* are shown as ellipses with dotted outlines.

Local variables are shown in a rectangle with a dotted outline.

Transistions are shown as curved arrows.

Events that trigger transitions are prefixed by two octothorpes `##`.

Non-blocking conditionals are shown as hexagons with *true* and *false* branches.

Transition code is shown as text attached to a transition.  Transition code is executed only whan a transition is taken.

Entry and exit code for states was not needed for this diagram and is not shown.  I suggest that entry and exit code be included as part of the text contained in states, with prefix syntax like "entry: ..." and "exit: ...".

In cases where diagrams/code are meant to be included in certain states but would be visually disturbing, I've used a dotted, double line to show the inclusion.

Non-blocking transitions are shown as dotted arrows.
## Drakon Control Flow
The Drakon visual syntax is described in [drakon-editor](http://drakon-editor.sourceforge.net)

I drew a Drakon diagram using *draw.io*.  The drawing is seen below.

This diagram contains two constructs not specified by the Drakon synax:
- a comment box (a callout)
- numeric labels at the points where flows intersect skewers.

These minor additions made it easier to transpile the diagrams into textual form.

![](step.png)
### Drakon Diagram As Text
```
flowchart Try-component {
  start main
  skewer main {
    unless has-children try-self/1
    memo-readiness-of-each-child
    step-each-child
    unless any-child-was-previously-ready try-self/2
    > activated/0
  }
  skewer try-self {
    : try-self/1
    : try-self/2
    unless self-has-input not-activated/3
    self-first-step-with-input
    > activated/0
  }
  skewer not-activated {
    : not-activated/3
    > finished/0
  }
  skewer activated {
    > finished/0
  }
  skewer finished {
    end
  }
}
```
# Syntax For Asynchronous Programs

## Components
In this form, rounded rectangle represent asynchronous components.

Sharp-edged, red rectangles represent synchronous snippets of code (in this case JavaScript).

Yellow circles represent async output ports.

Green circles represent async input ports.

Messages (data) flow from output port to input ports along arrows.  Message flow is uni-directional.

Output messages are queued (deferred send) and routed by parent Container components (in this example "Text Bench" and "Order Taker").

Each component has one input queue and all input messages are tagged and queued up in FIFO order.

Leaf components are shown with the colour *blue*.

Container components contain other components (Leaf or Container) and route messages between the contained components.

Further details (like fan-in, fan-out, Signatures, Implementations, etc., are discussed elsewhere).

![](testbench.png)
## FBP
[FBP](http://www.jpaulmorrison.com/fbp/fbp2.htm) describes a notation plus visualization of asynchronous components similar to the above.
# Syntax That Doesn't Work

### Diagram Syntax That Does Not Work

Using too many shapes and icons on diagrams makes the diagrams too complicated to be useful. 
For example, electronics schematics used to use a number of symbols, e.g. zig-zag lines for resistors, transistor symbols, etc.  Later, all 2D symbols were reduced to rectangles to reduce the visual busy-ness of diagrams, esp. symbols that represented VLSI.  VLSI was too variable to be represented by unique icons.

Drawings of constructs that are well-served by existing notations, e.g. mathematics expressions like `a = b + c`, doesn't work well, since there is no need to complicate pre-existing syntax by diagramming it.

Colours for *types* appears like a good idea, but doesn't work well in practice.  We tried using colours to signify *types* but quickly ran out of colours and created too much nuance in the visuals.

Using a grain that is too fine does not work well.  In an early project, we used some 20,000 instances of visual components, many of them simple, like inverters.  We found that there was too much detail and that it didn't help in understanding the code.  Better layering - better architecting - was needed.  In analogy, the *structured programming* revolution added no new technology to programming, it simply suggested how to organize use of the existing operations (assembler, at the time)


The issues of using Ohm-JS and why Ohm-JS is better than PEG which better that REGEX are discussed in the previously-mentioned book.

We will discuss the use of current programming languages as *assembler* for the next generation of progamming languages, esp. DaS. 
## The Next Generation of Programming Languages



A separate book will be devoted to a collection of text-parsing idioms.  A cookbook for pattern matching.

Future writing, whether in book form or in blog form, will discuss
4. Transpiling `helloworld.drawio` (a drawing) to Python (transpiling to Python instead of to Javascript, which the subject of this book)
5. Transpiling a drawing of a Python program to transpile `helloworld.drawio` to Python (a diagrammatic Python program that performs step 4)
6. Toolbox languages
7. Orthogonal Programming Languages.


## 2022-06-07-Parts of Programming

I think of programming in terms of *divide and conquer*.  Very roughly, programming breaks down into two (2) steps:

1. grok
2. re-format


Step (1) consists of understanding the input, whatever it is.  
- For websites, the input is data sent in by users.  In some cases, the input comes from a browser-based *form* while in other cases the input is less-organized and results from users pushing buttons in their browsers.  The button pushes are translated into arbitrary actions usually programmed-in as Javascript code attached to the buttons.  (See below, computer-to-computer input). 
- For spreadsheets, the input is a grid containing numbers and formulae.
- For internet-based computers, the input is information sent in by other computers.  Often this data is formatted as a stream of text usually called a *request*.
- For compilers, the input is usually a text file containing textual instructions that are meant to control the machine (an electronic computer), and, simlutaneously document the intentions of the original programmer so that other programmers could understand what is being done.

In step (2), programmers write scripts ("code") that send commands to the computer or requests for more information, based on the information contained in step (1).

Step (1) is often tangled up with the concepts of UX (User-eXperience) and break down into two parts, too:

3. Presenting data to users.  This should be the job of graphic designers and artists, but is usually tangled up with programming and tends to depend on the UX skills of technical programmers.
4. Accepting data from users in the form of modifications to the presentations (e.g. button pushes, arrow keys on the spreadsheets, keyboard inputs in text boxes) and then attempting to comb through it and organize it and pattern-match it in ways that make step (2) easier.  This step is, also, tangled up with what we call *programming*, and tends to depend on the engineering skills of programmers.  Usually if a programmer is a good Engineer, then the programmer's skills tend to be shallow in the UX department and vice versa.  What we currently call *programming* tends to involve all of the above, tangled up together.  The lack of separation between the various parts of programming results in uneven results.  Usually an app ("application") is either better in the UX department or better in the niggly-details department, but, usually not both.  Sometimes, programmers are generalists who have honed their skills in both departments, resulting in apps that are satisfying to users and to implementors of step (2).  Such balanced apps are rare and tend to become "overnight successes".

Note that the film and television industry has learned how to divide up work between graphic artists and programmers.

The gaming industry seems to have learned some orgnizational lessons from film and TV and seems to have advanced further into dividing the steps for programming games, than most other realms of programming.

The website-building industry is, also, learning to divide work up.  We see .html files for creating websites an we see .css files added to websites to "paint" them and allow for improved graphic-design of websites separated from the niggly details of simply making the websites function.

## HamburgerD0D - Start Here

Goal:
- create hamburger workbench from diagrams
- transpile the diagrams to JS
- future: *transpile the diagrams to CL, Racket, Python, C++, etc.*



### Screenshot Hamburger Workbench

Hamburger Workbench On Load
![](hD0D1.png)

Hamburger Workbench After Clicking Button
![](hD0D2.png)



## Diagram Programs
Note: this, DaS (Diagrams as Syntax) is not the same as what is called VPL (Visual Programming Languages).  The diagrams below are a hybrid of text plus very simple visual elements (rectangles, ellipses, lines, text).

Note: the diagrams below were created using draw.io, but, any convenient-to-use SVG editor would do.


### Diagram The Workbench

![](testbench.png)
The rounded boxes represent *concurrent* software components.

The green circles represent *input ports*.

The yellow circles represent *output ports*.

The red rectangles represent synchronous code snippets.  In this example diagram, code snippets are written in JavaScript.

The gray rectangle, labelled "Order Taker" represents a Container component.

Arrows and lines represent one-way message-sending paths.  The components are concurrent and the only way they can communicate is by sending messages. 
#### Message Sending

In fact, messages are never sent directly from one component to another, but are sent "upwards" to the Container for routing.

Containers can only route messages of their direct children (and themselves).

This method ensures:
- message sending is structured and encapsulated 
- components are truly independent.  Components cannot know who receives their messages nor, *if* their messages are received at all.  The parent Container can choose to route inputs and outputs to N.C. - no connection.  The parent Container controls all message routing, a component cannot hard-wire destinations into its own code, thus, making the code usable in multiple situations.

The blue rectangle, labelled "Phrase Parser" does not display any red boxes.  This component is a wrapper for a large piece of JavaScript software that is not worth showing on the diagram.  It is assumed that rectangles with no innards are "implemented elsewhere" and will be brought into the mix by whatever means necessary (e.g. by the loader or linker).  In the case of this example, the "Phrase Parser" code is included as a "<script src=... ></script>" tag in the .html.

The transpiler creates Javascript code for all of the concurent components and the drawn-out synchronous components, but leaves a hole for the non-drawn synchronous code of non-drawn-out components.

In fact, every component is compiled into two code snippets
1. the Signature
2. the Implementation .

A signature snippet is generated for each blue box and each Container box.

Red boxes generate Leaf code Implementation snippets that are attached to the surrounding blue boxes.

The tool also generates Implementation code (child list + routing table) for each Container component.

The box labelled "Phrase Parser" is blue but contains no red box.  In this case, the tool generates only a Signature for the blue box and "assumes" that the Leaf code for the box will be linked in by other means.

Note the use of fan-out, where two output ports are coalesced into a single output.  For example, the "order no choices" and "order with choices" outputs both feed the "food order" output of the Container.  Fan-in and fan-out are required for a reasonable component-based UXs, although fan-out implies semantic questions for the transpilation (Q: how messages are copied to multiple sinks, are they shared, copied or copied-on-write, or ...?).

### Diagram The Workbench With Probes

![](testbenchdb.png)

Here, I've added "probe" components to observe messages as they travel along the connections.

Ideally a single drawing can contain multiple instances of the same component.

In this example, though, for simplicity, I've created unique "probe" components and do not rely on multiple instantiation.

[In fact, the code for this POC does not support multiple instances of the same Component.  I expect to re-implement the system using DaS and will address the multiple instance issue then,.]

### Diagram Step

![](step.png)

The control flow that implements the step-wise operation of Container components can be written in a numbe of ways.  I chose to draw a Drakon diagram, for variety, in this POC.

The grammar and re-format specification are 
#### Transpiler Drakon

## Grammar
flowchart.ohm
```
flowchart {

Flowchart = "flowchart" name "{" "start" name Skewer+ "}"
Skewer
  = "skewer" name "{" Action LabelledAction+ "}" -- both
  | "skewer" name "{" Action "}"                 -- actiononly
  | "skewer" name "{" LabelledAction+ "}"        -- labelledactionsonly
  | "skewer" name "{" "}"                        -- neither
  
Action 
  = Unless
  | Result
  | Jump
  | End
  | Call
  | Send


LabelledAction 
  = ":" LabelDef Action -- action
  | ":" LabelDef        -- empty
  
Unless = "unless" name LabelRef Action?
Jump = ">" LabelRef Action?
Send = "send" name Value Action?
Call = MethodRef Action?
Result = ">>" YesNo Action?
End = "end" Action?

YesNo = 
  | "yes" -- yes
  | "no"  -- no

keyword = (
    "flowchart" 
  | "skewer" 
  | "start" 
  | "unless" 
  | "send" 
  | "end"
  | "yes"
  | "no"
  | "_"
  ) !namecharRest

bracket = "{" | "}" | "(" | ")" | "[" | "]"
separator = ":" | ">>" | ">" | "/" | bracket

LabelDef = Label
LabelRef = Label
Label = name "/" number

MethodRef = name !"/"

name
  = "_"        -- trigger
  | namestring -- name 
namestring = namecharFirst namecharRest*
namecharFirst = !keyword namechar 
namecharRest = !keyword namechar

namechar = !space !separator any

number = digit+

space
 += comment

comment
  = "//" (!"\n" any)* "\n"  -- singleLine
  | "/*" (!"*/" any)* "*/"  -- multiLine

string = dq (!dq any)* dq
dq = "\""

Value = name | number

}
```
## Re-Formatter
flowchart.fmt
```
Flowchart [kfc name lb kstart start @sk rb] = [[\nexports.${name} = function () {
var _ret = undefined;
var lambdas = {${sk}
_endoflambdas: null
};
return (function (_me) { return lambdas.${start} (_me, 0); });
}
]]


Skewer_both [ksk name lb a @la rb] = [[\n${name}: function (_me, _label) {
if (_label === 0) {${a}${la}
} else {
_me.panic ("${name}", _label); 
}
}\,]]

Skewer_actiononly [ksk name lb a rb] = [[\n${name}: function (_me, _label) {
if (_label === 0) {${a}
} else {
_me.panic ("${name}", _label); 
}
}\,]]

Skewer_labelledactionsonly [ksk name lb @la rb] = [[\n${name}: function (_me, _label) {
if (_label === 0) {${la}
} else {
_me.panic ("${name}", _label); 
}
}\,]]

Skewer_neither [ksk name lb rb] = [[\n${name}: function (_me, _label) {
_me.panic ("${name}", _label); 
}\,]]

Action [a] = [[\n${a}\n]]

LabelledAction_action [kcolon ldef cont] = [[\nreturn ${support.formatLabelFunction (ldef)};
} else if (_label === ${support.formatIndex (ldef)}) \{${cont}\n]]
LabelledAction_empty [kcolon ldef] = [[\nreturn ${support.formatLabelFunction (ldef)};
} else if (_label === ${support.formatIndex (ldef)}) {\n]]

Unless [ku n1 lref @cont]
  = [[if (!_me.${n1} ()) {
 return ${support.formatLabelFunction (lref)};
} else {
${cont}
;}]]

Jump [k n @cont] = [[return ${support.formatLabelFunction (n)};${cont}]]
Call [n @cont] = [[_me.${n} ();${cont}]]
Send [ksend n v @cont] = [[_me.send ("${n}", ${v}, _me.name, null);${cont}]]
Result [k v @cont] = [[_ret = ${v};${cont}]]
End [k @cont] = [[return _ret;${cont}]]

YesNo_yes [yn] = [[true]]
YesNo_no [yn] = [[false]]



LabelDef [n] = [[${n}]]
LabelRef [n] = [[${n}]]
Label [name kslash number] = [[${name}${kslash}${number}]]

MethodRef [n] = [[${n}]]



bracket [c] = [[${c}]]
separator [c] = [[${c}]]

name_trigger [k] = [[true]]
name_name [n] = [[${n}]]
namestring [first @rest] = [[${support.mangle (first + rest)}]]
namecharFirst [c] = [[${c}]]
namecharRest [c] = [[${c}]]

separator [sep] = [[${sep}]]

keyword [kw] = [[${kw}]]

space [c] = [[${c}]]

comment [c] = [[${c}]]

string [qb @cs qe] = [[${qb}${cs}${qe}]]
dq [c] = [[${c}]]
```

## Makefile Entries
```
...
step.js: step.drakon $(DRAKON) $(IDRAKON)
	./flowchart.bash <step.drakon >step.js
...
```

flowchart.bash
```
#!/bin/bash
prep=!/tools/pre/pre
cdir=`pwd`
${prep} '.' '$' flowchart.ohm flowchart.fmt --stop=1 --support=${cdir}/support.js
```
.

### Diagram Handling



![](handling.png)


The *handler* code is part of the Cos (component O/S) code.  

I've used diagrams to show the workings of this code as an example that this technique can be used for systems programming (i.e. writing low-level synchronous code).

I drew out the logic for the *handler* code as diagrams of nested boxes.

I, then, transpiled the diagram to `handling.das`.  The transpilation was done manually, to avoid excessive details in this example, and, to show the 1:1 correspondence of diagrams to `.das` code.

I used Ohm-JS to transpile `handling.das` into `handling.js`.  The transpiler is located in https://github.com/guitarvydas/duct, and invoked by `make handling.js`

The code for the transpiler (grammar plus re-format) are discussed in 
#### Transpiler DaS

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
```

### Diagram Routing

![](handling.png)



### Diagram Find Connection


![](findconnection.png)



### Diagrams Data Structures

## Components
![](json2generic-components.png)

## Messages
![](json2generic-message.png)

## Queues
![](json2generic-queue.png)

## Transpiled JSON

### Hamburger Workbench JSON

```
[
  [
    {
      "children": [],
      "connections": [],
      "id":"cell_12",
      "inputs": [],
      "name":"HTML Button",
      "outputs": ["click" ],
      "synccode":"me.send (&quot;click&quot;, true);"
    }
  ],
  [
    {
      "children": [],
      "connections": [],
      "id":"cell_15",
      "inputs": ["go" ],
      "name":"Phrase Faker",
      "outputs": ["short phrase", "long phrase" ],
      "synccode":"&lt;div&gt;&amp;nbsp; &amp;nbsp; me.send (&quot;long phrase&quot;, &quot;I Want A Hamburger With Ketchup And Bacon And Pickles&quot;);&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;"
    }
  ],
  [
    {
      "children": [],
      "connections": [],
      "id":"cell_22",
      "inputs": ["phrase" ],
      "name":"Phrase Parser",
      "outputs": ["order no choices", "order with choices", "parse error", "hook error" ],
      "synccode":""
    }
  ],
  [
    {
      "children": ["HTML Button", "Phrase Faker", "Order Taker" ],
      "connections": [
        {
          "receivers": [ {"receiver": {"component":"Phrase Faker", "port":"go"}} ],
          "senders": [ {"sender": {"component":"HTML Button", "port":"click"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Order Taker", "port":"phrase"}} ],
          "senders": [ {"sender": {"component":"Phrase Faker", "port":"short phrase"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Order Taker", "port":"phrase"}} ],
          "senders": [ {"sender": {"component":"Phrase Faker", "port":"long phrase"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Test Bench", "port":"food order"}} ],
          "senders": [ {"sender": {"component":"Order Taker", "port":"food order"}} ]
        }
      ],
      "id":"cell_6",
      "inputs": [],
      "name":"Test Bench",
      "outputs": ["food order" ],
      "synccode":""
    }
  ],
  [
    {
      "children": ["Phrase Parser" ],
      "connections": [
        {
          "receivers": [ {"receiver": {"component":"Phrase Parser", "port":"phrase"}} ],
          "senders": [ {"sender": {"component":"Order Taker", "port":"phrase"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Order Taker", "port":"food order"}} ],
          "senders": [ {"sender": {"component":"Phrase Parser", "port":"order no choices"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Order Taker", "port":"food order"}} ],
          "senders": [ {"sender": {"component":"Phrase Parser", "port":"order with choices"}} ]
        }
      ],
      "id":"cell_7",
      "inputs": ["phrase" ],
      "name":"Order Taker",
      "outputs": ["food order" ],
      "synccode":""
    }
  ]
]
```

## Makefile
```
...
testbench.json : tools testbench.drawio
	./generate.bash $(TOOLS) testbench.drawio
	mv out.json testbench.json
...
```

generate.bash
```
#!/bin/bash
# usage: generate.bash <tools root directory> <.drawio file>
#                      $1                     $2

# tools root - takes the place of $PATH
# change this for your own environment
root=`realpath $1`

infile=$2

${root}/d2f/d2f.bash ${root} ${infile} >fb.pl
# from this point on, we can ignore ${infile} since it's been converted to fb.pl
${root}/das2f/run-fb-pipeline.bash ${root} #2>/dev/null
${root}/das2j/layercomponent_query.bash >out.json
echo
echo 'out.json written'
echo

```

### Walkthroughs
#### Leaf


### Phrase Faker Walkthrough

![](walkthroughs-leaf-phrase-faker.png)

```
  [
    {
      "children": [],
      "connections": [],
      "id":"cell_15",
      "inputs": ["go" ],
      "name":"Phrase Faker",
      "outputs": ["short phrase", "long phrase" ],
      "synccode":"&lt;div&gt;&amp;nbsp; &amp;nbsp; me.send (&quot;long phrase&quot;, &quot;I Want A Hamburger With Ketchup And Bacon And Pickles&quot;);&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;"
    }
  ],
```



![](Recording%2020220511044219.webm)

![](Recording%2020220511044729.webm)


#### Container


### Test Bench Walkthrough

![](walkthroughs-container-testbench.png)
```
  [
    {
      "children": ["HTML Button", "Phrase Faker", "Order Taker" ],
      "connections": [
        {
          "receivers": [ {"receiver": {"component":"Phrase Faker", "port":"go"}} ],
          "senders": [ {"sender": {"component":"HTML Button", "port":"click"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Order Taker", "port":"phrase"}} ],
          "senders": [ {"sender": {"component":"Phrase Faker", "port":"short phrase"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Order Taker", "port":"phrase"}} ],
          "senders": [ {"sender": {"component":"Phrase Faker", "port":"long phrase"}} ]
        },
        {
          "receivers": [ {"receiver": {"component":"Test Bench", "port":"food order"}} ],
          "senders": [ {"sender": {"component":"Order Taker", "port":"food order"}} ]
        }
      ],
      "id":"cell_6",
      "inputs": [],
      "name":"Test Bench",
      "outputs": ["food order" ],
      "synccode":""
    }
  ],
```

![](Recording%2020220511045152.webm)
![](Recording%2020220511045320.webm)
![](Recording%2020220511045906.webm)




## Manually Transpiled Code From Diagrams

### Code Find Connection

```
implementation find_connection (etag)
  { for every item in connections of me => connection
      { synonym sender = connection.sender
          { when all
              {
                  sender.name is me
                  sender.etag == etag
              }
              { -> connection }
          }
      }
  }

```

### Code Handling

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
```

### Code Routing

```
implementation route
{ for every item in children of me => child
  { for every item in outputQueue of child.runnable => output_message
    { synonym message = output_message
      { find connection in me given child X message.etag => connection
        { lock connection
          { for every receivers in connection => dest
              { synonym params = {me, dest, message}
                { cond
                  { dest.name is not me
                    { @deliver_to_child_input <= params }
                  }
                  { dest.name is me
                    { @deliver_to_me_output <= params }
                  }
                }
            }
          }
        }
        { orelse
           { pass }
        }
      }
    }
    {@child.runnable.resetOutputQueue}
  }
}

sync deliver_to_child_input <= me, dest, message
   // map message for receiver
  { var input_message <= $i{{dest.etag, message.data} message}
    { lookup dest.name => receiver
      { @receiver.enqueueInput <= input_message }
    }
  }

sync deliver_to_me_output <= me, dest, message
  // map message for output
  { var output_message <= $o{{dest.etag, message.data} message}
    { @me.enqueueOutput <= output_message }
  }
```

### Code Step

```
flowchart Try-component {
  start main
  skewer main {
    unless has-children try-self/1
    memo-readiness-of-each-child
    step-each-child
    unless any-child-was-previously-ready try-self/2
    > activated/0
  }
  skewer try-self {
    : try-self/1
    : try-self/2
    unless self-has-input not-activated/3
    self-first-step-with-input
    > activated/0
  }
  skewer not-activated {
    : not-activated/3
    > finished/0
  }
  skewer activated {
    > finished/0
  }
  skewer finished {
    end
  }
}
```

## JavaScript

### JS Find Connection

```
// find_connection

function find_connection (_me, etag) {
    var _ret =  null;
    
    _me.connections.forEach (connection => {
        var sender = connection.sender;
        
        if ((sender.name === "_me") && (sender.etag === etag)) {
            
            _ret = connection;
        }
    });
    return  _ret;
}

````

### HTML The Workbench

```
<!DOCTYPE html>
<html>
  <head>
    <style>
      textarea {
          background-color: oldlace;
      }
    </style>
  </head>
  <body>

    <h1>Hamburger D0D Workbench</h1>

    <p>output:</p>
    <textarea id="output" rows="7" cols="90" placeholder="output">
    </textarea>


    <p id="status" >READY</p>


    <!-- Component Operating System -->
    <script src="cos.js"></script>

    <!-- Ohm-JS -->
    <script src="https://unpkg.com/ohm-js@16/dist/ohm.min.js"></script>

    <!-- Components for this app (see, also, hamburgerworkbench0d.drawio) -->
    <script src="phraseparser.js"></script>
    <script src="testbench.js"></script>

    <script>
      
      var testBench = new Test_Bench (null);
      var htmlbutton = testBench.lookupChild ("HTML Button");

      function buttonhandler () {
          htmlbutton.handler (htmlbutton, null);
          htmlbutton.container.wakeup ();
          let outs = testBench.outputs ();
          if (Array.isArray (outs)) {
              if (outs.length > 0) {
                  let order = outs [0].data;
                  //document.getElementById ('output').innerHTML = outs.toString () + '\ndone';
                  document.getElementById ('output').innerHTML
                      = order.item.toString () + '\nextra: ' + order.extras.toString () + '\ncondiments: ' + order.condiments.toString ();
              }
          }
      }

    </script>

    <br>
    <button onclick="buttonhandler ()">Hamburger</button>

  </body>
</html>

```

### JS Handling

```
// handling for Containers

deliverInputMessageToAllChildrenOfSelf = function (_me, message) {
    var _ret =  null;

    var connection = _me.find_connection (_me, message.etag);
    if (connection) {

        connection.receivers.forEach (dest => {
            var params = [_me, message, dest];
            if ((dest.name !== "_me")) {
                _me.deliver_input_from_container_input_to_child_input (params);
            } else if ((dest.name === "_me")) {
                _me.deliver_input_from_container_input_to_me_output (params);
            }
        });
    } else {
    }
    return  _ret;
}
```

### JS Routing

```
/// routing

function route () {
    var _me = this;
    var _ret = null;

    _me.children.forEach (child => {
        child.runnable.outputQueue.forEach (output_message => {
            var message = output_message;
            var connection = this.find_connection_in__me (this, child, message.etag);
            if (connection) {
                connection.receivers.forEach (dest => {
                    var params = [_me, dest, message];
                    if ((dest.name !== "_me")) {
                        deliver_to_child_input (params);
                    } else if ((dest.name === "_me")) {
                        deliver_to_me_output (params);
                    }
                });
            } else {
            };
        });
        child.runnable.resetOutputQueue ();
    });
    return _ret;
}

deliver_to_child_input = function ([_me, dest, message]) {
    var receiver = _me.lookupChild (dest.name);
    var input_message = new InputMessage (dest.etag, message.data,message.comefrom,receiver.name,message);
    receiver.enqueueInput (input_message);
}

deliver_to_me_output = function ([_me, dest, message]) {
    var output_message = new OutputMessage (dest.etag, message.data,message.comefrom,_me.name,message);
    _me.enqueueOutput (output_message);
}


```

### JS Step

```
/// step


Try_component = function () {
    var _ret = undefined;
    var lambdas = {
        main: function (_me, _label) {
            if (_label === 0) {
                if (!_me.has_children ()) {
                    return lambdas.try_self (_me, 1);
                } else {

                    _me.memo_readiness_of_each_child ();
                    _me.step_each_child ();
                    if (!_me.any_child_was_previously_ready ()) {
                        return lambdas.try_self (_me, 2);
                    } else {

                        return lambdas.activated (_me, 0);

                        ;}



                    ;}

            } else {
                _me.panic ("main", _label); 
            }
        },
        try_self: function (_me, _label) {
            if (_label === 0) {
                return lambdas.try_self (_me, 1);
            } else if (_label === 1) {

                return lambdas.try_self (_me, 2);
            } else if (_label === 2) {
                if (!_me.self_has_input ()) {
                    return lambdas.not_activated (_me, 3);
                } else {

                    _me.self_first_step_with_input ();
                    return lambdas.activated (_me, 0);


                    ;}


            } else {
                _me.panic ("try_self", _label); 
            }
        },
        not_activated: function (_me, _label) {
            if (_label === 0) {
                return lambdas.not_activated (_me, 3);
            } else if (_label === 3) {
                return lambdas.finished (_me, 0);


            } else {
                _me.panic ("not_activated", _label); 
            }
        },
        activated: function (_me, _label) {
            if (_label === 0) {
                return lambdas.finished (_me, 0);

            } else {
                _me.panic ("activated", _label); 
            }
        },
        finished: function (_me, _label) {
            if (_label === 0) {
                return _ret;

            } else {
                _me.panic ("finished", _label); 
            }
        },
        _endoflambdas: null
    };
    return (function (_me) { return lambdas.main (_me, 0); });
}
```

### JS Component Operating System

```
// COS
// Component Operating System


// messages

function InputMessage (etag, v, who, target, tracer) {
    this.etag = etag;
    this.data = v;
    this.tracer = tracer;
    this.comefrom = who;
    this.target = target;
    this.kind = "i";
    this.toString = function () { return recursiveToString (this); }
}

function OutputMessage (etag, v, who, target, tracer) {
    this.etag = etag;
    this.data = v;
    this.tracer = tracer;
    this.comefrom = who;
    this.target = target;
    this.kind = "o";
    this.toString = function () { return recursiveToString (this); }
}

function recursiveToString (m) {
    if (m) {
        return `(${m.comefrom}->${m.target}::[${m.kind}]${m.etag}:${m.data.toString ()}:${recursiveToString (m.tracer)})`;
    } else {
        return '.';
    }
}

// queue

function Queue () {
    this.queue = [];
    this.empty = function () { return (0 === this.queue.length) };
    this.enqueue = function (item) { this.queue.unshift (item); };
    this.dequeue = function () { return this.queue.pop (); };
    this.forEach = function (f) { return this.queue.forEach (f); };
    this.length = function () { return this.queue.length; };
    this.toArray = function () { return this.queue; }
}

/// routing

function route () {
    var _me = this;
    var _ret = null;

    _me.children.forEach (child => {
        child.runnable.outputQueue.forEach (output_message => {
            var message = output_message;
            var connection = this.find_connection_in__me (this, child, message.etag);
            if (connection) {
                connection.receivers.forEach (dest => {
                    var params = [_me, dest, message];
                    if ((dest.name !== "_me")) {
                        deliver_to_child_input (params);
                    } else if ((dest.name === "_me")) {
                        deliver_to_me_output (params);
                    }
                });
            } else {
            };
        });
        child.runnable.resetOutputQueue ();
    });
    return _ret;
}

deliver_to_child_input = function ([_me, dest, message]) {
    var receiver = _me.lookupChild (dest.name);
    var input_message = new InputMessage (dest.etag, message.data,message.comefrom,receiver.name,message);
    receiver.enqueueInput (input_message);
}

deliver_to_me_output = function ([_me, dest, message]) {
    var output_message = new OutputMessage (dest.etag, message.data,message.comefrom,_me.name,message);
    _me.enqueueOutput (output_message);
}


/// step


Try_component = function () {
    var _ret = undefined;
    var lambdas = {
        main: function (_me, _label) {
            if (_label === 0) {
                if (!_me.has_children ()) {
                    return lambdas.try_self (_me, 1);
                } else {

                    _me.memo_readiness_of_each_child ();
                    _me.step_each_child ();
                    if (!_me.any_child_was_previously_ready ()) {
                        return lambdas.try_self (_me, 2);
                    } else {

                        return lambdas.activated (_me, 0);

                        ;}



                    ;}

            } else {
                _me.panic ("main", _label); 
            }
        },
        try_self: function (_me, _label) {
            if (_label === 0) {
                return lambdas.try_self (_me, 1);
            } else if (_label === 1) {

                return lambdas.try_self (_me, 2);
            } else if (_label === 2) {
                if (!_me.self_has_input ()) {
                    return lambdas.not_activated (_me, 3);
                } else {

                    _me.self_first_step_with_input ();
                    return lambdas.activated (_me, 0);


                    ;}


            } else {
                _me.panic ("try_self", _label); 
            }
        },
        not_activated: function (_me, _label) {
            if (_label === 0) {
                return lambdas.not_activated (_me, 3);
            } else if (_label === 3) {
                return lambdas.finished (_me, 0);


            } else {
                _me.panic ("not_activated", _label); 
            }
        },
        activated: function (_me, _label) {
            if (_label === 0) {
                return lambdas.finished (_me, 0);

            } else {
                _me.panic ("activated", _label); 
            }
        },
        finished: function (_me, _label) {
            if (_label === 0) {
                return _ret;

            } else {
                _me.panic ("finished", _label); 
            }
        },
        _endoflambdas: null
    };
    return (function (_me) { return lambdas.main (_me, 0); });
}


// find_connection

function find_connection (_me, etag) {
    var _ret =  null;
    
    _me.connections.forEach (connection => {
        var sender = connection.sender;
        
        if ((sender.name === "_me") && (sender.etag === etag)) {
            
            _ret = connection;
        }
    });
    return  _ret;
}

// find_connection__in_me

function find_connection_in__me (_me, childname, etag) {
    var _ret =  null;
    
    _me.connections.forEach (connection => {
        var sender = connection.sender;
        
        if ((sender.name === childname) && (sender.etag === etag)) {
            
            _ret = connection;
        }
    });
    return  _ret;
}

// handling for Containers

deliverInputMessageToAllChildrenOfSelf = function (_me, message) {
    var _ret =  null;

    var connection = _me.find_connection (_me, message.etag);
    if (connection) {

        connection.receivers.forEach (dest => {
            var params = [_me, message, dest];
            if ((dest.name !== "_me")) {
                _me.deliver_input_from_container_input_to_child_input (params);
            } else if ((dest.name === "_me")) {
                _me.deliver_input_from_container_input_to_me_output (params);
            }
        });
    } else {
    }
    return  _ret;
}

// message delivery for Containers

function deliver_input_from_container_input_to_child_input (params) {
    var _me = params[0];
    var message = params[1];
    var dest = params[2];

    var destname = dest.name;
    var receiverrunnable = this.lookupChild (destname);
    
    var newm = new InputMessage (dest.etag, message.data, _me.name, receiverrunnable.name, message);
    receiverrunnable.enqueueInput (newm);
}
function deliver_input_from_container_input_to_me_output (params) {
    var _me = params[0];
    var message = params[1];
    var dest = params[2];
    
    var destname = dest.name;
    var receiverrunnable = this.lookupChild (destname);

    var newm = new OutputMessage (dest.etag, message.data, _me.name, receiverrunnable.name, message);
    receiverrunnable.enqueueOutput (newm);
}

// runnable (instances of components)

function send (etag, v, tracer) {
    let m = new OutputMessage (etag, v, this.name, "?", tracer); // Send knows who the sender is, but doesn't yet know who the receiver is
    this.outputQueue.enqueue (m);
}

function inject (etag, v, tracer) {
    let m = new InputMessage (etag, v, ".", undefined);
    this.inputQueue.enqueue (m);
}


function Runnable (signature, protoImplementation, container, instancename) {
    if (instancename) {
        this.name = instancename;
    } else {
        this.name = signature.name;
    }
    this.signature = signature;
    this.protoImplementation = protoImplementation;
    this.container = container;
    this.inputQueue = new Queue ();
    this.outputQueue = new Queue ();
    this.outputs = function () { return this.outputQueue.toArray (); };
    this.send = send;
    this.inject = inject;
    this.handler = function (me, message) {
        protoImplementation.handler (me, message);
    };
    this.hasOutputs = function () {return !this.outputQueue.empty ()};
    this.hasInputs = function () {return !this.inputQueue.empty ()};
    this.has_children = function () {return (0 < this.children.length); };
    this.dequeueOutput = function () {return this.outputQueue.dequeue ();};
    this.enqueueInput = function (m) { m.target = this.name; this.inputQueue.enqueue (m); };
    this.enqueueOutput = function (m) { m.target = this.name; this.outputQueue.enqueue (m); };
    this.begin = function () {};
    this.finish = function () {};
    this.resetOutputQueue = function () {
        this.outputQueue = new Queue ();
    }
    this.errorUnhandledMessage = function (message) {
        console.error (`unhandled message in ${this.name} ${message.tag}`);
        //process.exit (1);
        throw 'error exit';
    };
    if (container) {
        this.conclude = container.conclude;
    }
    this.memoPreviousReadiness = function () { this._previouslyReady = this.hasInputs (); };
    this.testPreviousReadiness = function () { return this._previouslyReady; };
    this.ready = this.hasInputs;
    this.busy = function () {return false};
    this.panic = function () { throw "panic"; }
}

function Leaf (signature, protoImplementation, container, name) {
    let me = new Runnable (signature, protoImplementation, container, name);
    me.route = function () { };
    me.children = [];
    me.connections = [];
    me.step = function () {
        if (! this.inputQueue.empty ()) {
            let m = this.inputQueue.dequeue ();
            this.handler (this, m);
        }
    };
    me._previouslyReady = false;
    return me;
}

function Container (signature, protoImplementation, container, instancename) {
    let me = new Runnable (signature, protoImplementation, container, instancename);
    me.route = route;
    me.step = function () {
        // Container tries to step all children,
        // if no child was busy, then Container looks at its own input
        // (logic written in step.drawio -> step.drakon -> step.js ; step returns
        //  a stepper function, which must be called with this)
        var stepperFunction = Try_component ();
        stepperFunction (this);
    },
    me.self_first_step_with_input = function () {
        if (! this.inputQueue.empty ()) {
            let m = this.inputQueue.dequeue ();
            this.handler (this, m);
        }
    },
    me.memo_readiness_of_each_child = function () {
        this.children.forEach (childobject => {
            childobject.runnable.memoPreviousReadiness ();
        });
    };
    me.any_child_was_previously_ready = function () {
        return this.children.some (childobject => {
            return childobject.runnable.testPreviousReadiness ();
        });
    };
    me.step_each_child = function () {
        this.children.forEach (childobject => {
            childobject.runnable.step ();
            childobject.runnable.route ();
        });
    };

    me.any_child_is_busy = function () {
        return this.children.some (childobject => {
            var ready = childobject.runnable.ready ();
            var busy = childobject.runnable.busy ();
            return (ready || busy);
        });
    }
    
    me.self_has_input = me.hasInputs;
    me.ready = me.hasInputs;
    me.busy = me.any_child_is_busy;
    me.hasWorkToDo = function () {
        var ready = this.ready ();
        var busy = this.busy ();
        return (ready || busy);
    };

    me.find_connection = find_connection;
    me.find_connection_in__me = function (_me, child, etag) {
        return find_connection_in__me (this, child.name, etag);
    };
    me.lookupChild = function (name) {
        var _ret = null;
        this.children.forEach (childobj => {
            if (childobj.name === name) {
                _ret = childobj.runnable;
            }
        });
        if (_ret === null) {
            console.error (`child '${name}' not found in '${this.name}'`);
            //process.exit (1);
            throw 'error exit';
        };
        return _ret;
    }
    if (protoImplementation.begin) {
            me.begin = protoImplementation.begin;
    }
    if (protoImplementation.finish) {
        me.finish = protoImplementation.finish;
    }
    me._done = false;
    me.conclude = function () { 
        this.container._done = true; 
    };
    me.done = function () {return this._done;};
    me.resetdone = function () {this._done = false;}
    me.wakeup = function () {
        if (this.container) {
            this.route ();
            this.container.wakeup (); // keep punting upwards until at top
        } else {
            this.resetdone ();
            this.route ();
            while ( (!this.done ()) && this.hasWorkToDo () ) {
                this.step ();
                this.route ();
            }
        }
    }

    return me;
}

```

## Transpilers
[Transpiler DaS](#transpiler-das)
[Transpiler Drakon](#transpiler-drakon)

## Github
[duct](https://github.com/guitarvydas/duct)
[hamburger workbench diagram to JSON - das2json](https://github.com/guitarvydas/das2json)
[hamburger workbench diagram to JavaScript - json2js](https://github.com/guitarvydas/das2json/tree/main/json2js)

## Appendices

