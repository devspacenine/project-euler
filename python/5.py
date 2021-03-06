"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

start_time = time.time()
answer = None

# Code here
x = 20
while True:
    if x % 2 == 0 and x % 3 == 0 and x % 4 ==0 and x & 5 == 0 and x % 7 == 0 and x % 11 == 0 and x % 13 == 0 and x % 17 == 0 and x % 19 == 0:
        if x % 6 == 0 and x % 8 == 0 and x % 9 == 0 and x % 10 == 0 and x % 12 == 0 and x % 14 == 0 and x % 15 == 0 and x % 16 == 0 and x % 18 == 0 and x % 20 == 0:
            answer = x
            break
    x += 20

# End timer
end_time = time.time()

print "Answer:   \t%d" % answer
print "Exec Time:\t%g microseconds\t%g seconds" % ((end_time - start_time) * 1000000, (end_time - start_time))
