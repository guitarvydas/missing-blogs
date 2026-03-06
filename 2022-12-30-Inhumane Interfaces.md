# 2022-12-30-Inhumane Interfaces# Inhumane Interfaces

Today's UI is built for ease-of-programming, with the result being a clunky UX.

What can be done to make UXs less clunky?

# Example

For example, I use Obsidian for editing markdown files.  As I move the cursor down the screen, lines auto-magically expand and contract depending on technical details within the lines directly underneath the cursor.

The result is that the the position of the cursor jumps from where I - the user - placed the cursor to a position where the underlying code wants to automatically place the cursor.  

The UI effect is jarring and unfriendly.

Worse yet, some tools re-draw the whole screen placing the cursor in a completely different physical position on the screen than where it was just a moment ago.  Example: I am focused on editing the text in the bottom 1/3 of the screen.  I perfform a simple operation and the screen redraws.  The cursor is automaticlly moved to the top portion of the screen, yet, my eyes are still looking at the place where the cursor used to be.  I need to pause - breaking my flow - to re-group and re-understand what I'm seeing on the screen.

# Ad-Hoc UIs

In the late 1900s, UIs did not have this behaviour.  The user was in control - at all times - of what was displayed on the screen.  For example, if the cursor was 5 lines from the top of the window, hitting the down-arrow moved the cursor down exactly one line down, to the 6th line, without re-adjusting the rest of contents of the window.  If the 6th line was some sort of composite, multiple line, the contents of the line did not automatically change.  The 6th line still looked the same, and, the cursor ended up on the 6th - single - line.

Yet, in the late 1900s, UIs were painstakingly hand-coded using ad-hoc logic.

# The Chasm

There is a gap - a chasm - between what is technically necessary and what should be shown to the user.

In analogy, this problem is like *core dumps* in the early days of computing.  Too much information is not always useful.  A *core dump* contains *all* of the information, but, that much information does not help debug specific problems.

Likewise, *catch/throws* are used in applications in lieue of more-useful 1-line error messages.  When I'm debugging my app, I don't want to know what assertions have been violated inside the IDE/compiler.  I'm not looking at the source code for the IDE and that information does not help me figure out what's wrong with *my* app.
 
# What Can Be Done?  Brainstorming

Maybe what is needed is a way to map from the ease-of-programming domain to the UI domain, i.e. 
1. recalculate the whole screen using FP, 
2. then make the UI suck less from a user's point of view.  E.G. create a mapping that doesn't move the contents of the screen (like the physical position of the cursor, or auto-expansion of details) unless instructed by the human user.

IIRC, the UNIX 'curses' library does something like this.  It caches the screen bitmap then uses newly-generated technical details to create the next screen bitmap, modifying as little as possible.  

Curses was invented to solve efficiency problems, but, maybe a similar strategy can be used to solve UX problems.
