# 2023-04-22-Auto Layout Is A UX Disaster# Auto Layout Is A UX Disaster

IMM, auto-layout results in disastrous UXs.

There are two kinds of code:
1. code for controlling machines, code that is machine-readable
2. code for communicating to human readers *why* code for controlling machines has been written the way it was - DI, Design Intent.  Code that is human-readable.

When laying out code for DI - human consumption - spatial relationships matter.  Do you want power-assist to help you lay out spatial relationships? Yes.  Do you want power-assist to change the layout every time you make a change? No.

When laying out code for machine consumption, spatial relationships don't matter.  Current electronic machines (aka "computers"), work only with sequential relationships.  Spatial layout doesn't matter to machines.  Auto-layout applied to this kind of code is just a waste of electrons.

Summary: layout only matters to human readers.  Human readers grok things that are laid out spatially.  Each time the layout changes, human readers need to expend brain-power to re-grok what's being presented.  Brain-power is bounded - users can burn brain power to think, or, they can burn brain power to re-grok what they've already grokked.