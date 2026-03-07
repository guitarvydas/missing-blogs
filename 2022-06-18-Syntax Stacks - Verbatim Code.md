# 2022-06-18-Syntax Stacks - Verbatim CodeUsing top-down-parsing technologies and advances like PEG and Ohm-JS, it is possible to build textual programming languages in small, stackable steps.

At the bottom-most layer, I define *verbatim* code.

The idea of *verbatim* code is to allow inclusion of code snippets in any language in a program script.  This idea has been seen before in the form of `#asm` statements in the C programming language.

For example
```
temp ⟪g.createSemantics ()⟫ ⇉ sem
```
consists of a `temp` declaration and contains a snippet of Javascript *verbatim* code `g.createSemantics ()`.  The meaning and format of this `temp` declaration is discussed elsewhere.  For purposes of this note, only the embedded *verbatim code* is of interest.

# Syntax Stacks
SCNs[^scn] - my word for "mini-DSLs" - can be built up in an incremental, layered manner at the syntactic level.

Each syntactic layer defines one SCN that is aimed for one - and only one - specific purpose.  This is contrary to the notion of GPLs (General Purpose Languages).

For example, the code (see appendix) defines only the bare minimum necessary to
1. define software components (`comp`, ports, `leaf`, etc.)
2. a set of common programming language constructs expected to be supported by most existing programming languages, e.g. `temp`, `do`, `if`, `send`.

In most cases, the above subset is not enough to specify a full program.  In such cases, we embed *verbatim code* in some other programming language to "do the rest".

Our SCN specifies the bare minimum to support software components, then is transpiled to a target language (in this case Javascript).  The *verbatim code* is left as-is, and, only the *verbatim* brackets are stripped off.  The result is a full program in the target language (in this case Javascript) which can then be compiled using existing compilers.

We should be able to *stack* such SCNs and produce a final resulting program.  In the example below, the stack is three (3) deep
1. transpile higher-level *component* code to lower-level target code (in this case Javascript, I imagine that it would be possible to target Python, Rust, etc.)
2. convert compound identifiers into a form accepted by the target language, e.g. in this case, I targetted Javascript, so I converted all spaces in names to underscores `_`
3. strip off *verbatim* brackets.

Note that step (1) could transpile to toolbox code, which would necessitate the addition of at least one more transpiler to the stack - transpilation of toolbox code to the target language.  I imagine that the toolbox pseudo-code language would contain constructs common to all modern programming languages, like first-class functions, persistent variables, etc.  TODO: define a basic toolbox language based on the union of common functionality found in modern programming languages.  TODO: rename this software-component language to something other than `.tbx`, e.g. `ctbx`, which transpiles into `.tbx`.

[^scn]: SCN mean Solution Centric Notation

# Unicode Brackets
I chose to use Unicode bracket characters in my syntax.  The choice is arbitrary and can be changed.

# Verbatim Grammar
```
verbatim {
main =
    | other* "⟪" main "⟫" main? -- bracketed
    | other+ -- pre
other = !"⟪" ! "⟫" any
}
```
# Verbatim Transpiler - Formatting
```
main_bracketed [@other lb main1 rb @main2] = [[${other}${main1}${main2}]]
main_pre [@x] = [[${x}]]
other [c] = [[${c}]]
```

The `verbatim.fmt` rule `main_bracketed` corresponds to the first branch of the grammar rule `main`, i.e.
```
    | other* "⟪" main  "⟫" main? -- bracketed
```

The above format rule `main_bracketed` has five (5) parameters that hold the captured sub-matches
1. `@other`
2. `lb`
3. `main1`
4. `rb`
5. `@main2`

The names `lb` and `rb` are meant to be reminiscent of `left bracket` and `right bracket`, respectively.

The first parameter `@other` is prefixed with `@` to signify that it corresponds to a repetition grammar sub-match, `other*`. TODO: Currently, the programmer must specify `@` explicitly.  This *could* be automated to glean the corresponence with `other*` directly from the grammar.  As it stands, the programmer is expected to write perfect formatting code and is presented with mysterious commas (`,`) when the format is specified incorrectly.  Cleanup and tightening is expected to be done later.

Likewise, the fifth parameter `@main2` corresponds to another "repetition" grammar sub-match `main?`.  (Ohm-JS defines three (3) repetition operators `+`/`*`/`?`.  See the Ohm-JS documentation.)

# Appendix Example Github
[tbx (toolbox)](https://github.com/guitarvydas/tbx)

See the Makefile, and, `transpiler.tbx`.