# 2022-05-28-Multitasking - How It Works

---

tags:
- graphicessay
- concurrency
---
This is a simplified schematic of the operation of multitasking on a single CPU:

## 0. Steady State
In the steady state, the CPU is running code and using a stack.  Which code and which stack?  The Operating System makes sure that these are correctly selected.
![](multitasking-steady-state.png)

## 1. Context Switch Step 1
A context switch from *process A* to *process B* involves several steps.

Step 1 consists of saving the current state of the CPU and labelling it "process A".

There are many ways to do this, the most optimal way depends on the hardware and CPU.

Originally, there was no stack pointer, so everything was done with clever assembler sequences.

CPU vendors have added hardware-assist to their instruction sets, to make context switching easier and faster.

!![multitasking-context-switch-step-1.png](multitasking-context-switch-step-1_16.png)
## 2. Context Switch Step 2

In step 2, we restore the state of *process B*, by overwriting CPU registers (etc.).

!![multitasking-context-switch-step-2.png](multitasking-context-switch-step-2.png)
## 3. Context Switch Step 3
In the final step, *process B* is resumed.

Again, the exact way that this is done depends on the hardware.  

One trick might be to futz with the return address on *process B*'s stack, then `RETURN` to *process B*.  In essence the *return* address is a pointer to the *continuation* of *process B*.

!![multitasking-context-switch-step-3.png](multitasking-context-switch-step-3.png)
