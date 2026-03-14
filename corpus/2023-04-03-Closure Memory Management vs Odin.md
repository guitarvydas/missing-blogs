# 2023-04-03-Closure Memory Management vs Odin
# Odin vs. Closures
>Odin only has non-capturing lambda procedures. For closures to work correctly would require a form of automatic memory management which will never be implemented into Odin.

https://odin-lang.org/docs/faq/

In normal circumstances, a local variable is allocated on The Stack and is automatically disappeared when the procedure returns.  

But, if the local variable is used in a "continuation", then the variable needs to be allocated on the heap (not the stack) and needs to be GCed in some way at some later time.  

Odin's decision to eschew closures punts the issue back to the designer.  

If you want heap-allocated variables, then you have to put them there AND you have to worry about how to get rid of them when the time comes.  

aside: If you continue down this path of reasoning, you conclude that GC is just a big epicycle that is needed to allow mutation (heap-allocated variables) while maintaining a "clean" syntax. IMO, syntax and semantics are 2 separate issues, but, are usually tangled together, resulting in bloatware and complexit).