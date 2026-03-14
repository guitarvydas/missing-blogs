# 2023-02-11-Computers Dont Just Compute
I tend to think of "computers" as "machines".  Small electronic machines, that take a bunch of low-power electrical inputs (3V-5V, milli-amps) and produce low-power electrical outputs, and, contain some "state" (aka RAM).  The machines are controlled by scripts, instead of, say, mechanical gears, mechanical pulleys, mechanical ratchets, etc..
![](2023-02-11-Computers%20Dont%20Just%20Compute%202023-02-11%2010.08.18.excalidraw.png)


You can hook low-power generalized electronic machines to "amplifiers" to control higher-power dumb devices (110V, 220V, amps ; motors, steppers, etc.).

For now, I will call "generalized electronic machines" GEMs instead of using the word "computers".  I think of a "computer" as a raisin-sized rPI (Raspberry PI, Arduino, etc.).  I call that a GEM to emphasize the fact that it can do more than just compute. 

Can GEMs compute?  Yep.

Is that all that GEMs can do?  Nope.

You can write scripts by hand ("Assembler").

You can write scripts using other apps ("compilers").

"Scripts" are for GEMs. "Programming Languages" are for other humans.

"Compilers" transpile "programming languages" to "scripts for GEMs"

There are ways to write specifications for scripts in a way that allows you to reuse parts of scripts for new scripts and that allows you to have less trouble when building scripts ("DRY" (Don't Repeat Yourself), type checking, so-called "computer science", etc.).

Currently, we are focused on writing specifications in call-stack-based, textual programming languages, but, that's not the only way to write script specs.

Call-stack-based programming languages have the side-effect that they restrict you to thinking only about calculation.

If you want to use a GEM to build a sequencer, you are out of luck, or worse, you have to invent epicycles that allow you to use calculator-only methods to specify sequencers (e.g. "control theory", "operating systems")

Aside: Control Theory was well documented in the 1950s, using things called "resistors" and "capacitors" and "inductors" and "Maxwell's Equations".  Note that Maxwell's Equations do not describe Electricity, they only describe a 2D subset of Electricity that we can use to calculate how to build a limited number of useful electronic things.  Electricity is - at least - a 4D effect (x/y/z/t).

Aside: Concurrency can be *faked out* through the use of Operating Systems.  To have True Concurrency, all you need to do is to use multiple rPIs (GEMs), each running single-threaded apps, connected by packets ("messages") sent to each other through wires.  To keep out of trouble, you simply need to invent the equivalent of Structured Programming for messaging - I call that "Structured Message Passing" (it may suprise you that I have opinions about that, too :-).
