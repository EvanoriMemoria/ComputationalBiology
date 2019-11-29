import numpy as np
import math
import sys

n = 100
rand_arr = np.random.randint(n+1, size=n)
sort_arr = np.sort(np.random.randint(n+1, size=n))
table = np.zeros((n, math.floor(math.log(n))+1), dtype=int)

def rangeMinimumQuerry():
    print(rand_arr)
    print(sort_arr)


rangeMinimumQuerry()
