# 2023-03-21-Brackets from ASCII to Unicode# Brackets

In ASCII there are but four (4) kinds of bracket pairs:
- `()`
- `{}`
- `<>`
- `[]`

This situation has led to programming language epicyles, such as strings that use only single-character delimiters, e.g. `"` or `'`, instead of matching pairs.

This situation can be easily corrected by using Unicode instead of ASCII, although some systems are built only for ASCII.

In situations where ASCII is hard-wired deeply into code, we can use double-characters to extend the set of available brackets, e.g.

- `<' ... '>` for matching string delimiters.  The beginning of a string is denoted by `<'` and the end of a string is delimited by `'>`.  The unicode equivalents are `“` and `”` (`\u201C` and `\u201D` in unicode, or, `%E2%80%9C` and `%E2%80%9D` in URL, respectively).  See http://xahlee.info/comp/unicode_index.html) 
- `<< ... >>` for matching small double brackets (`\uAB` and `\u8B`, or, `%C2%AB` and `%C2%BB`)
- `{{ ... }}` for matching large double brackets (`\u27EA` and `\u27EB`, or, `%E2%9F%AA` and `%E2%9F%AB`)
- `[[ ... ]]` for identifiers containing whitespace (`\u2722` and `\u2773`, or, `%E2%9D%B2` and `%E2%9D%B3`)

The use of matching brackets makes it possible to define nested items, like nested strings.  PEG pattern-matching technologies ("parsers") can match nested constructs.  

This allows definition of new kinds of programming languages, for example:
- languages that allow recursive, tree-structured syntax, 
- languages that allow nested strings,
- languages that allow snippets of nested *verbatim* code,
- etc.

Languages with recursive, tree-structured syntax allow layering of code using the Rule of 7.

# Table
|Unicode|ASCII synonym|ASCII synonym|HEX|URL|
|- |-- |-- |----- |--------- |
|‛|<'|@'|\u201B|%E2%80%9B|
|’|'>|'@|\u2019	|%E2%80%99|
|“	|<"	|@"|\u201C		|%E2%80%9C|
|”	|">	|"@|\u201D		|%E2%80%9D|
|« 	|<<	|@<	|\uAB		|%C2%AB|
|» 	|>>	|>@    	|\u8B		|%C2%BB|
|⟪	|{{	|@{    	|\u27EA		|%E2%9F%AA|
|⟫	|}}	|}@	|\u27EB		|%E2%9F%AB|
|❲	|[[	|@[	|\u2722		|%E2%9D%B2|
|❳	|]]	|]@	|\u2773		|%E2%9D%B3|
|λ	|@L	|@l	|\u39B		|%CE%9B|
|ϕ	|@@ |		|\u396		|%CE%A6|
|ė	|@E	|@e	|\u116		|%C4%96|

# Alternates
To avoid collisions with existing - intermediate - technologies, like Shopify's Liquid, synonyms are allowed.  See above.
