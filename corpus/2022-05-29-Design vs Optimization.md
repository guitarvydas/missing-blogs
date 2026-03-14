# 2022-05-29-Design vs Optimization
# Design Vs. Optimization

Programming consists of, roughly, two activities:
1. Designing the product.
2. Optimizing the product.

The idea of "optimization" is different depending on which activity you are performing.

During *design*, you probably have a souped-up workstation and can afford to waste CPU cycles.  During this phase, "optimization" means reducing turn-around time during development.  During the *design* phase, it is OK to waste CPU cycles to have the (souped-up) computer do as much work for you as possible.  In this case "optimization" doesn't mean speeding the program up, it means speeding up the *design* process.

When optimizing a product for release to customers, the emphasis, though, is on lowering "cost" to customers.  What does this even mean?  Lowering the hardware costs?  Speeding up the software?

# Nuanced Design
*Design* is performed on many levels, e.g.
- Architecture - how does the design fit with the surroundings?
- UX - how does the design fit with customers' expectations?
- Engineering - What are all of the niggly details required to make the design work?
- Security
- Testability
- Q/A-ability
- Scaling
- Field upgrading

# Nuanced Product Optimization
*Production Engineering* considers a number of factors unrelated to *design*...
- Speed up
- Footprint
- Hardware cost 
- Economies of scale
- Testing
- Q/A
- Maintenance
- Choice of Implementation Language (if you *have to* use only one language, which one?  Does the choice of language depend on the final product?)
- Choice of external technologies (databases, etc.)

# Conflation
Note that, currently, we schmoo all of the above activities into one big blob called "software development".

The result is that only *some* of the above factors are addressed, usually based on the whims/experience of the software developer(s).

Note that, currently, most popular programming languages emphasize *production engineering* over *design*.  

If you use a *compiler*, then you are working on *production engineering*.

Compilation is optimization.

Compilation used during the *design* phase is *premature optimization*.

In the past, attempts were made at addressing *design* issues, but these were wiped off the table in lieue of *production engineering* issues.  We used to talk about *rapid prototyping* and *REPL*s and *dynamic languages*.

[Note that Bret Victor's ideas, for example, devolve into UX+REPL issues - i.e. *design*].

# Waterfall Design
Waterfall design is the belief that *everything* about the problem is understood at the outset and that there will be no iterations during design.

Agile, more-and-more-elaborate-type-systems, etc., are attempts at trying to appease the *design* process while maintaining the Waterfall design mentality.

# Artform
*Design* is like Art.  

*Design* is creative.

We haven't figured out how to teach someone to be good at creativity, but, we know that the more different things you know, the more "creative" you can be (by picking and choosing ideas for solutions from a larger search space).

Production Engineering - optimization - is what you do *after* the creative process has been reduced.

Production Engineering makes incremental improvements along a choice of dimensions, to something that already exists.

Starting out *design* using only *production engineering* tools is like telling an artist to use only two colours - black and white (which can be blended to produce gray) - and to use straight lines only.

# Brainstorming
Art involves a lot of brainstorming.

Teaching people how to write songs[^sw] involves teaching them how to brainstorm and enhance their search space.

[^sw]: Aside: Songwriting consists of compressing a thought into very few words, and supporting the thought, using *prosody*, employing devices like melody, word accents, line lengths, chord structure, recording production, etc., etc.  For example, "Yesterday" (The Beatles) sounds *sad*, partly because the structure of the song uses 7 bars in the verse, instead of the happier-sounding 8 bars. Human senses perceive nuance in many dimensions.  Addressing only one dimension, like melody, often isn't enough.  Often, it is difficult to *measure* why someone doesn't "like" a song, but, that's only because the measuring tools are not good enough to characterize all of the nuances that human listeners "feel in their gut".

Programmers don't talk about brainstorming.  Maybe that's a *tell* that they are employing Production Engineering mentality?

Conferences are like brainstorming.  Half-baked ideas are floated. The "real meat" of a conference happens in the hallways.