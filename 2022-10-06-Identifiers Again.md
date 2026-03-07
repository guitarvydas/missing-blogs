# 2022-10-06-Identifiers Again- names containing spaces
- names composed of multiple synonyms
- nested names (recursive)

λ-calculus says that names are superfluous.

Names are meaningful only to human readers.  Machines don't care.

IN elementary school, we learned the equation for the slope of a line `y = mx + b`.  "m" means something to readers in-the-know, whereas other readers might need to see the name "slope".  The equation might be written as `y = slope * x + yintercept`.  Which version should you chose?  Both.  Let the user decide using an IDE.  Tooltips might provide a list of synonyms for each variable.  Let the users augment the list of synonyms to record their own understanding.

Names depend on context.  For example, in the above equation, are we trying to understand the details (using long names), or, are we trying to understand the structure (formula, using single-letter names)?

# How?

Use Unicode to augment the range of characters that can be used.  In the past, we used only ASCII, which provides only 128 choices.  This led to an artificial economy of character choice.

Use Ohm-JS, or PEG or recursive-descent parsing, to implement nesting.

# Proposed
Use Unicode brackets `❲` and `❳` to delimit identifiers.  Like quotes around strings, but with different characters for begin and end.

Use Unicode or-bars `⎟` to specify synonyms.

Special case - allow escaping `⎟` by using `\⎟`.

Special case - allow "old style" identifiers, without spaces, to exist unadorned.

```
identifierWithoutSpaces
❲ identifier containing spaces ❳
❲ identifier with spaces ❲ and recursively nested ❳❳
❲ x ⎟ synonym ❳
❲ x ⎟ Hello World Sequential ⎟ ❲\⎟name containing unicode-or-bars\⎟❳❳
```

# Notes
```
namestring = 
  | "❲" namestringcontainingspaces "❳"
  | notbracketnotspace+

namestringcontainingspaces = 
  | "❲" namestringcontainingspaces "❳"
  | notbracket+

notbracketnotspace =  !space !"❲" !"❳" !"⎟" escapedChar
notbracket =  !"❲" !"❳" !"⎟" escapedChar

escapedChar = 
  | "\" any
  | any
  
namewithsynonyms =
  | "❲" namewithsynonyms "⎟" namestring "❳"
  | "❲" namestring "❳"
  |  namestring
```