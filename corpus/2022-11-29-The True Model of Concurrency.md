# 2022-11-29-The True Model of Concurrency
The model for True Concurrency is the use of 1 CPU per Thread.

Any implementation that uses fewer CPUs than Threads has to fake-out concurrency.  

Faking-out concurrency on synchronous (Call-Return-based) architectures leads to epicycles and to danger.  

Trying to force-fit mutation and heaps onto such models results in even more epicycles and more danger (see "Mars Pathfinder" disaster ; refer to the epicycles called "Thread Safety", "Priority Inheritance", etc.)

Faking-out concurrency using FIFO-based components is, at least, closer to the True Model of Concurrency.

Using FIFO-based components to write IoT, Robotics, blockchain, internet, etc., etc. apps, models the reality of those kinds of apps.

Thinking this way was considered insane in the 1950s, but, is quite possible in 2022++ (cheap rPIs and Arduinos, cheap memory).