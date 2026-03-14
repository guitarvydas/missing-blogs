# 2022-08-12-Convenient Programming IDEs
[Jack Rusher makes a good point about convenient debugging](https://twitter.com/jackrusher/status/1558000856263540736):

Riffing on this idea:
- The main feature being used is "Lisp Restart" https://gigamonkeys.com/book/beyond-exception-handling-conditions-and-restarts.html
- "Restart" is more than simple class-based error conditions.
- Lisp Restart is a form of hot-loading.
- Restarts were invented in Lisp. I am unaware of this level of power being available for most other languages.
- The concept of restarts seems to have languished and does not appear in modern languages, such as JavaScript, Python, Haskell, Rust, etc.
- The Lisp Restarts UX  leaves something to be desired.  There is no overriding design principle to the UX.  Sometimes "abort" is triggered by hitting "3" and sometimes "abort" is triggered by some other keystroke.
- Restarts are technically harder when the main communications mechanism is LIFO (AKA call-stack, and functions).
- UNIX shell pipelines use FIFOs as the main communications mechanism.  Pipelines do not use LIFOs.
- "Restarts" can be much cheaper using FIFOs. Kill a process, replace it with another process with exactly the same FDs for stdin, stdout and stderr. ["Referential Transparency" appears to do the same in FP (Functional Programming), but, is usually based on LIFOs (the call stack) which inserts unwanted dependencies].
- ALL languages are interpreted.  Compilers are optimizations.  Compilers run some of the interpretation at "compile-time" and off-load work from the runtimes.
- Tailoring / revamping a language to appease compilation is premature optimization.  You trade expressitivity for optimization. You lose the ability to "think" more freely when you insist on using a language which appeases compilation.
- Hot-loading is a feature of the *runtime*.
- Lisp (and other so-called "dynamic" languages) have the feature that the runtime language is the SAME as the programming language.  Most "compiled languages" don't have this feature, for example, when you program in C and debug in GDB, you have to learn 2 languages, C and GDB's command language, whereas with Lisp, the command language of the debugger IS Lisp.  When there is a separate language for the debugger, that language is often stunted and lags behind the capabilities of the programming language.  For example, VSCode allows one to examine Objects, but one has to switch to a language of mouse-clicks to dig into Objects instead of using language-level expressions like `x.y.z`.  It is now 2022 and debuggers have been getting better, but, dynamic languages (like Lisp) had this level of introspection right out of the box in the mid-1900s.  With modern languages it is easily possible to insert *print* statements to view data, but, when debugging you want to examine data on-the-fly and you might not have anticipated which data needs to be examined.  Inserting *print* statements into the code before a run is called "printf debugging", which is generally a poor UX for understanding Design bugs.
- The apparent integration of a programming language and debugging environment is enhanced by using the same command language.  When the programming language and the debugging environment use the same language, it *appears* that the IDE is better-integrated (the UX is easier to use).
- Internally, the Lisp REPL calls Eval(), then punts to the runtime.  Hot-loading is implemented by the Lisp runtime, not Eval().  Hot-loading *could* be separated from the language IDE, but usually isn't.
- A "compiler" is simply Eval().  For example, imagine adding two integers, `a` and `b` together.  Eval() checks that `a` is an integer and checks that `b` is an integer then calls `AddInteger(a,b)`.  Using divide-and-conquer, we can snap the checking code away from Eval() and shove it into code that runs earlier.  I.E. the compiler runs functions `ensureInteger (a)` and `ensureInteger (b)`, then leaves instructions around for the runtime that say `AddIntegerButDontBotherCheckingSinceItIsGuaranteedThatTheOperandsAreIntegers (a, b)`
- line vs. tree oriented assembler
	- Lisp is tree-oriented Assembler
	- ASM is line-oriented Assembler.
	- property: no syntax to get in the way => easy to plumb units together
	- property: expression language, every operation returns a value (without needing explicit syntax), => easy to plumb units together
- Lisp syntax (or, lack of syntax) makes it easy to plug components together, and, makes it easier to imagine / invent hot-loading.  Compiler-appeasement languages tend to look at use-cases designed using dynamic languages and implement optimizations of these ideas.
- Sometimes, type-checkers slow down the process of Design.  You encode your first guess in a type system, then, you feel reluctant to change the Design (the Type System) as new revelations about the problem-space are encountered.
- One needs a Big Red Button, during Design, that wipes out everything done up to that point and lets you start from scratch (preserving hard-won knowledge).  Lisp and dynamic languages do this better than compiler-appeasement languages.  There is less friction in rewriting a Lisp program from scratch than for rewriting a carefully-crafted program containing a carefully-crafted type system (usually wrong) and containing premature optimizations.  
- FYI - carefully-crafted Type Systems are usually wrong during Design, since, once you get the Design right (or "good enough"), you stop working on it and ship it.  The majority of programmers only continue working on a Design if it is insufficient / buggy in some way ([FDD - Failure Driven Design](https://guitarvydas.github.io/2021/04/23/Failure-Driven-Design.html)).
- The Lispworks debugger is better than Slime.  Lispworks has more thought put into the UX and better-integration of the GUI tools.  Common Lisp has access to various features built into the language, but access by itself is not enough.  Example: we use HLLs[^hll] instead of assembler. Assembler supplies *all* of the operations necessary to implement any language, but, the UX matters and we choose to drape HLL syntax over assembler.  Example: we *can* write C programs in OO and FP styles, but we tend not to. Creating minimalist notations enables thinking more freely in various dimensions.

[^hll]: HLL ≣ High Level Language
- Lisp 1.5 and Sector Lisp have the feature that they are *pure* FP languages, with absolutely no mutation[^mut].  This makes it easier to clean up garbage (no heap).  This makes it easier to create (and destroy) variables - as parameters to Lambdas.  Variables can only be pushed onto the front of parameter lists in a stack-like manner (no random access, no heaps).  This makes it easier to hot-load program units[^unit]. 
	- Pure functions are actually synchronous state machines (functions block when calling other functions, waiting for the callee), which makes certain constructs more difficult to imagine than would otherwise be necessary[^obv].
[^mut]: well, no mutation, except for the global call-stack
[^obv]: The obvious answer is: don't use pure functions in such use-cases, switch to different notations.  The fact that operating systems need to resort to brute-force preemption is a *tell* that a different notation is needed to describe what is going on.
[^unit]: Where a "unit" is a pure, Curried function.  No mutation -> no heaps -> snap lambdas on-and-off the top-of-stack.  If you need to deal with things that have State - e.g. robots, IoT, blockchain, internet, etc. - hot-plugging becomes harder.
# Expressivity

## 2022-08-09-Expressivity Lost

A lot of expressitivity was lost in the mad rush to premature optimization (AKA compilation and over-use of synchronization and over-thinking of "efficiency").  Liveness was easier, multitasking was easier, hot-loading was easier, debuggers were easier, etc., etc.

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
