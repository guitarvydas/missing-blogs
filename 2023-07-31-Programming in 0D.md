# 2023-07-31-Programming in 0D
Programming in 0D consists of stringing lots of little Servers together.  

The Messages between each Client (a Server in its own right) and downstream server form a Protocol.  

The Protocols might be different between each pair.  

Kinda like CPS, but less ad-hoc. 0D makes it possible to isolate each Continuation.  

0D makes it possible to draw each Continuation as a separate Component.  Actually, *isolation* is what makes it possible to draw Components.  

*Isolation* (FIFOs instead of LIFOs) makes CPS tenable as *isolated* components.  Imagine CPS that uses Send() instead of CALL/RETURN.  CPS isn't usable across distributed machines, 0D, though, is usable across distributed machines.
