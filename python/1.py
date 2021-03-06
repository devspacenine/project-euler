"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

start_time = time.time()
answer = None

answer = sum([x for x in range(1000) if x % 3 == 0 or (x % 5 == 0 and x % 3 != 0)])

# End timer
end_time = time.time()

print "Answer:   \t%d" % answer
print "Exec Time:\t%g microseconds" % ((end_time - start_time) * 1000000)
