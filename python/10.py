"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time

start_time = time.time()
answer = None

# Code here
primes = [2]
candidate = 3
while True:
    if candidate >= 2000000:
        break

    is_prime = True
    for prime in primes:
        if prime > candidate**.5:
            break
        if candidate % prime == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(candidate)

    candidate += 2

answer = sum(primes)

# End timer
end_time = time.time()

print "Answer:   \t%d" % answer
print "Exec Time:\t%g microseconds\t%g seconds" % ((end_time - start_time) * 1000000, (end_time - start_time))
