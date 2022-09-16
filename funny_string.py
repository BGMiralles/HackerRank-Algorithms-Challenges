# Function Description:
#     Complete the funnyString function in the editor below.
#     funnyString has the following parameter(s):
#         string s: a string to test
#
# Returns:
#     string: either Funny or Not Funny
#
# Input Format:
#     The first line contains an integer `q`, the number of queries.
#     The next `q` lines each contain a string, `s`.

import os


def funnyString(s):
    norm_ascii = []
    for item in s:
        norm_ascii.append(ord(item))
    reversed_ascii = norm_ascii[::-1]
    i = 1
    while i < len(norm_ascii):
        diff_norm = abs(norm_ascii[i] - norm_ascii[i-1])
        diff_rev = abs(reversed_ascii[i] - reversed_ascii[i-1])
        if diff_norm != diff_rev:
            return "Not Funny"
        i += 1
    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
