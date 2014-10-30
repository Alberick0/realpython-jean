from __future__ import division
from random import randint

trial = 10000
flips = 0

# Heads = 0 | Tail = 1
for i in range(trial):
    flips += 1

    if randint(0,1) == 0:
        while randint(0,1) == 0:
            flips += 1
        flips += 1
    else:
        while randint(0,1) == 1:
            flips += 1
        flips += 1

print flips/trial
