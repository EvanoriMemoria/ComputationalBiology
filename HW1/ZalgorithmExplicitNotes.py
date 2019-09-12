TEST_STRING = "aabaabca$abaabaabcaabaabcaacccbbcabbcbabcbcabcbabcccbabbbbcacaaacbbbaacbbcbcaacbcaabaabcabacbaccabcbbcccabbbcabcbbbbcacccccaabaabcabacbabcabbacccbbbabaaa"
SPECIAL_CHARACTER = '$'


def z_alg(str):
    Z = [0]*len(str)
    left, right = 0, 0

    for i in range(1, len(str)):
        if i > right:  # if i is outside current z-box
            n = 0
            while n + i < len(str) and str[n] == str[n+i]:  # while the values match and the string has not ended
                n += 1  # keep doing naive computations
            Z[i] = n
            if n > 0:  # if the current Z value is greater than 0 we move the bounds of the z box
                left = i  # left is wherever the z-box started
                right = i+n-1  # right is where the z-box started, plus the length of the matching string minus one
        else:  # if i is inside current z-box
            p = i - left  # not overlapping portion of the outer z-box
            overlap = right - i + 1  # find overlapping portion of the two z-boxes

            if Z[p] < overlap:  # if the prefix Z value is inside the overlap portion of the z-boxes, our current
                # Z value is equal to the equivalent position at the start
                Z[i] = Z[p]
            else:  # otherwise, the secondary z-box has gone past the bound of the outer z-box, and we must naively
                # check for matches
                j = right + 1
                while j < len(str) and str[j] == str[j-i]:  # while the values outside both z-boxes match and the
                    # string has not ended
                    j += 1  # continue naive computations
                Z[i] = j - i  # the Z-value at our current index is equal to the length of the new z-box
                # then set the right and left bounds of this z-box to their correct positions
                left = i
                right = j-1

    return Z


print(z_alg("aabaabcaabaabaabc"))  # z algorithm test

Z = z_alg(TEST_STRING)  # run the test string through the algorithm
prefix_len = 0

# find the length of the prefix we are searching for
for i in range(len(TEST_STRING)):
    if TEST_STRING[i] == SPECIAL_CHARACTER:
        prefix_len = i

# if the length is matched in any of the z values, we found a prefix match in the string.
for i in range(len(Z)):
    if Z[i] == prefix_len:
        print("There is a total match at index %d" % i)
