# Function Description:
#     Complete the makingAnagrams function in the editor below.
#     makingAnagrams has the following parameter(s):
#         string s1: a string
#         string s2: a string
#
# Returns:
#     int: the minimum number of deletions needed
#
# Input Format:
#     The first line contains a single string, `s1`.
#     The second line contains a single string, `s2`.

import os


def makingAnagrams(s1, s2):
    x = set(s1) & set(s2)
    y = 0
    for l in x:
        y += min(s1.count(l), s2.count(l))
    return len(s1) + len(s2) - y * 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
