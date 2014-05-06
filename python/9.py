"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

start_time = time.time()
answer = None

# Code here
c = 997
b = 2
a = 1
found = False

while c > 5:
    diff = 1000 - c
    a = diff / 2
    b = (diff / 2) + (diff % 2)
    if a == b:
        a -= 1
        b += 1
    while a > 1:
        if (a**2 + b**2) == c**2 and (a + b + c) == 1000:
            answer = a * b * c
            found = True
            break
        a -= 1
        b += 1
    if found:
        break

    c -= 1

# End timer
end_time = time.time()

print "Answer:   \t%d" % answer
print "Exec Time:\t%g microseconds\t%g seconds" % ((end_time - start_time) * 1000000, (end_time - start_time))
