# 2022-06-08-Programming>`... do use REPLs ...`

I guess it depends on what you think a REPL is and what *programming languages* are.

IMO: *programming* is a way to control a machine.  *Programming languages* are just mid-1900s ideas on how to do this.  

I can imagine other ways to control machines instead of using scripts written with grids of non-overlapping, small bitmaps (characters).

From this perspective, I think that Bret Victor was just trying to show the same thing, i.e. you could use 2D graphics to control machines.

IMO a REPL is an interactive way to try out your program, regardless of the representation of the program.

So, a REPL for a text language is, usually, a text prompt which accepts text commands and executes them immediately and immediately shows you the results.

A REPL for a program which uses a graphical GUI, is a slider widget.  You give the program a command by sliding the slider, the command is interpreted immediately and you, immediately see the results.

Let's say that your control program is written in JavaScript and sits in a browser.

In one case, you accept commands in a text widget and call the appropriate JS code.

In another case, you accept commands in a slider widget and call the appropriate JS code.

Traditional Lisp REPLs didn't run in browsers.  Their "text widget" was console I/O (QWERTY, Teletype, etc.).

To me, it's all the same.  To me, a REPL means turn-around-time to results and how fine a grain for commands can be used.  It used to take a long time to run the whole program every time you made a small change, so the Lisp REPL worked on a function-grain.

I don't expect tht we'll ever not-need the REPL concept.  We'll keep scaling ideas up until what we want to try out takes a long time, even on modern hardware.  At that point, we need to decide whether we want to see partial results immediately or just run the whole thing and wait.

> ... There is no "one language to rule them all" ...

I think that all current languages are assembly - JS, Python, Haskell, etc, etc. 

Each language excels at something, but, tends to ignore something else.  PROLOG is a great example.  PROLOG is wonderful for exhaustive search, but, it's a PITA for simple formatting of output text.  I can do formatting in JavaScript without forcing relational concepts onto the task.  Likewise, Smalltalk is great, except at the edges.  Haskell is great for type-checking, but not every use of printf() needs massive type checking.  FP is great until you step out of its sweet spot, then you get stuff like callbacks.

Harel Statecharts are great for programming sequences of steps, but modern progamming teaching makes this politically incorrect.

If I was programming a ballistics calculation, I'd want to use FP and I wouldn't want to use Statecharts.  Yet, if I was programming a sequencer (music, robotics, etc.) I would choose Statecharts over FP.

I want to write code in whatever notation is convenient and then bolt the pieces together to form a final program.

I don't want to be forced to earn a PhD before writing programs.

[Programming is simple, but encumbered by overuse of ideas from analysis].

Back to assembler ...

IMO, the way we will ratchet humanity upwards is to build stuff up, then see problems in a new light, then re-express the problems more economically by inventing more notations.  Repeatedly.

Each notation elides *something* and reduces confusion in some dimension (but not all dimensions).  Some people can go a lot further before they become overwhelmed by details, but, in the end, the trick is to push details down, wrap them in a notation and move on.

Assembler is a high-level language.  It hides all of the details of VLSI electronics.  VLSI is, itself, a high-level language that elides all of the details of transistor-based electronics.  And so on down to molecules and atoms and sub-atomic particles, and, ... .  

Assembler elides some details and gives us a restricted API to work with.  On top of that API, we built FORTRAN.  On top of that API, we built notations like Haskell.

If it doesn't fit on a T-Shirt, then you haven't zoomed out far enough, and, haven't started using the next-level-up notation.  

If it DOES fit on a T-Shirt, ask to see the VLSI layout (I bet that won't fit on a T-Shirt...).

If you think that [*--your favourite notation--*] is the answer to everything, then you are promoting a fad.

> `... brain-damage that pervasive synchrony has caused ...`

Simple example.  You build apps which are interconnected like gearboxes from one end to the other.

You change something here and something over there suddenly works differently.

This is what happens when your programming language gives you synchronization when you didn't ask for it.  Everything you write is a cog, intimately connected to everything else.

AFAICT, every programming language hard-wires synchrony into the very lowest levels of your app.

Instead of removing the unneeded synchronization, programmers find "work-arounds."  Programmers invent words like "dependency" and then go about solving the "dependency problem".  Programmers invent ways to break synchrony and then use these techniques on top of synchrony ("thread libraries").

The idea of synchrony is so hard-wired into every programming language, that programmers can't even imagine non-synchronous ways of doing things.  (This was well-understood in the TTL electronics days, so it's not impossible).

Programs are expected to be composed of text.  Programming editors edit non-overlapping grids of bitmaps, strictly entered in a sequential manner (top to bottom, left to right), even though we've had overlapping windowing hardware for decades.

Some problems are easier to solve if you don't make them into gearboxes.  Problems like GUIs, robotics, IoT, etc.  But, that's not how programmers try to solve these problems.

Today's programming languages are great if you believe in the Waterfall Method.  If you believe in brainstorming and being able to change your mind - not so good.

# So, What Do You Do About It Right Now?
[tbd - next instalment]
