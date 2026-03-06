# 2023-03-27-Debugging Async MessagesA way to debug async is to use a tree of backtraces. Attach the backtrace to each message as a list of cause/effect messages.

A single backtrace of control-flow is not sufficient, we need to see where each message went and what new messages each message caused.

In Lisp (or any language that supports lists), tracking this is easy.  Just tack the causing message onto the end of every message. You automatically get a tree of messages) and then provide a "debugger" to examine the chain of events.

In the interim, emacs "lisp mode" formatting is good enough. Messages and their causes are formatted as recursive lists.  When indented with a pretty-printer, message flow ("backtrace") becomes easier to see.
