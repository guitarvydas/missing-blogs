# 2022-06-12-End User Programming
IMO, what end users want is:
- the ability to create ad-hoc designs and code using COPY and PASTE
- error checking that helps them never get into trouble
	- at least, a signal that tells them to hand over the code to a professional programmer

# Ad-Hoc
Ideas start out as ad-hoc designs.

Expunging ad-hoc code also expunges fresh ideas, as a side-effect.

Ad-hoc designs are *tightened up*, after the design process has mostly subsided and once there is a clear direction for a useful design (GUI, UX, etc.).

For example, Racket might not have *macros* if macros hadn't been invented in an *ad-hoc* manner in early dynamic Lisps[^1].

[^1]: Early Lisps included the concept of FEXPRs.  FEXPRs were later expunged to make the language(s) more compilable (production-hardened).

The field of accounting would be stunted if it were not for the invention of spreadsheets.  Early spreadsheets (if not current ones), allow ad-hoc code.  Spreadsheets provide a grid-based GUI and allow users to insert high-school math expressions into cells, including calls to heavier functions which are implemented under-the-hood.  Later versions of spreadsheets introduced newer organizing concepts like pivot tables.

- [ ] Most Dentists offices would not have ... early DBs FileMaker (what was Apple product?).  Ad-hoc uses of spreadsheets as DBs.
- [ ] cut/paste, hack on existing code to change it, 
	- [ ] hashtag program creation
	- [ ] Microsoft Access
	- [ ] HyperCard
	- [ ] ClarisWorks
	- [ ] DataView Obsidian

# Bring in the Pros

## What Causes Trouble?
## RY
More than one copy of similar program scripts leads to trouble.

Updating/fixing the COPY/PASTED code becomes a nightmare of ad-hoc changes in multiple places.

## Build and Forget
Lack of *build and forget* leads to trouble.  

Making a change to code "over here" causes something to work differently "over there".  This is so common in programming, that it has been given a name - dependency.


## Professional Programmer Training
Professional programmers are trained in DRY - Don't Repeat Yourself.  They look for processing similarities and parameterize the code, to centralize functionality.

Centralizing functionality is also called *locality of reference*.  You want to look in one place to see / learn everything there is to know about a specific aspect of the code.

Since the mid-1900s, programmers have been writing programs using only textual representations.

Most of the techniques that have been developed, involve *locality of reference* applied to textual representations of programs, e.g. *lambda*s, *structured programming*

## How?
- Create a metric?
- System notices similar code blocks (NiCad?)

A useful metric would be one that could be automated.  We tried LOC (lines of code) and Function Points, but, found that they can be cheated.

- [ ] comments don't work
- [ ] organizing all code by its data ignores control flow (e.g. OOP failure)
- [ ] ln, ln -s
- [ ] 