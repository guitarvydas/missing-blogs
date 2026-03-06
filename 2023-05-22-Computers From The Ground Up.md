# 2023-05-22-Computers From The Ground Up
script for https://youtu.be/QpHFidNG8z4

At a very basic level, a computer consists of a CPU and some disc. The CPU consists of some random transistor logic that  accesses really fast memory that we call registers, and it accesses fast memory called that we call RAM.  Using wires it connects to slower but cheaper memory called disk.

![CPU overview 2.png]

Registers are just a chunk of really, really fast memory, but very expensive in terms of the amount of size used up on a chip  and the number of transistors used up to make the thing.  It requires a bunch of  tricks and techniques to  make it really fast. And the distance from the random logic. Because electrons take time to travel along wires, the shorter the distance, that they can travel, the faster the access will be.

RAM means random access, memory. Random access means that you can  select any location in the memory  in any order, and then you can access that location and do something with it. You can read it, you can write it.  Writing it  is what we call mutation.  RAM usually consists of fast memory, which is  close to the cpu, but a little cheaper to make, and so we can make more of it.

And we have lots, lots more of it.

Disk memory uses an even cheaper technology, and therefore we can use way more of it. On the other hand, to get at it, we have to use  wires and technologies  that make the access much, much slower. Like orders of magnitudes slower than accessing Ram and RAM is  orders of magnitude slower than accessing registers.

They're all just really forms of memory. There are different techniques for developing memory and they have different costs.