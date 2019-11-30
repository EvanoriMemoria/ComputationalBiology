import numpy as np
import math
import random
import sys

VERBOSE = 0
n = 100
#arr = np.array([4, 6, 1, 5, 7, 3])
arr = np.random.randint(n+1, size=n)
#arr = np.sort(np.random.randint(n+1, size=n))
sparse = np.zeros((n, math.floor(math.log(n, 2))+1), dtype=int)


def preprocess():
    print("Beginning Pre-processing Step")
    for i in range(n):
        sparse[i][0] = i
    j = 1
    i = 0
    while 2**j <= n:
        if VERBOSE:
            print("first while {} is less than {}".format(2**j, n))
        while i+(2**j)-1 < n:
            if VERBOSE:
                print("i: {}, j: {}".format(i, j))
                print("if {} is less than {}".format(arr[sparse[i][j-1]], arr[sparse[i+2**(j-1)][j-1]]))
            if arr[sparse[i][j-1]] < arr[sparse[i+2**(j-1)][j-1]]:
                sparse[i][j] = sparse[i][j-1]
                if VERBOSE:
                    print("then sparse[{}][{}] = sparse[{}][{}]".format(i, j, i, j-1))
                    print("sparse[{}][{}] = {}".format(i, j, sparse[i][j-1]))
            else:
                sparse[i][j] = sparse[i+2**(j-1)][j-1]
                if VERBOSE:
                    print("else sparse[{}][{}] = sparse[{}][{}]".format(i, j, i+2**(j-1), j - 1))
                    print("sparse[{}][{}] = {}".format(i, j, sparse[i+2**(j-1)][j - 1]))
            i += 1
        j += 1
        i = 0
    print("Sparse Table Finished\n")
    return sparse


def rangeMinimumQuerry(low, high):
    mid = high-low+1
    k = int(math.log(mid, 2))
    option1 = arr[sparse[low][k]]
    option2 = arr[sparse[low+mid-2**k][k]]
    print("option1: {} at index {}\noption2: {} at index {}".format(option1, sparse[low][k], option2, sparse[low+mid-2**k][k]))
    print("option1 Sparse Coords: {}, {}\noption2 Sparse Coords: {}, {}\n".format(low, k, low+mid-2**k, k))
    return min([option1, option2])


print("n: {}".format(n))
print("First 20 integers of the array: {}\n".format(arr[:20]))
preprocess()
if n <= 100:
    print(sparse)
rand1 = random.randrange(n)
rand2 = random.randrange(n)
print("\nFinding lowest between index {} and {}".format(min([rand1, rand2]), max(rand1, rand2)))
print("Lowest value in range: {}".format(rangeMinimumQuerry(min([rand1, rand2]), max([rand1, rand2]))))
