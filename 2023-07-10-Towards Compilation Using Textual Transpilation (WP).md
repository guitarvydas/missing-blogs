# 2023-07-10-Towards Compilation Using Textual Transpilation (WP)
## Working Paper - Towards Compilation Using Textual Transpilation
Working paper - details subject to change...

Working on: converting Odin source code to Common Lisp source code.

## Odin Code
Expected textual manipulation of Odin source code, one step in converting it to Lisp: (see legend below)

```
// Clones the datum portion of the message.
c :: proc(m: Message) -> any {
    /*scopedvar*/ y := h(i)
}
```

## Annotated Pseudo Code

```
--->
```

```
⦚
❲c❳ :: ‹proc› (❲m❳ ) {
⇢
⎧
‹scopedvar›・❲y❳・⟪:=⟫・❲h❳(❲i❳)⦚
⎭
⇠
}
```

## Partially Processed Pseudo Code Containing Some Common Lisp

```
--->
```

```
⦚
❲c❳ :: ‹proc› (❲m❳ )⇢ {
⎧
  (let ((❲y❳ nil))
  ⇢
  ・❲y❳・⟪:=⟫・❲h❳(❲i❳)⦚
    ⇢
    ⎧
    ⇠
    ⎭
  ⇠
  ⎭
)
⇠
}
```

## Legend
`❲c❳` symbol ("c")
`‹proc›` keyword symbol ("proc")
`・` space in original source code
`⦚` newline in original source code
`⟪:=⟫` multiple character operator (":=")
`⇢` formatting command: indent
`⇠` formatting command: dedent
`⎧` edit command: begin edit scope selection (called "narrowing" in emacs)
`⎭` edit command: end edit scope selection

## Notes

- We probably want to differentiate between *semantic* scopes and *edit* scopes, but, I don't want to go down that rathole yet.

- At this point we don't care about human readability, we just want to make sure that we've included enough information for the machine to do its job for us.  We can use various syntaxes to elide machine details and to make the code more human-readable.

- Odin allows nested comments of the form `/* ... /* ... */ ... */`.

- Each *semantic scope* is specified by a *name* and an abstract *kind*.

- Each *scopedvar* declaration includes the name of the enclosing scope and the name (if any) of the variable

- Clearly, using Odin comments as pragmas is not ideal.  A proper uber-language would use keywords / Unicode characters.  The uber-language would then be mapped to other languages, like Odin, Python, etc.

Something like the following.  Odin code annotated with pragmas:
```
c :: proc(m: Message) -> any {
  /*/*beginsemanticscope*/ c proc */
  /*/*scopedvar*/ c y */
  y := h(i)
  /*/*endsemanticscope*/ c */
}
```

The above is nestable, so a scope within a scope might be:
```
c :: proc(m: Message) -> any {
  /*/*beginsemanticscope*/ c proc */
    /*/*scopedvar*/ c y */
    y := h(i)
    z = 7
    /*/*beginsemanticscope*/ c.2 proc */
      /*/*scopedvar*/ c.2 x */
      x := f(g)
    /*/*endsemanticscope*/ c.2 */
  /*/*endsemanticscope*/ c */
}
```

- Being very, very explicit about various kinds of scoping[^other] makes it possible to build a compiler using only text transpilation, i.e. source-to-source rewriting, e.g. using REGEXs or Ohm-JS or ...

[^other]: and, probably other items

- More information about each variable is required (e.g. allocation, freeing, etc.), but, I haven't gone down that rathole yet.

- hmmm, maybe *semantic scopes* subsume *edit scopes* and make *edit scopes* unnecessary?

- a 0D pipeline could be used to compile all of the above
	- where each component in the pipeline contains a recursive text-processor, like Ohm-JS
	- I don't think that REGEX is good enough, since it is not inherently recursive

- I picked a more human-readable syntax for the above, to aid in debugging
```
c :: proc(m: Message) -> any {
  /*❪⎧ c proc ❫*/
    /*❪+ c y ❫*/
    y := h(i)
  /*❪⎭ c ❫*/
}
```

```
c :: proc(m: Message) -> any {
  ❪⎧ c proc ❫
    ❪+ c y ❫
    y := h(i)
  ❪⎭ c ❫
}
```

```
c :: proc(m: Message) -> any {
❪⎧ c proc ❫
  ⇢
    (let ((y nil))
    ⇢
      y := h(i)
    )
    ⇠
  ⇠
❪⎭ c ❫
}
```

```
c :: proc(m: Message) -> any {
      ⇠
 c proc ❫
  ⇢
    (let ((y nil))
    ⇢
      (setf y (h i))
      )
    ⇠
  ⇠
  ❪⎭ c ❫
}
```

## July 11, 2023
- change verbatim characters from `` to ``
- drop manual scope begin and end annotations
- tokenizer recognizes annotations in the same way it recognizes comments, but annotation cannot contain comments and are recognized after comments
```
c :: proc(m: Message) -> any {
  /*❪⎧ c proc ❫*/
    /*❪+ c y ❫*/
    y := h(i)
  /*❪⎭ c ❫*/
}
```

```
c :: proc(m: Message) -> any {
  ❪⎧ c proc ❫
    ❪+ c y ❫
    y := h(i)
  ❪⎭ c ❫
}
```

```
c :: proc(m: Message) -> any {
❪⎧ c proc ❫
  ⇢
    (let ((y nil))
    ⇢
      y := h(i)
    )
    ⇠
  ⇠
❪⎭ c ❫
}
```

```
c :: proc(m: Message) -> any {
      ⇠
 c proc ❫
  ⇢
    (let ((y nil))
    ⇢
      (setf y (h i))
      )
    ⇠
  ⇠
  ❪⎭ c ❫
}
```

