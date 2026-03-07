# 2023-06-15-Efficiency
In my direct experience, humans can detect timescales of about 20msec (0.02 seconds).

Any hardware operation that takes more than 20msec feels "sluggish".

Any hardware operation that takes less than 20msec feels "fast".

So, a human will think that a computer operation is "fast" if it takes 0.000000010 seconds to run.

If the operation is 1,000x slower and takes 0.000010000 seconds to run, humans will still think that the operation is "fast".

In fact, a computer can run 20,000 x 0.000000010sec. operations before reaching the edge of human perception.

In the 1950s, computer operations were measured in micro-seconds (0.000001 seconds).  In 2023, computer operations are measured in nano-seconds (0.0000000001 seconds).

The ground truth has changed.  We need to re-think what "efficiency" means.  There is UX - application efficiency, and, DX - developer efficiency.

If we devote those 20,000 operations to graphics, we can display more realistic images in the UX.  OTOH, if we devote those 20,000 operations to DX, we get faster turn-around for developers which results in cheaper applications for end-users.

What is the appropriate trade-off?