# 2023-04-29-Loop Until... WIP for discussion ...

A State does a bit of work, then *yields* to the Dispatcher.

The *yield* at the end of State code is built-in.

There is a case where we wish to test a condition and proceed if the condition is met, and *yield* otherwise.  Essentially, this kind of State becomes 2 States - test then *yield* or *continue*.

We want this split to work even if the code executes some long-running process.  We want to set up the long-running process, and *yield* immediately without waiting for the long-running process to finish.  When finished, we want to run the *continuation* code.

In the bowels of UNIX, this is called `fork()`.  Fork immediately returns a status.  Basically the statuses are:
1. this is going to take a while
2. proceed, run the continuation.

In UNIX, (1) is a non-zero PID, while (2) is the value 0.  It is expected that the parent code executes a `wait` for the PID and after waiting, to execute the continuation code.

![Excalidraw/retry-2023-04-29-0705.png](retry-2023-04-29-0705.png)

In JavaScript, this kind of fork is represented by an async function that takes another function argument as its continuation.

In fact, this is a set of *asynchronous* operations and should not be expressed in a *synchronous* manner. HSMs are *synchronous* and, hence, cannot capture what is going on here.

Instead, we rewrite the code as three 0D components:

![Excalidraw/retry0d-2023-04-29-0705.png](retry0d-2023-04-29-0705.png)


```
TIMEOUT :: 1 * time.Second

leaf_setup :: proc(eh: ^Eh, msg: Message(any)) {
    fmt.println(eh.name, "/", msg.port, "=", msg.datum)
    data := Sleep_Data {
        init = time.tick_now(),
        msg  = msg.datum.(string),
    }
    send (eh, "output", data)
}

leaf_retries :: proc (eh: ^Eh, msg: Message(any)) {
    data := msg.datum.(Sleep_Data)
    elapsed := time.tick_since(data.init)
    if elapsed < TIMEOUT {
        send (eh, "retry", data)
    } else {
        send (eh, "output", data)
    }
}

leaf_continue :: proc (eh: ^Eh, msg: Message(any)) {
    data := msg.datum.(Sleep_Data)
    send(eh, "output", data.msg)
}
```

## The Test

Will two copies of the Component work asynchronously and run their respective continuations ASAP?  I *think* that the only thing preventing this from work at the moment, is that simplified 0D scheduler which is depth-first and will stall waiting for the first retry to finish.  

I *think* that putting `step ()` back into the scheduler will cause this system to run as expected, with the continuations running as soon as possible.

![Excalidraw/retry0dtwice-2023-04-29-0705.png](retry0dtwice-2023-04-29-0705.png)

This hasn't been tested yet.  I might be missing something obvious...
