import numpy as np
from string import *
import sys

#########################################################################

distance = []
distance_index = 0


def aligner(str1, str2, newstr1, newstr2, direction_matrix, n, m):
    """
    Creates and aligns the strings with insertions and deletions.

    :param str1: String. First string to be aligned
    :param str2: String. Second string to be aligned
    :param newstr1: String. Output of first string with insertions/deletions.
    :param newstr2: String. Output of second string with insertions/deletions.
    :param direction_matrix: Matrix. used to determine what the strings look like comparatively.
    :param n: Length of string 1
    :param m: Length of string 2
    :return: Both newly formatted strings.
    """
    global distance, distance_index
    alpha = int(sys.argv[2])
    beta = int(sys.argv[3])

    if direction_matrix[m][n] == 'D':
        newstr1 = str1[n-1] + newstr1
        newstr2 = str2[m-1] + newstr2
        if str1[n-1] == str2[m-1]:
            distance[distance_index] += 0
        else:
            distance[distance_index] += beta
        aligner(str1, str2, newstr1, newstr2, direction_matrix, n-1, m-1)
    elif direction_matrix[m][n] == 'H':
        newstr1 = str1[n-1] + newstr1
        newstr2 = '-' + newstr2
        distance[distance_index] += alpha
        aligner(str1, str2, newstr1, newstr2, direction_matrix, n-1, m)
    elif direction_matrix[m][n] == 'V':
        newstr1 = '-' + newstr1
        newstr2 = str2[m-1] + newstr2
        distance[distance_index] += alpha
        aligner(str1, str2, newstr1, newstr2, direction_matrix, n, m-1)
    else:
        distance_index += 1
        return newstr1, newstr2


# Determines the direction for the direction matrix and encodes it to a character.
def direction_finder(diagonal, horizontal, vertical):
    direc = max(diagonal, horizontal, vertical)

    if diagonal == direc:
        return 'D'
    elif horizontal == direc:
        return 'H'
    else:
        return 'V'


# Aligns the strings and creates the matrices
def global_alignment(str1, str2, match_score, mismatch_score, gap_score):
    score = [int(match_score), int(mismatch_score), int(gap_score)]
    n = len(str1) + 1
    m = len(str2) + 1
    score_matrix = np.zeros((m, n), dtype=int)
    direction_matrix = np.zeros((m, n), dtype=str)

    # Sets the values for the first column
    for i in range(m):
        score_matrix[i][0] = score[2] * i
        direction_matrix[i][0] = 'V'

    # Sets the values for the first row
    for j in range(n):
        score_matrix[0][j] = score[2] * j
        direction_matrix[0][j] = 'H'

    direction_matrix[0][0] = 0  # cell (0,0) has a value of 0, it is the end cell
    # Fills in the rest of the matrix values based on their score
    for i in range(1, m):
        for j in range(1, n):

            if str1[j-1] == str2[i-1]:
                effective_score = score[0]
            else:
                effective_score = score[1]

            diagonal = score_matrix[i-1][j-1] + effective_score
            horizontal = score_matrix[i][j-1] + score[2]
            vertical = score_matrix[i-1][j] + score[2]
            score_matrix[i][j] = max(diagonal, horizontal, vertical)
            direction_matrix[i][j] = direction_finder(diagonal, horizontal, vertical)

    aligner(str1, str2, '', '', direction_matrix, len(str1), len(str2))

#########################################################################


# Reads in the lines of the file and runs the rest of the program on them
def read_file(file):
    with open(file) as fp:
        line = fp.readline()
        line_storage = []
        while line:
            line_storage.append(line.rstrip())  # save other lines to an array for later comparison
            line = fp.readline()
    print(line_storage)
    center_star(line_storage)


# Aligns the strings and creates the matrices
def center_star(string_array):
    global distance
    center_test = np.zeros((len(string_array),), dtype=int)

    # compute pairwise distance between all strings.
    for string_index_1 in range(len(string_array)):  # find combination of the array
        for string_index_2 in range(len(string_array)):
            if string_index_2 <= string_index_1:
                pass
            else:
                string_pair = [string_array[string_index_1], string_array[string_index_2]]
                distance.append(0)
                global_alignment(string_pair[0], string_pair[1], 0, -1, -2)
                center_test[string_index_1] += distance[-1]
                center_test[string_index_2] += distance[-1]
    min_val = int(np.amin(center_test))
    center_string_index = list(center_test).index(min_val)
    print("Center String: {}\nSummed Distances: {}".format(string_array[center_string_index], center_test))


read_file(sys.argv[1])
# A couple examples, just in case.
# global_alignment("TCGCACCATGGCTACCCTTTTGACT", "TCCATACTTTCAACCCTTGACT", 1, -1, -2)
# global_alignment("TCGCACTCATGGCTACCT", "TCCATACTTTCAACCCTTGACT", 1, -1, -2)
