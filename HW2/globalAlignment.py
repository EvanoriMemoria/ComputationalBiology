import numpy as np
from string import *

TEST_STRING = "aabaabca$abaabaabcaabaabcaacccbbcabbcbabcbcabcbabcccbabbbbcacaaacbbbaacbbcbcaacbcaabaabcabacbaccabcbbcccabbbcabcbbbbcacccccaabaabcabacbabcabbacccbbbabaaa"


def aligner(str1, str2, newstr1, newstr2, direction_matrix, n, m):
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


def direction_finder(diagonal, horizontal, vertical):
    direc = max(diagonal, horizontal, vertical)

    if diagonal == direc:
        return 'D'
    elif horizontal == direc:
        return 'H'
    else:
        return 'V'


def global_alignment(str1, str2, match_score, mismatch_score, gap_score):
    score = [match_score, mismatch_score, gap_score]
    n = len(str1) + 1
    m = len(str2) + 1
    score_matrix = np.zeros((m, n), dtype=int)
    direction_matrix = np.zeros((m, n), dtype=str)

    for i in range(m):
        score_matrix[i][0] = score[2] * i
        direction_matrix[i][0] = 'V'

    for j in range(n):
        score_matrix[0][j] = score[2] * j
        direction_matrix[0][j] = 'H'

    direction_matrix[0][0] = 0
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

    print("Score Matrix")
    print(np.matrix(score_matrix))
    print("")
    print("Directional Matrix")
    print(np.matrix(direction_matrix))

    print("\nThese Strings")
    print(str1)
    print(str2)
    print("\nHave this is one of their optimal alignments:")

    aligner(str1, str2, '#', '#', direction_matrix, len(str1), len(str2))


#global_alignment("TCGCACCATGGCTACCCTTTTGACT", "TCCATACTTTCAACCCTTGACT", 1, -1, -2)
global_alignment("TCGCACTCATGGCTACCT", "TCCATACTTTCAACCCTTGACT", 1, -1, -2)
