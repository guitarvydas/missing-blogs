# 2022-07-30-Hierchical State Machine Example
# Use-Case - A Hierarchical State Machine to Control a Desk Lamp
Here’s how I think about state machines, very much based on Harel’s StateCharts.

---

# Lamp
The Problem To Be Solved:

- The Lamp has 3 toggle buttons
1. power (pwr) - toggles the lamp on and off
2. brightness - toggles the brightness of the lamp, when it is turned on
3. color - toggles the colour of the lamp when the lamp is turned on

---
# Brightness

- the lamp can be “dim”, “MID” and “HIGH” brightness

---
# Color
The lamp can be
- yellow
- green
- red

 ---
# Lamp Operation

When the lamp is turned ON, it is always in the “dim”, “yellow” state, regardless of what its previous settings were.

When the brightness is changed, the lamp always goes to the “yellow” color.

When the lamp is turned off, it forgets all of its settings.

---

# Disclaimer  

There might be better ways to define the operation of the Lamp, but this is what I chose for this example.

I tried to make this example as uncluttered as possible.

More details can be added later.

---
# Legend

In my drawings:
- a state is represented by an oval
- a default starting point is represented by a circle that points to the starting state
- a transition is defined by an arrow labelled with the button that it reacts to (power, brightness, color)
- a state containing other states is shown as an oval with a drop-shadow
- parallel states are not supported in this notation
	- parallel states are supported by a different notation (Components) 

---

# Design Sketches  
due to the limitations of my drawing tool 

1. I first show the state machine as a single flat diagram
2. I, then, collapse all of the substates and wrap them in their containing states

In general, flatness is bad, especially when the use-case is more complicated.
- Flatness leads to the "state explosion" problem.
- Harel's StateChart notation conquers the "state explosion" problem.
- HSM notation is based on Harel's StateChart solution.

Substates allow layering of concerns.

---
# Overriding

A parent's transition always overrides a child's transition.

This is opposite to the notion of *inheritance*.

---

# Overriding - Common Sense and 0D
You can look at a diagram and understand what it will do - a child state cannot affect a parent state, 

- ie. 0D behaviour.

Adding children can off-load work from the Parent, but cannot change the behaviour of the Parent.

---

# Overriding - Example
Example: The top-most state of the lamp is "off" or "on".  

When the lamp is switched from "on" to "off", all children machines are reset regardless of what state they are in.

---

# History
The Design might be better if the lamp remembered its previous brightness and its previous colour.

See Harel's *history* notation in his StateCharts paper, for how this might be done.

But, I chose not to implement *history* in this example, to keep things simple.

---
# Top Level Lamp

![](images/hsm-Lamp 0.png)

The Lamp has 3 toggle buttons
1. power (pwr) "on" and "off"
2. brightness "dim", "mid", "high" (3rd press goes back to "dim")
3. color "yellow", "green", "red" (3rd press goes back to "yellow")
---
# Flat Diagram
![](hsm-Lamp.png)

This diagram reads from Left to Right.

The top-most machine can be in 2 states
1. '?' (the default)
2. "ON".

The "ON" state contains another state machine which toggles the brightness of the lamp ("dim", "MID", "HIGH").

Each substate contains another state machine to toggle the colour of the lamp.

The 3 "colour" sub-machines are similar to one another.  We would like to have an editor / notation that allows for DRY (Don't Repeat Yourself).  DRY behaviour is provided in current programming languages using subroutines, which are simply ways to group similar text together to avoid Repeating Oneself.  Ideally, the DRY operation would be supported by the editor (suggestion: make 2 of the 3 copies "grayed out", leaving the 1 non-grayed-out machine be the "prototype".  Make all edits to any of the sub-machines be reflected in the prototype, or, prohibit editing any of the grayed-out copies.  The MVC model could be put to use here, in the editor.


---
# Collapsed Diagram

![](images/hsm-Lamp 2.png)