# 2022-06-08-Slides WP Writing a Script as a Diagram---
tags:
- slides
- DaS
---

I need to copy some files.  Normally, I would do this at the command line, and, if I wanted to do it more than once, I would capture the commands and shove them into a *.bash* script.

Not this time.  I am trying to write the script as a diagram, then evolve the diagram into code.

This WP note (Working Paper) is a capture of my thoughts as I go.

I already know how to transpile diagrams to code.  I discovered that hand-transpiling diagrams to fugly text is easy.  So easy even a machine could do it.  I guess that, for now, I will draw the diagrams and hand transpile them to Ohm-JS-able text code.  We'll see ...

# Top Level Script
!![dasscript-1. nested.png](images/dasscript-1. nested_15.png)
Not exactly rocket science...
1. clean out the target directory
2. for each file in the source directory, copy the file to the target directory
3. finalize, by renaming a certain file.

How hard can this be?

# Layer 2 - Rewrite Diagram as Communicating Components

!![dasscript-2. rewritten as component.png](images/dasscript-2. rewritten as component_15.png)

The inputs are async - they are not constrained to come "at the same time".

One of the inputs will be deconstructed into two named pieces "input-ports" and "output-ports".

There are 2 async inputs, which appear to have names on the diagram (the machine doesn't care about names, only human readers care).  I've used Unicode characters for the names, to keep me honest and to reduce the ASCII-only damage suffered by previous languages.

I imagine an *alist* for the "environment".  I call it `ū`, which happens to be a character in the Lithuanian alphabet.  I might have called it *env* but I wanted something shorter, and, I wanted to avoid Greek letters.

The point of an *environment* is to set up a map of scoped variables which can be used inside the scope.  If a variable name is not in the scope, it can't be used (and should cause some kind of error message).  This ain't rocket science.  Everyday functions have scopes.  Valid names within function scopes are those defined in the parameter list and those defined "locally".  I guess that *global variables* are in-scope, too, but we have been taught to avoid globals, so I only allow names that are explicitly wrapped in scopes, like nested Russian dolls.

The other input is a "start" ("go", "kick") input.  Its value, and, its name, don't matter.  It's a *trigger*.  The simple fact that it arrived is enough information.  A trigger carries even less information than a Boolean.  In electronics, this is called an *edge*, as in *edge-triggered*.

I used another Unicode character for its name.  On the diagram, it looks like an asterisk. In this (Obsidian) editor, it looks even more glorious.

So, the inputs are:
- ū an *alist* (AKA key/value map)
- ❇  a *trigger*

There's a greyed-out box called `_noname_1_` on the diagram.  The guts of this box are too involved to bother putting on this diagram, so I've pushed them into another diagram.  An ideal diagram-editor would allow me to draw a diagram, then multi-select a bunch of components and push them automagically to another diagram replacing the selection by a grayed-out box with the same inputs and outputs on its boundary as were in the top-level of the pushed-down selection. Or, something like that.  I believe - strongly - that an editor should know nothing about the data structures that it is editing, much like text editors.  Text editors edit text without knowing whether the text is a program or markdown or ... (whatever).  Some text editors add colour to the text, if the editor knows that the text is a program in some specific programming language.  Usually, the user has to tell the editor what kind of text is being edited and which plugin(s) to use for colourization.  Some editors are smart enough to run a plugin in the background which tries to guess what's in the text, then pull in the appropriate colourization plugin.  Editors that hard-wire knowledge about the contents of the text, have fallen by the wayside.  Hard-wiring is "bad", plugins are "better" and more flexible.  I guess that DaS editors will evolve into using plugins, too, instead of hard-wiring.  At the moment, most graphic editors hard-wire-assume that you want to create a painting instead of a technical drawing, e.g. a drawing of a program.  Sigh.

# Layer 3 - _noname_1_
The topmost diagram shows a *for each* box.

*For each* is actually an iterator and its guts break down into several components.

The *for each iterator* takes in a list of things (strings in this case) and feeds them, one by one, to a sub-component.

The sub-component is just like any other component.  There is nothing special about it.  It takes 2 inputs and produces 2 outputs (ū, ❇ as inputs, and ū, ❇ as outputs).

The sub-component is *wrapped* inside the *for each* box.

In text languages, we use *lambda*s (functions) to do this, and, we waste CPU power by using CALL/RETURN to implement the wrapping at runtime.

So, it seems that we need 3 boxes inside the implementation of this *for each*
1. something that creates a list of things to be iterated (the diagram shows this as 2 boxes - a constant string feeding into a "parser")
2. the logic for iteration
3. the sub-box which gets invoked repeatedly.

!![dasscript-3. _noname_1.png](images/dasscript-3. _noname_1_15.png)

The *for each* logic sends messages to the wrapped sub-component.  The messages make it *seem* that the sub-component is being invoked in the normal way, on a single item, instead of a list of items.

Each time the sub-component has done its thing, it fires a trigger on its ❇  output (actually, it actually fires its ū output, but we simply ignore that, it is uninteresting).

We re-route the ❇  messages from the sub-component back to the *resume* input of the *for each* box.

The *for each* box sends one item to the sub-component, then stalls until it gets a *resume* message.

The *for each* box keeps sending messages to the sub-component until there's nothing left to do.

When there's nothing left in the iteration list, the *for each* signals done-ness by outputing ū and ❇ .

If you look at the connections, you'll see where the outputs from *for each* go.

Something inside the `_no_name_1` box will take the original *for each* command, i.e. `for each file in '/Users/tarvydas/Dropbox/ps/%Hamburger Workbench - A Light Introduction to Ohm-JS'  ⇒ «f»`, apart and produce a list of filennames.  It will, also, send the bind-to variable name, `«f»`, to the *for each* handler.  In this case, the input string is the name of a directory and we want to get a list of files that are inside the directory.  We want each file in the list to be associated with `«f»` and to be sent out for work to the sub-component or *for each*.


# Layer 4 - Foreach State Machine

What is the logic for the *for each* box?  I like state machines, so I've drawn the logic out as a state 
machine.

!![dasscript-4. foreach-state-diagram.png](images/dasscript-4. foreach-state-diagram_15.png)

We see that the *for each* state machine has 4 inputs:
1. ū, to set the environment (in this simple example, this does nothing useful)
2. name, the variable name that will be used to hold each successive filename
3. [filenames], a list of filenames (strings)
4. resume, a trigger that signals when the sub-component is ready to do more work

The *for each* state machine has 4 outputs:
1.  ū, sent downstream to the next component, when the *for each* has finished iterating
2. done, sent downstream to the next component, when the *for each* has finished iterating (this is routed to the  ❇  input of the next top-level component in the pipeline)
3. sub-ū, sent to the sub-component when we want the sub-component to do work, we push a new key/value pair onto the ū before asking for work.  In this case the key will be `«f»` an the value will be the string name of a file.
4. kick, routed to the ❇  input of the sub-component, a message for the sub-component to do its thing

Note that it matters which order the messages are sent in.  We have to know - make a convention - that ❇  means "go".  This means that `sub-ū` will need to be sent before  ❇ .  Putting things in order is just "life", it's not rocket science.

On the state diagram, the ellipses with solid boundaries are blocking states (states that wait for inputs) and the dashed-boundary ellipses are non-blocking states (what we currently call "functions").

The hexagon represents a conditional.  I couldn't draw it inside its enclosing state, so I broke it out and joined it to its enclosing state using a dashed double-line.  I don't know what the best representation is for this kind of thing, but this works and I'll use it for now. You would immediately think that I could use zooming to draw a very small hexagon inside the enclosing state.  I think that the conditional is important enough information to need to be drawn explicitly as a large, readable, graphic instead of requiring zooming.  I am the Architect and I get to decide what is important enough to be drawn big.  Another Architect might choose to draw this differently.  Maybe someone will invent a feature for a drawing editor that handles this case better, like, say, the MacOS dock magnifier feature.  For now, what I have works with draw.io and I will use it.  For now.

Transitions between states are shown as arrows and are annotated with the input that triggers them, along with any code that gets executed when they are fired.  Solid arrows mean "wait for the next message, then check its etag".  Dashed arrows mean "transition right now, don't wait".

Note that I didn't bother to put lines on the state diagram joining the transitions to the ports (inputs and outputs) that they are associated with.  That would be too visually noisy and wouldn't be readable.  Maybe in the future, we will have program-diagram-editors that have layers and use alpha-channel graying out to show such various connections?

Q: If we used graphic, alpha-channel editors instead of paper to draw electronics schematics, would we still have a *ground* symbol?
[![Earth Ground.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Earth_Ground.svg/25px-Earth_Ground.svg.png)](https://en.wikipedia.org/wiki/File:Earth_Ground.svg)![Earth Ground.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Earth_Ground.svg/25px-Earth_Ground.svg.png
