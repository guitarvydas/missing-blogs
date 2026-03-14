# 2023-10-20-Software Atoms Continued
Atoms are
- stand-alone
- composable
- asynchronous.

![](coupling-atom.drawio.svg)
Not atomic: `f`.

Stand-alone : requires `x`

Composable: yes, but within certain restrictions
- 1 in, 1 out
- textual (text macro).

Asynchronous: no.
- `f∘x` is not inherently asynchronous
	- based on CPU model with shared, global Registers
	- based on CPU model with shared, global RAM
	- based on CPU model with single, shared, global stack.
- workarounds to make `f∘x` asynchronous exist, but are onerous
	- preemption
	- stack switching
	- register saving and restoring, sometimes with hardware assist
	- aka "epicycle" - make-work, accidental complexity to force-fit asynchroncity onto synchronous notation
	- restrictions required by the work-arounds limit the solution-space -> stunted thinking, more gotchas, more epicycles
- inputs must all come at the same time
	- in fact, inputs come as a block of data that is then destructured into sub-fields
- outputs must all be sent at the same time
	- outputs must be coalesced into a single heterogenous blob, which can be destructured later