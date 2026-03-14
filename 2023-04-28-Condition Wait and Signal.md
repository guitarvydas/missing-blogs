# 2023-04-28-Condition Wait and Signal# Condition Wait and Signal
## What Is A Condition?
A *condition* is a queue of processes that are *blocked* waiting for something to happen, i.e. waiting on the Condition.

A *process* blocks itself by calling `wait(...)` specifying which *condition* it is waiting for[^sq].   At the operating system level, *blocking* consists of setting your own State to "blocked" and *yield*ing to the Operating System Scheduler.  The Scheduler runs any process that is in the State "running". All "blocked" processes are ignored by the Scheduler.

[^sq]: Specifying a *condition* boils down to supplying a pointer to a queue.

A process becomes unblocked when some other process *signals* the condition.  This simply sets the process's State to "running".  At some time in the future, the Scheduler will run the process, since it is in the "running" State.

## What Is A Process?
A *process* is a piece of code that is a State Machine, with two States:
1. running
2. blocked.

![](images/Drawing%202023-04-28%2019.02.18.excalidraw.png)

The *blocked* State is only an optimization.  The process *could* enter into a busy-wait loop, burning CPU cycles continuously polling for something to happen.  The optimization is to chop the process into two parts
1. code to run immediately, until the process becomes *blocked*
2. code to run when the process becomes *unblocked*, i.e. a continuation.

This optimization allows the Scheduler to use the otherwise-wasted CPU cycles to run any other process while waiting for the *blocked* process to become *unblocked* - *running* again.

## Blocking and Unblocking

![](images/2023-04-28-Condition%20Wait%20and%20Signal%202023-04-28%2019.21.13.excalidraw.png)


## Condition Queue

![](images/2023-04-28-Condition%20Wait%20and%20Signal%202023-04-28%2019.09.59.excalidraw.png)


## Wait(...)
`Wait(Condition)` causes the process to set its own State to `blocked` and saves a pointer to its own continuation.  The process enqueues itself on the Condition's queue.

## Signal(...)
`Signal(Condition)` causes the Condition queue to be dequeued (once) and the dequeued process's State to be set to `running`.

The Dispatcher will run the process when it gets around to it.

## Who Calls Wait() and Who Calls Signal()?
A process calls `wait()` to block itself.

Some other process calls `signal()` to unblock the process.

The gist of this is that some process wants to do I/O and tells some other sub-process to do the work.  The process then blocks itself, waiting for a signal that the I/O is finished.

The sub-process does the I/O, then it calls Signal to wake up the waiting process.  Then it does nothing more, i.e. it commits suicide[^idle] letting the waiting process to do the rest of the interesting cleanup and messaging work.

[^idle]: Or returns to its *idle* state.

## The Dispatcher

![](images/2023-04-28-Condition%20Wait%20and%20Signal%202023-04-28%2022.08.49.excalidraw.png)
