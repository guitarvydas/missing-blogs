# 2022-11-08-Robotics Use-Case
I consider a very simple use-case in robotics, then discuss this in the context of current General Purpose Programming Languages and propose a Layered Programming Language.

## A Simple Use-Case

Use-case in robotics:

There a 3 things in a line.

1. me.
2.  humanoid robot
3. a small box from Amazon.

!![robot use case.png](images/robot use case_14.png)

I want the robot to hand me the box.

The robot simply reaches with its right hand, picks up the box, then swings its right hand in a large arc towards me and drops the box in my lap.

The code is "Give me the box.".  I will call that kind of code "DI" (for Design Intent).

That's the spec, but, what happens underneath?

The robot's right hand cannot reach me unless the robot turns its torso.

To look natural, the robot's eyes must track the box in its right hand.  The eyes can turn only so far, so when the range of eye motion is used up, the robot must turn its head.  The eyes move from right to left, when the left-most position is reached (or before then), the head must turn a bit and the eyes must snap back to the right-most position.

Furthermore, the robot's hand can't reach the box nor me, unless the robot moves its arm.  And so on, in increasing detail.

## A Mess of Details
How do you write this sort of code in a functional manner?  A mess of details.  The details depend on the underlying hardware, too.

## Don't Waste My Time With Details
I'm the CEO of the robotics company.  I don't want to waste my time specifying the mess of details.  That's your job.  

In fact, details are the job of the Engineer(s) and Coding is the job of the Implementor(s).  Engineers think this through, but, don't actually write the code.

Analogy: building construction (Architects, Engineers, blueprints, Construction Workers).

## Mimicking the Human Body

The human body has 100's of joints and actuators (muscles).  The human-DI, the intent, is set by the human's "consciousness", then, this single-threaded "consciousness" gets out of the way and lets the actions happen without trying to micro-manage the actions.  For example, we don't walk through a closed door by commanding the fingers to grasp the doorknob and turn it, then command the arm to pull back, ...  We simply "will it, all, to happen".

Most of the popular computer programming languages that we use today, are made for writing micro-management code.

Most popular languages are really single-threaded at heart and would be great for programming the robots's "consciousness", but, that's not how we use these languages.  We have bolted ad-hoc, assembler-like operations onto the sides of languages (called "thread libraries") to allow even more micro-management. I think that we would want to have the eye-controller "send an event" to the head-controller (to tell the head to turn). Programmers tinker with Events, using ad-hoc, flat concepts like Pub/Sub.  By "flat", I mean "unstructured", the way that Assembler was before the Structured Programming revolution.  We could use a similar revolution to help us structure Events, e.g. "Structured Message Passing".

In fact, I think that we should want to build this kind of software in layers, then stack the layers to make the final robot.

## How Would I Start To Program This?
1. Speak the DI phrase "give me the box".
2. Use an AI speech-to-text converter to turn this spoken phrase into a blob of text, so that current text-processing tools can be used.
3. Use Ohm-JS to grok the text phrase "give me the box"
4. Use Fab[^fab] to convert the grokked phrase into more lower-level phrases, like:
	1. figure out where I am
	2. make a plan to grasp the box
	3. make a plan to swing the grasped box to the target
	4. make a plan to release the grasped box onto the target destination (ie. drop box onto my lap)
	5. make a script of Commands to carry out plans 1-4 in sequence
	6. carry out the script
5. Obviously, each of the plans 1-4 contain sub-plans.
	- For example, plan (3) might be something like:
		- Tell the hand to swing over to the target
			- The hand software needs to tell the arm software to move at the right time
				- The arm software needs to tell the torso software to swivel at the right time
		- Tell the eye software to track the box
			- The eye software needs to tell the head to swivel at the right time
				- The head software needs to tell the torso software to swivel, if it's not already in the correct positition - at the right time
		- ...

Step 5 shows how I think about this - in layers.

Flattening the layers to fit the functional programming model is make-work, and, wanton obfuscation of the original DI.

## A Programming Language Of Layers
What I want is a programming language that lets me program in layers.

At the moment, I think that I need two (2) simple concepts:
1. Leaf code
2. Container code.

Leaf code is what we call "programming" these days.  Python would be Leaf Code.  Haskell would be Leaf Code.  Rust would be Leaf Code.  Etc.

Leaves produce results by creating Messages and leaving them on their own Output Queue.

Container code doesn't need to do much:
	- Containers contain other Components - Leaves or Containers (recursively) 
	- Containers shepherd messages between their direct Children, using Routing Tables.
	- Containers produce results by creating Messages and leaving them on their own Output Queue (just like Leaves do - in fact, you can't tell if a Component is a Leaf or a Container unless you look inside).

### Message Shepherding
Containers shepherd messages in one of four (4) ways:
1. Down
2. Up
3. Across
4. Pass Through

Leaves can't shepherd messages.  A Leaf can only leave messages on its own output queue.

#### Down
A Container reacts to an input message by moving it to zero or more of its Children.

#### Up
A Child can create a result message that is repurposed as the result message of its parent Container.

In this case, the Child's message is moved from the Child's output queue to the parent's output queue.
#### Across
Child-to-Child messaging.

A Child cannot (must not) refer directly to another Child.

A Child leaves an output message on its own output queue and its *parent* handles the routing of the message.

The message can be moved to one (1) or more (>1) other Children.

Or, the message can be ignored and not moved to any other Child.  The *parent* decides what the routing policy is for some messages.

#### Pass Through
An edge case: a Container can react to an input message by moving it to its own output queue without handing it off to any Child.

### Layering
Given that Containers are recursive, I think that the above programming language design gives me layers.

The "secret" to what's going on here is subtle.  Most General Purpose Programming Languages (like Python, Rust, etc.) use *functions* which boil down to the use of the call-stack.  The "secret" to layering[^0d] is to use Queues instead of Stacks.  Since the functional notation is ingrained in our consciousness as needing a call-stack, I would suggest using another notation for queue-based message sending.

[^0d]: In fact, a precursor to this "secret" is the "secret" of 0d.

At this moment, I'm tinkering with syntax like:

`š.outputs/push (⟪𝜌port 𝜌data š 𝜌message⟫)`

This experiment can be found in https://github.com/guitarvydas/0d. 

Beware: this work is experimental.

Beware, also, this suggested notation subsumes a bunch of notions, like Orthogonal Programming languages, Unicode brackets for messages, unicode symbols like `š` for *self* and "𝜌" for parameters, "/" for method invocation, etc., etc.

Collaborators welcome (no experience necessary).

[^fab]: Fab is an adjunct tool that I use with Ohm-JS so that I can avoid writing detailed semantics in Javascript.