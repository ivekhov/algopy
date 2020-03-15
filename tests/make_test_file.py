import os
from random import randint

with open('test.txt', 'w') as f:
    start = 0
    stop = 1000001
    min_loc = 0
    max_loc = 65535

    for i in range(start, stop):
        f.write(str(randint(min_loc, max_loc)))
        f.write("\n")
    f.write("\n")
#
