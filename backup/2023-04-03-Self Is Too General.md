# 2023-04-03-Self Is Too General# SELF is too General

I struggled with "self". My conclusion is that "self" is over-generalized and encourages mutation (probably a similar conclusion to Odin's 'no builtin closures' edict). I think that I managed to remove the need for a generalized "self", but, since Python provides "self" I used it in py0d and explicitly removed the need for it in cl0d

In the Lisp community, there was a push to write CONS-less code. CONS is the only place that GC can happen, adding unknow-ability to the running-time of the code. Writing CONS-less code made the code running-time knowable and predictable.

Maybe there needs to be a push for writing SELF-less code? 

