# 2023-04-25-Scratch Broadcast BlocksAre Scratch Broadcast blocks the same as 0D?

https://en.scratch-wiki.info/wiki/Broadcast_()_(block)

Yes and No.

Technically, they are similar.

Psychologically, the are not in the same ballpark.

I argue that 0D (aka decoupling / aka necessary-condition-for-concurrency) needs to be driven deep into the notation and not added on as bag on the side.

There is a subtle difference between AX and DX (and UX) (Academic eXercise, Developer eXperience, User eXperience, resp.).  Just having a capability doesn't necessarily mean that it will foment fresh ideas on solving problems.

For example, if only AX mattered, then everyone would be using Assembler instead of higher-level languages.  Or, everyone would use Lisp instead of ???.

If all you've got is a hammer, then everything looks like a nail.  If all you've got is Functions, then everything looks like an instantaneous function (timing looks to be irrelevant). [aside: one of the issues with making everything a Function is the "particle/wave duality" of IF-THEN-ELSE.  In a Function, IF represents the conditional value of data.  In code, though, IF gets used way beyond its Functional meaning, leading to ad-hoc gotchas and pronouncements about State being bad,]

This statement in the above Scratch page...

> Recursion is a process where a script calls into itself. Broadcast scripts can perform a limited kind of recursion, called tail recursion, by broadcasting their own message at the end of the script, restarting the script and forming a loop.

...means that Scratch got it wrong.  Recursion and message-sending are not the same thing.  Recursion is LIFO, whereas message-sending is FIFO. The above statement says that Scratch has tried to force a LIFO behaviour onto FIFO message-sending (that looks like the hammer-and-nail thing, again :-).