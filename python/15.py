"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""
import time

start_time = time.time()
answer = None

# Code here
def test():
    print "yay"
    while 1:
        x = yield
        print "got x", x

c = test()
c.send(None)
c.send("corey was here")

# End timer
end_time = time.time()

print "Answer:   \t%d" % answer
print "Exec Time:\t%g microseconds\t%g seconds" % ((end_time - start_time) * 1000000, (end_time - start_time))
