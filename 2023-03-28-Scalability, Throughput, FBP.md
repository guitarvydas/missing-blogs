# 2023-03-28-Scalability, Throughput, FBPThere is definitely a link between FBP and parallelism and multithreading.  

FBP "classic" uses processes "under the hood" to implement decoupled components.

FBP "classic" prescribes a certain way to structure such processes - by passing data on conveyor belts between components.

*Scaling* vs. *throughput* vs. *latency* are conflicting requirements.  You - the designer - must decide which is more important and design for it.  

No tool gives you everything at once.  

For example, most existing programing languages (e.g. Rust, Python, etc.) emphasize low-level efficiency at the expense of making everything synchronous (the "von Neumann bottleneck").

If you want *scalability*, eschew optimization, eschew DAGs, and so on.  It is harder to scale units of code that are tightly coupled.  Optimization (low-level) usually works by making code tightly-coupled.

If you want sheer throughput speed, you can use a hot General Purpose Programming Language (there ain't nothing hotter than Assembler, but, you have to enjoy blowing your own feet off).   But, GPLs only improve throughput on single islands of software (nodes).

Throughput is, also, helped by not-waiting for things to happen.  Let components run at their own speed.  Optimize the speed of components that are on the critical path, but, only after you measure where the hot spots are.  FBP, and UNIX, and StateCharts, and ..., are good starting points.

If you want *low latency*, keep things physically close together and join them together with perfect channels that never go down and never fail to deliver data.  Current GPLs (General Purpose Programming Languages, like Rust, Python, etc.) rely on the "perfect transmission" model.  There is an underlying assumption that function calls and returns "just work".  It is utterly unimaginable to consider the idea of low-level CALL/RET failing.  On the internet, though, this kind of thing is not a "bug", but is a part of the requirement that needs to be designed-for (e.g. using "network protocols").

IMO, *scalability* is the most interesting feature.  I argue that you need *scalability* for things like robotics, internet, gaming, blockchain, etc.  I would start by Designing a system with pluggable, decoupled pieces.  Then, I would hire a young Production Engineer(s) to buff the pieces and make them "more efficient" (aka throughput).  Maybe I'd hire a graybeard Production Engineer to look into lowering the latency of my design.  If I'd have designed this kind of system enough times myself (e.g. 3x, per Brooks), maybe I could do it all myself.  If I hadn't tried the design and hadn't gone back to the drawing board at least 3x, I'd be engaging in something called "The Waterfall Method of Design", i.e. supreme confidence in one's own understanding of the problem space, tempered only by Reality (wherein Designs are usually left unrepaired, sigh).
 
[aside: I am interested in the nuts-and-bolts.  I am concluding that there is something deeper than parallelism and multithreading.  Decoupling is the "secret" to schedulability.  I currently call this "0D" (zero dependency).  I currently have examplars of 0D written in Python and Common Lisp.  It should be easy to write 0D in JavaScript, WASM, etc. but the idea of doing so makes me yawn and, thus, I avoid it.]

[aside: Yes, yes, people have figured out how to fake out multithreading using low-level, function-based GPLs.  They call this fakery "threading libraries" and tend not to notice the bag of epicycles that this approach drags along with it (e.g. "thread safety", "semaphores", "priority inversion", etc, etc).  Today, we have cheap CPUs and cheap memory.  This wasn't the case in the 1950s when this kind of fakery was invented.  FBP deals with the idea of multiple, cheap CPUs (optimizing something that hasn't been mentioned above: cost, $).  Existing versions of FBP use existing threading libraries but elide them, making it more likely that designs will port easily to cheaper hardware.]