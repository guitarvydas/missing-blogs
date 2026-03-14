# 2022-05-28-Faking Concurrency
Async and concurrency can be faked on a single CPU through the use of epicycles, but, epicycles cause gotchas (see Mars Pathfinder disaster, thread safety, etc.).

2 separate rPIs connected by a wire are parallel and are async.  Neither one needs faked concurrency nor faked async, but we program them that way anyway.

(See, also, 
## 2022-05-30-Fire and Forget

---
tags:
- graphicessay
- concurrency
- fireandforget
- multitasking
- 0D
- closures

---

# Fire And Forget
![](fireandforget-fire-and-forget.png)

### 2022-06-04-Fire and Forget

Fire-and-forget - most often called "concurrency" and "paralellism" entails two aspects:
- snipping dependencies
- the element of *time*, non-synchronization.

Humans understand *synchronization* at a visceral level.

For example, humans deal with other humans ("Hi, how are you?", "Can you do this for me...?", "I need this by Tuesday") on a daily basis.  

Synchronization is done on an as-needed basis ("give it to me when you're done.")

There is no need to install synchronization into *every* program[^ps].

[^ps]: I call this "pervasive synchronization".

Too much synchronization slows everything down.  

When there is too much synchronization, the slowest player determines the final speed of the result.

[aside: I found Harel's Statecharts to be a brilliantly wonderful idea.  I found Harel's synchronous analysis of Statecharts to be entirely unpractical, because it required all orthogonal states to be fully synchronized and micro-managed.]

The lazy way to analyze the behaviour of a system is to imagine micro-management - every action is synchronized at a very low-level.  Every action, even "concurrent" actions, are imagined to consist of small micro-steps that are fully synchronized with the operation of other actions.  
A less-lazy way to analyze the behaviour of a system is to imagine that it is composed of asynchronous levels (layers).

Example: A Swiss clock contains many interlocking gears, the micro-actions of the clock are completely synchronized with other actions of the clock.  The clock proceeds to tell time based on interlocking micro-actions.  

In the micro-managed model, two clocks are just like one bigger clock - all actions of each clock are completely synchronized and are dependent on each other's micro-steps.

In an async model, the two clocks are completely independent.  The actions of one clock's gears do not affect, do not slow down, the action of the other clock's gears.

# Simultaneity
![](fireandforget-simultaneity.png)

# Faking Multitasking on 1 CPU
![](fireandforget-faking-on-1-cpu.png)
# Anti 0D
Tools that appease the use of dependencies instead of addressing the fundamental problem (getting rid of dependencies).
![](fireandforget-anti-0D.png)
# Execution
![](fireandforget-execution.png)
# Operating System Processes
![](fireandforget-operating-system-processes.png)
# Multiple Single CPUs
![](fireandforget-multiple-single-cpus.png)iple Single CPUs

# Closures
![](fireandforget-closures.png)
)