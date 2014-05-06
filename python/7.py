"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time

start_time = time.time()
answer = None

# Code here
primes = [2]
candidate = 3
while True:
    is_prime = True
    for prime in primes:
        if prime > candidate**.5:
            break
        if candidate % prime == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(candidate)

    if len(primes) == 10001:
        answer = candidate
        break

    candidate += 2

# End timer
end_time = time.time()

print "Answer:   \t%d" % answer
print "Exec Time:\t%g microseconds\t%g seconds" % ((end_time - start_time) * 1000000, (end_time - start_time))
