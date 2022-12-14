# Function Description:
#     Complete the function twoStrings in the editor below.
#     twoStrings has the following parameter(s):
#         string s1: a string
#         string s2: another string
#
# Returns:
#     string: either YES or NO
#
# Input Format:
#     The first line contains a single integer `p`, the number of test cases.
#     The following `p` pairs of lines are as follows:
#         The first line contains string `s1`.
#         The second line contains string `s2`.
#
# Output Format:
#     For each pair of strings, return YES or NO.

import os
import string


def twoStrings(s1, s2):
    for x in string.ascii_lowercase:
        if x in s1 and x in s2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
