# 2023-05-29-Slices in OdinA slice is a pair.  A slice is a meta-object.

In C, we have the meta-object called a "pointer".  It is the index, in memory, of the beginning of a datum.  A "pointer", being an address, fits into most registers and can be stored (allocated) in a number of places - as a parameter (on the stack or in a register), as a local (on the stack), on the heap.

In Odin, a similar meta-object is called a "slice".  It is a pair.  Its minimum size is 2 pointers.  It, too, can be allocated in a number of places (a pair of registers, on the parameter stack, on the local stack, in the heap).

A slice consists of
1. a pointer
2. a length.

In the "worst case" the length can contain as many bits as any pointer, e.g. pointer=0, length=all of RAM.

Part of my confusion was the statement that slices are allocated on the heap.  I was thinking of the actual data that the slice points to, instead of the slice meta-object itself.  And this was clouding my perception.

I guess that a "string" is just a slice that points to a block of characters.  A lot more things than just strings can be represented this way.
