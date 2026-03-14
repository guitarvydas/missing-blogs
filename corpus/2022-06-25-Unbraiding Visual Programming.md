# 2022-06-25-Unbraiding Visual Programming
# Unbraiding Visual Programmig
Rhetorical questions:

Are you (the programmer) trying to parse paintings or technical diagrams?

What is the difference between the two?

When programmers write programs using state-of-the-art IDEs (i.e. programming languages), do they use Microsoft Word or vscode?

# 0D
Diagrams, on paper or on whiteboard, have a certain meaning to most humans.

People understand that boxes drawn on diagrams represent *independent* components.

Modern programming languages, like Rust, Haskell, Python, etc., etc. do not inherently support the creation of *independent* components[^1].  Programmers must resort to extreme measures and workarounds, to create simulations of *independent* components.

If programming languages supported creation of 0D (zero-dependency) components, it would be easier to map diagrams to programs.

[^1]: Functions are state machines that block ("waiting for result from callee").  When you call a function, you are creating an implicit synchronization (regardless of whether you want synchronization).  Synchronization is a dependency.  Furthermore, most programming languages encourage programmers to hard-wire names of functions into their code.   DLLs are epicycles invented to ameliorate this hard-wiring, but, DLLs continue to create synchronization dependencies by binding the RETURN path.