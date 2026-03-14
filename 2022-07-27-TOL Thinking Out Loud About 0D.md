# 2022-07-27-TOL Thinking Out Loud About 0D
[Part 1 - The Problem](https://share.descript.com/view/lLHa9jaC9q9)

[Aside: eval](https://share.descript.com/view/xIlbRH4zlpM)

[Part 2 - Would Having Used A Static Language Have Helped?](https://share.descript.com/view/qQuJlYEoOuv)

[Aside: Epicycles](https://share.descript.com/view/jGY9VryQtPm)

[Structured Message Passing (Leadup Part 1)](https://share.descript.com/view/e2cxl0Ga6wX)

[Structured Message Passing (Leadup Part 2)](https://share.descript.com/view/LQdQRjlm31T)

[Design Rules](https://share.descript.com/view/kMno5tJhzxC)

[Aside: Design Rules](https://share.descript.com/view/9x85t8LOzUd)

[Structured Message Passing (Leadup Part 3)](https://share.descript.com/view/6h6h73oHZXv)

[Structured Message Passing](https://share.descript.com/view/pDyKpgerYRq)

# Text and Diagrams
## Part1 - The Problem
I've written some code. And there's a bug. Instead of just fixing the bug, I'm trying to figure out why I made the bug.  This happens to be in Java script. It's a dynamic language. As far as I can tell right now, the problem is that I am violating structured programming principles.

Structured programming says you have one input, which is this. That's actually a single input destructured  into four parts. But I have multiple outputs. There's five places.  I see now, looking back over this that I wrote the code up to around here. In one go. I knew what I wanted to return, which was a list of three things, a Boolean, a string, and another string. But then later I came back to it and wrote this code. And I wrote a list that had only two things.

JavaScript makes the third thing undefined.¶

```
function transpile (src, grammarName, grammars, fmt) {
    [matchsuccess, grammar, cst, errormessage] = patternmatch (src, grammarName, grammars);
    if (!matchsuccess) {
        return [false, "", "pattern matching error<br><br>" + errormessage];
    } else {
        [success, semanticsFunctionsAsString] = fmtjs (fmt);
        var evalableSemanticsFunctions = '(' + semanticsFunctionsAsString + ')';
        var sem = grammar.createSemantics ();
        try {
            semobj = eval (evalableSemanticsFunctions);
        } catch (err) {
            return [false, null, 'error compiling .fmt specification<br><br>' + err.message + ' ' + semanticsFunctionsAsString];
        }
        try {
            sem.addOperation ("_fmt", semobj);
        } catch (err) {
            return [false, null, "error in .fmt specifcation<br><br>" + err.message];
        }
        var generatedFmtWalker = sem (cst);
        try {
            //tracing = true;
            var generated = generatedFmtWalker._fmt ();
        } catch (err) {
            return [false, generated];
        }
        return [true, generated];
    }
}


function patternmatch (src, grammarName, grammars) {
    try {
        var grammarSpecs = ohm.grammars (grammars);
    } catch (err) {
        return [false, undefined, undefined, err.message];
    }
    try {
        var grammar = grammarSpecs [grammarName];
    } catch (err) {
        return [false, undefined, undefined, `grammar ${grammarName} not found in given grammars`];
    }
    if (grammar === undefined) {
        return [false, undefined, undefined, `grammar '${grammarName}' not found in given grammars`];
    }

    try {
        var cst = grammar.match (src);
    } catch (err) {
        return [false, undefined, undefined, err.message];
    }
    return [true, grammar, cst, ""];
}

```
## Aside: Eval
I use a eval in this place here on a string. That seems to be frowned upon in general, but it actually turns out to be exactly the same thing as using a compiler. A compiler takes a string. We call it a file. It, evals the string. And then outputs the result of the eval. And I'm just doing it programmatically.
## Part 2 - Would Using A Static Language Have Helped?
So the question arises if I had used a static language, would my problem have gone away? I think in the short term. Yes. But, I thinkthat solution is an epicycle. The real problem is that return is an adhoc assembler statement that is peppered throughout the code.
## Aside: Epicycles
What is an epicycle?

Today for political correctness, we use the term "workaround" instead of the word epicycle.

The term "epicycle" comes from the Ptolemaic universe that preceeded Copernican thinking.

We see that - for programming - the epicycle of using one in and one out in a synchronous fashion - the way we think of functions at the moment - is breaking down.

We have all sorts of tells and aren't noticing.

One of the tells is that we think that callbacks are hard.

Another tell is that JavaScript programmers don't want to use monads and the other complicated forms of functional programming - epicycles - that are being developed to support the continued use of synchronous functions.

Another tell is that multitasking is considered to be hard. Multitasking is quite simple. It's on the order of about 10 bytes long. Why do we need operating systems that are thousands of bytes long?
## Structured Message Passing Part 1
I would suggest that what we really want is to wrap the functions in some sort of an envelope that gives us what we call structured programming.

We already kind of have that. We call it processes. We need one input, one output .We need a way to capture all the returns and jam them into one place.

That kind of happens under the hood.

And then if we look at this, we realize maybe structured programming isn't what we really want for distributed programming. Maybe we want multiple outputs.

In Structured programming - functional programming - what we get is that the single output is always routed to the caller.

What we want in distributed programming is zero or more outputs that are routed to different places, maybe the caller, or maybe other places. At the moment - in functional programming - we usethe derisive term "side effect". But, that's not really what's going on here and that's not the way we structure internet solutions.

![](images/design rules-function in dynamic language.png)

## Structured Message Passing Part 2
So what's the first step in converting from the way we program in what I call zero D - which is zero dependency?

The number one thing is to understand what we're doing. I've used a dynamic language and I've written a function called transpile. It takes input and it produces output and there's nothing that checks the input and nothing that checks the output.

![](images/design rules-function in dynamic language.png)

We already know how to handle that problem. We do it in websites and we call it input validation. At least for one side.

![](images/design rules-website.png)

So we get stuff in. We don't know what it is. It could be anything from the user. We validate it. If it's okay, then we call the function to handle it.  We extend the idea further. Then we want input validation and output validation. That's kind of what we're doing with the static languages and type checkers. Except that we're also imposing the synchronous constraint on the way thatwe write code in those kinds of languages.

We want to break that constraint.

The model that I'm looking at is 

![](images/design rules-IO validation.png)

we get some input into a component. The component validates the input. And it either passes it on to the function or it declares some kind of error saying that the input was invalid. When the function is done, we grab its output and we run through another validator. And the same thing, we either pass the result on, or we say the output was invalid.

I call that design rules. Currently we call this "type checking", but the error case is handled only at compile time. And it requires that one write code in a synchronous manner.
## Design Rules
We simply chop up the previous diagram into separate components and we get something like this diagram. So we get a component for input validation, a component for output validation and a component that holds the original function that I was trying to get working.

And each one of them has separate ports.

![](images/design rules-Type Checking Pipeline.png)

## Aside: Design Rules Are More Powerful Than Type Checking
What I haven't said so far is that design rules can actually be morepowerful than type checking.

In type checking all you can do is check the DSL that you are given as a programming language.

Whereas, with design rules, you can program up a check to validate input and output depending on your project or on a sub project level.
## Structured Message Passing Part 3

Now the problem becomes slightly simpler. We just look at the transpile function and ask ourselves, how can we make it work more like a component that has one input and one output.

![](images/design rules-Copy of Type Checking Pipeline.png)

In this particular piece of code, what we have is one input, which comes in as a block and then is destructured into four parameters,but the returns come in different places. And they use the hardware supported  global variable  call stack and we need to breakthat.

So the first step is simply to replace the returns by accesses to a FIFO output queue.

This is already what happens under the hood with compilers. Except that compilers don't use a FIFO queue. They use the call stack.

# Structured Message Passing


## 2022-07-27-Structured Message Passing

---
tags: 
copied_to_pages: "true"
---

---
# Structured Message Passing
video: [Structured Message Passing](https://share.descript.com/view/pDyKpgerYRq)

---
# Structured Message Passing

"Structured message passing" implies that we must encapsulate every aspect of Components

- data flow

and 

- control-flow

---
# Scalability
Scalability comes from Structured message passing 

You can only scale a system where Components are not tangled together.

---

# Existing Languages
   - simply stop using hardware-supported CALL / RETURN for communication between Components
   - create 2 classes of Components

---

# Don't Use CALL/RETURN
- Don't use hardware-supported CALL/RETURN for communications between Components

- use FIFOs instead

- it's OK to use CALL/RETURN for code *inside* a component, but not as a means for communicating between Components

---

# 2 classes of Components
- Leaf Components (code)
- Container Components (routers)

---

Structured message passing implies that we must encapsulate every aspect of components.

That includes data flow and control flow.

We can't just concentrate on data flow.

Scalability comes from structured message passing.

You can only scale a system when components are not tangled together.

How do you do this using existing languages? Simply stop using hardware supported call return for communication between components. And create two classes of components, not one class.

So, how do you not use call return? It's simple. Just use FIFOs.

It's okay to continue using call return for code inside a component. But don't use call return as a way of communicating between components.

Creating two classes of components. I see there being leaf components for code and container components for routers that compose components and route messages between them, but they don't actually do anything.They can run other components.

Container components devolve into other container components or leaf components.  Stepping means we finally get down to a leaf and a leaf just does something and stops.

1. "Structured message passing" implies that we must encapsulate every aspect of Components - data and control-flow
2. Scalability comes from Structured message passing (you can only scale a system where Components are not tangled together)
3. Structured message passing is straight-forward using existing languages
   - simply stop using hardware-support CALL/RETURN for communication between Components, use FIFOs instead
     - it's OK to use CALL/RETURN for code inside a component, but not as a means for communicating between Components
   - create 2 classes of Components
     - Leaf Components (code)
     - Container Components (routers)

# Github
https://github.com/guitarvydas/fmt-js

# Disclaimer
I am experimenting with Discord as a way to communicate.  

I seem to edit myself less when speaking than when writing.  Although, I drag words out as I think.  (I, also, insert a lot of "ums", but Discord helps me remove those).

All of the above is "stream of consciousness", and should not be considered to be final, correct, etc.

I guess that I am creating a Twitch-like stream of how I am thinking, where I get to edit the stream down to only a few minutes...

I vacillate between using *studio sound* and not using it.  Therfore, the sound quality of the clips is inconsistent.  Some clips have background noise and others don't.  
