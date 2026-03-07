# 2023-08-23-Layered Software
The idea of snapping building blocks together is easier when only one simple type is used.  

LEGO == "round peg" into "round hole".

The UNIX idea of a simple inter-command type - characters delimited by newlines - is already too complicated (!).  Workarounds to handle binary data instead of 7-bit ASCII bytes were invented, and, then, came Unicode.

It is possible to build up more complex types using layers of types.

Types in networks are layered this way.  Types in PLs are not layered in the same manner.  IMO, the concepts espoused in something like the OSI 7-layer model need to be applied to programming.

My feeling at this time, is that a software Message for coupling software components is (1) a Tag and (2) Data.  One can complexify on the way up and simplify on the way down.  Type checking and type stripping can be done by software components, but, the components need to be isolated from one another, e.g. free from hidden and visible dependencies (aka "0D", anti-CALL/RETURN).  The premature-optimization crowd can be mollified by allowing some components to be optimized out at "compile time".


We have all of the tools, we just don't bother to organize this way.  In the same way that we wrote spaghetti code when everything looked like a GOTO.



# See Also
### Blogs
- https://publish.obsidian.md/programmingsimplicity (see blogs that begin with a date 202x-xx-xx-)
- https://guitarvydas.github.io/ (up to about mid-2022)
### Videos
https://www.youtube.com/@programmingsimplicity2980
### Books
leanpub'ed (disclaimer: leanpub encourages publishing books before they are finalized)
https://leanpub.com/u/paul-tarvydas
### Discord
https://discord.gg/Jjx62ypR  all welcome, I invite more discussion of these topics
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice needed)