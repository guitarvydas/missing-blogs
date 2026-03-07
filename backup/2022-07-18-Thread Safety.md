# 2022-07-18-Thread SafetyThread Safety is only an issue when shared memory is allowed.

Thread Safety means that 
- multiple processes can share memory
- multiple processes can share memory safely, without altering each other's version of the shared memory


# Old Model Of Computing
In the mid-1900s,
- CPUs were very expensive
- Memory was scarce and expensive.

It made sense to "optimize" software techniques and software languages to preserve such scarce resources.

For example, the concept of GC - Garbage Collection - was invented to allow reclaiming memory, and to reuse memory in different processes.

Kinds of GC:
- Biblical Flood
	- Explored in UNIX® and other operating systems
	- Explored in the C programming language.
	- Wipe memory after use, reuse the same memory in other processes.
- Malloc/Free
	- Explored in the C programming language
	- K&R C manual.
	- manual management, programmer codes calls to malloc() and free()
- Mark and Sweep
	- Early Lisps
- Generational
	- Smalltalk

## Fragmentation
Epicycle caused by re-using memory.

Expend CPU cycles to coalesce chunks of memory.  

Two adjacent chunks are coalesced into a single larger chunk.

Applied recursively across all memory, the goal being to coalesce all unused memory into a single chunk.

Unused chunks of memory are chained together using a linked list.  (N.B. an array is an optimized linked list, where the the CDR of linked list cells is not needed because items are stored contiguously in memory.)
## Access Speed Hierarchy
Access to memory, by the CPU, is governed by the electrical distance of the memory from the CPU.

### Registers
Registers are small pieces of memory that are physically "very close" to the CPU.  Electrons need to travel only a short distance to reach registers.

### RAM
RAM - Random Access Memory - is memory that is further away from the CPU, but is accessible fairly quickly.

Electronic design of RAM is such that quick access to RAM is enabled,
- e.g. RAM is accessed via 2 buses
	1. the *address bus* sets up the index for accessing (addressing) RAM locations
	2. the *data bus* holds the value at a given location in memory and presents this value to the CPU (for reading or for writing)
#### Bus Width
It takes longer to access memory in a serial fashion than in a parallel fashion.

Memory access speed is improved by adopting parallel access methods.

For example, all bits of an address are presented in parallel
- one wire for each bit of the address

For example, all bits of a value are presented in parallel
- one wire for each bit in the value(s).
- for example, a *byte* value requires 8 wires
- optimizing wiring, so that only one wire is used ...
	- requires serialization and results in slower access time
	- each bit of an address/value must be presented in a *time window* in serial
		- e.g. the first time slot presents the lowest (highest) address/data bi, then the second time slot presents the next address/data bit, and so on.
		- time slots must be stacked in series, the total time taken being the length of the stack
#### Endianess
The word derives from "end".

Which "end" of an address/value is presented first in a serial scheme.

CPUs are electrically designed to access memory in a certain order.  The order is designed-in by hardware engineers.  Designs that access the lowest bit first are called "little Endian", designs that access the highest bit first are called "big Endian".

#### Settling Time
When you slam a digital signal (a 1 or a 0) onto a bus, the electrical signal tends to vibrate first, then settle down.

The time that it takes for the signal to settle down to a reliable value is called the "settling time".

Hardware manufacturers of ICs and digital devices, guarantee a certain settling time for signals.  Manufacturers document these guarantees, often as tables in the documentation of the devices.

##### Debounce Time
"Debounce" is another word for "settling time".  

"Debounce" is often used to describe the algorithms used to read data from physical devices, such as keyboards.

For example, when you hit the letter "j" on a keyboard, the data does not appear instantly on the wire from the keyboard.  It takes a certain amount of time (milliseconds, microsecond, nanoseconds) for the letter to appear as a steady value.

Settling time is not always the same.  Some electrical signals settle down more quickly than others.  The best that a manufacturer can do is to guarantee the worst-case settling time for their products.

Example: imagine a key on a computer keyboard.  When you press the key, a flap of metal is squished down and makes contact with another piece of metal.  The movable flap may bounce around a few times, after being moved (pressed down by the keystroke), then the flapping settles down and a reliable connection is made.  As the flap bounces, the connection appears to go from 0 to 1 back to 0, and so on.

Over time, we humans have discovered ways to make the flapping take less time and how to squish electrical connections into smaller-and-smaller spaces (aka "miniaturization").

We continue to seek tricks that make it cheaper to mass produce electrical switches that have smaller footprints and the smaller settling times.

##### Dust

As we make electrical connections smaller, particles, such as dust, loom as larger problems to be contended with.

If a transistor is built to be 10cm by 10cm, then dust doesn't affect the transistor.  Dust particles are very much smaller than the (large) transistor.

As we try to shrink transistors, the size of dust particles begins to matter.  For example, if the parts of a transistor are about the same size as dust particles, then a single dust particle might fall into the transistor and short it out.

When we shrink transistor designs to make them smaller than dust particles, it becomes important to keep dust away from the transistors.  This matters most during manufacturing, when the insides of transistors are exposed to the surrounding air.  As part of the manufacturing process, we tend to encase transistors in plastic.  The casing tends to shield the finished products from dust in the air.  Unfinished products, though, need to be built in "clean rooms" where expensive filters are used to keep dust away from the exposed innards of electronic devices. 

