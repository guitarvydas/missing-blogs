# 2023-08-01-Rules of Message Passing# Rules of Message Passing

I think that the following cases need to be addressed, when thinking about Message Passing.

![](images/2023-08-01-Rules%20of%20Message%20Passing%202023-08-02%2006.31.45.excalidraw.svg)
In the last case, bugs will happen if C and D don't see all messages in exactly the same order.

For example, if
1. A sends a message
2. B sends a message
3. A sends another message,
then, C and D should, both, see `aba` in their input queues.

If fact, race conditions might happen if A and B fire messages too rapidly for the hardware/software to differentiate.  Again, both receivers C and D should see *exactly* the same stream of messages, e.g.
- `aab`, or
- `baa`,
- etc.

Subtle bugs will occur if C and D see different sequences of events, e.g. if C gets `aab` while D gets `aba`.

We can prevent this problem under-the-hood, if all of the Components, A, B, C, and, D are "close together" physically and, if the extra work needed is "not noticeable" by Users (and Developers).  It becomes much harder to prevent this problem - efficiently and generally - if the Components are physically spread out, e.g one Component in Toronto, one in L.A., one in Paris and one in London, where propagation delays and latencies become noticeable to Users.  And, when the hop count changes for each message send. In such cases, it is better to tune the prevention fix to fit the application.  Things like timestamps and sequence numbers have been tried, but a one-size-fits-all general solution does not exist.  Of course, the problem gets even worse when we begin to travel to other star systems and Relativity effects become noticeable.  I think that Dave Ackley's work is beginning to address Relativity in DPU[^dpu] communication.

[^dpu]: DPU ≡ Distributed Processing Unit, instead of Central Processing Unit (CPU).



## Locking and Timing

![](Rules%20of%20Message%20Passing.pdf)


### Async
## Structured Message Passing

https://publish.obsidian.md/programmingsimplicity/2022-08-09-Structured+Message+Passing

### Up and Down but Not Sideways
#### Down
#### Up
#### Faking Sideways Messaging (Peer to Peer)
For flexibility, just don't do this.  If you want to send a message to a peer, send it up to your parent and let the parent route the message.

In extreme cases, one might wish to optimize peer to peer sending at the expense of flexibility.  In such cases, a Production Engineer might tweak the system to allow direct peer to peer sending, but that invites design problems (inflexibility, calcification) that should not be encouraged in early stages of design.

Such optimizations should not be the default, but should only be applied when measurements prove that a system needs to be more efficient, and that adding peer to peer Message Sending would increase system efficiency.

# Appendix - Working Notes
https://kinopio.club/shell-gazelle-4D437fB--BloDN3Nemz9U
