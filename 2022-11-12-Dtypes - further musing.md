# 2022-11-12-Dtypes - further musingIn Lisp, a dtype would be a “symbol” - a name that implies no further structure.  

An S/SL dtype is basically an enum.  A numeric token that means something ONLY to the underlying implementation code.

S/SL (and Lisp) allow you to manipulate these things without needing to know what’s underneath.  Symbolic computation.  (Manipulate means: move, assign, pass as parameter, …).  

I used to buid electronics. ICs are like “opaque tokens”.  I could build things with them, I could put them in little plastic baggies, etc. , but, I never bothered to saw one open to see what kind of oxides (rust) was being used.

Compiler-writers know this concept as “tokenization” or “scanning”.  A string of characters is too ugly / inefficient to handle, so a front-end (The Scanner) collects up all of the strings in a table and assigns numeric codes (“tokens”) to them.  Subsequent passes deal only with the tokens.  A Parser - the next pass down the line - checks to see that the tokens form valid phrases, for example “If … then … else … end if” is tokenized first, “if” = 1, “then” = 32, “else” = “77”, “end” = 101.  The preceding phrase would be transformed into “1 … 32 … 77 … 101 1” which is cheaper (more efficient) to pattern match (“parse”) because the CPU can handle numbers more efficiently that strings of characters.

Aside: in Python, the code
```
"xyz" == "xyzd"
```
is less efficient than
```
1 == 12
```

In the first case, the Python engine has to match "x", then "y", then "z", then mismatch on "d".  In the second case, the Python engine just compares two numbers.  The first case takes 4 steps before the answer is known, the second case needs only 1 step.  The lesson: convert all hoary data thingies into numbers when possible.  Only the first pass (The Scanner) needs to bother with a hash table and lookups, the rest of the passes get to deal with (much more efficient) numeric codes.

An interesting question, which I haven't answered yet, might be: "how do I implement dtypes in Python?".  Dtypes are very, very similar to Python classes and require the programmer to exhibit extreme discipline in keeping the concepts separated.  

A first, knee-jerk, idea for creating dtypes in Python would be to construct a tree of strings and another tree of Classes with a map that relates the first tree to the second.  Nuances, such as optimization and tokenization, come in the form of assigning numeric codes to each string and to save token-mapping in some other hash table ("map").  There are, probably, better ways to do this - less stupid and more nuanced - but, I'll leave that to Python experts.  I think that you could create the first tree as a Python Class, but, then you *might* fall down into the undisciplined rathole of giving too many details (like "int", "float", "complex", Boolean, Sequence, Text, etc.).  

Python makes it *very* convenient to over-supply a bunch of details.  I assert that you need to elide details to climb up to the next level in thinking.  For now, you need to exhibit discipline and *manually* separate symbols from implementation details.

Some day, languages that suppress such low-level details will be available, but, for now, you have to make the separation yourself.

In fact, some detail-suppression languages already exist:
1. Assembler elides the toggle switches that were used on early electronic computers
2. C elides the ugly details of programming in Assembler
3. S/SL elides the ugly details of strings and types.
4. Molecules elide the ugly details of Atoms
5. Atoms elide the ugly details of sub-atomic particles
6. ...
