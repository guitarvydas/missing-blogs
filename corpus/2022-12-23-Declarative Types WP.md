# 2022-12-23-Declarative Types WP
[evolving thoughts]

# Declarative Types Working Paper
A declarative type is a type with a name but no implementation.  

Like a "handle" in some operating systems.

The implementation of the type is punted to the underlying toolbox code.

A dtype can be defined:
- by listing the names of fields
- by listing the symbolic names of values (like an Enum).

The primary goal is to provide all details needed by a dumb machine to understand and work with these objects.  "Readability", especially human readability, is not a goal.

The primary goal is to normalize all access to typed data.  Normalization breeds automatability, whereas non normalization breeds special cases and discourage automatability.

By *implementation*, I mean specification of a field's type, e.g. *int*, *string*, *SomeOtherUserDefinedType*, etc, etc.

# Names - Relative and Absolute
A name is a classical id, or a path.

A path is a list of ids separated by "/".

Paths can be absolute or relative.

Absolute paths begin with "/".

Relative paths do not begin with "/".

A relative path can refer to its parent by using `../`.  A relative path can be prefixed by `./` which is like a no-op and means "relative to here"

Any id can be
- classical - a string of characters containing no whitespace
- bracketed - a list of ids (recursive) contained in matching brackets `❲` and `❳`.

# atoms:
string literal - a string of characters bracketed by `“` and `”` which can contain escaped chars `\“` and `\”` and `\/`
number literal - a string of digits 0-9
dtype
id - quoted name
@symbol - evaluated name

Note that a character literal is just a degenerate, 1-character string literal.  Let the compiler figure out how to optimize character literals, if appropriate.

# defining dtypes

Dtypes are defined using the `defdtype` command.
```
defdtype ⟨char dd⟩
defdtype ⟨dd k b index source⟩
defdtype ⟨dd* dd index⟩
defdtype ⟨yesno 'yes 'no⟩
```

Note that `dd*` is just a name (without whitespace).  The 3rd definition says that there exists a dtype called `dd*`
that contains two fields `dd` and `index`.  In this case, `dd*` is meant to represent a collection (list) of data descriptors, indexed by the field `index`

To define an enum-like dtype, prefix each field name with `'`, like in the 4th definition.

According to the above syntax, it would be possible to rewrite the fourth definition as:
```
defdtype ⟨❲yes no❳ 'yes 'no⟩
```
or
```
defdtype ⟨./❲yes no❳ 'yes 'no⟩
```

# using dtypes
```
⟨char ⟨dd 1 param "c"⟩⟩
⟨yesno yes⟩
⟨yesno no⟩
⟨yesno @x⟩
```

Fields of a dtype usage are atoms.  Fields are literals, except when prefixed by `@` in which case they are evaluated.

