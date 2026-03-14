# 2023-08-03-Orthogonal Programming Languages - De-Evolution of VTables for Integers
# De-Evolution of VTables for Integers

This is a graphic essay on how *vtables* apply to all operands, including lowly *Integers*.

I argue that Programming Languages should contain two (2) languages each:
- a language for expressing implementation of Data
- a language for expressing Control Flow.

Where an example of Control Flow would be code that is meant for sequencing operations and might branches, like *if ... then ... else*.

Control Flow has no place in Data implementation.  Data implementation *does* use the concept of Conditional Evaluation.  The concept of Conditional Evaluation should not be tangled up with sequencing of scripts.  Tangling the two concepts together often results in ad-hoc use of *state* and often leads to mysterious bugs

Each of the two sub-languages contain differing sets of restrictions and syntax, depending on their purpose.

What we call "GPLs" (General Purpose Programming Languages) today - eg. Python, Rust, etc. - fall mostly into the camp of Data Implementation languages, but, have some Control Flow constructs tangled into them.

Data appears as *Operands* in Control Flow code.

Control Flow languages are *scripting languages* that cannot construct data.  These languages can only
- move Operands from place to place
- invoke methods on Operands
- create new Operands
- clone Operands
- destroy Operands (reclaim storage used by Operands).

Compile-time and run-time vtables.

From the optimization perspective, It is insufficient to describe *Classes* for Operands whose methods can be called only at run-time.

It should be possible to create compile-time classes and invoke methods on these classes at compile-time, instead of later.  The compile-time methods may result in creating code that calls run-time methods on run-time classes.

This essay is still a work-in-progress and will change as the ideas are developed further.

## Subtle Evolution of Static Type Checking


![DrawIO/integerfree.drawio.svg](integerfree.drawio.svg)