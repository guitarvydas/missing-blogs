# 2022-11-26-Why Do We Use Text For Programming Languages?
The only reason that we use text and not diagrams for programs is that in the 1950s, computer hardware could handle text, but couldn’t handle vector graphics.  We developed more modern technologies for non-programmers, but, programmers themselves are still stuck in the 1950s.

Worse yet, 1950s computers could only handle text that was arranged on grids of non-overlapping, fixed-size bitmaps.

Well, the other reason for using textual programming languages is that we are used to using writing technologies based on clay tablets.  After 2,000 years, we've progressed to using graphite and rubber on paper.  We didn't imagine that computers were something other than "better clay tablets".  Our continued use of 2D writing technologies has severely limited the way that we think about things.  We write equations in 2D to express simple physical concepts, like sound, that are 4D phenomena (x/y/z/t).  Mathematics seems complicated to many people, because it is not natural and is a round-about way of describing multi-dimensional phenomena that we experience daily.  Complexity comes from the fact that we try to describe 4D effects by collapsing them down to 2D.  For example, Mechanical Engineers are taught to draw multiple 2D views of simple 4D objects (top, front, side, simply ignoring time).

Computers allow us - for the first time? - to express and explore at least 4 dimensions of our reality.  We can shift the camera perspective on a 3D model and "walk around it" - and - we can watch models evolve over time.  We couldn't do this easily with paper and other clay-tablet technologies and mathematics.  They key word here is "easily".  Mathematicians and Physicists are able to build 2D "models" of real phenomena, but only a select few can understand what's going on (usually after several years of University training).  It seems that our notions about programming are based on the idea that "if it's good enough for mathematicians, it must be good for programming, too".
 
Further: Note that it is just plain hard to draw a sensible diagram using a synchronous (function-based) language.  It becomes laughingly simple to draw diagrams if you use 0D components.  

Rhetorical question: why can we draw diagrams of computer networks?  Because each node on the network is - essentially - a 0D component.  

Why don’t we do everything this way?  

Uh, because of our built-in fear-bias regarding “efficiency”.  We are preconditioned to worry about saving bytes instead of saving development time.  Without handcuffing ourselves with clay-tablet 2D technologies, we *could* trickle-down better apps to end-users, but, we don't.
  
Further further: computers in 2022++ are *fundamentally different* from computers in the 1950s.  In the 1950s, each computer had only 1 CPU and limited memory.  In 2022++ we want to build distributed systems such as blockchain, IoT, robotics, internet, etc.  Ideas from 1950s don’t map very well to 2022++.  But, we continue to force ourselves to use ideas from the 1950s.   From a product-design perspective, modern CPUs are little more than fancy FPGAs.  Modern CPUs don't deserve all of the adulation we heap upon them in the form of creating Sciences for building 1950s UIs (aka "programmming languages") and 1960s IDEs (aka "operating systems").  Our end-users suffer from our tools' deficiencies - we insist on having end-users pay premium prices for bloated operating systems and we insist on having end-users accept the fact that whatever they buy will be buggy without recourse in Law[^engineeringlaw].

[^engineeringlaw]: Real Engineers are forced to take courses in Tort Law and are reminded of their obligation to produce bug-free products lest they be sued.  For example, in Canada, Engineers are given "iron rings", on graduation, to remind them of a buggy bridge design that turned out to be fatal.

Sigh.