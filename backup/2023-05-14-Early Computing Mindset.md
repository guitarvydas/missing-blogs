# 2023-05-14-Early Computing Mindset"...programming languages and systems still suffer from early computing technology..."

Programming languages and systems suffer from early computing mindset.

CPUs and Memory used to be VERY expensive.  It was unimaginable to use a computer to run just one app.  Computing time was meted out in $s and accounted for.  The same CPU was shared across business departments and across university courses.  Budgets for computing time were allocated.  As a student, I was told how many $'s of CPU time I could use for doing my assignments.

Backtracking, e.g. Early's algorithm for parsing, was denounced as impractical.

Computing within these restrictions required mutation and memory conservation, i.e. Garbage Collectors and reuse of variables.

All programming languages were based on the idea that only a single thread was available.  A global, shared state (the callstack) made sense.

Some people thought that having 640K of memory was extravagance.

Today, though, the ground rules have changed.  We can have bowls full of CPUs, and, memory is ridiculously cheap.  Everyone carries around more computing power in their pockets than was needed to land humans on the moon.

But, we continue to think in terms of ground rules that accomodate the 1950s mindset, instead of today's mindset.  Supposedly-new programming languages are but variations on themes from the 1950s.

Operating systems and thread libraries are artefacts of 1950s thinking.  They are based on the meme that "everything must run on a single CPU".  Developers need preemption while debugging code.  End-users don't need preemption, but, are forced to pay for it anyway.  In fact, McCarthy showed how to write preemptionless threads in 1956 - anonymous functions (later rigidified into closures).  But, this idea was ignored due to extreme allergies to Lisp and its supposed "interpretation".  Instead, people built big, honking closures in assembler and C, using the sledge-hammer of preemption to control ad-hoc blocking caused by function calling.  Preemption encourages developers to ship buggy code, a practice that is not tolerated (by Law) in any other kinds of industries.  Shipping buggy code has been further embellished with epicycles such as CI/CD.

Today, hardware efficiency matters a whole lot less than it did in the 1950s, except to people indoctrinated to believe that there is only one kind of efficiency.  There's hardware efficiency, Design time efficiency, Production Engineering efficiency, Implementation time efficiency, etc., etc.

Attempts at automatic parallelization will never succeed because: 
1. a specific solution will always be more "efficient" than a generalized solution (N.B. "efficiency" comes in more than one flavour) and
2. efforts at automated parallelization are based on towers of epicycles which are based on 1950s memes.

Preemptionless threading cuts out a lot of bloatware and hardware-supported inefficiency (it costs time to preempt a running process).  More recently, Tunney built Sector Lisp in a very pure functional style resulting in a full language in less than 512 bytes[sic], then built an even smaller language (BLC - Binary Lambda Calculus). Reducing the number of types helps a lot, too. Lambda calculus means that "everything is a function that takes exactly one input and produces exactly one output", regardless of how you wish to spin the inner structuring of input data and output data using destructuring.