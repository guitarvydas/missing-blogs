# 2022-11-18-Simplicity

> It's interesting how going from LIFO to FIFO can simplify programming. 

Yes, it is *so* simple that I resisted the concept.  I was sure that it had to be more complicated than that.

I've been thinking about this for years, and, to see the concepts reduce to a simple change from LIFOs to FIFOs was almost discouraging.

The reality is that I love `/bin/*sh`, and I love `concurrency` and I am very interested in `FBP`.  All of these technologies have one thing in common - they use FIFOs for inter-component communication.

Functions, though, are based on the use of LIFOs (stacks).  Pure FP is stack-based - call a function, push a return-bookmark on the stack. (Aside: that's mutation, btw.  And, if your hands aren't sufficiently tied behind your back, realize that the *call-stack* is a *global variable* baked into hardware)

It is *possible* to write code for communicating components using functions, e.g. the invention of "operating systems", but this make the result less-simple and more-complicated than necessary.

For me, reading Harel's original paper on StateCharts[^harel] was a life-changing event.  The paper shows that it is possible to write serious code as technical diagrams, and, it is possible to think about code using something other than *inheritance* as we have come to know it.  Harel doesn't point out either of these issues, I had to let them ooze into my psyche over time.

[^harel]: https://www.wisdom.weizmann.ac.il/~harel/papers/Statecharts.pdf

