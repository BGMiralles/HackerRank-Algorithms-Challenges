# Function Description:
#     Complete the anagram function in the editor below.
#     anagram has the following parameter(s):
#         string s: a string
#
# Returns:
#     int: the minimum number of characters to change or -1.
#
# Input Format:
#     The first line will contain an integer, `q`, the number of test cases.
#     Each test case will contain a string `s`.

import os
from collections import Counter


def anagram(s):
    if len(s) % 2 == 1:
        return -1

    first, last = s[:len(s) // 2], s[len(s) // 2:]
    c = Counter(first) - Counter(last)
    return len(list(c.elements()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
