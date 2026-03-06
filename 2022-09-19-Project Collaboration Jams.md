# 2022-09-19-Project Collaboration Jams# Suggested Goals

Suggested goal: to create Discords[^github] on a per-*project* basis.  A project is created by a team of domain experts, where the various domains needed for the project are very different from one another.

[^github]: Should these be Discords or github projects?  Or both?  Probably: discuss on Discord, develop code in github.

Programmers bring all their tools to bear on a specific problem to make solving the problem "ridiculously easy"[^fbp].

[^fbp]: FBP (Flow Based Programming) should make programming "ridiculously easy".  FBPers must demonstrate this. Champions of "more strong typing makes programming ridiculously easy" must demonstrate this.  Champions of any language XYZ that makes programming "ridiculously easy" must demonstrate this.

Goal: "Creatives" (creative people, usually non-programmers) invent something appealing for other non-programmers, e.g. a game.  Creatives use the tools provided by programmers to knock out the desired game(s) without needing to "learn how to program", nor the need to touch Racket, Clojure, Rust, monads, lambda calculus, etc.

Goal: Architects gather the requirements based on the desires (inventions) of Creatives.

Goal: Engineers produce MVPs of the game(s).

Goal: Production Engineers make the game(s) run faster/better/smaller.

Goal: Test Engineers work out testing strategies with the goal of zero (0) defects in the field and zero (0) updates[^mature].

[^mature]: Every mature industry produces products that have 0 defects in the field.  Automobiles, bridges, etc.  The industries are regulated by govenments and laws.  Defects are severely punished by fines and jail time for the project purveyors.  For example, the Pinto gas-tank fire "problem".  Canadian Engineers wear "iron rings" to remind them of their responsibility.  A course in Tort Law is a requirement of Canadian Engineering education.

Goal: Maintenance Engineers work out strategies for adding new features and producing new games.  Each version of the game(s) is frozen in time.  New games might look the same as a previous game(s), but are completely different products.  Strategies are needed for *stealing* previous work and previous ideas to drastically shorten the production cycle.

Goal: Security Engineers work on strategies for hardening the game(s) for use in the real world.

Goal: iteration back-and-forth between all participants[^iter].  

[^iter]: One-way design - without iteration - is called "The Waterfall Method".  Iteration in programming is called "REPLs".

Goal: ... *further discussion*

# Projects
A project is created by a team of domain experts, where the various domains needed for the project are very different from one another.

Programming is a specific domain.  Programming is only a *part* of a project.

Programmers are not Creatives.  Creatives are not Programmers.  Architects are not Engineers.  Engineers are not Architects.  Production Engineers are not MVP Engineers.  MVP Engineers are not Production Engineers.  Test Engineers are specialists.  Maintenance Engineers are specialists.  Etc., etc.  Engineers don't write code, engineers produce blueprints for construction of code.

A project needs multiple domain experts.

# Starting Points - Start Small

Start small and specific.  Hope to learn by doing.

Suggestions:

1. Cube Cat game
2. Ghost Stars game

## Cube Cat
https://hg.sr.ht/~oofoe/qube-cat/browse/qc.rkt?rev=tip

Cube Cat exists and is playable.  A good - simple - starting point.

Cube Cat was created as part of a game jam.

Cube Cat is open sourced.

## Ghost Stars
https://oofoe.itch.io/ghost-stars

Ghost Stars is visually appealing, but, not very finished / playable.  What is the next step?

Ghost Stars was created as part of a game jam.

Cube Cat is open sourced.

# Elements
### NPCs
Non-player characters.  

Actors. 

Concurrency.  

Declarative logic rules.

## Scripts & Storyboards
How do programmers enable creatives to sketch out ideas on whiteboards, then translate the ideas to working games?

How can we minimize the tension between artistic ambition and implementation?" Artistic ambition should almost always win -- that's how you get good games.

How is provenance - the continuuation from conception to realization - accomplished/expressed?

# Arbiter - What is "Success"?
The decision of whether a combination of technologies is a "successful approach" for building programs must not be made be programmers.

For starters: we'll appoint The Oracle to be the inventor of Cube Cat.  The Oracle gets the final say for deciding on what is "easy".

