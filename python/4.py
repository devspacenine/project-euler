"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

start_time = time.time()
answer = None

largest = 0

for x in xrange(100, 999):
    for y in xrange(100, 999):
        product = x * y
        if str(product) == "".join(reversed(str(product))) and product > largest:
            largest = product

# End timer
end_time = time.time()

print "Answer:   \t%d" % largest
print "Exec Time:\t%g microseconds" % ((end_time - start_time) * 1000000)
