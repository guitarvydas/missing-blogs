# 2022-07-16-LCSM Software Components (WP)Working Paper
!![lcsm.png](lcsm_14.png)
# Synopsis
A software component has an interface that contains:
- exactly one *reset* input `☒`
- exactly one *step* input `◻︎`
- any number of message inputs `on ➢❲state❳/❲port❳/❲guard predicate❳`
- any number of message outputs `❲port❳`

# 2 Kinds of LCSMs
1. Leaf
2. Container

A Leaf contains code.

A container contains children LCSMs and a routing table.

A container can route messages:
- from the output of a Child to a set of Receivers
- from the input of itself to a set of Receivers.

# Output Messages
Any LCSM can output messages that contain:
1. an output port name
2. data

Messages are always deferred - they are not sent immediately, but queued up on the LCSM's output queue.  The LCSM's parent Container can route the messages, once the LCSM has finished
# Reset
A Container delegates *reset* to all of it children.

A Leaf executes the exit code for the current state and returns itself to the *default* state.

All inputs are cleared from the input queue.

All outputs are cleared from the output queue.
# Step
When a *step* input is received (called), the LCSM
- checks the *reset* pin and executes a return to the *default* state if it has been commanded to *reset*
- otherwise, if it is not in the *default* state, it performs a single step 
- if it is in the *default* state and if there are more that zero (0) input messages on the input queue, it pulls one input message, marks itself as busy and begins stepping its own code by executing one step of its code
- if it is in the *default* state and there are zero (0) input messages, it does nothing and marks itself as unbusy
# Consuming Input Messages
# Internals
## Handler
## Delegation of Input Messages
## Exit "Stack"
## Input Queue
## Output Queue
## Busy
## Ready
# States
## Default State
## Other States
# Stepping an Input Message
A Container delegates a *step* command to all of its children.

A Leaf begins processing the input message.

If the Leaf is a state machine, the Leaf executes one step of the state machine and returns execution to its Container, awaiting the next *step* command.

If the Leaf is a 1-state state machine (containing only a *default* state), the Leaf processes the message and returns execution to its Container.  Its state is not changed and it remains in the *default* state.
# Guard Predicates
# State Change
When a Leaf changes its state, it:
1. executes the exit function of the current state
2. executes the entry function of the next state
3. sets its own state to the next state.
# Examples
## Comment Stripper
### Python
### Draw.io
## Implementing Functions and Functional Programming

