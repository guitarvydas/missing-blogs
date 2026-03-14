# 2022-07-06-BRS-Wheel Reinvention Jam Ideas
# Announcement
https://handmade.network/jam

# Brainstorming For Wheel Reinvention Jam
- **dungeon scripting DSL**
	- scripting DSL -> JSON, C++, etc.
	- based on Ghost Stars tech
	- taste: https://github.com/guitarvydas/ghost_stars
	
- **Secrets of Sector Lisp**
	- report on SL
		- why is the GC only 40 bytes?  
			- Garbage Collection in 40 bytes, how is this possible?
			- J. Tunney created this version of GC (this GC is not based on McCarthy's original GC)
		- after 50-70 years of banging our heads on programming fads, Sector Lisp (based on McCarthy's original Lisp) is Orders of Magnitude smaller than any programming language
			- why?  
			- I believe that this smallness cannot be attributed only to assembler tricks, there must be something else at work
				- what is this "Je ne sais quoi"?
				- can we apply these secrets to other programs and programming languages?
				- will this lead to a better understanding of the reasons for "code bloat"?
	- create Sector Lisp implemented in Ohm-JS 
		- transpile SL to SL
		- transpile SL to  C/C++
		- ostensibly: create a Sector Lisp Embeddable Language
	- changing our mind: we will follow the path of least resistance, whereever that takes us
	- taste: *previous notes* [TBD]
	- collaborators:
		- no experience necessary
		- I hope to impart how to use Ohm-JS to collaborators
			- thinking "macros" instead of "compilers"
			- *toolbox* languages, don't re-invent compilation, use existing compilers to do the heavy lifting
			- YAGNI approach to programming
		- SL is quite simple
			- implementing SL should take only a few hours, 
			- but, understanding *why* SL is small might take longer, I dunno
	- First Principles Thinking
		- https://fs.blog/first-principles/
		- what *first principles* are at work here?

