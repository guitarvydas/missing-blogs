# 2023-04-03-Flexibility# Flexibility
## Unhandled messages 
In the final version, unhandled messages simply get dropped on the floor.  This aids flexibility.  You can use Components that have outputs that you don't care about.  For now, though, while bootstrapping, I don't expect to ignore any messages and produce an error message.

## Test cases
I made drawings of the low-level test cases and pushed them to the repo on the main branch https://github.com/guitarvydas/py0d/blob/main/doc/tests.md . Most of the tests are "obvious" (at least to me :-), but, I did write up the feedback test in greater detail. (Feedback ain't recursion).

## Flexibility

The underlying principle is "flexibility".   The ultimate goal is to take an existing design, unplug a component and plug in a new one, without affecting the design.  In general, this needs indirection to work, and, it needs 2 APIs on each component (input API, output API).  Or, to restate the goal, to take an existing design and shuffle its Components and Connections to get a new design, without rewriting any of the Components themselves.  This is what FP calls "referential transparency", but, to do this in FP, you have to submit yourself to a regimen of self-flagellation.  This can be done more simply by using well-defined Containers and Leaves.  In general, optimization removes flexibility.  Most programming languages emphasize optimization under the guise of "efficiency" at the expense of flexibility. Very 1950s. I emphasize flexibility at the expense of "efficiency". I am confident that someone will find a way to make this stuff "more efficient" - I've seen it happen time and again.
