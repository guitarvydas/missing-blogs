# 2023-04-25-Apples And Oranges and Concurrency# Apples and Oranges and Concurrency

Concurrency is not a *thing*. 

All 8 billion humans on this planet understand that.

Except programmers.

## Overwrought Example.

Someone stands in the middle of the floor. 

In their right hand, they've got an apple, and, in their left hand, they've got an orange. 

Most people would say - okay, I get that.

But, not programmers. 

Programmers say, that's not a human. That's some kind of god. That god has a third hand growing out of the top of their head. 

They've got an apple and an orange, and in their middle hand they've got a salt shaker.

They've taken a Sharpie marker and crossed out the word "Salt" and written in the word "Threads".

When the god shakes the thread shaker, instead of salt, out come woo-woo particles of an element called *concurrency*. 

This element does not appear on any periodic table.

If we take away the thread shaker, the apple and the orange are no longer distinct. They become an appange that can be held only in one hand. Say the left hand.

When we sprinkle *concurrency* onto the appang, the appang becomes two distinct things - an apple and an orange Without the sprinkles, it's one thing.

## So what's the point? Conclusion. 

Objects in real life are concurrent and asynchronous.

Sometimes, you need to synchronize objects.  

When you need synchrony, you really need it.  But, not always.

Over-use of synchronization leads to epicycles, accidental complexity and bloatware.

CPUs are meant to run single threads, not multiple threads.

CALL / RETURN is not meant to support mathematical functions. Mathematical functions are meant to be instantaneous.  This is something that CPUs can never do. 

The implementation of thread libraries on top of single-threaded CPUs is simply an academic showpiece that involves towers of epicycles, make-work, self-flaggelation and accidental complexity.

The existence of thread libraries does not lead to a useful mind-set.  The fact that something *can* be done is quite different from the notion of whether it *should* be done.

All that we need to do is to run single programs on single CPUs, and then, join them together by pairs of one-way wires[^onewire]. 

The notation we're using to talk about applications was based in the 1950s when everything looked like it needed to be run on a single CPU.

CPUs were so expensive that we had to timeshare them. 

Today, though, we have multiple CPUs. 

Say, in one hand we have a Raspberry Pi. In the other hand, we have an Arduino.

We run a Tetris program on the Raspberry Pi. On the Arduino we run a mail client.

The questions to ask are, 
- Are these two applications thread safe? 
- Can they share memory?

The answer to the first question is "of course they are thread safe".  The applications are on separate, decoupled CPUs.

The answer to the second question is "no". The apps are on separate CPUs.  The applications cannot share memory.

If the apps were on the same cpu, then the answer would be, well, there's a bunch of gotchas in trying to fake out this woo-woo particle called *concurrency*.

[^onewire]:  Note that using a single, bidirectional wire is but an optimization of the more basic concept of two directional wires.

## See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity
- https://github.com/guitarvydas
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
WIP - leanpub'ed
https://leanpub.com/u/paul-tarvydas
### Video/Audio of this Essay
https://www.youtube.com/watch?v=T72dy4TQ9WA

---



