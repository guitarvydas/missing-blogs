# 2022-07-31-Hierarchical Messages
A Message is
1. a datum
2. a Message that wraps another Message


Akin to network protocol layers where a packet is wrapped by header and trailer information which is unpacked at certain levels.

![hm-network protocol.png](images/hm-network protocol.png)




An alternate view of a hierarchical message might be to imagine each port as a wrapper

![hm-hm.png](hm-hm.png)

[Disclaimer: I imagine that Messages could be wrapped to any degree, but, my drawing skills prevent me from showing more than 2 ports]