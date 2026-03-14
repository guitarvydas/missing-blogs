# 2023-06-21-0D-Working Paper## Overview
0D (Zero Dependency) is composed of 3 main portions:
1. DaS syntax compiler
2. Component Palette
3. Runtime(s)

Each portion should be a stand-alone tool.  

There should be no requirement to tie the portions together using anything like a well-defined intermediate representation (like JSON?[^json]).

[^json]: I'm not a fan of JSON.  I think that it is inefficient.  On the other hand, it exists and most modern languages have libraries  for reading and writing it.

It should be possible to optimize a particular solution, but, this should not be a requirement.  Example: if we determine that JSON is too inefficient, we should be able to (easily) switch to using a more-efficient representation (i.e. data structures in memory) on a *per project basis*.  The intermediate form remains JSON, but, a specific project might wish to side-step its use.

## Details
1. DaS syntax compiler
	1. convert a drawing to JSON
2. Component Palette
	3. a namespace-like thing that is a collection of useful components
		1. a directory?
		2. a hierarchy of directories?
	4. components in the palette can be Leaves
	5. components in the palette can be Containers
		1. should Containers in the palette be compiled into code?
		2. should Containers remain in the palette as JSON?
		3. should Containers remain in the palette as diagrams?
	6. palette components are *black boxes* 
		1. goal: dev can reach into palette and pull out black boxes, then snap them together to form new solutions to various problems
		2. palette may contain Patterns
			1. e.g. "if you want to solve a problem that is similar to this one, grab this Pattern then hack it into submission"
3. Runtime(s)
	1. Lisp
	2. Odin, optimized
	3. Odin, completely dynamic (non-optimized)
	4. future: BLC?  Sector Lisp?
	5. a "golden" standard against which all runtimes are compared
		1. probably dynamic, non-optimized
		2. describes intended semantics without reference to specific implementation details
## Examples
- use the 0D tool to build a simple bash-like script (e.g. Obsidian to Github Pages)
- use the 0D tool to build a compiler - candidate RT0D
- use the 0D tool to build a game - e.g. https://oofoe.itch.io/sparxline?hidden=true, open-source / free itch.io games (game jams)
- use the 0D tool to build Slider, aka editor for Text Visualization
- use the 0D tool to implement some simple problem in robotics (e.g. some example from ROS)
- use the 0D tool to implement some hoary problem in robotics (e.g. some example from ROS)
- use the 0D toolset to work on a real app 
	- e.g. Kagi
	- show the techniques used in optimized form on a per-project basis (e.g. Kagi YAGNI use of the toolset)

## Tasks
1. break existing Odin0D into 3 separate portions which use/emit JSON only
2. finish implementing obs2ghp, even if bandaids are used
3. finish RT0D description / transpiler
	1. get it to transpile into Lisp or Python (example of dynamic example)
	2. get it to transpile into Odin (example of static implementation)