# Function Description:
#     Complete the stringConstruction function in the editor below. It should return the minimum cost of copying a string.
#     stringConstruction has the following parameter(s):
#         s: a string
#
# Input Format:
#     The first line contains a single integer `n`, the number of strings.
#     Each of the next `n` lines contains a single string, s[i].
#
# Output Format:
#     For each string s[i] print the minimum cost of constructing a new string p[i] on a new line.

import os


def stringConstruction(s):
    return len(set(s))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
