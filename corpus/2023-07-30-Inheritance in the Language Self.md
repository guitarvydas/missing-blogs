# 2023-07-30-Inheritance in the Language SelfDave Ungar was a principle in devising the Self programming language.

Self explored
- prototype-based inheritance (now called *prototypal inheritance*)
- JIT (Just In Time compilation)

From my perspective, prototype-based inheritance is the dynamic version of class-based inheritance.

I believe that prototype-based inheritance is more powerful than class-based inheritance.  Class-based inheritance needs to discard certain features of prototype-based inheritance to make it possible to statically check the code at compile-time.

Dave Ungar mentions learning from Randy Smith, in a lecture in this video around 14:30 https://www.youtube.com/watch?v=3ka4KY7TMTU . What he saw led to Self.

For the record: I conclude that *dynamic* programming languages make it easier to *design* programs than using *static* programming languages.  In my view, making a language static snips off certain avenues of thought for the sake of optimization.  Ideally, one should *design* a program using dynamic languages, and, optimize later only when measurements *prove* that a program is "too slow".  Static languages make it possible to predict - at compile time - whether a program is inconsistent.  This is a feature that dynamic languages do not have, but, I think that the cost of this kind of pre-checking is too high.

https://en.wikipedia.org/wiki/Self_(programming_language)

https://en.wikipedia.org/wiki/David_Ungar

# Appendix - Implementing Prototype Based Inheritance
It is possible to implement prototype-based inheritance using alists or hashtables in Common Lisp. I can try to explain, if you'd like...

# See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity (see blogs that begin with a date 202x-xx-xx-)
- https://guitarvydas.github.io/ (up to about mid-2022)
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
WIP - leanpub'ed (leanpub encourages publishing books before they are finalized)
https://leanpub.com/u/paul-tarvydas
### Discord
https://discord.gg/Jjx62ypR
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice needed)