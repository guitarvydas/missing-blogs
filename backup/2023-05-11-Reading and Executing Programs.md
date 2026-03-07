# 2023-05-11-Reading and Executing Programs> Programs must be written for people to read and only incidentally for machines to execute
> Hal Abelson, Structure and Interpretation of Computer Programs

I deeply disagree with this statement.  I don't think that the statement is wrong, but, I do think that it is only a part of a bigger picture.

I will try to explain my perspective by riffing on the above quote...

0. there are multiple views on any problem
	- Physics tells us to use *simplifying assumptions* in notations for thinking about a problem (*SCN*) while remembering that the *assumptions* are *simplifications* and are *not* Reality
	- there is no one Silver Bullet - there are many Silver Bullets, at least one for each different view of a problem domain
0. The point of a Program is
	- to control a machine
	- to express to other human readers *why* certain choices were made in writing the Program.

You cannot deal with only one aspect of the problem, while ignoring the other parts of the problem.  It is not sufficient to *only* write programs for human readability, a complete program must address, both, human readability and machine readability.

If the expression of a block of knowledge is expressed in an SCN, but, is too complicated for others to understand, then even the goal of the above statement has failed.  The goal is to understand something complicated and to explain it in an understandable manner.  A sub-goal is to use the SCN to derive (interpolate, not extrapolate) properties of the block of knowledge.  This is but a sub-goal, not the main goal of the above statement.  Maybe the above statement should be modified to: "... for other mathematicians to read and manipulate ..."

# Random Notes 
The goal of programming is to control the machine. The goal of a notation is to support the programming activity by making it possible for the programmer to create a program that controls machine, and to think about the program more easily

And to describe why certain choices were made in writing the program a certain way from that point of you slapping all of the details of annotation programming notation into a single notation actually fights against the beam principle of making easier to think about and easier to understand what's there

For example, type checking, does not need to be convoluted with the actual code that sequences the machine type checking is used to allow a machine to check that the intentions of the programmer were maintained, but are otherwise inconsequential to the final result of controlling the machine

In some cases types demonstrate to others what the original programmer was thinking, and why, he built the code, a certain way in some cases types for the sick complete set of types form here on impenetrable wall of detail that detracts from understanding and such a such a deep level of information is needed only if the reader wishes to explore details out of at a greater depth

Mathematics was traditionally performed by writing on paper or clay tablets, and necessitated the medium assassinated that all of the details will be in one place to avoid having to manually flip around pages and find more information today we machines that can do this work for us and stitch together multiple inputs, for example the actual control instructions in one file and the actual types that help programmer get the express vehicle information correctly other file in the machine and stitch those two together and then use the tape file to check the control file readers can dig into the tape file to see more detail when they want more detail after they've after they understood, the general overview of the intent of the program
