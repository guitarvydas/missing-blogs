# 2023-07-04-Mainframes to PCsWhat was the Big Change in the shift from using Mainframes to PCs?

On the surface, it looks like the big change was that hardware became faster.

BUT, the big change was/is a memetic shift from time-sharing to distributed computing
	- DPUs instead of CPUs
		- Distributed Processing Units instead of Central Processing Units
	- function-based notations, e.g. SICP, FORTRAN, do not cope well with the DPU meme
		- it's not impossible to use function-based notations to cope with the DPU meme, but it is harder than necessary
		- evidence: invention of epicycles like thread libraries, operating systems (esp. preemption, and hard-wired, pervasive  synchronization)
		- evidence: purer-than-pure functional programming is espoused in Sector Lisp
			- Sector Lisp is less than 512 bytes long (the whole language, including a 40-byte garbage collector)
			- yet, the nearest contender is orders of magnitude larger, i.e. bloatware
				- I think that the nearest contender is Lua, which is only 24 times larger than Sector Lisp
				- most other languages are 100s of times larger
		- evidence: computers have RAM (state) and time-based sequencing (aka opcodes), yet, functional notations deny the existence of *state* and *time*
		- evidence: the CPU callstack is a hard-wired, shared, global variable, i.e. the callstack is not very well suited to implementing functions (this requires epicycles and bloatware as work-arounds)
		- evidence: electronics - e.g. CPUs - have *propagation delays*, yet, functional notation simply ignores that fact[^model]
		- evidence: invention of a woo-woo particle called *concurrency* ; sprinkle *concurrency* onto a program and it, magically, becomes asynchronous[^async], whereas previously it was not asynchronous
		- evidence: function-based programming has been touted as The Silver Bullet since about 1954 (FORTRAN) ; 2023-1954 = 69 years of promises, which have yet to deliver more reliable user experiences (Phishing attacks have increased, GUI usability has become worse, apps deal with ever-narrower domains, etc.)

[^model]: You *can* model state and time using function-based notation, but, that's not as good as having a notation built specifically for those concepts.  The fact that you *can* do something does not imply the you *should* do that thing.

[^async]: Even though the underlying substrate for the program was, originally, asynchronous.  This pre-existing asynchronicity was squeezed out of the program through the over-use of synchronicity.

## Conclusions
1. Don't insert doo-dads into languages if they push the underlying paradigm out of its sweet spot
	- e.g. we wantonly inserted *mutation* and *random access* (heaps) into functional programming
		- which resulted in bloatware
		- which resulted in the *need* for complications such as type-checking
2. It's OK to use more than one notation.
3. early *game software* got it more right: sell a cheap base of hardware, insert cartridges that take over the whole machine
4. if the shoe doesn't fit, don't wear it
	- don't use functions to solve *every* kind of problem
	- functional notation - what is often conflated with the notion of *mathematics* - is suitable for expressing the use of computers as *calculators* - ONLY.  Computers can be more kinds of things, not just *calculators*.  E.g. sequencers (iMovie, Garage Band, IoT, robotics, blockchain, etc.)
5. Formalization[^formal] is OK, but does not imply that only functional notation can be used to express the results of formalization.
6. Functional notations have become The Silver Bullet and a Religion for programming, blinding us to other ways of thinking about programming problems[^religion].

[^formal]: "Formalization" is deep thought that is expressed in some sort of intermediate form (e.g. *mathematics*).  If this intermediate form is not converted into a human-understandable explanation, then, only 1/2 of the job is done.  For example, Physicists try to explain how things work by (1) thinking about and experimenting with some aspect of Reality, then, (2) explaining what is going on.  Not all Physicists rely on mathematics for their intermediate form, e.g. Feynman diagrams.  Notations other than *mathematics* can be used for formalization.  Physicists communicate with other Physicists using their intermediate notations, but "normal people" are excluded from this form of communication.

[^religion]: Religious belief in the use of *mathematics notation* causes True Believers to discard observations about Reality that happen to be inconvenient for the notation (instead of the other way around - problem first, then notation(s)).  For example, compression of the 4D phenomenon of electricity down to a 2D notation called Maxwell's Equations, causes True Believers to overlook bits of pertinent Reality, indirectly causing phenomena like "Free Energy conspiracy theories".  Physicists use a technique called *simplifying assumption*s to elide complex details while deep-diving into a single aspect of some phenomenon.  It appears that True Believers tend to forget that a notation is but a *simplifying assumption* and begin to believe that such a simplified notation is Truth.  I would imagine that McCarthy knew that Lisp 1.5 was but a convenient - single - way to use computers, but, this notion has been lost on subsequent generations of True Believers. 

## Appendix - Further
I haven't succeeded in reducing my thoughts into a single-line, convincing elevator argument, yet.  If one is so inclined, one can view my intermediate thoughts and progress in this digital garden: https://kinopio.club/invite?spaceId=5Op_YdR16ma3TX9DLxx4V&collaboratorKey=uWSd2c2s7rKYJUVd_16On&name=sicp-considered-harmful

## Appendix - Apples and Oranges and Concurrency
essay: https://publish.obsidian.md/programmingsimplicity/2023-04-25-Apples+And+Oranges+and+Concurrency
video reading of the same essay: https://www.youtube.com/watch?v=T72dy4TQ9WA

## Appendix - The ALGOL Bottleneck
https://www.youtube.com/watch?v=2OEyAjCqgGM

## Appendix - Sector Lisp
https://justine.lol/sectorlisp2/
