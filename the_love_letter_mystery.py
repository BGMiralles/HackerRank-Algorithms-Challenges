# Function Description:
#     Complete the theLoveLetterMystery function in the editor below.
#     theLoveLetterMystery has the following parameter(s):
#         string s: the text of the letter
#
# Returns:
#     int: the minimum number of operations
#
# Input Format:
#     The first line contains an integer `q`, the number of queries.
#     The next `q` lines will each contain a string .

import os
import string


def theLoveLetterMystery(s):
    a = string.ascii_lowercase
    alphabet = dict(zip(a, range(len(a))))

    count = 0
    for index in range(len(s) // 2):
        if s[index] != s[-(index + 1)]:
            count += abs(alphabet[s[index]] - alphabet[s[-(index + 1)]])

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
