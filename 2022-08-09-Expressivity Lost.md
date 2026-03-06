# 2022-08-09-Expressivity LostA lot of expressitivity was lost in the mad rush to premature optimization (AKA compilation and over-use of synchronization and over-thinking of "efficiency").  Liveness was easier, multitasking was easier, hot-loading was easier, debuggers were easier, etc., etc.

Sector Lisp - decidedly a dynamic language - clocks in at less than 512 bytes [sic - bytes, not K, not M, not G, not T].

Parsing *checks* for design errors.  
- Parsing can be done as a side-chain without affecting the underlying language.

Declaration-before-use *checks* for design errors (AKA typos).
- Declaration-before-use currently requires major overhauls to the underlying language.  For example, the most important code is usually placed at the bottom of a file.
- Declaration-before-use was invented in the mid-1900s based on "efficiency" biases of the mid-1900s.  Those considerations are no longer valid.  Multi-pass compilers are OK today.

Type checking *checks* for design errors.  
- Type checking currently requires major overhauls to the underlying language.  
- Something is wrong here.
- IMO "static languages" aren't worth all the trouble they cause.  
	- At least, in the form they are today.
	- Can we have dynamic languages AND before-hand type checking?  Lint? Type-checking pipelines?
- IMO "design rules" are better than type-checking anyway (design rule = per-project script that checks preconditions and types and ... (anything else that the Architect thinks is important)))