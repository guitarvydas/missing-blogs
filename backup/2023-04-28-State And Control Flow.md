# 2023-04-28-State And Control Flow# State and Control Flow

The "problem" with State is that you can do ad-hoc things with it.  State is sometimes needed and the trick is to identify each use-case and to wrap such use-cases in syntax, i.e. not to give programmers access to willy-nilly State, but to give them useful versions of State.  State machines need to keep a State variable (as in Eh).  Wrapping this single use-case into a higher-level syntax (state machine) makes useful use of state without allowing the programmer to do anything-and-everything with state.  Every Leaf proc and every Container proc needs to maintain a persistent State variable.  OTOH, every different Leaf proc instance and every different Container instance will have a unique set of States that are only meaningful in their own context.  A local-only declaration of "`State :: ...`" defines the exact values of the state that are only known to the given machine, yet, those values are stored in the "inherited" slot in Eh.  

The switch statement in a state machine is a boiler-plate that we can elide with syntax.  Interestingly, we can enumerate all of the possible states for that instance of the Component 

Every Leaf and every Component will have a switch boiler-plate in it - which, of course, can then be elided with syntax. 

The idiom "`eh.state = int(State.B)`" can be elided with syntax, such as `next B`".

I kinda like bubbles as syntax to represent States.  One bubble to represent each possible state.

I kinda like curvy arrows as syntax for "`next`" (there's more, but I'll leave it that for now))).

Example: testing-*type*-then-branching is a frequently used control flow paradigm, yet, it can be abused and sprayed throughout code making the code hard to understand.  OO elided this use-case and called it "method dispatch" - the basis of OO.  Control-flow, like State, is too general.  One should strive to create languages that capture useful use-cases of control-flow and State and to wrap syntax around these use-cases.  Giving programmers prefab instead of giving programmers just a bag of nuts and bolts so that they can build anything.
