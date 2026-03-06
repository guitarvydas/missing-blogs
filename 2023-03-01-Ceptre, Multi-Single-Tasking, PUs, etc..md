# 2023-03-01-Ceptre, Multi-Single-Tasking, PUs, etc.Multi-single-tasking:

Brainstorming, half-baked...

I would have ignored Ceptre in the past.  It claims to be a language for writing games.  The very idea makes me yawn. But, one of the guys at the Torlisp monthly meetup is deeply into robotics and Scheme and another guy, in the film industry, uses Racket for hobbying in game programming.  My own interest is in concurrency and simplicity and compiler-writing.  These fields are all related.  Watching the 2015 Strangeloop presentation about Ceptre piqued my interest.  Ceptre is logic programming, but with a twist - it has a built-in notion of explicit ordering.  I thought that I could knock off a better game language using my diagrams of state machines. I continued to learn about Ceptre.  Aside: Ohm-JS has buit-in explicit ordering and is "not" context-free.  I have to wonder if Ceptre is to generalized formalism as PEG (Ohm-JS) is to context-free grammar formalisms.

Dunno yet.

FYI, I watched the Ceptre talk.  I then read the paper and now am reading the thesis.  And in the background (foreground?) I am trying to convert Dungeon Crawler (.ceptre) into PROLOG.  I think that Ceptre can be simplified down to a small handful of primitives which are easy to express in PROLOG or Lisp or JS or ..., but they are not the first thing that you think of when programming PROLOG.  From there, of course, I would expect to generate code for Dungeon Crawler in Lisp and JS and Python and …

In the back of my mind is the question “Is This Steam Engine Time?” (Paul Morrison).  Are we seeing a shift away from single-threaded languages (Python, JS, Rust, Haskell, lambda calculus, etc.) to ???.  Certainly, hardware in 2022++ is drastically different from hardware in 1950 and we should be finding better ways to cope with this New Reality ("The Great Reset in Computing")…

FYI: The drastic difference in hardware is the reality that we now have cheap CPUs and cheap memory.  Both of these notions were completely unimaginable in 1950.  Instead of crushing our hardware with bloatware like Linux, we can simply throw rPIs at a problem, each running single-threaded programs.  There is no need to fake out multitasking anymore. Multicore is just a clumsy way to bridge across the two drastic realities, i.e. to force-fit 1 CPU programming languages onto many-CPU-programming.  In fact, we shouldn't even call CPUs CPUs anymore, since there's nothing Central about them.  Early adopters of 1950s computing built games.  Maybe early adopters of 2022++ computing will build new kinds of games with 1,000s of PUs, for example 1 processor for each player and for each NPC.

Ceptre:  [https://www.youtube.com/watch?v=bFeJZRdhKc https://futureofcoding.slack.com/archives/C5U3SEW6A/p1674614304225439

Call/Return https://futureofcoding.slack.com/archives/C5T9GPWFL/p1675094970899729?thread_ts=1674396396.762359&cid=C5T9GPWFL

I have not investigated this, but it, too, appears to be barking up the same tree: https://www.youtube.com/watch?v=5YjsSDDWFDY&list=PLcGKfGEEONaDO2dvGEdodnqG5cSnZ96W1&index=28

FBP (Flow Based Programming) https://jpaulm.github.io/fbp/