from __future__ import division
from random import randint

print "Toss of a dice"

def toss():
    return randint(1,6)

print "The toss of a dice was", toss()

print "simulates 10,000 throws of a dice and displays the average"
average = 0
for i in range(0, 10000):
    average += toss()
print 'the average toss is:', average/10000
    
