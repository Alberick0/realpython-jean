from __future__ import division
from random import random

candidate_a = 0
candidate_b = 0
total_a = 0
total_b = 0


for i in range(0, 10000):

    for v in (0.87, 0.65, 0.17):

        if random() < v:
            candidate_a += 1
        else:
            candidate_b += 1

    if candidate_a > candidate_b:
        total_a += 1
    else:
        total_b += 1



print "Probability that Candidate A wins:", total_a/10000
print "Probability that Candidate A wins:", total_b/10000
