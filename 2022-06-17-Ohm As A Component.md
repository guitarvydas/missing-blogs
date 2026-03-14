# 2022-06-17-Ohm As A Component
# Ohm-JS As A Component
I want to think of Ohm-JS as a black box (a *component*).

1. First, I draw the the signature of the desired Ohm-JS transpiler component.
2. I manually transcribe the signature into `.tbx` ("toolbox") format.  I call input and output parameters *ports*.
3. I add an Implementation.
4. I use an Ohm-JS grammar plus a `.fmt` spec to re-write the `.tbx` file into a `.js` file
5. I modify the .HTML ("baseline") function to use the black box (the `.js` file from step (4))
6. Re-test.

> [!tip] To create a black box, it is not enough to have *input* parameters.  The black box must have ***output* parameters**, too.

This is quite easy to do.  The black box does not *call* other functions, it simply sends *deferred messages*.

Deferred messages are messages that are not delivered immediately, but, simply pushed onto an output queue belonging to the component (semantically[^opt]).  

[^opt]: This can be optimized, later.

**Of Note**: Step (2) can be automated.  I perform this step manually for explanatory purposes.   See elsewhere for my technique of automatically transpiling diagrams to text code.

## 1. Black Box Transpiler Signature
![](fmt-Transpiler.png)


## 2022-06-18-Black Box Software Components

![](fmt-Transpiler.png)

> [!tip] A black box does not know where its output messages will be routed.

In fact, a black box does not even know *if* its output messages will be routed to any receivers.

A black box simply sends messages to its outputs and lets its Container decide how to route messages.  Output messages are simply appended (deferred) to a Component's output queue and are left for the direct Container to deal with.

Message routing is done solely by a component's container.  The container does not care (nor know) how its children components are implemented (as Leaves or as Containers).  

Each component, Leaf or Container, has 1 input queue and 1 deferred output queue.

Messages are tagged by the input they are associated with, and then appended to the input queue of a component.  A tag is a port id.

Containers receive *step* commands, and delegate these commands to their children.  

Containers route messages from each activated child.

Containers contain 
- children components
- a routing table
	- messages can be routed from a child's output to other children's inputs
	- messages can be routed from a container's inputs to its children
	- messages can be routed from a child's output to a container's output
	- (rarely occurring edge-case) messages can be routed from a container's inputs to its own outputs
	- child messages can be routed to NC (No Connection)
	- child inputs can be marked NC ; a child does no work if its input queue is empty
	- container inputs can be routed to NC.

A Container is *busy* if any of its children is *busy*.  

A Component processes 1 input message to completion before pulling another input message for processing.

This implies that a Container must step all of its children to completion before pulling another input message.  

A Container may be activated multiple times with *step* commands.  It must delegate these *step* commands to its children until all children's activity has subsided.

A Container can refer only to its direct children.  A Container cannot refer to children of children.

A component, Leaf or Container, cannot refer to its peers.  

A Container can only send messages to its direct children, or send messages to its direct parent.  

Messages being sent downwards are usually in the form of commands.  

Messages being sent upwards are usually in the form of filtered information.  

A component "sends" messages to its parent by leaving deferred messages in its own output queue.  The direct parent can inspect and deal with the output queues of its direct children.

### Fan-in
A component, Leaf or Container, can receive messages from mutiple sources.

The component must process messages in order of arrival, one input message at a time.

### Fan-out
A component, Leaf or Container, can create messages that are routed to multiple receivers.

This implies that the component's Container must deal correctly with message copying, or, that message data is considered read-only (copy-on-write) by all receivers.  [Note that Javascript objects follow a copy-on-write policy using prototypal inheritance. Object fields are read by recursive lookup, but when written, the fields affect/create only *own* data.]

Fan-out is affected by the "Messages Must Not Interleave" rule.

## Messages Must Not Interleave
A message must arrive "at the same time" at all receivers.

