# Function Description:
#     Complete the repeatedString function in the editor below.
#     repeatedString has the following parameter(s):
#         s: a string to repeat
#         n: the number of characters to consider
#
# Returns:
#     int: the frequency of a in the substring
#
# Input Format:
#     The first line contains a single string, `s`.
#     The second line contains an integer, `n`.

import os


def repeatedString(s, n):
    aa = s.count('a')
    mul = int(n // len(s))
    sli = n % len(s)
    count = s[:sli].count('a')
    total = aa * mul + count
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
