# 2023-10-15-Examining Dynamic Program Structure
## Examining Dynamic Program Structure

The execution `make dev` of the `find-and-replace` program dumps the dynamic structure of the program in "Lisp format". The dump can be pretty-printed by a Lisp pretty printer (in my case Emacs lisp-mode's "indent-region" command). This formatted version shows the live relationships between components. We use `◦1` syntax to uniquely identify component instances. Components can be used multiple times in a Design, then the components are instantiated at runtime, with each instance being assigned a unique ID.

```
(main
(Front End
(Delineate Words
(word◦1)
(Transpiler
(All Before 4
(deracer◦2)
(deracer◦3)
(deracer◦4))
(OhmJS◦5)
(fakepipe
(deracer◦6)
(fakepipename◦7)
(syncfilewrite2◦8)
(deracer◦9)
(trash◦10))
(fakepipe
(deracer◦11)
(fakepipename◦12)
(syncfilewrite2◦13)
(deracer◦14)
(trash◦15)))
(wordjs◦16)
(word◦17))
(Escape Whitespace
(escapesohm◦18)
(escapes◦19)
(escapesrwr◦20)
(Rewriter
(Transpiler
(All Before 4
(deracer◦21)
(deracer◦22)
(deracer◦23))
(OhmJS◦24)
(fakepipe
(deracer◦25)
(fakepipename◦26)
(syncfilewrite2◦27)
(deracer◦28)
(trash◦29))
(fakepipe
(deracer◦30)
(fakepipename◦31)
(syncfilewrite2◦32)
(deracer◦33)
(trash◦34)))
(rwr◦35)
(rwrohm◦36)
(rwrsemjs◦37)
(Read Text File
(Low Level Read Text File◦38)
(Ensure String Datum◦39))
(Transpiler
(All Before 4
(deracer◦40)
(deracer◦41)
(deracer◦42))
(OhmJS◦43)
(fakepipe
(deracer◦44)
(fakepipename◦45)
(syncfilewrite2◦46)
(deracer◦47)
(trash◦48))
(fakepipe
(deracer◦49)
(fakepipename◦50)
(syncfilewrite2◦51)
(deracer◦52)
(trash◦53))))))
(?◦54)
(Read Text File
(Low Level Read Text File◦55)
(Ensure String Datum◦56))
(Finalize
(Decode
($rt/decode.js))
(Cleanup
($rt/cleanup.js)))
(Back End
($m4 fr/find.ohm)
(find◦57)
(iRewriter
(nulltester◦58)
(rwr◦59)
(rwrohm◦60)
(rwrsemjs◦61)
(Transpiler
(All Before 4
(deracer◦62)
(deracer◦63)
(deracer◦64))
(OhmJS◦65)
(fakepipe
(deracer◦66)
(fakepipename◦67)
(syncfilewrite2◦68)
(deracer◦69)
(trash◦70))
(fakepipe
(deracer◦71)
(fakepipename◦72)
(syncfilewrite2◦73)
(deracer◦74)
(trash◦75)))
(Transpiler
(All Before 4
(deracer◦76)
(deracer◦77)
(deracer◦78))
(OhmJS◦79)
(fakepipe
(deracer◦80)
(fakepipename◦81)
(syncfilewrite2◦82)
(deracer◦83)
(trash◦84))
(fakepipe
(deracer◦85)
(fakepipename◦86)
(syncfilewrite2◦87)
(deracer◦88)
(trash◦89)))
(Read Text File
(Low Level Read Text File◦90)
(Ensure String Datum◦91))
(stringconcat◦92))
($m4 fr/find.rwr)
(find◦93)))
```

```
(main
 (Front End
    (Delineate Words
           (word◦1)
           (Transpiler
            (All Before 4
             (deracer◦2)
             (deracer◦3)
             (deracer◦4))
            (OhmJS◦5)
            (fakepipe
             (deracer◦6)
             (fakepipename◦7)
             (syncfilewrite2◦8)
             (deracer◦9)
             (trash◦10))
            (fakepipe
             (deracer◦11)
             (fakepipename◦12)
             (syncfilewrite2◦13)
             (deracer◦14)
             (trash◦15)))
           (wordjs◦16)
           (word◦17))
    (Escape Whitespace
        (escapesohm◦18)
        (escapes◦19)
        (escapesrwr◦20)
        (Rewriter
         (Transpiler
          (All Before 4
               (deracer◦21)
               (deracer◦22)
               (deracer◦23))
          (OhmJS◦24)
          (fakepipe
           (deracer◦25)
           (fakepipename◦26)
           (syncfilewrite2◦27)
           (deracer◦28)
           (trash◦29))
          (fakepipe
           (deracer◦30)
           (fakepipename◦31)
           (syncfilewrite2◦32)
           (deracer◦33)
           (trash◦34)))
         (rwr◦35)
         (rwrohm◦36)
         (rwrsemjs◦37)
         (Read Text File
               (Low Level Read Text File◦38)
               (Ensure String Datum◦39))
         (Transpiler
          (All Before 4
               (deracer◦40)
               (deracer◦41)
               (deracer◦42))
          (OhmJS◦43)
          (fakepipe
           (deracer◦44)
           (fakepipename◦45)
           (syncfilewrite2◦46)
           (deracer◦47)
           (trash◦48))
          (fakepipe
           (deracer◦49)
           (fakepipename◦50)
           (syncfilewrite2◦51)
           (deracer◦52)
           (trash◦53))))))
 (?◦54)
 (Read Text File
       (Low Level Read Text File◦55)
       (Ensure String Datum◦56))
 (Finalize
  (Decode
   ($rt/decode.js))
  (Cleanup
   ($rt/cleanup.js)))
 (Back End
       ($m4 fr/find.ohm)
       (find◦57)
       (iRewriter
    (nulltester◦58)
    (rwr◦59)
    (rwrohm◦60)
    (rwrsemjs◦61)
    (Transpiler
     (All Before 4
          (deracer◦62)
          (deracer◦63)
          (deracer◦64))
     (OhmJS◦65)
     (fakepipe
      (deracer◦66)
      (fakepipename◦67)
      (syncfilewrite2◦68)
      (deracer◦69)
      (trash◦70))
     (fakepipe
      (deracer◦71)
      (fakepipename◦72)
      (syncfilewrite2◦73)
      (deracer◦74)
      (trash◦75)))
    (Transpiler
     (All Before 4
          (deracer◦76)
          (deracer◦77)
          (deracer◦78))
     (OhmJS◦79)
     (fakepipe
      (deracer◦80)
      (fakepipename◦81)
      (syncfilewrite2◦82)
      (deracer◦83)
      (trash◦84))
     (fakepipe
      (deracer◦85)
      (fakepipename◦86)
      (syncfilewrite2◦87)
      (deracer◦88)
      (trash◦89)))
    (Read Text File
          (Low Level Read Text File◦90)
          (Ensure String Datum◦91))
    (stringconcat◦92))
       ($m4 fr/find.rwr)
       (find◦93)))
```


## See Also
### Blogs
[blog](https://guitarvydas.github.io/)

[obsidian blogs](https://publish.obsidian.md/programmingsimplicity) (see blogs that begin with a date 202x-xx-xx-)
### Videos
[videos - programming simplicity playlist](https://www.youtube.com/@programmingsimplicity2980)
### Books
leanpub'ed (disclaimer: leanpub encourages publishing books before they are finalized - these books are WIPs)
[Programming Simplicity Takeaways, and, Programming Simplicity Broad Brush](https://leanpub.com/u/paul-tarvydas)
### Discord
[Programming Simplicity](https://discord.gg/Jjx62ypR) all welcome, I invite more discussion of these topics, esp. regarding Drawware and 0D
### Twitter
@paul_tarvydas
### Mastodon
(tbd, advice needed re. most appropriate server(s))

<script src="https://utteranc.es/client.js" 
        repo="guitarvydas/guitarvydas.github.io" 
        issue-term="pathname" 
        theme="github-light" 
        crossorigin="anonymous" 
        async> 
</script> 
