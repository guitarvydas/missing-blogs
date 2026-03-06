# 2023-06-09-Odin Internals - Baby StepsI'm trying to figure out what `copy` is in strings.odin https://github.com/odin-lang/Odin/blob/master/core/strings/strings.odin#L25.  

## Basics
- the Odin compiler source begins as C++
	- `src/gb/gb.h` contains some fundamental defs
		- I assume that `gb` means `ginger bill`
		- `gb_global` boils down to `static`
		- there is, also `gb_internal` which must mean something semantically different from `gb_global` but boils down to the same thing when expressed as C++
- Builtins
	- implemented in Odin, which get boiled down to C++ (boiled down to C, then assembler)
	- tagged with @builtin in the source code, e.g. `core/runtime/core_builtin.odin`
	- src/check???? defines builtins
		- builtin names listed in a table in src/checker_builtinprocs.hpp
		- src/checker.hpp contains a def for `BuiltinProc`
	- unlike most Odin procs, builtins do not need to be prefaced by a package name
		- the package name is implicitly supplied by looking it up in a table
		- each builtin is described by a struct `BuiltinProc`, which contains the package name

## Copy
- `copy` is defined as an overload proc in core_builtin.odin https://github.com/odin-lang/Odin/blob/master/core/runtime/core_builtin.odin#L60
	- copy_slice, or
	- copy_from_string
	- both, use intrinsics.mem_copy