"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time

start_time = time.time()
answer = None

# Code here
longest = 0
for start in xrange(2,1000001):
    item = start
    chain = []
    while item != 1:
        chain.append(item)
        if item % 2:
            item = 3 * item + 1
        else:
            item //= 2
    chain.append(1)

    if len(chain) > longest:
        longest = len(chain)
        answer = start

# End timer
end_time = time.time()

print "Answer:   \t%d" % answer
print "Exec Time:\t%g microseconds\t%g seconds" % ((end_time - start_time) * 1000000, (end_time - start_time))
