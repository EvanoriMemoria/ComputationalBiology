import numpy as np
import math
import random

VERBOSE = 0
n = 6
arr = np.array([4, 6, 1, 5, 7, 3])  # Little test array
#arr = np.random.randint(n+1, size=n)  # Random n length array of random integers between 0 and n
#arr = np.sort(np.random.randint(n+1, size=n))  # Sorted n length array of random integers between 0 and n
sparse = np.zeros((n, math.floor(math.log(n, 2))+1), dtype=int)


def preprocess():
    print("Beginning Pre-processing Step")
    for i in range(n):
        sparse[i][0] = i
    j = 1
    i = 0
    # Iterate through the columns of the sparse table
    while 2**j <= n:
        if VERBOSE:
            print("first while {} is less than {}".format(2**j, n))
        # Iterate over the rows of the sparse table - only the values we need
        while i+(2**j)-1 < n:
            if VERBOSE:
                print("i: {}, j: {}".format(i, j))
                print("if {} is less than {}".format(arr[sparse[i][j-1]], arr[sparse[i+2**(j-1)][j-1]]))
            # Compare two previous values and set the current value equal to the lesser
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

# Returns the minimum value from the sparse table between the given indices
def rangeMinimumQuery(low, high):
    mid = high-low+1
    k = int(math.log(mid, 2))
    option1 = arr[sparse[low][k]]
    option2 = arr[sparse[low+mid-2**k][k]]
    print("option1: {} at index {}\noption2: {} at index {}".format(option1, sparse[low][k], option2, sparse[low+mid-2**k][k]))
    print("option1 Sparse Coords: {}, {}\noption2 Sparse Coords: {}, {}\n".format(low, k, low+mid-2**k, k))
    return min([option1, option2])


print("n: {}".format(n))
if n > 20:
    print("First 20 integers of the array: {}\n".format(arr[:20]))
else:
    print("Array: {}\n".format(arr[:n]))
preprocess()
if n <= 100:
    print(sparse)
rand1 = random.randrange(n)
rand2 = random.randrange(n)
print("\nFinding lowest between index {} and {}".format(min([rand1, rand2]), max(rand1, rand2)))
print("Lowest value in range: {}".format(rangeMinimumQuery(min([rand1, rand2]), max([rand1, rand2]))))
