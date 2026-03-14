# 2023-06-10-Simplifying Assumptions
Physicists use something called *simplifying assumptions* when thinking about complex problems and designing notations to describe these problems and solutions to these problems.

Programmers use but one *simplifying assumption* - sequential operation, synchrony - which fits one use-case for PEMs (Programmable Electronic Machines, aka "computers"), but, does not fit well with other use-cases for PEMs, like sequencing.

Physicists *remember* what the parameters are for their *simplifying assumptions* and *when* those assumptions *can* be applied and *when* they *cannot* be applied.

Programmers, though, try to use the same *simplifying assumption* (sequentialism) for solving *all* problems.  This is called a Silver Bullet and a *fad*.  This practice leads to epicycles (aka "accidental complexity").  The fact that 50+ years of research has led to development of workarounds (aka epicycles, accidental complexity) for dealing with out-of-bounds use-cases using the same *simplifying assumption* has lulled programmers into a sense of complacency about their use of a single Silver Bullet.  

It is *possible* to use the synchronous *simplifying assumption* to describe non-synchronous activities, e.g. thread libraries. This fact does not mean that the problem has been solved in the best way possible.  The fact that something *can* be done does not mean that it *should* be done.

The fad of using function-based programming languages has not led to more reliable software.

When Ford Motor Company produced automobiles whose gas tanks exploded on impact (Pinto), people screamed and sued Ford.  When software fails in the field, though, people simply wait for an update.  For some reason, broken software is accepted as the norm, and, people just shrug their shoulders and tolerate it.

The simplifying assumption of function-based programming started in 1954 with FORTRAN and has blossomed into a virulent religion.

Example: functional programming has made GUIs in 2023 worse than GUIs in the 1970s.  When editing a simple file of text, the screen may jump and re-display itself to appease technical concerns.  This behaviour is disconcerting to the end-user.  This behaviour did not happen in older GUIs, like spreadsheets and word processors.  In fact, old word processors did redisplay the contents of the file, say, if the end-user's cursor hit the bottom of the window, but the redisplay happened in a fashion that did not jerk the end-user's attention.  The end-user was always in control of what was displayed, whereas today, the underlying function-based code is in control.  The screen redisplays at the whim of technical concerns instead of doing only what the user intended.

*...screenshot needed...*

The function-based *simplifying assumption* is appropriate for keeping technical details in synch, but, the function-based *simplifying assumption* is not appropriate for creating GUIs.  

I argue that programmers should use *simplifying assumptions*, but, that they should use *many* such simplifying assumptions.  The main reason that programmers think using only one assumption is that it has been believed that programming languages are difficult to create, and, that programming languages must be based solely on textual expression.  Both of these problems were based on biases developed in the 1950s, based on the limitations of 1950s hardware technologies.  

Today, in 2023, both biases are wrong - the ground rules have changed.  

It is possible to invent new syntaxes for programming languages in hours instead of years, using PEG-based technologies such as Ohm-JS.  It is possible to layer these new syntaxes over existing compilers, thus, obviating the need to deal with all of the nitty-gritty details of producing binary code.

Several drawing (visual) editors exist, e.g. draw.io, Excalidraw, etc.  They all boil diagrams down into textual representations.  The resulting text is not very human-readable, but, that doesn't matter.  Humans don't need to read the text, only machines - PEMs - need to read the text.  Humans can draw diagrams, machines can transpile the diagrams into text.  The fact that these diagrams boil down to text means that we can use existing textual language tools to further compile the diagrams into binary code.  Coupled with the trick of using existing compilers, this means that programmers can build diagram-based programs, then, compile the diagrams to binary code using only a small amount of effort (e.g. hours/days instead of years or never).

## See Also
2023-06-10-DaS - Diagrams as Syntax