For example, if A sends ẋ to C, D and E, and, B sends ẏ to C and E, then, C and E must see ẋ before ẏ or ẏ before ẋ.  The situation where C and E see ẋ/ẏ in a different order must not happen, i.e. C must not see ẋ,ẏ while E sees ẏ,ẋ.

A simplistic way to ensure this rule is to send messages atomically by locking all of the queues of all receivers before appending a message.  There might exist optimizations to this method that I haven't thought of yet.


## 2. `.tbx` Transcription
> [!tip] Implementation Details
> Feel free to skip section 2.
> 

I have (arbitrarily) chosen Unicode bracket characters, "⟨" and "⟩", to bracket port-names (input and output).  I use Unicode bracket characters, "❲" and "❳", to wrap identifiers that have whitespace in them.  I use the Unicode character "⤇" as a separator between input ports and output ports (left of "⤇", and right of "⤇", resp.).

I chose Unicode brackets,  "⟪" and "⟫", for verbatim code sequences.  Verbatim code contains raw code in some programming language (in this case JavaScript) and is skipped-over by the transpilers.  Verbatim brackets are simply stripped out in the final step of automatic transpilation of `.tbx` to *programming language* (`.js` in this case), leaving the raw code as part of the final result.

## 3. `.tbx` Implementation
> [!tip] Implementation Details
> Feel free to skip section 3.
> 

I use brace brackets `{ ... }` to enclose Implementation code immediately following Signatures.

There are two kinds of recognized Implementations
1. `{ Leaf { ... }  }`
2. `{ Component { ... } }`

Programmers supply code for message handling by writing Implementations.  

All of the other code is boiler-plate and automatically supplied by the system.

`Leaf` component Implementations have 
1. `persistent` variable declarations ("instance variables" in OOP terminology)
2. `on` event transitions
	- transitions supply a single source (input) port name and some code
	- TODO: add guards (calls to predicates that must return `yes` before a transition is fired)
	- a block of code (see elsewhere for valid code phrases).

```
comp transpiler ⟨go⟩ ⟨src⟩ ⟨❲grammar name❳⟩ ⟨❲grammar text❳⟩ ⟨❲hook name❳⟩ ⟨❲semantics hooks❳⟩ ⤇  ⟨success⟩ ⟨❲transpiled text❳⟩ ⟨error⟩ {
  leaf {
   persistent src
   persistent ❲grammar name❳
   persistent ❲grammar text❳
   persistent ❲hook name❳
   persistent ❲semantics hooks❳
   on ⟨src⟩:               save ⇉ src
   on ⟨❲grammar name❳⟩:    save ⇉ ❲grammar name❳
   on ⟨❲grammar text❳⟩:    save ⇉ ❲grammar text❳
   on ⟨❲hook name❳⟩:       save ⇉ ❲hook name❳
   on ⟨❲semantics hooks❳⟩: save ⇉ ❲semantics hooks❳
   on ⟨go⟩:
     temp ⟪ohm.grammars (this.❲grammar text❳)⟫ ⇉ gs
     temp ⟪gs[this.❲grammar name❳]⟫ ⇉ g
     temp ⟪g.match (this.src)⟫ ⇉ cst
     if (⟪cst.succeeded ()⟫) {
       temp ⟪g.createSemantics ()⟫ ⇉ sem
       do ⟪sem.addOperation (this.❲hook name❳, this.❲semantics hooks❳);⟫
       temp ⟪sem (cst)[this.❲hook name❳] ()⟫ ⇉ result
       send true ⤇ ⟨success⟩
       send result ⤇ ⟨❲transpiled text❳⟩
     } else {
       send false ⤇ ⟨success⟩
       send ⟪g.trace (src)⟫ ⤇ ⟨error⟩
     }
  }
}
```

**Of Note**: The `.tbx` implementation supplies the *bare minimum* code phrasing necessary to implement a component.  Code that does "something else" is written in another language and included as *verbatim* code.  In the above example, I've included snippets of JavaScript as *verbatim* code. TODO: it might be possible to define layers of toolbox languages that allow phrasing common to most other programming languages (e.g. lambdas, mutation, etc.).  This is an area of active research.
# 4. `.tbx` As `.js`
> [!tip] Implementation Details
> Feel free to skip section 4. on first reading
> 

