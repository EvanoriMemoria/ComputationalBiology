import numpy as np
import math
import sys

n = 100
rand_arr = np.random.randint(n+1, size=n)
sort_arr = np.sort(np.random.randint(n+1, size=n))
sparse = np.zeros((n, math.floor(math.log(n))+1), dtype=int)


def preprocess(input):

    for i in range(n):
        sparse[i][0] = i
    j = 1
    i = 0
    while 2**j <= n:
        while i+(2**j)-1 < n:
            if input[sparse[i][j-1]] < input[sparse[i+2**(j-1)][j-1]]:
                sparse[i][j] = sparse[i][j-1]
            else:
                sparse[i][j] = sparse[i+2**(j-1)][j-1]
            i += 1
        j += 1
    return sparse


def rangeMinimumQuerry():
    print(rand_arr)
    print(sort_arr)


print(preprocess(rand_arr))
rangeMinimumQuerry()
