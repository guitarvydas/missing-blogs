# 2022-09-29-Paralleism Simplified - 0D and Scheduling# Parallelism is 2 concepts
1. 0D - creating decoupled units (zero dependency)
2. Scheduling - arranging the units in time.

# 0D
# Scheduling
## Sequential
## Simultaneous
### Parallel
### Concurrent

---


# Parallelism is two concepts.

1. the first is 0D, and,
2. the second is scheduling 

# 0D
0D means zero dependency 

0D is the idea of creating decoupled of units of whatever we are designing.

In Software, we create completely decoupled units of software.

The units cannot refer to each other 
- you cannot hardwire the names of other functions inside of functions 
- you cannot block waiting for functions to return values 
- you can only send messages with some kind of data between units and you do not implicitly wait for an answer 
- if you need to wait for an answer then you perform some sort of synchronization handshake.

# Scheduling
The second concept is called scheduling.

Scheduling breaks down into 2 kinds
1. there is sequential scheduling, and,
2. simultaneous scheduling

## Sequential
Sequential is what we are used to.

Sequential scheduling is the idea of just arranging units to come one after another in time.

## Simultaneous
Simultaneous is what we often call parallel.

Simultaneity breaks down into two kinds of parallelism.

### Parallelism
*Parallelism* is where are the units of software are completely the same and basically run at the same speed, but, result in faster execution when started at the same time 

### Concurrency
Then, there's *concurrency* where are the units contain different kinds of code.

The units all start at the same time, but they'll run at their own speed and finish at different times.

The encapsulating wrapper waits for all of the units to finish work before producing its own summarized result.
