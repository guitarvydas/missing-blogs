# 2023-08-04-C Stack Allocation
"...  don't quite follow why C doesn't allocate things by value on the stack ..." 

It's, actually, quite obvious and a wonderful example of premature optimization and lack of belief in Future of Programming.  

When C was invented, the prevailing thought was that 640K RAM was an enormous luxury.  Structure sharing through the use of pointers (although, it wasn't called that) was considered de rigueur.  

Stack and heap use the very same memory (the flat address space), the only difference is how it gets reclaimed Pop SP, vs, free() - hardware supports the former, while explicit software is required for the latter.  

Functional Programming was laughed at as being too memory inefficient.  Ironically, pure FP makes GC easier, as seen in the 40-byte GCer in Sector Lisp.  

The addition of mutation to pure FP was fundamentally evil, but, wasn't recognized as such. 

Even McCarthy built a GCer that assumed the presence of mutation.  Justine Tunney has built a better GCer than McCarthy's original.  

Aside: I worked hard to avoid studying for exams and remember spending an afternoon in the CSC library reading papers on GC instead of studying.  A paper that stuck in my mind was one that suggested that GC was never necessary - just keep allocating memory without ever freeing it.  I cannot remember what the reference for that paper might be.  

Another paper that stood out contained the use of 1-byte pointers, i.e. indices into 256-byte pages, with the last few bytes reserved as connector references to the next pages.

As an example of how severe this premature-optimization meme was, Burroughs invented Huffman encoded opcodes.  The smallest two opcodes were 2 bits long (00 and 01, IIRC).  Hardware burned extra cycles in an effort to constrain memory use.  In this case, they optimized the size of program space.

I continue to argue that "language matters".  If you are forced to think about a problem in one way, you will come up with certain solutions and discard other possible avenues of thought.  In this case, the premature-optimization meme influenced the design of the C language which influenced subsequent software designs.  [Note that UNIX processes are nothing more than closures built in an ad-hoc manner.  Greenspun's 10th Rule deja vu all over again].

