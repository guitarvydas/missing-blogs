# 2022-06-16-Like That Editor# Like That Editing
Programmers are taught to aovid duplicating code.

The name for this concept is *DRY* - Don't Repeat Yourself.

Programmers use ad-hoc manual techniques to achieve DRY.

I suggest that programmers' machines can help them automate the process of creating code in a DRY manner.

# Applicable Technologies, See Also
Technologies like *git* and *diff* can be applied.

[Paul Bassett's Framing Software Reuse](https://www.amazon.ca/Framing-Software-Reuse-Lessons-World/dp/013327859X) discusses the issues of *reuse* vs. *multiple use*.  

Bassett suggests a text-based script editing system to achieve multiple use.

[NiCad](https://www.cs.usask.ca/~croy/papers/2011/CR-NiCad-Tool-ICPC11.pdf) discusses technology for detecting cloned software text-based code.

SVG and various editors, like [draw.io](https://app.diagrams.net) support the idea of floating, overlapping blocks of text, and, they support transparency.

Most text editors support CUT/COPY/PASTE using mouse and keyboard shortcuts.

# Like That Editors
I suggest that new operations be added to editors in addition to CUT/COPY/PASTE. 

Something like, SELECT/HASHTAG-PASTE.

That would essentially make it possible to say "like that block of highlighted text, except ...".

After selecting a block of text, the programmer would move the cursor, then, HASHTAG-PASTE the selected text.

The editor would show the text as if it were PASTEd in, but would mark the new text in some way (e.g. alpha 50%, dashed border) to show that the text refers to an original somewhere else.  Edits would proceed as normal, but, changes would be highlighted to indicate difference from the original.

In essence, this is a form of edit-time prototypal inheritance.  Since OO class-based inheritance is but a subset of prototypal inheritance, this same editor could be used to create OO classes without a runtime penalty.

Presently, programmers already perform the above operations manually in an ad-hoc manner by lassoing common code into parameterized functions.  This results in a runtime cost which causes extra work for compilers to unwind ("inline" functions and runtime method lookup and calling).

## Text Editor

At first, programmers can indicate which blocks are overridable.  In time, methods to automate overriding will be developed, and, will require no extra information from programmers.

!![../pm/like that editor-text.png](images/like that editor-text.png)
## Diagram Editor
!![../pm/like that editor-diagram.png](images/like that editor-diagram.png)