```
function Transpiler () {
    this.getOutputMap = function () {
        let map = {};
        this.outputqueue.forEach (output => {
            map [output.port] = output.data;
        });
        return map;
    }
    this.outputqueue = [];
    this.src = undefined;
    this.grammar_name = undefined;
    this.grammar_text = undefined;
    this.hook_name = undefined;
    this.semantics_hooks = undefined;
    this.handler = function (message) {
        message.port = message.port.replace (/ /g, '_');
        if (message.port === "src") {
            this.src = message.data;
        }
        if (message.port === "grammar_name") {
            this.grammar_name = message.data;
        }
        if (message.port === "grammar_text") {
            this.grammar_text = message.data;
        }
        if (message.port === "hook_name") {
            this.hook_name = message.data;
        }
        if (message.port === "semantics_hooks") {
            this.semantics_hooks = message.data;
        }
        if (message.port === "go") {
            let gs = ohm.grammars (this.grammar_text);
            let g = gs[this.grammar_name];
            let cst = g.match (this.src);
            if (cst.succeeded ()){
                let sem = g.createSemantics ();
                sem.addOperation (this.hook_name, this.semantics_hooks);
                let result = sem (cst)[this.hook_name] ();
                this.outputqueue.push ({port: "success", data: true});
                this.outputqueue.push ({port: "transpiled_text", data: result});
            }else{
                this.outputqueue.push ({port: "success", data: false});
                this.outputqueue.push ({port: "error", data: g.trace (src)});
            }
        }
    }
}
```

The `.ohm` grammar...
```
comp {
  Main = "comp" nameDef InputPort+ "⤇" OutputPort+ Implementation?

  Implementation = "{" (LeafImplementation | ContainerImplementation) "}"

  LeafImplementation = "leaf" "{" Handler "}"

  ContainerImplementation = "container" "{" Handler "}"

  Handler = PersistentVariable+ Transition+

  PersistentVariable = "persistent" nameRef

  Transition = "on" SourcePort ":" Code+

  Code =
    | "save" "⇉" nameRef -- save
    | TempVariable -- temp
    | IfStatement -- if
    | "do" verbatim -- do
    | "send" Expression "⤇" SinkPort -- send

  TempVariable = "temp" Expression "⇉" nameDef
  IfStatement = "if" "(" Expression ")" "{" Code+ "}" "else" "{" Code+ "}"

  Expression =
    | verbatim
    | operand

  operand =
    | nameRef

  Port = "⟨" #nameRef "⟩"
  InputPort = Port
  OutputPort = Port
  SourcePort = Port
  SinkPort = Port

  name =
    | "❲" (!"❳" any)* "❳" -- bracketed
    | ident -- single

  nameDef = name
  nameRef = name
    
  verbatim = "⟪" (!"⟫" any)* "⟫"
  
  keyword = ("save" | "send" | "do" | "temp" | "if" | "else" | "comp" | "leaf" | "container" | "on" | "persistent") &separator
  ident = !keyword ident1 identrest*
  
  ident1 = "_" | letter
  identrest = alnum | ident1

  separator = " " | "\n" | "\t"  
}
```

