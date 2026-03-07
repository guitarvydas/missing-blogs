# 2023-08-23-Structuring of Events---
copied_to_pages: "true"
---

## Summary

IMO, Events are not bad.  Unstructured use of Events is bad.

The Holy Grail of Programming Language design is the encouragement/enforcement of the use of Nesting.  

It is folly to treat, both, control flow composition and data composition in the same way.

Pub/Sub, CPS, FP, UNIX pipelines, etc. are unstructured.

IMO, "complexity" is not caused by Events, but, by the unstructured use of Events.
## Discussion
IMO, EVENTs are not bad, and, GOTOs are not bad.  

UNSTRUCTURED use of EVENTs / GOTOs, though, is bad for human understanding.  Electronic machines have no problem understanding and acting upon unstructured GOTOs and EVENTs, though.  Machines don't care, they're just machines.

The Holy Grail of Programming Language design is the encouragement/enforcement for the use of Nesting.  

Russian Dolls are examples of full-blown Nesting. https://en.wikipedia.org/wiki/Matryoshka_doll

To achieve Nesting, one must first achieve Isolation (my wording, now superseded by "0D").  Partial isolation of only data is called Encapsulation (seen in OO, Closures, etc).  Primordial nesting of files can be seen in Hierarchical File Systems (seen in UNIX, etc.) A File is an encapsulated bunch of data.  An example of an unstructured file system is DOS (flat file system). UNIX applies structure to File thingies in a hierarchical manner, i.e. a UNIX File is defined recursively - it can contain (a) a bunch of data, or, (b) a list of Files (called Files and Directories, resp.)

Once you have Isolation , you can plug units together in some more-structured, layered manner.  

## Message Passing

Event-passing is also called message-passing.  Most implementations of message-passing that I've seen are at the DOS level of technology - i.e. unstructured, e.g. Pub/Sub.  I would consider this to be "complicated", esp. when scaled.  A successful model for Structured Message Passing is the Org Chart used in successful, scalable businesses (not necessarily computer-related).  In this model, "commands" travel downward and "summaries" travel upward.

Note that I lump CPS into the GOTO camp.  CPS creates units of isolated functionality, but enforces no structure on their arrangement.  The first time that I saw CPS was in Denotational Semantics. IIRC, the implementation of PROLOG in "On Lisp" uses CPS  (or was that PAIP PROLOG?  I was looking at both at the same time and my memory is hazy).

State Machines that communicate via Message Passing tend to fulfil only the prerequisites for Structured Message Passing, but do not achieve full-blown nesting, i.e. State Machines isolate data and control flow, but enforce no further arrangement of such units.  Harel's StateCharts DO enforce `nesting.

## StateCharts

StateCharts conflate two orthogonal issues:
- control flow description, composition and inheritance using LIFOs
- concurrency, using FIFOs

These issues can be teased apart and separately understood.
## Notes

- The needs of inheritance for Control Flow composition are different from the needs for inheritance for data composition.  It is folly to treat both in the same way.  StateCharts specify inheritance for control flow, but leave inheritance for data unspecified.  When discussing control flow inheritance, to underline the fact that there is a difference, I use the phrase "Parental Authority".

- Concurrency and Isolation are two orthogonal ideas.  One can have Isolation without parallelism, or concurrency, or simultaneity.  I call this "0D".

- OO, CPS, Pub/Sub, UNIX pipelines, etc. provide only the atomic basis for nesting, but, do not achieve full-blown nesting.

- "Complication" arises when something looks "too busy", usually caused by scaling.  Simplicity is defined as "the lack of nuance".  I talk about the Rule of 7.  I would suggest that Events are not the cause of complication, but, that the *unstructured use* of Events probably causes complexity.

- An example of full-blown, structured message-passing is the scalable arrangement of businesses.  This arrangement is often documented as Org Charts.

- Lispers love Lisp and put up with its minimal syntax, because Lisp provides a grab-bag of assembler-level operations which can be arranged in a structured manner using Lisp's recursive syntax. (Atoms and Lists).



# See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity (see blogs that begin with a date 202x-xx-xx-)
- https://guitarvydas.github.io/ (up to about mid-2022)
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
leanpub'ed (disclaimer: leanpub encourages publishing books before they are finalized)
https://leanpub.com/u/paul-tarvydas
### Discord
https://discord.gg/Jjx62ypR  all welcome, I invite more discussion of these topics
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice needed)