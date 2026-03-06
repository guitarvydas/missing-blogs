# 2022-06-26-Compiling vs. ModellingModeling is an attempt to use *same* notation to 

- modelling == bottom-up, single notation to describe a problem and its solution (assumption: there must be only one way to solve a given problem (I don't concur))
- compiling = bowl of SCNs == top-down, design a notation for every sub-problem (many specific languages instead of one GPL), then solve the sub-problem and show how you solved it

SCN means "Solution-Centric Notation".  Note the word "Solution".  SCNs describe a specific solution to some problem. There might be more than one way to solve a problem.  An SCN shows the details of *how* a Software Architect decided to solve the problem.

SCNs are like programming languages, but, are lighter weight.

SCNs are like light-weight DSLs (Domain Specific Languages).  DSLs are like general purpose programming languages, but more specific.

## Building SCNs
SCNs can be built in a few hours using top-down parsing techniques.  Currently, I favour Ohm-JS and its Ohm-Editor and my helper tool *prep*.  Before that, I used S/SL and TXL and hand-built recursive-descent parsers.  I don't do any of the heavy lifting, since, that would slow me down.  I rely on *toolbox languages* to do my heavy lifting.  I currently use JavaScript and Python, before that I used Common Lisp, before that I used Assembler.  I could use static languages like Haskell, Rust, C++, etc., for toolboxes, but I don't bother, since they have been severely tweaked for human readability, restricting what kind of code I can generate automatically (generating code is like compiling).  I imagine that I could use existing compiler technologies like LLVM, but I haven't looked into them (I value simplicity and I expect that I won't find simplicity therein).

# Bowl of SCNs
Assumption:
- it is easier to create a new notation than to design a model using a GPL
- designing new languages in an afternoon
	- possible, if you don't bother to do everything that a full-blown compiler does
		- create new language, but, punt heavy lifting to existing compilers/languages
		- easy with TDP (top-down-parsing)
			- e.g. manually-built recursive-descent parsers
			- e.g. S/SL is a mini-DSL for building recursive-descent parsers
			- e.g. TXL.ca - strongly typed, functional, mini-DSL for parsing
			- parsing is even easier with PEG
			- Ohm-JS is a DSL designed with PEG principles, Ohm-JS allows easy creation of multiple syntaxes
- to design a programming language or SCN, you must pick symbols and phrases of symbols to make a useful UX
	- this was done for text-based programming languages
	- not done yet for technical diagrams of software
	- done for technical diagrams for Construction ("blueprints")
	- done for technical diagrams for Electronics ("schematics")
	- done for technical diagrams for Chemical Engineering ("molecules")
	- defied by Lambda-Calculus approaches to programming
		- lambda calculus breaks programs down into sub-atomic pieces (closures and lambdas)
		- but, this approach does not result in useful UXs
		- this approach is like a bowl of [rice](https://www.brainyquote.com/quotes/mitch_hedberg_297490)
# Modeling Using Only A GPL
Assumption:
- GPL approach makes you think that building a new language (notation) is difficult and time-consuming
- GPL approach: build "everything" from scratch, including assembler emission
- building parsers based on Language Theory-based specifications
	- Language Theory (e.g. CFGs, LR(k), etc.) doesn't cover all of the cases and puts restrictions on languages and language specs
	- not as flexible as TDP
		- but then, assembler is more "flexible" than most GPLs
		- what is the cut-off? what is the trade-off?
			- bugs vs. automated checking
			- give up flexibility for automated checking
			- how does giving-up flexibility affect open-mindedness re. new designs?
- Current crop of Language Theory specifications result in text-only programming languages
	- this affects open-mindedness, PL designers choose to create text-only programming languages because of path of least resistance, not because of UX needs (i.e. closed-minded approach - text-based tools promulgate text-based GPLs)