# 2022-06-07-Thinking About Language Stacks
The ability of PEG to specify matches of balanced brackets, allows one to think about languages differently, e.g. it is possible to imagine "language stacks" and "transpilers".

Below, a simple grammar in Ohm-JS that skips over anything that isn't a brace bracket...

```
main = matched main?
matched =
  | "{" main "}" -- nested
  | anythingelse -- bottom
anythingelse = !"{" !"}" any
```

