# 2022-12-21-Clockwork-inessAt this moment, I believe that software development is severely one-sided.

The problem with software is the attempt to make everything into clockwork - including Design (bad idea).

Humanity has spent 1,000's of years developing methods to deal with and control independent units (like, other people, and like, more recently, LEGO block childrens' toys).  Clockworkiness is fairly young, though - only a few 100 years old.  Software as clockwork is even younger (70-ish years).  Software is "hard" because it violates normal human assumptions about how things work (i.e. independently, instead of clockwork-y).

Node-based software and diagrams are but a symptom of trying to break out of clockwork-iness and (back) into independence.

Clockwork-iness works for Production Engineering, but, clockwork-iness is anathema to Design.  Split the two apart and you get better productivity.

The "fad" that I see is the idea that clockwork-iness takes top priority.  That fad is leading us into epicycles (called, in politically-correct circles "work arounds"). An example I often use is the Mars Pathfinder disaster.  It was solved in the same way that we take Aspirin - fixed the symptom, but did not cure the cause. (Cause: building async on top of sync on top of async)

LEGO is not clockwork-y.  Software fools programmers into thinking that they are building with LEGO blocks.  Far from the truth.

Example: Your description of the way that Film Industry projects are managed is - at least to me - a process for managing independent pieces (assets, creators).  Software using clockwork languages (i.e. just about every programming language that is popular - Rust, C++, Python, Racket, etc., etc.) does not work like that and resists that kind of project structure.  But, software COULD be made to work like that and COULD be managed in the same way. [The "answer" is infuriatingly simple: using queues instead of CALL/RETURN for inter-component communcation].

Grafting diagrams and node-based ideas onto a clockwork substrate doesn't make it "independent" or "better".  It just makes it "more complicated" (anti-clockwork-iness built on top of clockwork-iness built on top of anti-clockwork-iness).

Missing technological piece: how to bolt Design assets together, then, Production Engineer them in a clockwork manner.  My current answer: 0D + Ohm + Lisp.  Lisp was on the right track, but then the clockwork-fadists derailed it and made it more clockwork-y.  Lisp got 1 thing right and 1 thing very wrong.  (a) During Design, there are only 2 entities: things and lists-of-things.  Things are Leaf nodes.  Lists are recursive - list can contain other lists and/or Leaves. (b) Lots of people hate Lisp "syntax" and, therefore, have ignored the bit that Lisp got right.

Another example of epicycle-icity: robotics.  Current languages (C++, Python, etc.) insist that the WHOLE robot work in a clockwork manner, instead of like a bunch of loosely-coupled rPIs.  In essence, the WHOLE robot is single-threaded (it only looks like it's multi-threaded ; back-filling using pub/sub is asking for unexpected gotchas and more Mars Pathfinder disasters).  The development of "behavior trees" is an attempt to graft async on top of sync.