The `js-comp.fmt` re-formatter into Javascript...
```
Main [kcomp NameDef @InputPort karrow @OutputPort @Implementation] = [[function ${fmt.capitalize (NameDef)} () {${Implementation}\n}]]

Implementation [lb x rb] = [[${x}]]

LeafImplementation [kleaf lb Handler rb] = [[
this.getOutputMap = function () {
  let map = {};
  this.outputqueue.forEach (output => {
    map [output.port] = output.data;
  });
  return map;
}
${Handler}]]

ContainerImplementation [kcontainer lb Handler rb] = [[
this.outputqueue.forEach (output => {
    map [output.port] = output.data;
  });
  return map;
}
${Handler}]]

Handler [@PersistentVariable @Transition] = [[\nthis.outputqueue = [];${PersistentVariable}\nthis.handler = function (message) {\nmessage.port = message.port.replace (/ /g, '_');
${Transition}
}]]

PersistentVariable [kpersistent NameRef] = [[\nthis.${NameRef} = undefined;]]

Transition [kon SourcePort kcolon @Code] = [[\nif (message.port === "${SourcePort}") {${Code}\n\}]]

Code_save [ksave karrow NameRef] = [[\nthis.${NameRef} = message.data;]]
Code_temp [TempVariable] = [[${TempVariable}]]
Code_if [IfStatement] = [[${IfStatement}]]
Code_do [kdo verbatim] = [[\n${verbatim}]]
Code_send [ksend Expression karrow SinkPort] = [[\nthis.outputqueue.push (\{port: "${SinkPort}", data: ${Expression}\});]]

TempVariable [ktemp Expression karrow NameDef] = [[\nlet ${NameDef} = ${Expression};]]
IfStatement [kif lp Expression rp lb @Code rb kelse lb2 @Code2 rb2] = [[\n${kif} ${lp}${Expression}${rp}${lb}${Code}\n${rb}${kelse}${lb2}${Code2}\n${rb2}]]

Expression [x] = [[${x}]]

operand [NameRef] = [[${NameRef}]]

Port [lb NameRef rb] = [[${NameRef}]]
InputPort [Port] = [[${Port}]]
OutputPort [Port] = [[${Port}]]
SourcePort [Port] = [[${Port}]]
SinkPort [Port] = [[${Port}]]

name_bracketed [lb @cs rb] = [[${lb}${cs}${rb}]]
name_single [ident] = [[${ident}]]

nameDef [Name] = [[${Name}]]
nameRef [Name] = [[${Name}]]

verbatim [lb @cs rb] = [[${lb}${cs}${rb}]]

ident [ident1 @identrest] = [[${ident1}${identrest}]]

ident1 [c] = [[${c}]]
identrest [c] = [[${c}]]

keyword [kw la_sep] = [[${kw}]]
separator [c] = [[${c}]]
```

**Of interest**: the output queue is flattened into a single JavaScript object (a *dictionary*) by the `this.getOutputMap ()` function.  TODO: is this a good idea?, should the output queue have only one of each value or should it have a stack for each value? (AKA *alist*).

## 5. Modify HTML
```
  function baseline () {
      let src = document.getElementById('src').value;
      let transpiler = new Transpiler ();
      transpiler.handler ({port: "src", data: src});
      transpiler.handler ({port: "grammar name", data: "baseline"});
      transpiler.handler ({port: "grammar text", data: grammars});
      transpiler.handler ({port: "hook name", data: "walk"});
      transpiler.handler ({port: "semantics hooks", data: rewriteRules});
      transpiler.handler ({port: "go", data: true});
      let result = transpiler.getOutputMap ();
      if (result.success) {
          document.getElementById('status').innerHTML = "OK";
          document.getElementById('output').value = result.transpiled_text;
      } else {
          document.getElementById('output').value = result.error;
          document.getElementById('status').innerHTML = "parse FAILED";
      }
  }
```

Of Note: The above code calls `transpiler.handler (...)` 6 times, once for each input port.  

This could be optimized to use only one input port by changing the signature. 

But, why optimize this?  The above code is for machines, not humans, to read.  It doesn't matter what the code *looks* like to human eyes. 

Note that current programming languages use the single-port method.  All inputs arrive in a single block (non-homogenous) at the same time to a function.  The function, then, desctructures the block into what looks like separate parameters.

It might be more beneficial (AKA flexible) to leave the input ports separated as shown in the above signature.  This might allow distributed apps to function more simultaneously (parallelism is but a subset of simultaneity, IMO).  Separate ports can be fired at different times.

## 6. Re-Test
Load `index4reordering0D.html` into a browser and click the "Test" button.

## Github
[tbx](https://github.com/guitarvydas/tbx)
