import numpy as np
from string import *
import sys


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

    if direction_matrix[m][n] == 'D':
        newstr1 = str1[n-1] + newstr1
        newstr2 = str2[m-1] + newstr2
        aligner(str1, str2, newstr1, newstr2, direction_matrix, n-1, m-1)
    elif direction_matrix[m][n] == 'H':
        newstr1 = str1[n-1] + newstr1
        newstr2 = '-' + newstr2
        aligner(str1, str2, newstr1, newstr2, direction_matrix, n-1, m)
    elif direction_matrix[m][n] == 'V':
        newstr1 = '-' + newstr1
        newstr2 = str2[m-1] + newstr2
        aligner(str1, str2, newstr1, newstr2, direction_matrix, n, m-1)
    else:
        print(newstr1)
        print(newstr2)
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


# Reads in the lines of the file and runs the rest of the program on them
def read_file(file):
    with open(file) as fp:
        line = fp.readline()
        cnt = 0
        line_storage = ['', '']
        while line:
            if line.startswith('>'):
                line = fp.readline()  # Skip lines that start with >
            else:
                line_storage[cnt] = line.rstrip()  # save other lines to an array for later comparison
                line = fp.readline()
                cnt += 1
    global_alignment(line_storage[0], line_storage[1], sys.argv[2], sys.argv[3], sys.argv[4])


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

    #print("Score Matrix")
    #print(np.matrix(score_matrix))
    #print("")
    #print("Directional Matrix")
    #print(np.matrix(direction_matrix))

    print("\nThese Strings")
    print(str1)
    print(str2)
    print("\nHave this as one of their optimal alignments:")

    aligner(str1, str2, '', '', direction_matrix, len(str1), len(str2))


read_file(sys.argv[1])
#global_alignment("TCGCACCATGGCTACCCTTTTGACT", "TCCATACTTTCAACCCTTGACT", 1, -1, -2)
#global_alignment("TCGCACTCATGGCTACCT", "TCCATACTTTCAACCCTTGACT", 1, -1, -2)
