# 2023-07-19-Odin0D Working Papersnapshot of today's thoughts: 
- odin0d repo contains a mess of little experiments
- I hope to consolidate the branches into 2 main streams today
- (1) statically typed, (2) dynamically typed
- dynamic type branch is likely to atrophy in light of discovery that ChatGPT can map the syntax of Odin code to less typeful code, like Python and Common Lisp
	- for now, the Odin version is considered to be the "golden" version
	- future: maybe invent a pseudo-syntax that can be transliterated into Odin, Python, Common Lisp 
	- Odin code is structured differently from GC'ed code, due to considerations for memory allocation, which can be ignored when writing in a GCed language
- hope to create a 2nd usage video using newer component shapes (blue rectangles with pins, which we've been using for several months now)
- experimented with syntax mapper using Ohm-JS
	- goal was to strip type info out of Odin code to make the code "more readable" for experimental purposes
	- result 1: tokenizer pass 
	- result 2: "skim parsing" technique (much simpler than full-blown CFG, more like REGEX-y style of thinking)
	- result 3: partial conversion of Odin code to Common Lisp, unfinished
		- maybe 100% conversion is not necessary, maybe not even possible
		- maybe 80% conversion is good enough, with manual cleanup to produce working code
		- maybe last 20% expressed as very specific patterns and rewrites, to fit 100% FDD mentality
		- REGEX can't do this, but PEG (Ohm-JS) can because of recursive matching
- typeful code is "less readable" with respect to experimentation and on-boarding (initial understanding of what is going on)
	- expectation: stripping type info from Odin code will help communicate the underlying structure of what is intended - DI (Design Intent)
- observation: 
	- it seems that git and github are aimed at more methodical development and encourage a Waterfall approach
	- I tend to try out little experiments, using (mis-using?) git and github as a backup and UNDO tool
		- using github for UNDO is cumbersome, 
			- since you have to manually remember to create new branches before pushing them
			- this approach leaves lots of little dangling branches containing experiments, but, not shippable code
			- looking at a sea of little dangling branches becomes confusing after a while, as the project moves forward, I tend to forget to delete little experimental branches, and, just move on.  Later, I forget what the little branches were mean to accomplish and if they contain useful code
			- fooling with git interferes with Flow during Design and Experimentation
				- I don't know "when" I'm going to want to UNDO to a certain spot, nor "where" I want to UNDO back to ; trying to predict "where" is generally impossible, you can only know what you really wanted after-the-fact
				- I haven't encountered any UNDO feature that is helpful for this kind of work.  Most UNDOs are linear and it is difficult to remember which bits were useful and which were dead ends
					- At The Moment, I'm using Kinopio to draw a graph of my experimental development tree, then edit the tree using Kinopio ; I wish that this were automated in some way. I don't yet know what this means ; maybe a first step is to automatically generate a Kinopio representation of the git tree of branches, and then to annotate and edit the tree in Kinopio
				- I'm currently using GitKraken which gives a visual representation of the git branch tree, but it doesn't let you edit the tree except using git commands (which are non-visual)
			- 
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