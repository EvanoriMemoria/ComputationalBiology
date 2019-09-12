TEST_STRING = "aabaabca$abaabaabcaabaabcaacccbbcabbcbabcbcabcbabcccbabbbbcacaaacbbbaacbbcbcaacbcaabaabcabacbaccabcbbcccabbbcabcbbbbcacccccaabaabcabacbabcabbacccbbbabaaa"
SPECIAL_CHARACTER = '$'


def z_alg(str):
    Z = [0]*len(str)
    left, right = 0, 0

    for iter in range(1, len(str)):
        if iter > right:  # if i is outside current z box
            right = iter
            left = iter
            while right < len(str) and str[right-left] == str[right]:  # naively compute matches
                right += 1
            Z[iter] = right-left
            right -= 1
        else:  # if i is inside current z box
            k = iter-left
            if Z[k] < right-iter+1:  # check the equivalent z value in the prefix, if it is larger set the new Z value to that value
                Z[iter] = Z[k]
            else:  # else there is no equivalent z value, naively compute.
                left = iter
                while right < len(str) and str[right-left] == str[right]:
                    right += 1
                Z[iter] = right-left
                right -= 1

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
        print("There is a perfect match at index %d" % i)