##### 20 Milliseconds
In the early days of computing, it was discovered 
- that humans perceived settling times less than 20 milliseconds as "instantaneous"
- that humans perceived settling times longer than 20 milliseconds as "sluggish"

##### Cost of Debouncing
It is cheaper to make hardware that has long settling times.

To shorten settling time, designers need to resort to design tricks and technologies that are more expensive than long settling-time designs.

#### Address Width
A 16-bit CPU uses 16 wires for dropping addresses onto the address bus in parallel.

A 64-bit CPU uses 64 wires.

Obviously, the number of wires affects the pin-out of CPU ICs.  The number of pins on the outside of an IC is determined by the bus widths supported by the CPU.

4-bit CPUs (e.g. 4004) require fewer pins than 8-bit CPUs.

8-bit CPUs require fewer pins than 64-bit CPUs.

And so on.

#### Data Width

The width of the data bus - the number of wires allocated to a piece of data - also affects the final pin-out of CPU ICs.

A byte-oriented 16-bit CPU needs 16 wires for addresses plus another 8 wires for data values.  That's 24 wires (pins) plus whatever other wires are needed by the CPU, e.g.
- 1 wire for +ve power
- 1 wire for ground
- at least 1 wire for the WRITE signal
- probably 1 (or more) wire(s) for hardware interrupts
- 1 wire for RESET
- etc., etc.

Early CPU ICs were fairly small, having only some 30+ pins (connections) on them.

Later, CPU ICs became larger, and more compact, as wider buses were accomodated.

As the bus widths increased, the number of pins increased and the need for "miniaturization" increased.

It used to be possible for hobbyists to wire-up early CPUs using soldering irons without leaving blobs of solder between pins that would short them out.  Now, more precision is required to wire-up pins on CPUs and early techniques, such as hand-held soldering irons, don't work very well.

The tips (the hot end) of soldering irons became smaller and smaller as the number of pins on CPUs increased, until other techniques, such as wave soldering, and soldering stations with magnifying glasses, were needed.  These techniques tend to be too expensive for hobbyists to use when building one-off devices, and, tend to be cost-effective only in mass-production situations.
### Tape, Drums, Disk
It was found that digital signals could be persisted as magnetic blips in chemical compounds called "oxides".

The magnetic blips could be read back by moving the oxide material across a magnetic pickup called a "read head".

At first, oxides were painted onto long strips of plastic - tapes.  Larger, then smaller and smaller (reel-to-reel, cassettes, DAT, 8-Track).

Then, we started painting the oxides onto circular platters.  The read heads were positioned in fixed places and the platters were rotated past the read heads so that the magnetic blips could be read back.

Then, the read heads were placed onto movable arms (disk arms) and platters were stacked to increase the density of information available in single rotations of the platters.

Disk "file systems" were invented to read and write information on the oxides on the platters.

As tricks and techniques were invented to make disks smaller and smaller, gotchas appeared in the form of dust particles.  Dust on platters could obscure information and limited the distance from the read heads to the platters (the closer the read heads were to the oxides, the less power (cheaper) was needed to make the contraptions work).

### Physical Disk Problems
Physical read heads and spinning platters had problems, such as:
- occassionally, the distance between read heads and the platters could not be maintained and the heads would physically scratch the oxide off of the platters ("head crash")
- dust - small dust particles could obscure huge amounts of data, especially as more infomration was packed into smaller spaces
- physical motion (hit) - if a disk was moved or banged, the heads would bounce and the data reads/writes became unreliable
- software ("file systems") became more and more complex having to deal with all of the above contingencies
- digital bits were used to sanity-check (ECC) the data on the platters.  This, of course, used up data bits for non-data purposes and reduced the data densities on disk platters.

### Solid State Disk
Many of the problems of physical disks were alleviated by removing all requirements for physical motion from the disk packs and resorting to the use of transistors - instead of oxides - to store information.
### USB
Universal Serial Bus.

More and more devices were invented with varying non-standardized connections.

A standard was invented to unify access to all new kinds of devices.  This resulted in a standard set of software, called "Plug'N'Play" to access the devices.

Since the design for the standard had to accomodate all sorts of devices at low cost, the standard was devolved to include only serial access.

Software-wise, the standard became very complicated, containing unified and generalized ways to communicate with devices.

### Internet, IoT, Robotics, Etc.

The ultimate distance between data and CPUs is the internet.  

A CPU accesses the internet using a small number of wires and requests data from anywhere in the world.

The request and the response get bounced around the network of computers and take a "long" time to make the round trip.

We, humans, perceive this request/response delay as "lag time" and "slowness of the connection".

To make matters worse, the response often contains instructions that must be interpreted by the browser on the requestors' CPUs.  So, not only is there a lag due to the request/response delay time, there is also a block of time required to process the response.

### Caches

To ameliorate the lag times involved in accessing memory and accessing the internet, we invented *caches*.

Caches are copies of memory that are physically closer to the CPUs than the actual required data.

The idea is that it is *much* faster to access the data from a cache than wait for the data to come from the source.

We get the data once from the source, then we copy the data to the cache and "hit the cache" on subsequent accesses to the same data.

## Cache Gothas
- coherency
	- does the cache hold the most recent version of the data?
	- browsers have a RELOAD button to refresh the cache
	- browsers use agressive caching

# New Model Of Computing
uni-directional wires
bi-directional wires are but an optimization (2 wires becomes 1)
# ROM - Read-Only Memory