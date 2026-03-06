# 2022-07-11-Extending Flow-Based Programming# Attention to UX Instead of Mathematical Niceties
- need for abstraction
	- lasso a group of components with a total of N ports
	- replace group of components by a single component with fewer than N ports 
		- implies fan-out for implementation
		- implies single-entry & single-exit points, abstracting FIFOs (bounded queues) down to single input and single output

!![diagrammatic abstraction.png](images/diagrammatic abstraction_69.png)

# Secret Sauce of FBP
0D

No dependencies.

Often mis-named "parallelism".

Parallel software components imply 0D.

0D components do not imply parallelism.


# Programming Languages are IDEs for programming
- PLs (IDEs) invented in mid-1900s
	- to appease hardware capabilities of the day
- based on cells of bitmaps ("characters")
- cells may not overlap
- cells are fixed-sized
	- font sizing affects many cells at the same time
- windows are not fixed-size
- rectangles on a diagram are not fixed-size
	- it is convenient to use a diagram editor to change the size of a rectangle
	- it is not convenient to use a diagram editor to change the size of a piece of text (by dragging a corner, say)


# Fan-Out
- one output feeds many inputs
- requires copying, or, copy-on-write, or, ...
- copying
	- implies memory management (GC (Garbage Collection)
- copy-on-write
	- JavaScript assignment semantics, creating *own* variables