I wish that I had more experience with the Film Industry.  It appears that in the film industry, *someone* has a vision, then pulls a team together to produce a product based on the vision.  Film assets are stand-alone unlike software functions which are tightly coupled to other software functions.

I do have *some* experience with songwriting.  Songs written with collaborators are usually better than songs written by solitary writers.  In the past, collaborations used to be done by pairs of people, but the concept has grown.  IIRC, "The Big Bang" was written by Rock Mafia using some 9 co-writers.  I think that a particular song in 2022 uses 19 co-writers (don't quote me on this).

Civil Engineering, also, works with collaborations.  The main Architect scopes out the project and the lay of the land.  An Engineer(s) sketches out a suitable design and uses a support team to perform calculations and to create blueprints.  The Architects and Engineers don't build the buildings - this is done by tradespeople who have experience using specific tools.

# Time Limit
*I dunno, does there need to be a time limit?  Discussion encouraged.*

# Future
Port these games to iOS and learn from the process.

Port these games to Android and learn from the process.

# My Biases / Thoughts
*All* programming consists of two (2) activities:
1. Grok
2. Output

## 1. Grok - understanding, input validation, parsing

Parsing is currently limited to mostly textual input.  Programming does not need to be rooted in text, but, currently is.

The "best" text-parsing tool is Ohm-JS.  The enabling technology of Ohm-JS is PEG ("parsing expression grammars").  PEG allows one to approach parsing in a layered - one (1) problem at a time - approach, instead of the blunderbuss approach of solving *every problem* in a unified, flat notation (like previous parsing tools such as YACC, Bison, compiler generators, etc.).

Text for programs is a very restricted form of prose.  Other kinds of syntaxes - e.g. DaS (diagrams as syntax) - are possible and need to be restricted in the way that text programs are a restricted forms of prose.  For example, technical diagrams are not the same as general drawings and visual Art.  Technical diagrams might be composed only of[^svg]:
1. boxes
2. ellipses
3. lines
4. text
5. groups/layers of the above.

[^svg]: Note that SVG supports such items.

## 2. Output - Fabrication, Formatting, Re-Arranging

The process of formatting output has been around for a long time, e.g. report-generation software like RPG and "#" syntax in BASIC.

The best practice, today, seems to be simple JavaScript *template strings* and/or Python *f-strings*.

The Grok pass produces a *map*.  The Fabrication pass pulls fields from the map and produces output strings (easily).

I've used PROLOG-like syntax to pattern-match the input and to produce JS *maps* (JS "namespaces" and "objects") and JavaScript Template-string syntax to format the results of the pattern-match.  I've used Python f-strings like JS template-strings.  I've used Ohm-JS to build mini-DSLs (SCNs) to help me express Grok/Fabricate and to generate code (PROLOG+JS+Bash).

## Consulting
I've been a Software Consultant for several decades.

I've always assumed that my customers understand their domains better than I do.

My "job" is to meet them "half way".  Create tools, a notation - for expressing their ideas.  Make tools so that my customers can build robust, scalable software without having to think about programming.  I know about programming.  They don't.  They know about their domains, I don't.

My customers don't care about generality.  They only want to solve their own problems.  I wade through general programming languages and programming ideas and pull out what is best for customers' problem domains.

# Cottage Industry vs. Engineering 
The term "cottage industry" is characterized by the fact that a single practitioner (or a team) "wears all of the hats" - design, implementation, testing, etc., etc. This kind of approach creates POCs (Proofs of Concept) and early versions of a product.  Cottage industry products appeal to innovators and early adopters.

"Engineering", though, is the attempt to cubby-hole specific responsibilties and to assign sub-tasks to experts in each cubby-hole.  Engineering is an attempt to sub-divide an industry and to make the results appeal to the majority of users.

Aside: Karpov (Chess Master beaten by Big Blue) now runs contests that use computers to calculate all possible moves and humans to make the decisions.  Chess-playing is now sub-divided into Board-calculation agents and Creative agents. The machine-doable portion of the chess-playing problem has been cleaved off and turned into a clockwork problem in a specific cubby-hole.  The remaining bits - the Creative portion - fit into a different cubby-hole.

A "cottage industry" might also be characterized by the number of product defects that are experienced in the field.  Mature industries produce products that do not need to be upgraded and have no defects (within restricted product boundaries and guarantees). 