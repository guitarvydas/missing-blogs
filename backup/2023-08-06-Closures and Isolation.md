# 2023-08-06-Closures and Isolation
Closures help you encapsulate data.

Closures do not *prevent* you from isolating control flow, they just don't *help* you do that.

It's like in the days of GOTO-only assembler where you could write structured code if you wanted to but you had to be careful and very disciplined.

UNIX processes give you the benefits of control flow isolation.  I've given this concept the fancy name of "0D". Rob Pike calls this "concurrency".  [Concurrency is not Parallelism - It's Better]

Docker is just a more confined version of UNIX processes.  You shouldn't have to care, but if you do care about Docker innards, see "Containers Aren't Magic" by Julia Evans.

But, UNIX processes also give you a heavy weight solution to the 0D problem.  This will psychologically prevent you from using this idea in the small. That's what I'm interested in - being allowed to treat lines of code like UNIX processes. I think that the Actor model was originally envisioned this way...

There's no magic here - just a fancy, mostly meaningless name "0D".  The self-discipline you need is to, both, encapsulate data AND encapsulate control flow.  Don't leak data, don't leak control flow.  ATM, I think that a Class with exactly 2 methods will do the trick.
1. do something, here's a command code, and, here's some more data if you want it
2. return to me a list of results.

The Class can have many more *internal* methods, but only 2 methods are exported.

If you're really, really into State Machines, like me, then you will break (1) down into two pieces - 

- 1a start doing something, but don't take too long
- 1b continue doing what you were doing, but don't take too long, and, tell me if I should ask you to continue again.

If you go down this rathole, you'll end up realizing that you want to pile up results in a FIFO queue.  Everyone knows how to create a Queue Class in code.  No magic.  

Even a List which is reversed at the last moment will do.

And, you'll realize that "isolating control flow" means that you must not cross-call methods in other Objects (Classes).  Stuff your results into an output queue, and, let your parent handle the work of moving the appropriate results to their appropriate destination(s). 

ATM, there is only 1 - and only one - parent - the Operating System.  I think that it is possible to delete that heavy-weight concept and make little operating-systemlets.  I call these Containers (which clashes with Docker's notion of Containers.  Sigh).

Can you do this with closures? Yep.  Can you do this with Classes? Yep. Can you do this with Assembler? Yep. The only difference is convenience. I would argue that drawware is wildly more convenient than textual programming languages.

Can you do this with Docker?  Yep.  Size and bloatware are the only issues.  Docker and Linux processes implement *isolation* in the extreme, using hardware assist and traps to the O/S and MMUs and super-security isolation over top of UNIX processes, and, ...

UNIX processes, and Docker, treat all apps as if they were hostile and as if they were security risks - which leads to more code.  I'm interested in treating the *internals* of a *single* app - i.e. you can strip all of that bloat away, but I won't prevent bugs in your app from self-corrupting your app (bugs are bugs, surprise!:-)

Can you do this some other way, e.g. with Functions?  Probably, but don't ask me, I'm bigoted.
